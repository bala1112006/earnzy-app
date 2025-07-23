import streamlit as st

# --- Login Setup ---
st.set_page_config(page_title="EARNZY Admin Login", page_icon="🔐", layout="centered")

# --- Pre-defined login values ---
USERNAME = "Bala"
PASSWORD = "bala10112006"

# --- Session check ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- LOGIN FORM ---
if not st.session_state.logged_in:
    st.markdown("""
        <style>
            .login-container {
                background: #ffffff;
                padding: 30px 40px;
                border-radius: 16px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.1);
                max-width: 400px;
                margin: 80px auto;
                text-align: center;
            }
            .login-container h2 {
                margin-bottom: 20px;
                color: #f63366;
            }
            input {
                border-radius: 8px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<h2>🔐 EARNZY Admin Login</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("✅ Login successful! Loading dashboard...")
            st.rerun()
        else:
            st.error("❌ Invalid credentials. Try again.")

    st.markdown("</div>", unsafe_allow_html=True)

# --- DASHBOARD UI ---
else:
    # Stylish UI begins
    st.set_page_config(page_title="EARNZY Admin", layout="wide")

    st.markdown("""
        <style>
            html, body { font-family: 'Poppins', sans-serif; background-color: #f4f6fc; }
            .title { text-align: center; font-size: 2.5em; font-weight: bold; color: #222; margin-top: 10px; }
            .subtitle { text-align: center; font-size: 1.1em; color: #555; margin-bottom: 30px; }
            .grid { display: flex; flex-wrap: wrap; justify-content: center; gap: 25px; }
            .card {
                width: 310px;
                padding: 25px;
                border-radius: 20px;
                background: linear-gradient(to bottom right, #ffffff, #f1f3f6);
                box-shadow: 0 8px 24px rgba(0,0,0,0.08);
                text-align: center;
                transition: all 0.3s ease;
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 30px rgba(0,0,0,0.12);
            }
            .card img { width: 70px; margin-bottom: 15px; }
            .card h3 { font-size: 1.3em; color: #333; }
            .card p { color: #555; font-size: 0.95em; }
            .btn {
                margin-top: 10px;
                padding: 10px 20px;
                background: linear-gradient(to right, #f63366, #ff4b2b);
                color: white;
                text-decoration: none;
                font-weight: bold;
                border-radius: 8px;
                display: inline-block;
            }
            .btn:hover {
                background: linear-gradient(to right, #ff4b2b, #f63366);
            }
            @media (max-width: 768px) {
                .card { width: 90%; }
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🚀 EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Manage notifications, users, and more</div>", unsafe_allow_html=True)
    st.markdown("<div class='grid'>", unsafe_allow_html=True)

    # --- CARD 1 ---
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/9068/9068749.png'>
            <h3>Send Notification</h3>
            <p>Push rich FCM alerts with title, body & image.</p>
            <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
        </div>
    """, unsafe_allow_html=True)

    # --- CARD 2 ---
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/5986/5986056.png'>
            <h3>Play Integrity</h3>
            <p>Verify Play Protect certified safe devices.</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    # --- CARD 3 ---
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/6645/6645114.png'>
            <h3>Device Block</h3>
            <p>See & manage rooted/tampered device list.</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    # --- CARD 4 ---
    st.markdown("""
        <div class='card'>
            <img src='https://cdn-icons-png.flaticon.com/512/553/553416.png'>
            <h3>Notification Logs</h3>
            <p>Track sent alerts by admin + timestamps.</p>
            <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- Logout ---
    if st.button("🔓 Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size: 13px;'>© 2025 EARNZY Admin | Built with ❤️ by Bala</p>", unsafe_allow_html=True)