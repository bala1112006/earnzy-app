import streamlit as st
import requests

# --- App Config ---
st.set_page_config(page_title="EARNZY Admin", layout="wide")

USERNAME = "Bala"
PASSWORD = "bala10112006"
EXPECTED_API_KEY = "bala10112006"  # Expected API key for validation

# --- Session Init ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# --- Custom CSS ---
st.markdown("""
<style>
html, body, .stApp {
    background-color: #000;
    color: white;
    padding-top: 96px !important;
}
section[data-testid="stSidebar"] > div {
    background-color: #111 !important;
    padding: 20px;
    border-radius: 12px;
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

# =====================
# 🔐 LOGIN PAGE
# =====================
if not st.session_state.logged_in:
    with st.container():
        st.markdown("## 🔐 Admin Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.session_state.page = "Dashboard"
                st.rerun()
            else:
                st.error("❌ Invalid credentials")
    st.stop()

# =====================
# ✅ MAIN APP UI
# =====================

# --- Sidebar ---
with st.sidebar:
    st.markdown("## 🔧 Admin Menu")

    if st.button("🏠 Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()

    if st.button("✉️ Notification"):
        st.session_state.page = "Notification"
        st.rerun()

    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "Dashboard"
        st.rerun()

    st.markdown("---")
    st.markdown("👤 Logged in as: **Bala**")

# --- Main Pages ---
if st.session_state.page == "Dashboard":
    st.markdown("## 🧠 Dashboard")
    st.markdown("""
        <div class='center-card'>
            <h3>📢 Notifications Sent</h3>
            <p><b>Loading count...</b></p>
            <p>Track push alerts sent via panel.</p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Notification":
    st.markdown("# ✉️ Send Push Notification")
    topic = st.text_input("📍 Topic (e.g. all_users)")
    title = st.text_input("📰 Title")
    body = st.text_area("📝 Message")
    image = st.text_input("🖼️ Image URL (optional)")
    device_token = st.text_input("📱 Device Token (optional)")
    api_key = st.text_input("🔑 API Key", type="password")

    if st.button("🚀 Send Notification"):
        if topic and title and body and api_key:
            # Validate API key
            if api_key != EXPECTED_API_KEY:
                st.error("❌ Invalid API key")
            else:
                # Prepare the payload
                payload = {
                    "topic": topic,
                    "title": title,
                    "body": body,
                }
                if image:
                    payload["image"] = image
                if device_token:
                    payload["device_token"] = device_token

                # Send the POST request
                try:
                    response = requests.post(
                        "https://api.earnzy.com.in/notify",
                        headers={"Content-Type": "application/json", "auth": api_key},
                        json=payload,
                    )
                    if response.status_code == 200:
                        st.success("✅ Notification sent successfully!")
                    else:
                        st.error(f"❌ Failed to send notification: {response.status_code} - {response.text}")
                except requests.RequestException as e:
                    st.error(f"🛑 Error sending notification: {str(e)}")
        else:
            st.warning("⚠️ Please fill all required fields (Topic, Title, Message, API Key).")

# --- Footer ---
st.markdown("<div class='footer'>© 2025 EARNZY Admin — Designed for Bala 🖤</div>", unsafe_allow_html=True)