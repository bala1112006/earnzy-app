import streamlit as st

# --- Page Setup ---
st.set_page_config(
    page_title="EARNZY Admin Panel",
    page_icon="⚙️",
    layout="wide"
)

# --- Custom Styles ---
st.markdown("""
    <style>
        .centered {
            text-align: center;
        }
        .card {
            background-color: #ffffff;
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            transition: 0.3s ease;
            margin-bottom: 20px;
        }
        .card:hover {
            box-shadow: 0 6px 15px rgba(0,0,0,0.2);
        }
        .btn-custom {
            padding: 10px 20px;
            font-size: 17px;
            background-color: #f63366;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            text-decoration: none;
        }
        .btn-custom:hover {
            background-color: #e02155;
        }
        @media screen and (max-width: 768px) {
            .card { padding: 18px; }
            .btn-custom { width: 100%; font-size: 18px; }
        }
    </style>
""", unsafe_allow_html=True)

# --- Title Header ---
st.markdown("<h1 class='centered'>⚙️ EARNZY Admin Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p class='centered'>Manage your app features and tools securely</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Cards Layout ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='card'>
        <h3>📢 Send Push Notification</h3>
        <p>Send image-rich notifications to all app users instantly using FCM.</p>
        <a class='btn-custom' href='https://earnzy-notify.streamlit.app' target='_blank'>🚀 Open Notifier</a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='card'>
        <h3>🧪 Play Integrity API</h3>
        <p>Verify if a device is secure and untampered before allowing access.</p>
        <a class='btn-custom' href='#' onclick="alert('Coming Soon!')">🔒 Coming Soon</a>
    </div>
    """, unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class='card'>
        <h3>📵 Device Block List</h3>
        <p>Manage rooted or banned devices directly via Firebase.</p>
        <a class='btn-custom' href='#' onclick="alert('Coming Soon!')">🔐 Coming Soon</a>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class='card'>
        <h3>📊 Notification Logs</h3>
        <p>Track which admin sent which notification and when.</p>
        <a class='btn-custom' href='#' onclick="alert('Coming Soon!')">📈 Coming Soon</a>
    </div>
    """, unsafe_allow_html=True)

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='centered' style='font-size: 13px;'>Made with ❤️ for EARNZY Team</div>", unsafe_allow_html=True)