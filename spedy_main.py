import streamlit as st

# Sidebar for navigation
st.sidebar.title("Menu")
selection = st.sidebar.radio("Navigate", ["Dashboard", "AskSpendy", "Settings"])

# Main area based on sidebar selection
if selection == "Dashboard":
    st.title("Dashboard")
    st.write("Welcome to your finance and budgeting app. This is the dashboard.")
    # Add dashboard components here

elif selection == "AskSpendy":
    st.title("AskSpendy")
    st.write("AskSpendy will be your AI assistant for financial queries.")
    # Add interactive AI or Q&A features here

elif selection == "Settings":
    st.title("Settings")
    st.write("Customize your preferences here.")
    # Add settings and configuration options here
