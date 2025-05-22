
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
CATEGORY_PATHS = {
    "AI Tools": os.path.join(MODULES_DIR, "ai"),
    "Sponsorship Tools": os.path.join(MODULES_DIR, "sponsorship"),
    "Ops Tools": os.path.join(MODULES_DIR, "ops"),
    "Finance Tools": os.path.join(MODULES_DIR, "finance"),
    "Membership Tools": os.path.join(MODULES_DIR, "membership")
}

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

    category = st.sidebar.selectbox("Choose a Tool Category", list(CATEGORY_PATHS.keys()))
    selected_path = CATEGORY_PATHS[category]
    tools = []

    for file in os.listdir(selected_path):
        if file.endswith(".py") and file != "__init__.py":
            tool_name, tool_mod = load_tool(os.path.join(selected_path, file))
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
