import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for dynamic widgets
if 'available_widgets' not in st.session_state:
    st.session_state['available_widgets'] = ['AI Insights', 'Total Accounts']
if 'dashboard_widgets' not in st.session_state:
    st.session_state['dashboard_widgets'] = []

# Ensure "Total Accounts" is added by default on the first load
if 'Total Accounts' not in st.session_state['dashboard_widgets'] and 'Total Accounts' in st.session_state['available_widgets']:
    st.session_state['dashboard_widgets'].append('Total Accounts')
    st.session_state['available_widgets'].remove('Total Accounts')

# Sidebar for navigation
st.sidebar.title("Menu")
selection = st.sidebar.radio("Navigate", ["Dashboard", "AskSpendy", "Settings"])

# Sample transactions data
data = [
    {"amount": -50.75, "account": "Intesa Sanpaolo", "date": "2025-01-15", "place": "Supermarket", "category": "Groceries"},
    {"amount": -120.00, "account": "Unicredit", "date": "2025-01-14", "place": "Gas Station", "category": "Transportation"},
    {"amount": -300.00, "account": "Intesa Sanpaolo", "date": "2025-01-13", "place": "Electronics Store", "category": "Shopping"},
    {"amount": -15.25, "account": "Unicredit", "date": "2025-01-12", "place": "Cafe", "category": "Dining"},
    {"amount": -500.00, "account": "Intesa Sanpaolo", "date": "2025-01-11", "place": "Online Store", "category": "Shopping"},
    {"amount": -20.00, "account": "Unicredit", "date": "2025-01-10", "place": "Pharmacy", "category": "Health"},
    {"amount": -75.00, "account": "Intesa Sanpaolo", "date": "2025-01-09", "place": "Restaurant", "category": "Dining"},
    {"amount": -45.00, "account": "Unicredit", "date": "2025-01-08", "place": "Cinema", "category": "Entertainment"},
    {"amount": -60.00, "account": "Intesa Sanpaolo", "date": "2025-01-07", "place": "Gym", "category": "Fitness"},
    {"amount": -25.00, "account": "Unicredit", "date": "2025-01-06", "place": "Bookstore", "category": "Education"},
]

transactions_df = pd.DataFrame(data)

# Function to render widgets on the dashboard
def render_widgets():
    for widget in st.session_state['dashboard_widgets']:
        with st.expander(widget, expanded=True):
            if widget == 'AI Insights':
                st.markdown("### AI Insights")
                st.write("Your Dining spending was higher by 15% than last month.")
                if st.button("Remove", key=f"remove_{widget}"):
                    st.session_state['dashboard_widgets'].remove(widget)
                    st.session_state['available_widgets'].append(widget)

            elif widget == 'Total Accounts':
                st.markdown("### Total in Accounts")
                total_balance = 20000 + 15000  # Sum of all accounts
                st.markdown(f"""
                <div style="padding: 15px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;">
                    <h2 style="color: #333;">Total Balance: €{total_balance:,}</h2>
                    <p><strong>Intesa Sanpaolo:</strong> €20,000</p>
                    <p><strong>Unicredit:</strong> €15,000</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Remove", key=f"remove_{widget}"):
                    st.session_state['dashboard_widgets'].remove(widget)
                    st.session_state['available_widgets'].append(widget)

# Main area based on sidebar selection
if selection == "Dashboard":
    # Title and subtitle
    st.markdown("<h1 style='margin-top: -50px;'>Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='margin-top: -20px;'>Welcome to your finance and budgeting app</h3>", unsafe_allow_html=True)

    # "Add Widget" button in the top-right corner
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col2:
            if st.button("Add Widget"):
                st.session_state['show_widget_selector'] = True

    if st.session_state.get('show_widget_selector', False):
        with st.expander("Available Widgets", expanded=True):
            for widget in st.session_state['available_widgets']:
                if st.button(f"Add {widget}", key=f"add_{widget}"):
                    st.session_state['dashboard_widgets'].append(widget)
                    st.session_state['available_widgets'].remove(widget)
                    st.session_state['show_widget_selector'] = False

    st.markdown("<div style='margin-bottom: 30px;'></div>", unsafe_allow_html=True)  # Add spacing
    render_widgets()  # Render the widgets

    # Collapsible widget box for recent transactions
    with st.expander("Recent Transactions", expanded=True):
        st.markdown("#### 📊 Recent Transactions")
        st.dataframe(
            transactions_df,
            height=300,  # Adjust height for scrollable view
        )

elif selection == "AskSpendy":
    st.title("AskSpendy")
    st.write("AskSpendy will be your AI assistant for financial queries.")
    # Add interactive AI or Q&A features here

elif selection == "Settings":
    st.title("Settings")
    st.write("Customize your preferences here.")
    # Add settings and configuration options here
