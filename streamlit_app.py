import streamlit as st

# ---- Page Config ----
st.set_page_config(
    page_title="EARNZY Admin",
    page_icon="🛠️",
    layout="centered"
)

# ---- Title ----
st.markdown("<h1 style='text-align: center;'>🛠️ EARNZY Admin Panel</h1>", unsafe_allow_html=True)
st.caption("Manage app features, send notifications, and monitor tools.")

st.markdown("---")

# ---- Admin Options ----
st.subheader("📋 Available Tools")

st.markdown("### 🔔 Send Push Notification")
if st.button("Open Notification Sender"):
    st.switch_page("app.py")  # Only works when deployed as multipage Streamlit app

# Future options
st.markdown("### 🚧 Under Development")
st.markdown("- 🔐 Device Blocking UI (soon)")
st.markdown("- 📈 View Notification Logs")
st.markdown("- 🧪 Play Integrity Check")

# ---- Footer ----
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 13px;'>Made with ❤️ for EARNZY</div>", unsafe_allow_html=True)