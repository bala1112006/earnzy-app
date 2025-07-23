import streamlit as st

# ✅ Page setup
st.set_page_config(
    page_title="EARNZY Admin",
    page_icon="🛠️",
    layout="wide"
)

# ✅ Custom CSS for mobile + fixed layout + beautiful UI
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f8f9fc;
        }
        .main-title {
            text-align: center;
            font-size: 2.4em;
            font-weight: bold;
            color: #111;
            margin-top: 10px;
        }
        .sub-title {
            text-align: center;
            font-size: 1em;
            color: #555;
            margin-bottom: 40px;
        }
        .card {
            background: white;
            border-radius: 18px;
            padding: 25px 20px;
            margin-bottom: 25px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.06);
            text-align: center;
            transition: 0.3s ease;
        }
        .card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 25px rgba(0,0,0,0.08);
        }
        .card img {
            width: 64px;
            margin-bottom: 15px;
        }
        .card h3 {
            margin: 10px 0 8px;
            font-size: 1.3em;
        }
        .card p {
            font-size: 0.95em;
            color: #666;
        }
        .btn {
            display: inline-block;
            margin-top: 12px;
            padding: 10px 18px;
            background-color: #f63366;
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
        }
        .btn:hover {
            background-color: #e02155;
        }
        .card-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }
        @media (max-width: 768px) {
            .card {
                width: 100% !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Title & Subtitle
st.markdown("<div class='main-title'>🚀 EARNZY Admin Panel</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Manage your app with tools like push notification, integrity check, and device blocking</div>", unsafe_allow_html=True)

# ✅ Cards Grid
st.markdown("<div class='card-grid'>", unsafe_allow_html=True)

# ✅ Push Notification Card
st.markdown("""
    <div class='card' style='width: 300px;'>
        <img src='https://cdn-icons-png.flaticon.com/512/9068/9068749.png'>
        <h3>Push Notification</h3>
        <p>Send title, body and image via FCM to all users.</p>
        <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Play Integrity Card
st.markdown("""
    <div class='card' style='width: 300px;'>
        <img src='https://cdn-icons-png.flaticon.com/512/5986/5986056.png'>
        <h3>Play Integrity</h3>
        <p>Verify if a device is safe and unrooted via API.</p>
        <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Blocked Device Card
st.markdown("""
    <div class='card' style='width: 300px;'>
        <img src='https://cdn-icons-png.flaticon.com/512/6645/6645114.png'>
        <h3>Device Block List</h3>
        <p>Control rooted or banned devices using Firebase.</p>
        <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Notification Logs Card
st.markdown("""
    <div class='card' style='width: 300px;'>
        <img src='https://cdn-icons-png.flaticon.com/512/553/553416.png'>
        <h3>Notification Logs</h3>
        <p>Track when and what notification was sent.</p>
        <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Close grid
st.markdown("</div>", unsafe_allow_html=True)

# ✅ Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size: 13px;'>© 2025 EARNZY Admin Panel | All rights reserved.</p>", unsafe_allow_html=True)