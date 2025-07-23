import streamlit as st

# --- Config ---
st.set_page_config(page_title="EARNZY Admin", layout="wide")

USERNAME = "Bala"
PASSWORD = "bala10112006"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# --- CSS: Minimal Black UI + 1 Centered Card ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #000000;
        color: white;
    }

    .block-container {
        padding: 0 2rem !important;
    }

    .sidebar {
        background-color: #111;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(255,255,255,0.05);
        height: 100%;
    }

    .stButton > button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #ff4b2b, #ff416c);
    }

    input, textarea {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #444 !important;
        border-radius: 6px !important;
    }

    .nav-button {
        display: block;
        background: none;
        border: none;
        color: white;
        font-size: 16px;
        text-align: left;
        padding: 12px;
        margin-bottom: 8px;
        border-radius: 8px;
        transition: 0.2s;
        width: 100%;
    }

    .nav-button:hover {
        background-color: #222;
    }

    .center-card {
        max-width: 400px;
        margin: 60px auto;
        background: #111;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 0 20px rgba(255,255,255,0.05);
        text-align: center;
    }

    .center-card h3 {
        font-size: 1.4em;
        margin-bottom: 10px;
        color: white;
    }

    .center-card p {
        font-size: 0.95em;
        color: #aaa;
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 12px;
        color: #777;
    }
    </style>
""", unsafe_allow_html=True)

# --- Login ---
if not st.session_state.logged_in:
    st.markdown("## 🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("❌ Wrong credentials")

# --- Main Layout ---
else:
    # Sidebar
    with st.sidebar:
        st.markdown("<div class='sidebar'>", unsafe_allow_html=True)

        if st.button("🏠 Dashboard", key="dash_btn"):
            st.session_state.page = "Dashboard"
        if st.button("✉️ Notification", key="notify_btn"):
            st.session_state.page = "Notification"
        if st.button("🔓 Logout", key="logout_btn"):
            st.session_state.logged_in = False
            st.session_state.page = "Dashboard"
            st.experimental_rerun()

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("👤 **Logged in as:** Bala")
        st.markdown("</div>", unsafe_allow_html=True)

    # Page: Dashboard
    if st.session_state.page == "Dashboard":
        st.markdown("## 🧠 Dashboard")

        st.markdown("""
            <div class='center-card'>
                <h3>📢 Notifications Sent</h3>
                <p><b>Loading count...</b></p>
                <p>Track push alerts sent via panel.</p>
            </div>
        """, unsafe_allow_html=True)

    # Page: Notification
    elif st.session_state.page == "Notification":
        st.markdown("# ✉️ Send Push Notification")

        topic = st.text_input("📍 Topic (e.g. all_users)")
        title = st.text_input("📰 Title")
        body = st.text_area("📝 Message")
        image = st.text_input("🖼️ Image URL (optional)")

        if st.button("🚀 Send Notification"):
            if topic and title and body:
                st.success("✅ Notification sent successfully!")
                # Replace with API call
            else:
                st.warning("⚠️ Please fill all required fields.")

    # Footer
    st.markdown("<div class='footer'>© 2025 EARNZY Admin — Built for Bala 🖤</div>", unsafe_allow_html=True)