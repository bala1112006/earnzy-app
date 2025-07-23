import streamlit as st
import requests

# ---- Page Config ----
st.set_page_config(
    page_title="📢 EARNZY Notifier",
    page_icon="📲",
    layout="centered"
)

# ---- Title and Info ----
st.markdown("<h2 style='text-align: center;'>📢 EARNZY Push Notification Panel</h2>", unsafe_allow_html=True)
st.caption("Send secure push notifications to all app users via FCM + Firebase.")

st.markdown("---")

# ---- Input Fields ----
with st.form("notify_form"):
    col1, col2 = st.columns(2)
    with col1:
        title = st.text_input("🔖 Title", placeholder="e.g. 🔥 Daily Task")
    with col2:
        auth = st.text_input("🔐 Auth Token", placeholder="Enter your secret auth", type="password")

    body = st.text_area("📝 Message Body", placeholder="e.g. Claim your 20 coins now!", height=100)
    image = st.text_input("🖼️ Image URL (optional)", placeholder="https://yourcdn.com/image.png")

    submit = st.form_submit_button("🚀 Send Notification")

# ---- On Submit ----
if submit:
    if not all([title.strip(), body.strip(), auth.strip()]):
        st.warning("⚠️ Please fill all required fields: Title, Body, and Auth Token.")
    else:
        with st.spinner("Sending notification..."):
            try:
                response = requests.post(
                    f"https://api.earnzy.com.in/notify?auth={auth.strip()}",
                    headers={"Content-Type": "application/json"},
                    json={
                        "topic": "all_users",
                        "title": title.strip(),
                        "body": body.strip(),
                        "image": image.strip()
                    }
                )
                if response.ok:
                    st.success("✅ Notification sent successfully!")
                    st.code(response.text, language="json")
                else:
                    st.error(f"❌ Error: {response.status_code}")
                    st.code(response.text, language="json")
            except Exception as e:
                st.error("❌ Failed to send notification.")
                st.exception(e)

# ---- Footer ----
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 13px;'>Made with ❤️ for EARNZY</div>", unsafe_allow_html=True)