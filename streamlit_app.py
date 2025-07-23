import streamlit as st

# --- Config ---
st.set_page_config(page_title="EARNZY Admin", layout="wide")

USERNAME = "Bala"
PASSWORD = "bala10112006"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Custom Dark UI CSS ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #000000;
        color: white;
    }
    .block-container {
        padding: 1rem;
    }
    input, textarea {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #444 !important;
        border-radius: 6px !important;
    }
    .stButton > button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        padding: 0.6em 1.3em;
        font-weight: bold;
        border-radius: 6px;
    }
    .stButton > button:hover {
        background: linear-gradient(to right, #ff4b2b, #ff416c);
    }
    .stMarkdown h1, h2, h3 {
        color: white;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        margin-top: 50px;
        color: #777;
    }
    </style>
""", unsafe_allow_html=True)

# --- Login Page ---
if not st.session_state.logged_in:
    st.markdown("## 🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Logged in successfully!")
            st.rerun()
        else:
            st.error("❌ Wrong username or password")

# --- Main Panel with Sidebar ---
else:
    # Sidebar navigation
    page = st.sidebar.radio("🔘 Navigation", ["🏠 Dashboard", "✉️ Notification", "🔓 Logout"])

    st.sidebar.markdown("---")
    st.sidebar.markdown("👑 Logged in as: **Bala**")

    if page == "🏠 Dashboard":
        st.markdown("# 🧠 EARNZY Admin Dashboard")
        st.markdown("Welcome to the EARNZY panel. Use the sidebar to navigate.")

        st.markdown("### 🔒 Security")
        st.markdown("- Root Detection: ✅ Enabled")
        st.markdown("- Play Integrity: ✅ Active")

        st.markdown("### 📊 Stats")
        st.markdown("- 🔔 Notifications sent: `1321`")
        st.markdown("- 📱 Active users today: `209`")

    elif page == "✉️ Notification":
        st.markdown("# ✉️ Send Push Notification")

        topic = st.text_input("📍 Topic (e.g. all_users)")
        title = st.text_input("📰 Title")
        body = st.text_area("📝 Message")
        image = st.text_input("🖼️ Image URL (optional)")

        if st.button("🚀 Send Notification"):
            if topic and title and body:
                st.success("✅ Notification sent successfully!")
                # [Your API call goes here]
            else:
                st.warning("⚠️ Please fill all required fields.")

    elif page == "🔓 Logout":
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<div class='footer'>© 2025 EARNZY Admin Panel — Designed by Bala 🖤</div>", unsafe_allow_html=True)