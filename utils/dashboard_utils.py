import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu

def load_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

            /* Main container */
            .main {
                background: linear-gradient(135deg, #0d47a1, #1de9b6);
                color: #f4f4f8;
                font-family: 'Poppins', sans-serif;
            }

            /* Sidebar */
            .css-1d391kg {
                background: rgba(13, 71, 161, 0.1);
                backdrop-filter: blur(10px);
            }

            /* Cards */
            .stCard {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 10px;
                padding: 1rem;
                margin: 0.5rem 0;
            }

            /* Headers */
            h1, h2, h3 {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            /* Metrics */
            .metric-container {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                padding: 1rem;
                margin: 0.5rem 0;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }

            .metric-value {
                font-size: 2rem;
                font-weight: 600;
                color: #4facfe;
            }

            .metric-label {
                font-size: 0.9rem;
                color: #a5f3fc;
            }

            /* Tables */
            .dataframe {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }

            /* Charts */
            .plotly-chart {
                background: rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                padding: 1rem;
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)

def create_sidebar(role):
    with st.sidebar:
        # Profile section
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("assets/CORTEX PM LOGO.png", width=50)
        with col2:
            st.markdown(f"### {role}")
            st.text(f"Welcome, {st.session_state.get('username', 'User')}")

        st.divider()

        # Navigation menu based on role
        if role == "Admin":
            selected = option_menu(
                "Main Menu",
                ["Dashboard", "Users", "Projects", "Reports", "Settings"],
                icons=['house', 'people', 'folder', 'file-text', 'gear'],
                menu_icon="cast",
                default_index=0,
            )
        elif role == "Faculty":
            selected = option_menu(
                "Main Menu",
                ["Dashboard", "Students", "Assignments", "Grades", "Settings"],
                icons=['house', 'people', 'clipboard', 'star', 'gear'],
                menu_icon="cast",
                default_index=0,
            )
        else:  # Student
            selected = option_menu(
                "Main Menu",
                ["Dashboard", "Projects", "Submissions", "Grades", "Settings"],
                icons=['house', 'folder', 'cloud-upload', 'star', 'gear'],
                menu_icon="cast",
                default_index=0,
            )
        
        return selected

def show_metrics(role):
    cols = st.columns(4)
    if role == "Admin":
        metrics = [
            {"label": "Total Users", "value": "1,234", "delta": "+12%"},
            {"label": "Active Projects", "value": "456", "delta": "+5%"},
            {"label": "Faculty", "value": "45", "delta": "0"},
            {"label": "Students", "value": "1,189", "delta": "+15%"}
        ]
    elif role == "Faculty":
        metrics = [
            {"label": "Active Students", "value": "156", "delta": "+3%"},
            {"label": "Projects", "value": "48", "delta": "+2%"},
            {"label": "Pending Reviews", "value": "12", "delta": "-25%"},
            {"label": "Avg. Grade", "value": "85%", "delta": "+5%"}
        ]
    else:  # Student
        metrics = [
            {"label": "Active Projects", "value": "3", "delta": "0"},
            {"label": "Completed", "value": "5", "delta": "+1"},
            {"label": "Avg. Grade", "value": "88%", "delta": "+2%"},
            {"label": "Due Soon", "value": "2", "delta": "0"}
        ]

    for col, metric in zip(cols, metrics):
        with col:
            st.metric(
                label=metric["label"],
                value=metric["value"],
                delta=metric["delta"]
            )

def show_activity_feed(role):
    st.subheader("Recent Activity")
    with st.container(height=400, border=True):
        if role == "Admin":
            activities = [
                "New faculty member registered - Dr. Smith",
                "Project submission deadline updated",
                "System backup completed",
                "New batch of students added"
            ]
        elif role == "Faculty":
            activities = [
                "New project submission from John Doe",
                "Grade updated for Project X",
                "Feedback provided on Assignment Y",
                "New announcement posted"
            ]
        else:  # Student
            activities = [
                "Project X grade received",
                "New assignment posted",
                "Feedback received on Project Y",
                "Upcoming deadline reminder"
            ]
        
        for activity in activities:
            st.write(f"• {activity}")

def show_quick_stats():
    st.subheader("Quick Stats")
    with st.container(height=400, border=True):
        fig = go.Figure(data=[go.Pie(labels=['Complete', 'In Progress', 'Not Started'],
                                   values=[35, 45, 20])])
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0),
                         paper_bgcolor='rgba(0,0,0,0)',
                         plot_bgcolor='rgba(0,0,0,0)',
                         font=dict(color='#a5f3fc'))
        st.plotly_chart(fig, use_container_width=True)

def add_footer():
    st.markdown("""
        <div style='position: fixed; bottom: 0; width: 100%; text-align: center; padding: 10px; background: rgba(13, 71, 161, 0.1); backdrop-filter: blur(10px);'>
            © 2024 CortexPM | All Rights Reserved
        </div>
    """, unsafe_allow_html=True)