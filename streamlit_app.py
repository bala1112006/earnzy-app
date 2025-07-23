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
            font-family: 'Inter', sans-serif;
            background: #0a0a15;
            color: #e0e0e0;
        }
        .stApp {
            background: #0a0a15;
        }
        .sidebar .sidebar-content {
            background: #1a1a2e;
            color: #e0e0e0;
        }
        .title {
            text-align: left;
            font-size: 2.2em;
            font-weight: 800;
            color: #00ffcc;
            margin-bottom: 0.2em;
        }
        .subtitle {
            text-align: left;
            font-size: 1em;
            color: #a0a0b0;
            margin-bottom: 1.5em;
        }
        .stTabs [data-baseweb="tab-list"] {
            background: #1a1a2e;
            border-radius: 10px;
            padding: 5px;
        }
        .stTabs [data-baseweb="tab"] {
            color: #a0a0b0;
            font-weight: 500;
            padding: 10px 20px;
            border-radius: 8px;
            margin: 5px;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background: #2a2a4e;
            color: #00ffcc;
        }
        .stTabs [aria-selected="true"] {
            background: #2a2a4e;
            color: #00ffcc;
            font-weight: 600;
        }
        .tab-content {
            background: #1a1a2e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }
        .action-card {
            background: #25253f;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            transition: transform 0.2s ease;
        }
        .action-card:hover {
            transform: translateY(-3px);
            background: #2f2f5a;
        }
        .action-card h3 {
            font-size: 1.2em;
            color: #00ffcc;
            margin: 0 0 10px 0;
        }
        .action-card p {
            font-size: 0.9em;
            color: #b0b0c0;
            margin-bottom: 15px;
        }
        .btn {
            padding: 8px 16px;
            background: linear-gradient(to right, #00ffcc, #00cc99);
            border-radius: 6px;
            color: #0a0a15;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s ease;
        }
        .btn:hover {
            background: linear-gradient(to right, #00cc99, #00ffcc);
            color: #fff;
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
            .action-card {
                padding: 15px;
            }
            .title {
                font-size: 1.8em;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<div class='title'>EARNZY Admin</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Manage your platform with ease</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Navigation")
    selected = st.radio(
        "",
        ["Dashboard", "Settings", "Logs"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.markdown("<p style='font-size: 0.9em; color: #606070;'>© 2025 EARNZY</p>", unsafe_allow_html=True)

# --- Main Content ---
st.markdown("<div class='title'>⚡ EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Control notifications, security, and devices seamlessly</div>", unsafe_allow_html=True)

# --- Tabs for Features ---
tab1, tab2, tab3 = st.tabs(["Notifications", "Security", "Devices"])

with tab1:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='action-card'>", unsafe_allow_html=True)
    st.markdown("<h3>Push Notification</h3>", unsafe_allow_html=True)
    st.markdown("<p>Send title, body, and image via FCM to all app users instantly.</p>", unsafe_allow_html=True)
    st.markdown("<a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='action-card'>", unsafe_allow_html=True)
    st.markdown("<h3>Notification Logs</h3>", unsafe_allow_html=True)
    st.markdown("<p>Track history of notifications sent by admin with timestamps.</p>", unsafe_allow_html=True)
    st.markdown("<a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='action-card'>", unsafe_allow_html=True)
    st.markdown("<h3>Play Integrity</h3>", unsafe_allow_html=True)
    st.markdown("<p>Verify devices before login to block rooted or modified systems.</p>", unsafe_allow_html=True)
    st.markdown("<a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='tab-content'>", unsafe_allow_html=True)
    st.markdown("<div class='action-card'>", unsafe_allow_html=True)
    st.markdown("<h3>Device Block</h3>", unsafe_allow_html=True)
    st.markdown("<p>View & manage rooted or tampered device access from Firebase.</p>", unsafe_allow_html=True)
    st.markdown("<a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>© 2025 EARNZY Admin | Designed with ❤️ by Bala</div>", unsafe_allow_html=True)