from supabase import create_client
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

def init_connection():
    """Initialize connection to Supabase"""
    try:
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_KEY")
        
        if not supabase_url or not supabase_key:
            st.error("Supabase credentials not found in environment variables.")
            return None
            
        client = create_client(supabase_url, supabase_key)
        return client
    except Exception as e:
        st.error(f"Failed to connect to Supabase: {str(e)}")
        return None

# User management functions
def get_user_by_email(client, email):
    """Fetch user details by email"""
    try:
        response = client.table('users').select("*").eq('email', email).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        st.error(f"Error fetching user: {str(e)}")
        return None

def create_user(client, user_data):
    """Create a new user in the database"""
    try:
        response = client.table('users').insert(user_data).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        st.error(f"Error creating user: {str(e)}")
        return None

def verify_credentials(client, email, password):
    """Verify user credentials"""
    try:
        response = client.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return response.user if response else None
    except Exception as e:
        st.error(f"Authentication failed: {str(e)}")
        return None

# Project management functions
def create_project(client, project_data):
    """Create a new project"""
    try:
        response = client.table('projects').insert(project_data).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        st.error(f"Error creating project: {str(e)}")
        return None

def get_user_projects(client, user_id):
    """Fetch all projects for a user"""
    try:
        response = client.table('projects').select("*").eq('user_id', user_id).execute()
        return response.data if response.data else []
    except Exception as e:
        st.error(f"Error fetching projects: {str(e)}")
        return []

def update_project_status(client, project_id, status):
    """Update project status"""
    try:
        response = client.table('projects').update({"status": status}).eq('id', project_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        st.error(f"Error updating project status: {str(e)}")
        return None

# File management functions
def upload_file(client, file_path, file_content):
    """Upload a file to Supabase storage"""
    try:
        response = client.storage.from_('project-files').upload(file_path, file_content)
        return response.get('Key') if response else None
    except Exception as e:
        st.error(f"Error uploading file: {str(e)}")
        return None

def get_file_url(client, file_path):
    """Get public URL for a file"""
    try:
        return client.storage.from_('project-files').get_public_url(file_path)
    except Exception as e:
        st.error(f"Error getting file URL: {str(e)}")
        return None