import streamlit as st
import hashlib
import json
import os
st.set_page_config(
    page_title="My Trader's Hub ",  # Page title in the browser tab
    page_icon=":sparkles:",       # Page icon, can use emoji or path to an image
    layout="wide"                 # Layout of the app: 'wide' or 'centered'
)

# Your application code starts here
st.title("Welcome to My Trader's Hub 📈💵:rocket:")
st.write("💲Trader's Hub offers secure financial analysis for options trading with customizable views and key metrics like the Put-Call Ratio (PCR).")
# File path for user storage
USER_FILE = 'users.json'

# Helper functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

# Load existing users
users_db = load_users()

# Login page
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username in users_db and verify_password(users_db[username], password):
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.session_state['page'] = 'main'  # Redirect to main application
            st.rerun()  
        else:
            st.error("Invalid username or password")

# Signup page
def signup_page():
    st.title("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign Up"):
        if username in users_db:
            st.error("Username already exists")
        else:
            users_db[username] = hash_password(password)
            save_users(users_db)
            st.success("Account created successfully! Please log in.")
            st.session_state['page'] = 'login'  # Redirect to login after successful signup

# Main application
def main_app():
    st.write(f"Welcome, {st.session_state['username']}!")
    # Import and run `nse.py` after login
    try:
        import nse
        nse.main()  # Ensure that `nse.py` has a `main` function
    except ImportError:
        st.error("Failed to import the Trader's Hub .")

# Check login state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'  # Default to login page

# Sidebar for navigation
if not st.session_state['logged_in']:
    page = st.sidebar.selectbox("Login / Signup", ["Login", "Sign Up"])
    if page == "Login":
        st.session_state['page'] = 'login'
    elif page == "Sign Up":
        st.session_state['page'] = 'signup'

# Show the appropriate page based on the session state
if st.session_state['logged_in']:
    main_app()
else:
    if st.session_state['page'] == 'login':
        
        login_page()
    elif st.session_state['page'] == 'signup':
        signup_page()
