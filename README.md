# ☕ Coffee Barista AI Agent

An AI-powered coffee shop assistant built with **Google Agent Development Kit (ADK)**, **Google Gemini**, and **Streamlit**.

The agent helps customers discover drinks and pastries based on their preferences while grounding its recommendations in a predefined coffee shop menu.

---

## 📌 Overview

Coffee Barista AI is a conversational AI agent designed to act as a virtual coffee shop barista.

Customers can ask questions such as:

- "I want a sweet cold coffee."
- "I'm dairy-free. What can I have?"
- "What pastries do you have?"
- "Do you have a caramel frappuccino?"

The agent retrieves information from the available menu and uses Gemini to provide natural-language recommendations.

---

## ✨ Features

- ☕ Coffee and pastry recommendations
- 🔎 Menu-based grounding
- 🥛 Dietary preference handling
- 🚫 Prevents recommendations of unavailable menu items
- 💬 Conversational interaction
- 🤖 Google ADK-based agent architecture
- 🌐 Streamlit web interface
- 🧠 Gemini-powered responses

---

## 🏗️ Architecture

                    Customer
                       │
                       ▼
              ┌─────────────────┐
              │    Streamlit    │
              │       UI        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   ADK Runner    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Barista Agent  │
              │     Gemini      │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   get_menu()    │
              │   Menu Tool     │
              └────────┬────────┘
                       │
                       ▼
                  menu.json
🛠️ Technologies
Python
Google Agent Development Kit (ADK)
Google Gemini
Streamlit
Git
GitHub
📂 Project Structure
coffee_barista_agent/
│
├── agent.py
├── app.py
├── menu.json
├── requirements.txt
├── README.md
└── .gitignore
agent.py

Contains the main ADK agent, Gemini model configuration, menu retrieval tool, and ADK application definition.

app.py

Contains the Streamlit user interface and connects the UI to the ADK agent.

menu.json

Contains the available coffee and pastry menu data.

requirements.txt

Contains the Python dependencies required to run the project.

⚙️ Setup
1. Clone the repository
git clone https://github.com/Viyan-Dabre/coffee-barista-agent.git
cd coffee-barista-agent
2. Create a virtual environment
python -m venv .venv
3. Activate the environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
🔑 Gemini API Key

The application requires a Gemini API key.

Set it as an environment variable.

Windows PowerShell
$env:GOOGLE_API_KEY="YOUR_API_KEY"

Do not put your API key directly inside the source code or commit it to GitHub.

▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will be available locally at:

http://localhost:8501
🤖 Run with Google ADK

The agent can also be tested using the ADK development interface:

adk web

The ADK development UI will be available locally and allows direct interaction with the agent.

🧪 Agent Behavior

The agent is instructed to:

Recommend only items available in the menu.
Use menu information when making recommendations.
Respect explicitly stated dietary restrictions.
Never assume dietary restrictions that the customer has not mentioned.
Ask one clarifying question when the customer's request is unclear.
Avoid inventing unavailable products or prices.
Example

Customer:

I want a sweet cold coffee.

Agent:

I highly recommend our Iced Caramel Macchiato for $5.25.

🔒 Safety & Grounding

The agent uses the menu as its source of truth.

For example, if a customer asks:

Do you have a Caramel Frappuccino?

The agent should not invent the product.

Instead, it explains that the item is not currently available and suggests relevant items that actually exist in the menu.

🚧 Current Status
Completed
 Google ADK agent
 Gemini integration
 Menu retrieval tool
 Dietary preference handling
 Menu grounding
 Hallucination prevention instructions
 Streamlit interface
 Local testing
 Git repository
 GitHub repository
Planned
 Enhanced RAG implementation
 Production deployment
 Cloud Run deployment
 Improved UI/UX
 Automated evaluation
 Additional menu data
 Production monitoring
🔮 Future Improvements

Possible future improvements include:

Vector database-based menu retrieval
More advanced RAG pipelines
Order creation
Cart functionality
Customer preferences and memory
Order history
Multi-agent architecture
Voice interaction
Cloud deployment
Automated evaluation and monitoring
👨‍💻 Author

Viyan Dabre

GitHub: https://github.com/Viyan-Dabre