import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="EARNZY Admin Panel",
    page_icon="🧠",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        html, body {
            font-family: 'Poppins', sans-serif;
            background: #f1f3f6;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            font-weight: 700;
            color: #1e1e2f;
            margin-top: 0.5em;
        }
        .subtitle {
            text-align: center;
            font-size: 1.1em;
            color: #5a5a5a;
            margin-bottom: 2em;
        }
        .grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 25px;
        }
        .card {
            width: 320px;
            padding: 24px;
            border-radius: 20px;
            background: linear-gradient(to bottom right, #ffffff, #f4f6fa);
            box-shadow: 0 10px 30px rgba(0,0,0,0.06);
            text-align: center;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 14px 35px rgba(0,0,0,0.1);
        }
        .card img {
            width: 70px;
            margin-bottom: 15px;
        }
        .card h3 {
            font-size: 1.3em;
            margin: 10px 0;
            color: #2b2b3c;
        }
        .card p {
            font-size: 0.95em;
            color: #5e5e68;
            margin-bottom: 15px;
        }
        .btn {
            padding: 10px 20px;
            background: linear-gradient(to right, #ff416c, #ff4b2b);
            border-radius: 8px;
            color: white;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            transition: background 0.3s ease;
        }
        .btn:hover {
            background: linear-gradient(to right, #ff4b2b, #ff416c);
        }
        @media (max-width: 768px) {
            .card { width: 90%; }
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<div class='title'>🚀 EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Stylish control panel to manage notifications, security, and devices</div>", unsafe_allow_html=True)

# --- Cards Section ---
st.markdown("<div class='grid'>", unsafe_allow_html=True)

# --- Card 1: Notification Sender ---
st.markdown("""
<div class='card'>
    <img src='https://cdn-icons-png.flaticon.com/512/9068/9068749.png'>
    <h3>Push Notification</h3>
    <p>Send title, body, and image via FCM to all app users instantly.</p>
    <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
</div>
""", unsafe_allow_html=True)

# --- Card 2: Play Integrity ---
st.markdown("""
<div class='card'>
    <img src='https://cdn-icons-png.flaticon.com/512/5986/5986056.png'>
    <h3>Play Integrity</h3>
    <p>Verify devices before login to block rooted or modified systems.</p>
    <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
</div>
""", unsafe_allow_html=True)

# --- Card 3: Device Block List ---
st.markdown("""
<div class='card'>
    <img src='https://cdn-icons-png.flaticon.com/512/6645/6645114.png'>
    <h3>Device Block</h3>
    <p>View & manage rooted or tampered device access from Firebase.</p>
    <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
</div>
""", unsafe_allow_html=True)

# --- Card 4: Logs ---
st.markdown("""
<div class='card'>
    <img src='https://cdn-icons-png.flaticon.com/512/553/553416.png'>
    <h3>Notification Logs</h3>
    <p>Track history of notifications sent by admin with timestamps.</p>
    <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
    <hr>
    <p style='text-align:center; font-size: 13px;'>© 2025 EARNZY Admin | Designed with ❤️ by Bala</p>
""", unsafe_allow_html=True)