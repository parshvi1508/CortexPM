import streamlit as st

# Page configuration
st.set_page_config(page_title="CortexPM", layout="centered")

# Initialize session state 
if 'login_action' not in st.session_state:
    st.session_state['login_action'] = False
if 'register_action' not in st.session_state:
    st.session_state['register_action'] = False
if 'about_action' not in st.session_state:
    st.session_state['about_action'] = False
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

        body {
            background: linear-gradient(135deg, #0d47a1, #1de9b6);
            color: #f4f4f8;
            font-family: 'Poppins', sans-serif;
            margin: 0;
            padding: 0;
        }
         /* Logo */
        .logo-container {
            text-align: center;
            margin-bottom: 0.75em;
        }

        .logo-container img {
            max-width: 300px;
            width: 100%;
        }
        /* Title */
        h1 {
            text-align: center;
            background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            letter-spacing: -0.5px;
            margin-bottom: 0.2em;
            margin-top: 0.5em;
            font-size: 2.8em;
        }

        /* Tagline*/
        h2 {
            text-align: center;
            color: #a5f3fc;
            font-family: 'Poppins', sans-serif;
            font-weight: 300;
            font-size: 1.5em;
            letter-spacing: 0.5px;
            margin-bottom: 2em;
            margin-top: 0.5em;
        }

        /* Section headers */
        h3 {
            color: #e0f7fa;
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 1.8em;
            margin: 1em 0;
            background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Input fields */
        .stTextInput > div > div > input {
            background-color: rgba(255, 255, 255, 0.05);
            color: #e0f7fa !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            padding: 8px 12px;
            font-family: 'Poppins', sans-serif;
        }

        /* Select box*/
        .stSelectbox > div > div {
            background-color: rgba(255, 255, 255, 0.05);
            color: #e0f7fa ;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
        }

        /* Button */
        .stButton>button {
            background: linear-gradient(135deg, #0d47a1, #1de9b6);
            color: white;
            font-family: 'Poppins', sans-serif;
            font-size: 16px;
            font-weight: 500;
            border-radius: 8px;
            padding: 10px 24px;
            border: none;
            transition: all 0.3s ease;
            box-shadow: 0px 4px 10px rgba(13, 71, 161, 0.3);
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #1565C0, #00BFA5);
            transform: translateY(-2px);
            box-shadow: 0px 6px 15px rgba(13, 71, 161, 0.5);
        }

        /* Info box */
        .stAlert {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            color: #e0f7fa;
        }

        /* Success message*/
        .element-container .stSuccess {
            background: linear-gradient(135deg, rgba(13, 71, 161, 0.1), rgba(29, 233, 182, 0.1));
            backdrop-filter: blur(10px);
            border: 1px solid rgba(29, 233, 182, 0.3);
            color: #e0f7fa;
        }

        /* Error message */
        .element-container .stError {
            background: rgba(255, 82, 82, 0.1);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 82, 82, 0.3);
            color: #ffcdd2;
        }

        /* main container*/
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 1em 0.5em;
            max-width: 1200px;
            margin: 0 auto;
        }


        /* Footer  */
        .footer {
            text-align: center;
            padding: 20px;
            color: #a5f3fc;
            font-family: 'Poppins', sans-serif;
            font-size: 0.9em;
        }

        .footer a {
            color: #4facfe;
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer a:hover {
            color: #00f2fe;
        }

        /* Label text*/
        .stTextInput > label {
            color: #a5f3fc !important;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
        }

        .stSelectbox > label {
            color: #a5f3fc !important;
            font-family: 'Poppins', sans-serif;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
st.image("assets/CORTEX PM LOGO.png", width=None) 

# Title and tagline
st.markdown("<h1>CortexPM</h1>", unsafe_allow_html=True)
st.markdown("<h2>Empowering Collaboration, Tracking Success</h2>", unsafe_allow_html=True)

# Navigation buttons
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
        st.session_state['about_action'] = not st.session_state['about_action']
        st.session_state['login_action'] = False
        st.session_state['register_action'] = False

if st.session_state['about_action']:
    st.markdown("### About CortexPM")
    st.info(
        "CortexPM is a streamlined project management system designed for seamless communication and effective project tracking "
        "among students, faculty, and administrators. Our mission is to empower collaboration and enhance productivity through a "
        "user-friendly platform tailored to the needs of educational institutions."
    )

if st.session_state['login_action']:
    st.markdown("### Choose your role to log in")
    role = st.selectbox("Select Role:", ["Admin", "Faculty", "Student"], key="role_select")
    if role:
        st.markdown(f"You have chosen to log in as **{role}**")
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
st.markdown("""
    <div class='footer'>
        © 2024 CortexPM | 
        <a href='#'>Terms of Service</a> | 
        <a href='#'>Privacy Policy</a> | 
        <a href='#'>Contact Us</a>
    </div>
""", unsafe_allow_html=True)