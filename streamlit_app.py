import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="EARNZY Admin Panel",
    page_icon="🚀",
    layout="wide"
)

# --- Custom CSS Style ---
st.markdown("""
    <style>
        body { background-color: #f4f6f9; }
        .main-title {
            text-align: center;
            font-size: 2.4em;
            font-weight: bold;
            color: #222831;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #555;
            margin-bottom: 40px;
        }
        .card-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
        }
        .card {
            background: linear-gradient(145deg, #ffffff, #f1f1f1);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border-radius: 16px;
            padding: 30px;
            width: 320px;
            text-align: center;
            transition: all 0.3s ease;
        }
        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        }
        .card h3 {
            margin-top: 10px;
            font-size: 1.4em;
            color: #222;
        }
        .card p {
            color: #555;
            font-size: 1em;
        }
        .card a {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 20px;
            background-color: #f63366;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        .card a:hover {
            background-color: #e02155;
        }
        @media (max-width: 768px) {
            .card { width: 90%; }
        }
    </style>
""", unsafe_allow_html=True)

# --- UI Header ---
st.markdown("<div class='main-title'>🚀 EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Manage features, send push alerts, and control your app securely</div>", unsafe_allow_html=True)

# --- UI Cards ---
st.markdown("<div class='card-container'>", unsafe_allow_html=True)

# Card 1: Notification Sender
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/9068/9068749.png' width='80'/>
        <h3>Send Notification</h3>
        <p>Send FCM push notifications with title, body, and image.</p>
        <a href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
    </div>
""", unsafe_allow_html=True)

# Card 2: Device Block
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/6645/6645114.png' width='80'/>
        <h3>Device Block List</h3>
        <p>View and manage blocked rooted/tampered devices.</p>
        <a href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# Card 3: Play Integrity
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/5986/5986056.png' width='80'/>
        <h3>Play Integrity Check</h3>
        <p>Validate real, secure devices using Google's API.</p>
        <a href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# Card 4: Logs
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/553/553416.png' width='80'/>
        <h3>Notification Logs</h3>
        <p>Track history of notifications sent by admin.</p>
        <a href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center; font-size:13px;'>© 2025 EARNZY Admin | Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)