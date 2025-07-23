import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="EARNZY Admin Panel",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS ---
st.markdown("""
    <style>
        html, body {
            font-family: 'Arial', sans-serif;
            background: #1a1a2e;
            color: #e0e0e0;
        }
        .stApp {
            background: #1a1a2e;
        }
        .sidebar .sidebar-content {
            background: #25253f;
            color: #e0e0e0;
        }
        .title {
            text-align: center;
            font-size: 2.2em;
            font-weight: 700;
            color: #00ffcc;
            margin-bottom: 0.5em;
        }
        .subtitle {
            text-align: center;
            font-size: 1em;
            color: #a0a0b0;
            margin-bottom: 1.5em;
        }
        .grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            padding: 20px;
        }
        .card {
            width: 300px;
            padding: 20px;
            background: #2a2a4e;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            text-align: center;
            transition: transform 0.2s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card h3 {
            font-size: 1.3em;
            color: #00ffcc;
            margin: 10px 0;
        }
        .card p {
            font-size: 0.9em;
            color: #b0b0c0;
            margin-bottom: 15px;
        }
        .btn {
            padding: 8px 16px;
            background: #00cc99;
            border-radius: 6px;
            color: #1a1a2e;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            transition: background 0.3s ease;
        }
        .btn:hover {
            background: #00ffcc;
        }
        .footer {
            text-align: center;
            font-size: 0.85em;
            color: #606070;
            margin-top: 2em;
            padding-top: 1em;
            border-top: 1px solid #2a2a4e;
        }
        @media (max-width: 768px) {
            .card { width: 100%; }
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<h2 style='color: #00ffcc; text-align: center;'>EARNZY Admin</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #a0a0b0; text-align: center;'>Manage your platform</p>", unsafe_allow_html=True)
    st.markdown("---")
    option = st.selectbox("Navigation", ["Dashboard", "Notifications", "Security", "Devices", "Logs"], index=0)
    st.markdown("---")
    st.markdown("<p style='color: #606070; text-align: center;'>© 2025 EARNZY</p>", unsafe_allow_html=True)

# --- Main Content ---
st.markdown("<div class='title'>⚡ EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Control notifications, security, and devices seamlessly</div>", unsafe_allow_html=True)

# --- Cards Section ---
st.markdown("<div class='grid'>", unsafe_allow_html=True)

if option == "Dashboard" or option == "Notifications":
    st.markdown("""
        <div class='card'>
            <h3>Push Notification</h3>
            <p>Send title, body, and image via FCM to all app users instantly.</p>
            <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
        </div>
    """, unsafe_allow_html=True)

if option == "Dashboard" or option == "Security":
    st.markdown("""
        <div class='card'>
            <h3>Play Integrity</h3>
            <p>Verify devices before login to block rooted or modified systems.</p>
            <a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

if option == "Dashboard" or option == "Devices":
    st.markdown("""
        <div class='card'>
            <h3>Device Block</h3>
            <p>View & manage rooted or tampered device access from Firebase.</p>
            <a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

if option == "Dashboard" or option == "Logs":
    st.markdown("""
        <div class='card'>
            <h3>Notification Logs</h3>
            <p>Track history of notifications sent by admin with timestamps.</p>
            <a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>© 2025 EARNZY Admin | Designed with ❤️ by Bala</div>", unsafe_allow_html=True)

# --- Version ---
st.markdown("<p style='text-align: center; color: #606070; font-size: 0.8em;'>Version 1.0.0</p>", unsafe_allow_html=True)