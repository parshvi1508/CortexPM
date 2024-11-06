# pages/admin/dashboard.py
import streamlit as st
from dashboard_base import render_dashboard

def main():
    render_dashboard("Admin")

if __name__ == "__main__":
    main()