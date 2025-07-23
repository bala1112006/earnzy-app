import streamlit as st

# --- Session State for Login ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# --- Login Screen ---
if not st.session_state['authenticated']:
    st.markdown("""
        <style>
            .login-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                background: #1a1a2e;
                color: #e0e0e0;
            }
            .login-box {
                background: #2a2a4e;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
                text-align: center;
            }
            .login-box h2 {
                color: #00ffcc;
                margin-bottom: 20px;
            }
            .login-box input {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: none;
                border-radius: 5px;
                background: #3a3a5e;
                color: #e0e0e0;
            }
            .login-box button {
                padding: 10px 20px;
                background: #00cc99;
                border: none;
                border-radius: 5px;
                color: #1a1a2e;
                font-weight: 600;
                cursor: pointer;
                transition: background 0.3s ease;
            }
            .login-box button:hover {
                background: #00ffcc;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown("<h2>Login to EARNZY Admin</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "Bala" and password == "bala10112006":
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- Page Setup ---
    st.set_page_config(
        page_title="EARNZY Admin Panel",
        page_icon="⚡",
        layout="wide"
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
                padding: 10px 20px;
                background: #00cc99;
                border: none;
                border-radius: 5px;
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

    # --- Main Content ---
    st.markdown("<div class='title'>⚡ EARNZY Admin Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Control notifications, security, and devices seamlessly</div>", unsafe_allow_html=True)

    # --- Cards Section ---
    st.markdown("<div class='grid'>", unsafe_allow_html=True)

    st.markdown("""
        <div class='card'>
            <h3>Push Notification</h3>
            <p>Send title, body, and image via FCM to all app users instantly.</p>
            <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='card'>
            <h3>Play Integrity</h3>
            <p>Verify devices before login to block rooted or modified systems.</p>
            <a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='card'>
            <h3>Device Block</h3>
            <p>View & manage rooted or tampered device access from Firebase.</p>
            <a class='btn' href='#' onclick=\"alert('Coming Soon')\">Coming Soon</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # --- Footer ---
    st.markdown("<div class='footer'>© 2025 EARNZY Admin | Designed with ❤️ by Bala</div>", unsafe_allow_html=True)

    # --- Version ---
    st.markdown("<p style='text-align: center; color: #606070; font-size: 0.8em;'>Version 1.0.0</p>", unsafe_allow_html=True)