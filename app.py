import streamlit as st
import requests

st.set_page_config(page_title="EARNZY Push", page_icon="🚀")

st.title("📢 Send Push Notification")
st.caption("Send notifications via FCM with custom data")

title = st.text_input("Notification Title", "🔥 Daily Task")
body = st.text_input("Notification Body", "Claim 20 coins now!")
image = st.text_input("Image URL", "https://earnzy.com.in/assets/daily.png")

if st.button("🚀 Send Now"):
    payload = {
        "topic": "all_users",
        "title": title,
        "body": body,
        "image": image
    }
    try:
        res = requests.post("https://api.earnzy.com.in/notify?auth=bala10112006", json=payload)
        st.success("✅ Notification sent!")
        st.code(res.text)
    except Exception as e:
        st.error(f"❌ Failed to send: {e}")