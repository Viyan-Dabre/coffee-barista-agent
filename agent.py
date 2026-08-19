import json

from google.adk.agents import LlmAgent
from google.adk.apps import App


def get_menu() -> str:
    """Retrieves the coffee shop menu from menu.json."""
    try:
        with open("menu.json", "r", encoding="utf-8") as f:
            menu_data = json.load(f)
            return json.dumps(menu_data)
    except Exception as e:
        return json.dumps(
            {"error": f"Could not retrieve menu: {str(e)}"}
        )


barista_agent = LlmAgent(
    name="barista_agent",
    model="gemini-3.6-flash",
    instruction="""
You are a friendly barista at ☕ Coffee Shop.

Your job is to recommend drinks and pastries to customers based on their preferences.

Rules you MUST follow:

1. You must recommend items ONLY from the menu returned by get_menu().
2. Do NOT recommend or suggest any item that is not present in the menu.
3. If a user's preference is vague or unclear, ask exactly ONE friendly clarifying question to narrow down what they want.
4. Be warm and welcoming, but remain professional.
5. Ground your recommendations in the actual tags, descriptions, and allergens listed in the menu.
6. If a user is dairy-free, recommend ONLY items tagged 'dairy-free' or with no dairy allergens.
7. Never assume a customer's dietary restrictions, allergies, preferences, or ingredients they want to avoid unless they explicitly mention them.
""",
    tools=[get_menu],
)


app = App(
    name="coffee_barista_agent",
    root_agent=barista_agent,
)