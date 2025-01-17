import streamlit as st

# Sidebar for navigation
st.sidebar.title("Menu")
selection = st.sidebar.radio("Navigate", ["Dashboard", "AskSpendy", "Settings"])

# Main area based on sidebar selection
if selection == "Dashboard":
    # Title and subtitle
    st.markdown("<h1 style='margin-top: -50px;'>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top: -20px;'>Welcome to your finance and budgeting app</h3>", unsafe_allow_html=True)

    # Widget box for accounts
    st.markdown("---")  # Horizontal rule for visual separation
    st.markdown("### 🏦 Total in Accounts")
    
    # Widget-like box styling
    total_balance = 20000 + 15000  # Sum of all accounts
    st.markdown(f"""
    <div style="padding: 15px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;">
        <h2 style="color: #333;">Total Balance: €{total_balance:,}</h2>
        <p>💳 <strong>Intesa Sanpaolo:</strong> €20,000</p>
        <p>💳 <strong>Unicredit:</strong> €15,000</p>
    </div>
    """, unsafe_allow_html=True)

elif selection == "AskSpendy":
    st.title("AskSpendy")
    st.write("AskSpendy will be your AI assistant for financial queries.")
    # Add interactive AI or Q&A features here

elif selection == "Settings":
    st.title("Settings")
    st.write("Customize your preferences here.")
    # Add settings and configuration options here
