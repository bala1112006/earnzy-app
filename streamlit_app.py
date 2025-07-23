import streamlit as st

# --- Config ---
st.set_page_config(page_title="EARNZY Admin", layout="centered")

USERNAME = "Bala"
PASSWORD = "bala10112006"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Global Dark Theme CSS ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    .block-container {
        padding: 1rem;
    }
    input, textarea {
        background-color: #111 !important;
        color: #ffffff !important;
        border: 1px solid #444 !important;
        border-radius: 6px !important;
    }
    .stTextInput > div > div > input {
        background-color: #111 !important;
        color: #fff !important;
    }
    .stButton > button {
        background: linear-gradient(to right, #ff416c, #ff4b2b);
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 6px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background: linear-gradient(to right, #ff4b2b, #ff416c);
    }
    .stMarkdown h1, h2, h3, h4 {
        color: white;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        margin-top: 40px;
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

# --- Clean UI After Login ---
else:
    st.markdown("# ✉️ Send Push Notification")

    topic = st.text_input("📍 Topic (e.g. all_users)")
    title = st.text_input("📰 Title")
    body = st.text_area("📝 Message")
    image = st.text_input("🖼️ Image URL (optional)")

    if st.button("🚀 Send Notification"):
        if topic and title and body:
            st.success("✅ Notification sent successfully!")
            # Here you'd trigger your backend API request
        else:
            st.warning("⚠️ Please fill all required fields.")

    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<div class='footer'>© 2025 EARNZY Admin | Built with 🖤 by Bala</div>", unsafe_allow_html=True)