import streamlit as st

# Set page configuration
st.set_page_config(page_title="CortexPM", layout="centered")

# Initialize session state for tracking actions
if 'login_action' not in st.session_state:
    st.session_state['login_action'] = False
if 'register_action' not in st.session_state:
    st.session_state['register_action'] = False
if 'about_action' not in st.session_state:
    st.session_state['about_action'] = False

# Custom CSS for gradient background and polished theme
st.markdown("""
    <style>
        /* Gradient background for dashing first impression */
        body {
            background: linear-gradient(135deg, #0d47a1, #1de9b6);
            color: #f4f4f8;
            font-family: 'Arial', sans-serif;
        }

        /* Center Title and Tagline */
        h1, h2 {
            text-align: center;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }

        h2 {
            font-weight: lighter;
            color: #e0f7fa;
        }

        /* Button styles */
        .stButton>button {
            background-color: #333;
            color: #1de9b6;
            font-size: 16px;
            border-radius: 8px;
            padding: 8px 20px;
            font-weight: bold;
            transition: background-color 0.3s ease, color 0.3s ease;
            box-shadow: 0px 4px 10px rgba(29, 233, 182, 0.5);
        }
        .stButton>button:hover {
            background-color: #1de9b6;
            color: #333;
        }

        /* Center container layout */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Main container layout
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Title and tagline
st.markdown("<h1>CortexPM</h1>", unsafe_allow_html=True)
st.markdown("<h2>Empowering Collaboration, Tracking Success</h2>", unsafe_allow_html=True)

# Conditional display based on the button clicked
if not st.session_state['about_action']:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔒 Login"):
            st.session_state['login_action'] = True
            st.session_state['register_action'] = False
            st.session_state['about_action'] = False

    with col2:
        if st.button("📝 Register"):
            st.session_state['register_action'] = True
            st.session_state['login_action'] = False
            st.session_state['about_action'] = False

    with col3:
        if st.button("ℹ️ About"):
            st.session_state['about_action'] = True

# Display About information separately
if st.session_state['about_action']:
    st.markdown("### About CortexPM")
    st.info(
        "CortexPM is a streamlined project management system designed for seamless communication and effective project tracking "
        "among students, faculty, and administrators. Our mission is to empower collaboration and enhance productivity through a "
        "user-friendly platform tailored to the needs of educational institutions."
    )

# Display Login or Registration form based on selection
if st.session_state['login_action']:
    st.markdown("### Choose your role to log in:")
    role = st.selectbox("Select Role:", ["Admin", "Faculty", "Student"], key="role_select")
    if role:
        st.session_state['role'] = role
        st.markdown(f"You have chosen to log in as **{role}**.")
        st.markdown("### Enter your credentials")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Submit"):
            st.success(f"Logged in as {role}!")
            st.session_state['logged_in'] = True

elif st.session_state['register_action']:
    st.markdown("### Register New Account")
    register_role = st.selectbox("Register as", ["Admin", "Faculty", "Student"], key="register_role")
    name = st.text_input("Full Name")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password != confirm_password:
            st.error("Passwords do not match.")
        else:
            st.success(f"Registered as {register_role}. You can now log in.")
            st.session_state['register_action'] = False
            st.session_state['login_action'] = True

# End main container
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2024 CortexPM | [Terms of Service](#) | [Privacy Policy](#) | [Contact Us](#)")
