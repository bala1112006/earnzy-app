import streamlit as st

# --- Config ---
st.set_page_config(page_title="EARNZY Admin", layout="wide")

USERNAME = "Bala"
PASSWORD = "bala10112006"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# --- Custom CSS ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #000000;
        color: white;
        padding-top: 96px !important;  /* ~2 inch space */
    }

    section[data-testid="stSidebar"] > div {
        background-color: #111 !important;
        padding: 20px;
        border-radius: 12px;
        height: 100%;
        box-shadow: 0 0 20px rgba(255,255,255,0.05);
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
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        width: 100%;
        margin-bottom: 10px;
    }

    .stButton > button:hover {
        background: linear-gradient(to right, #ff4b2b, #ff416c);
    }

    .center-card {
        max-width: 400px;
        margin: 40px auto;
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

    @media(max-width: 768px){
        .center-card { width: 90%; margin-top: 60px; }
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN FIX ---
if not st.session_state.logged_in:
    st.markdown("## 🔐 Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Logged in successfully!")
            st.stop()  # Pause after login to avoid showing login form
        else:
            st.error("❌ Wrong credentials")
    st.stop()  # Always stop when not logged in

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("## 🔧 Admin Menu")

    if st.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"

    if st.button("✉️ Notification"):
        st.session_state.page = "Notification"

    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "Dashboard"

    st.markdown("---")
    st.markdown("👤 Logged in as: **Bala**")

# --- PAGE: DASHBOARD ---
if st.session_state.page == "Dashboard":
    st.markdown("## 🧠 Dashboard")

    st.markdown("""
        <div class='center-card'>
            <h3>📢 Notifications Sent</h3>
            <p><b>Loading count...</b></p>
            <p>Track push alerts sent via panel.</p>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE: NOTIFICATION ---
elif st.session_state.page == "Notification":
    st.markdown("# ✉️ Send Push Notification")

    topic = st.text_input("📍 Topic (e.g. all_users)")
    title = st.text_input("📰 Title")
    body = st.text_area("📝 Message")
    image = st.text_input("🖼️ Image URL (optional)")

    if st.button("🚀 Send Notification"):
        if topic and title and body:
            st.success("✅ Notification sent successfully!")
            # Add API logic here
        else:
            st.warning("⚠️ Please fill all required fields.")

# --- FOOTER ---
st.markdown("<div class='footer'>© 2025 EARNZY Admin — Built with ❤️ by Bala</div>", unsafe_allow_html=True)