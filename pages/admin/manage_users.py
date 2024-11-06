import streamlit as st
import db
from db import init_connection, get_user_by_email, create_user, update_user

def app():
    st.set_page_config(page_title="CortexPM - Manage Users", layout="wide")

    # Initialize Supabase connection
    supabase = init_connection()

    if not supabase:
        st.error("Failed to connect to Supabase. Please try again later.")
        return

    st.title("Manage Users")

    # Fetch all users
    users = supabase.table("users").select("*").execute().data

    with st.expander("Add New User"):
        with st.form("add_user_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            role = st.selectbox("Role", ["Admin", "Faculty", "Student"])
            department = st.text_input("Department")

            if st.form_submit_button("Create User"):
                user_data = {
                    "full_name": name,
                    "email": email,
                    "password_hash": password,
                    "role": role.lower(),
                    "department": department
                }
                new_user = create_user(supabase, user_data)
                if new_user:
                    st.success(f"User '{new_user['full_name']}' created successfully.")
                else:
                    st.error("Failed to create user. Please try again.")

    st.subheader("Existing Users")
    if users:
        with st.expander("View Users"):
            user_table = st.table([
                {
                    "Name": user["full_name"],
                    "Email": user["email"],
                    "Role": user["role"].capitalize(),
                    "Department": user["department"],
                    "Last Login": user["last_login"].strftime("%Y-%m-%d %H:%M:%S") if user["last_login"] else "N/A",
                    "Active": "Yes" if user["is_active"] else "No"
                } for user in users
            ])

            with st.form("update_user_form"):
                user_email = st.selectbox("Select User", [user["email"] for user in users])
                new_name = st.text_input("New Full Name", value=[user["full_name"] for user in users if user["email"] == user_email][0])
                new_role = st.selectbox("New Role", ["Admin", "Faculty", "Student"], index=[user["role"] for user in users if user["email"] == user_email][0])
                new_department = st.text_input("New Department", value=[user["department"] for user in users if user["email"] == user_email][0])
                is_active = st.checkbox("Account Active", value=[user["is_active"] for user in users if user["email"] == user_email][0])

                if st.form_submit_button("Update User"):
                    user_data = {
                        "full_name": new_name,
                        "role": new_role.lower(),
                        "department": new_department,
                        "is_active": is_active
                    }
                    updated_user = update_user(supabase, [user["id"] for user in users if user["email"] == user_email][0], user_data)
                    if updated_user:
                        st.success(f"User '{updated_user['full_name']}' updated successfully.")
                    else:
                        st.error("Failed to update user. Please try again.")

    else:
        st.info("No users found.")