import streamlit as st

# ✅ Page setup
st.set_page_config(
    page_title="EARNZY Admin",
    page_icon="🛠️",
    layout="wide"
)

# ✅ Custom CSS for modern UI + animations + mobile responsiveness
st.markdown("""
    <style>
        /* Base styles */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #1a1a1a;
            margin: 0;
            padding: 0;
        }

        /* Title and subtitle */
        .main-title {
            text-align: center;
            font-size: 2.8em;
            font-weight: 700;
            color: #1a1a1a;
            margin-top: 20px;
            animation: fadeInDown 1s ease-in-out;
        }
        .sub-title {
            text-align: center;
            font-size: 1.1em;
            color: #4a4a4a;
            margin-bottom: 50px;
            animation: fadeIn 1.2s ease-in-out;
        }

        /* Card grid */
        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            padding: 20px;
            justify-items: center;
        }

        /* Card styles */
        .card {
            background: white;
            border-radius: 16px;
            padding: 30px;
            margin-bottom: 20px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            animation: fadeInUp 0.8s ease-in-out;
            position: relative;
            overflow: hidden;
        }
        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.15);
        }

        /* Card icon */
        .card img {
            width: 60px;
            margin-bottom: 15px;
            filter: brightness(1.1);
        }

        /* Card title and description */
        .card h3 {
            margin: 10px 0;
            font-size: 1.4em;
            font-weight: 600;
            color: #1a1a1a;
        }
        .card p {
            font-size: 0.95em;
            color: #6b7280;
            margin-bottom: 15px;
        }

        /* Button styles with ripple effect */
        .btn {
            display: inline-block;
            padding: 12px 24px;
            background: linear-gradient(45deg, #ff3366, #ff6b6b);
            color: white;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95em;
            position: relative;
            overflow: hidden;
            transition: background 0.3s ease;
        }
        .btn:hover {
            background: linear-gradient(45deg, #e02155, #ff4d4d);
        }
        .btn::after {
            content: '';
            position: absolute;
            width: 100px;
            height: 100px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple 0.6s linear;
            top: 50%;
            left: 50%;
            transform-origin: center;
            pointer-events: none;
        }
        .btn:active::after {
            animation: ripple 0.6s linear;
        }

        /* Animations */
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes ripple {
            to { transform: scale(4); opacity: 0; }
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 0.85em;
            color: #6b7280;
            margin-top: 40px;
            padding: 20px 0;
            border-top: 1px solid #e5e7eb;
        }

        /* Mobile responsiveness */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.2em;
            }
            .sub-title {
                font-size: 1em;
            }
            .card {
                width: 100%;
                padding: 20px;
            }
            .card-grid {
                grid-template-columns: 1fr;
                padding: 10px;
            }
            .btn {
                padding: 10px 20px;
                font-size: 0.9em;
            }
        }

        /* Page load animation */
        .stApp {
            animation: fadeIn 0.5s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Title & Subtitle
st.markdown("<div class='main-title'>🚀 EARNZY Admin Panel</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Effortlessly manage your app with powerful tools for notifications, integrity, and device control</div>", unsafe_allow_html=True)

# ✅ Cards Grid
st.markdown("<div class='card-grid'>", unsafe_allow_html=True)

# ✅ Push Notification Card
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/9068/9068749.png' alt='Push Notification'>
        <h3>Push Notifications</h3>
        <p>Send engaging notifications with title, body, and images via FCM to all users.</p>
        <a class='btn' href='https://earnzy-notify.streamlit.app' target='_blank'>Open Sender</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Play Integrity Card
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/5986/5986056.png' alt='Play Integrity'>
        <h3>Play Integrity</h3>
        <p>Verify device safety and ensure unrooted devices via API checks.</p>
        <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Blocked Device Card
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/6645/6645114.png' alt='Device Block'>
        <h3>Device Block List</h3>
        <p>Manage rooted or banned devices seamlessly using Firebase.</p>
        <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Notification Logs Card
st.markdown("""
    <div class='card'>
        <img src='https://cdn-icons-png.flaticon.com/512/553/553416.png' alt='Notification Logs'>
        <h3>Notification Logs</h3>
        <p>Monitor and track all sent notifications with detailed logs.</p>
        <a class='btn' href='#' onclick="alert('Coming Soon')">Coming Soon</a>
    </div>
""", unsafe_allow_html=True)

# ✅ Close grid
st.markdown("</div>", unsafe_allow_html=True)

# ✅ Footer
st.markdown("""
    <div class='footer'>
        © 2025 EARNZY Admin Panel | All rights reserved.
    </div>
""", unsafe_allow_html=True)