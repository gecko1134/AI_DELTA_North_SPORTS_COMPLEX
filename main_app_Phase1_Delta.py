
import os
import sys
import streamlit as st
import importlib.util
import json

# App Configuration
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

MODULES_DIR = os.path.join(BASE_DIR, "modules")
AI_DIR = os.path.join(MODULES_DIR, "ai")

# Load Users
with open(os.path.join(BASE_DIR, "users.json")) as f:
    users = json.load(f)

# Login Function
def login():
    st.sidebar.header("🔐 Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        user = users.get(email)
        if user and user["password"] == password:
            st.session_state.user = {"email": email, "role": user["role"]}
        else:
            st.sidebar.error("Invalid credentials")

# Logout
def logout():
    if st.sidebar.button("Logout"):
        st.session_state.user = None

# Dynamic Tool Loader
def load_tool(path):
    tool_name = os.path.basename(path).replace(".py", "")
    spec = importlib.util.spec_from_file_location(tool_name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return tool_name, mod

# Role-based Tool Permissions
ROLE_ACCESS = {
    "admin": ["all"],
    "sponsor": ["ai_matchmaker"],
    "board": ["demand_forecasting", "churn_prediction", "ai_strategy_dashboard", "ai_risk_alerts"],
    "foundation": ["ai_personalization_engine", "ai_voice_assistant"]
}

# App Launcher
def run():
    st.set_page_config(page_title="SportAI Suite", layout="wide")

    if "user" not in st.session_state or not st.session_state.user:
        login()
        return

    user = st.session_state.user
    role = user["role"]
    st.sidebar.success(f"Logged in as {user['email']} ({role})")
    logout()

    st.title("🏟️ SportAI Suite – Intelligent Tools")
    st.header("Category: AI Tools")

    tools = []
    for file in os.listdir(AI_DIR):
        if file.endswith(".py") and file != "__init__.py":
            tool_name, tool_mod = load_tool(os.path.join(AI_DIR, file))
            if "all" in ROLE_ACCESS.get(role, []) or tool_name in ROLE_ACCESS.get(role, []):
                tools.append((tool_name, tool_mod))

    tool_labels = [t[0].replace("_", " ").title() for t in tools]
    selected = st.sidebar.selectbox("Select a Tool", tool_labels)

    for label, mod in tools:
        if label.replace("_", " ").title() == selected:
            if hasattr(mod, "run"):
                mod.run()
            elif hasattr(mod, "main"):
                mod.main()
            else:
                st.warning(f"No run() or main() found in {label}")
