import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="EARNZY Notifier", page_icon="🔔", layout="centered")
st.title("🔔 EARNZY Notification Sender")
st.markdown("Send FCM push notifications to all users via API")

# Input Fields
title = st.text_input("📌 Notification Title", "🔥 Daily Task")
body = st.text_input("📝 Notification Body", "Claim 20 coins now!")
image = st.text_input("🖼️ Image URL (Optional)", "https://earnzy.com.in/assets/daily.png")
auth_token = st.text_input("🔐 Auth Token", "bala10112006", type="password")

# Submit Button
if st.button("🚀 Send Notification"):
    with st.spinner("Sending..."):
        try:
            url = f"https://api.earnzy.com.in/notify?auth={auth_token}"
            headers = { "Content-Type": "application/json" }
            data = {
                "topic": "all_users",
                "title": title,
                "body": body,
                "image": image
            }

            response = requests.post(url, headers=headers, json=data)
            st.success("✅ Notification sent!")
            st.code(response.text, language="json")

        except Exception as e:
            st.error(f"❌ Failed to send: {str(e)}")