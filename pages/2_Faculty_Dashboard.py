import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.dashboard_utils import (
    load_css, create_sidebar, show_metrics,
    show_activity_feed, show_quick_stats, add_footer
)

def main():
    st.set_page_config(page_title="CortexPM - Faculty Dashboard", layout="wide")
    load_css()
    
    # Create sidebar and get selected page
    selected_page = create_sidebar("Faculty")
    
    # Main content
    if selected_page == "Dashboard":
        st.title("Faculty Dashboard")
        show_metrics("Faculty")
        
        # Layout for activity feed and quick stats
        col1, col2 = st.columns([2, 1])
        with col1:
            show_activity_feed("Faculty")
        with col2:
            show_quick_stats()
    
    elif selected_page == "Students":
        st.title("Student Management")
        # Add student management content here
        
    elif selected_page == "Assignments":
        st.title("Assignment Management")
        # Add assignment management content here
        
    elif selected_page == "Grades":
        st.title("Grade Management")
        # Add grade management content here
        
    elif selected_page == "Settings":
        st.title("Settings")
        # Add settings content here
    
    add_footer()

if __name__ == "__main__":
    main()