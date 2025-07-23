import streamlit as st

# ---- Page Config ----
st.set_page_config(
    page_title="EARNZY Admin Dashboard",
    page_icon="🛠️",
    layout="centered"
)

# ---- Custom Header ----
st.markdown("""
    <h1 style="text-align:center; font-size:2.3em;">🛠️ EARNZY Admin Panel</h1>
    <p style="text-align:center; font-size:1.1em; color:gray;">
        Manage your app – send notifications, monitor status, and more.
    </p>
    <hr>
""", unsafe_allow_html=True)

# ---- Main Options ----
st.subheader("📋 Tools Available")

# Button: Open Notification Sender Page
st.markdown("""
<div style='text-align:center;'>
    <a href="https://earnzy-notify.streamlit.app" target="_blank">
        <button style="padding: 0.7em 1.4em; font-size: 1.1em; background-color: #f63366; color: white; border: none; border-radius: 6px; cursor: pointer;">
            🚀 Open Notification Sender
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# Future items
st.markdown("### 🧪 Coming Soon:")
st.markdown("- 🔐 Device Block Management")
st.markdown("- 📈 Analytics & Logs")
st.markdown("- 🧩 Play Integrity Verification")

# ---- Footer ----
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 13px;'>Made with ❤️ by EARNZY Team</div>", unsafe_allow_html=True)