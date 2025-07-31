#!/usr/bin/env python3
"""
Script to change password for a specific user.
"""

import os
import sys
import django
import getpass

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from chatbot.models import User

def change_password():
    print("=== Password Change Script ===")
    print("-" * 30)
    
    try:
        # Get username
        username = input("Enter username: ").strip()
        
        if not username:
            print("Error: Username cannot be empty")
            return
        
        # Check if user exists
        try:
            user = User.objects.get(username=username)
            print(f"Found user: {username}")
        except User.DoesNotExist:
            print(f"Error: User '{username}' does not exist")
            return
        
        # Get new password
        new_password = getpass.getpass("Enter new password: ").strip()
        
        if not new_password:
            print("Error: Password cannot be empty")
            return
        
        # Confirm password
        confirm_password = getpass.getpass("Confirm new password: ").strip()
        
        if new_password != confirm_password:
            print("Error: Passwords do not match")
            return
        
        # Update password
        user.password = new_password
        user.save()
        
        print(f"Success: Password updated for user '{username}'")
        
    except KeyboardInterrupt:
        print("\n\\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    change_password() 