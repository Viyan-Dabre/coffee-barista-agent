import asyncio

import streamlit as st
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import app


st.set_page_config(
    page_title="Coffee Barista AI",
    page_icon="☕",
    layout="centered",
)

st.title("☕ Coffee Barista AI")
st.caption("Your personal AI coffee shop assistant")


@st.cache_resource
def get_session_service():
    return InMemorySessionService()


session_service = get_session_service()

runner = Runner(
    app=app,
    session_service=session_service,
)


async def create_customer_session():
    return await session_service.create_session(
        app_name=app.name,
        user_id="customer",
    )


async def get_agent_response(session_id, prompt):
    response = runner.run_async(
        user_id="customer",
        session_id=session_id,
        new_message=types.Content(
            role="user",
            parts=[
                types.Part(text=prompt)
            ],
        ),
    )

    answer = ""

    async for event in response:
        if event.is_final_response():
            if event.content and event.content.parts:
                answer = event.content.parts[0].text

    return answer


if "session_id" not in st.session_state:
    session = asyncio.run(create_customer_session())
    st.session_state.session_id = session.id


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if prompt := st.chat_input("What would you like today?"):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        answer = asyncio.run(
            get_agent_response(
                st.session_state.session_id,
                prompt,
            )
        )

        if not answer:
            answer = "Sorry, I couldn't generate a response."

        st.write(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )