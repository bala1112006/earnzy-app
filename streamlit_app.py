import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="EARNZY Admin", layout="wide")

# --- Login credentials ---
USERNAME = "Bala"
PASSWORD = "bala10112006"

# --- Session flag ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Global DARK MODE UI ---
st.markdown("""
    <style>
    html, body, .stApp {
        background-color: #000000;
        color: white;
    }

    .block-container {
        padding: 0 2rem !important;
    }

    input, textarea {
        background-color: #111 !important;
        color: white !important;
        border: 1px solid #333 !important;
        border-radius: 6px !important;
    }

    .title {
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
        color: white;
    }

    .subtitle {
        text-align: center;
        font-size: 1.1em;
        color: #bbbbbb;
        margin-bottom: 40px;
    }

    .login-box {
        max-width: 400px;
        margin: 100px auto;
        padding: 30px;
        background: #111;
        border-radius: 16px;
        box-shadow: 0 0 20px rgba(255,255,255,0.08);
    }

    .login-box h2 {
        text-align: center;
        color: #ffffff;
        margin-bottom: 20px;
    }

    .dashboard {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 24px;
        padding: 20px;
    }

    .card {
        width: 300px;
        background: #1a1a1a;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 0 15px rgba(255, 255, 255, 0.05);
        text-align: center;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-6px);
        box-shadow: 0 0 25px rgba(255, 255, 255, 0.1);
    }

    .card img {
        width: 64px;
        margin-bottom: 15px;
    }

    .card h3 {
        color: white;
        font-size: 1.3em;
        margin-bottom: 10px;
    }

    .card p {
        color: #cccccc;
        font-size: 0.95em;
        margin-bottom: 15px;
    }

    .btn {
        padding: 10px 20px;
        background: #f63366;
        color: white;
        font-weight: bold;
        text-decoration: none;
        border-radius: 8px;
        transition: 0.3s;
    }

    .btn:hover {
        background: #ff4b2b;
    }

    .footer {
        text-align: center;
        font-size: 13px;
        color: #777;
        margin-top: 40px;
    }

    @media (max-width: 768px) {
        .card { width: 90%; }
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN SCREEN ---
if not st.session_state.logged_in:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown("<h2>🔐 EARNZY Admin Login</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Wrong ID or password.")

    st.markdown("</div>", unsafe_allow_html=True)

# --- DASHBOARD ---
else:
    st.markdown("<div class='title'>🧠 EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Premium black theme — white text — stylish experience</div>", unsafe_allow_html=True)

    st.markdown("<div class='dashboard'>", unsafe_allow_html=True)

    # Card 1
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/9068/9068749.png'>
            <h3>Push Notification</h3>
            <p>Send title, message & image to all users.</p>
            <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
        </div>
    """, unsafe_allow_html=True)

    # Card 2
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/5986/5986056.png'>
            <h3>Play Integrity</h3>
            <p>Detect rooted / unsafe devices using API.</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    # Card 3
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/6645/6645114.png'>
            <h3>Device Block</h3>
            <p>Block root users by Android ID remotely.</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    # Card 4
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/553/553416.png'>
            <h3>Notification Logs</h3>
            <p>Track all messages sent by admin panel.</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<div class='footer'>© 2025 EARNZY Admin | Built by Bala 💻</div>", unsafe_allow_html=True)