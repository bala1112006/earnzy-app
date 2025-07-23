import streamlit as st

# --- App Config ---
st.set_page_config(
    page_title="EARNZY Admin",
    page_icon="📱",
    layout="wide"
)

# --- Login Credentials ---
USERNAME = "Bala"
PASSWORD = "bala10112006"

# --- Session State ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Global CSS to remove block theme ---
st.markdown("""
    <style>
        /* Remove native padding/margin */
        .block-container {
            padding: 0 1.5rem !important;
        }

        /* Global font and background */
        html, body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(to right, #f8f9fc, #eef1f7);
        }

        .title {
            text-align: center;
            font-size: 2.3em;
            font-weight: bold;
            margin-top: 20px;
            color: #212529;
        }

        .subtitle {
            text-align: center;
            font-size: 1em;
            color: #5c5f66;
            margin-bottom: 35px;
        }

        .login-box {
            max-width: 400px;
            margin: 100px auto;
            padding: 30px 25px;
            background: white;
            border-radius: 16px;
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.1);
        }

        .login-box h2 {
            color: #f63366;
            text-align: center;
            margin-bottom: 20px;
        }

        .dashboard {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 25px;
            padding: 20px 10px;
        }

        .card {
            width: 300px;
            background: white;
            border-radius: 18px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.08);
            padding: 24px;
            text-align: center;
            transition: 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        }

        .card img {
            width: 60px;
            margin-bottom: 14px;
        }

        .card h3 {
            font-size: 1.2em;
            color: #1d1d2c;
            margin-bottom: 8px;
        }

        .card p {
            font-size: 0.95em;
            color: #555;
        }

        .btn {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 18px;
            background: linear-gradient(to right, #ff416c, #ff4b2b);
            color: white;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
        }

        .btn:hover {
            background: linear-gradient(to right, #ff4b2b, #ff416c);
        }

        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 13px;
            color: #888;
        }

        @media (max-width: 768px) {
            .card {
                width: 90%;
            }
        }
    </style>
""", unsafe_allow_html=True)

# --- LOGIN UI ---
if not st.session_state.logged_in:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown("<h2>🔐 Admin Login</h2>", unsafe_allow_html=True)

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
    st.markdown("<div class='title'>🚀 EARNZY Admin Panel</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Fully custom layout – mobile-ready, no default Streamlit UI</div>", unsafe_allow_html=True)

    st.markdown("<div class='dashboard'>", unsafe_allow_html=True)

    # Card 1
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/9068/9068749.png'>
            <h3>Push Notification</h3>
            <p>Send image-rich FCM messages to all users</p>
            <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
        </div>
    """, unsafe_allow_html=True)

    # Card 2
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/5986/5986056.png'>
            <h3>Play Integrity</h3>
            <p>Verify untampered devices using Google API</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    # Card 3
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/6645/6645114.png'>
            <h3>Device Block</h3>
            <p>Block rooted or bypassed users by device ID</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    # Card 4
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/553/553416.png'>
            <h3>Notification Logs</h3>
            <p>Track all sent alerts by timestamp + sender</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- Logout Button ---
    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    # --- Footer ---
    st.markdown("<div class='footer'>© 2025 EARNZY Admin Panel — Built for mobile</div>", unsafe_allow_html=True)