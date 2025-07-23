import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="EARNZY Admin Panel",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        html, body {
            font-family: 'Arial', sans-serif;
            background: #f5f5f5;
            color: #333;
        }
        .stApp {
            background: #f5f5f5;
        }
        .sidebar .sidebar-content {
            background: #ffffff;
            border-right: 1px solid #ddd;
        }
        .header {
            font-size: 1.8em;
            font-weight: bold;
            color: #222;
            margin: 0.5em 0;
        }
        .subheader {
            font-size: 1em;
            color: #666;
            margin-bottom: 1.5em;
        }
        .section-container {
            background: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.2em;
            font-weight: 600;
            color: #222;
            margin-bottom: 10px;
        }
        .section-content {
            font-size: 0.9em;
            color: #555;
            margin-bottom: 15px;
        }
        .action-btn {
            padding: 8px 16px;
            background: #007bff;
            border-radius: 5px;
            color: white;
            font-weight: 500;
            text-decoration: none;
            display: inline-block;
            transition: background 0.2s ease;
        }
        .action-btn:hover {
            background: #0056b3;
        }
        .footer {
            text-align: center;
            font-size: 0.85em;
            color: #777;
            margin-top: 2em;
            padding-top: 1em;
            border-top: 1px solid #ddd;
        }
        .stExpander {
            border: 1px solid #eee;
            border-radius: 5px;
        }
        @media (max-width: 768px) {
            .section-container {
                padding: 15px;
            }
            .header {
                font-size: 1.5em;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- Helper Function for Feature Sections ---
def render_feature_section(title, description, button_text, button_url=None, coming_soon=False):
    with st.expander(title, expanded=False):
        st.markdown(f"<div class='section-container'>", unsafe_allow_html=True)
        st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section-content'>{description}</div>", unsafe_allow_html=True)
        if coming_soon:
            st.button(button_text, on_click=lambda: st.warning("This feature is coming soon!"))
        else:
            st.markdown(f"<a class='action-btn' href='{button_url}' target='_blank'>{button_text}</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<div class='header'>EARNZY Admin</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Manage your platform</div>", unsafe_allow_html=True)
    st.markdown("---")
    menu = ["Home", "Notifications", "Security", "Devices", "Logs"]
    choice = st.selectbox("Navigate", menu, index=0, label_visibility="collapsed")
    st.markdown("---")
    st.markdown("<div class='footer'>Version 1.0.0</div>", unsafe_allow_html=True)

# --- Main Content ---
st.markdown("<div class='header'>⚙️ EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Manage notifications, security, and devices with ease</div>", unsafe_allow_html=True)

# --- Dynamic Content Based on Sidebar Selection ---
if choice == "Home":
    st.write("### Overview")
    st.markdown("Welcome to the EARNZY Admin Panel. Use the sidebar to navigate to specific features.")
    st.markdown("**Quick Stats** (Placeholder):")
    st.metric("Active Users", "10,000")
    st.metric("Notifications Sent", "500")
    st.metric("Devices Blocked", "25")

elif choice == "Notifications":
    render_feature_section(
        title="Push Notification",
        description="Send title, body, and image via FCM to all app users instantly.",
        button_text="Open Sender",
        button_url="https://earnzy-notify.streamlit.app"
    )
    render_feature_section(
        title="Notification Logs",
        description="Track history of notifications sent by admin with timestamps.",
        button_text="View Logs",
        coming_soon=True
    )

elif choice == "Security":
    render_feature_section(
        title="Play Integrity",
        description="Verify devices before login to block rooted or modified systems.",
        button_text="Manage Integrity",
        coming_soon=True
    )

elif choice == "Devices":
    render_feature_section(
        title="Device Block",
        description="View and manage rooted or tampered device access from Firebase.",
        button_text="Manage Devices",
        coming_soon=True
    )

elif choice == "Logs":
    st.write("### Notification Logs")
    st.markdown("View the history of all actions performed in the admin panel.")
    st.info("Log viewing is under development. Check back soon!")

# --- Footer ---
st.markdown("<div class='footer'>© 2025 EARNZY Admin | Designed by Bala</div>", unsafe_allow_html=True)