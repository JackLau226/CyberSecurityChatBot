#!/usr/bin/env python3
"""
Script to add multiple users to the database.
Input format: username\tpassword
Enter '*' to stop and create all users.
"""

import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cybersec_tutor.settings')
django.setup()

from chatbot.models import User

def add_users():
    print("=== User Addition Script ===")
    print("Enter users in format: username\\tpassword")
    print("Enter '*' to stop and create all users")
    print("Example:")
    print("k24100001\\tQi9UpsI!")
    print("k24100002\\tQuBQd5B&")
    print("-" * 40)
    
    users_to_add = []
    
    while True:
        try:
            user_input = input("Enter user (or '*' to finish): ").strip()
            
            if user_input == '*':
                break
                
            if not user_input:
                continue
                
            # Split by tab character
            parts = user_input.split('\t')
            if len(parts) != 2:
                print("Error: Invalid format. Use: username\\tpassword")
                continue
                
            username, password = parts[0].strip(), parts[1].strip()
            
            if not username or not password:
                print("Error: Username and password cannot be empty")
                continue
                
            users_to_add.append((username, password))
            print(f"Added to queue: {username}")
            
        except KeyboardInterrupt:
            print("\n\\nOperation cancelled by user.")
            return
        except Exception as e:
            print(f"Error reading input: {e}")
            continue
    
    if not users_to_add:
        print("No users to add.")
        return
    
    print(f"\\nCreating {len(users_to_add)} users...")
    
    success_count = 0
    error_count = 0
    
    for username, password in users_to_add:
        try:
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                print(f"Error: User '{username}' already exists")
                error_count += 1
                continue
            
            # Create new user
            user = User.objects.create(
                username=username,
                password=password,
                tokens=0  # Initialize with 0 tokens
            )
            print(f"Success: Created user '{username}'")
            success_count += 1
            
        except Exception as e:
            print(f"Error creating user '{username}': {e}")
            error_count += 1
    
    print(f"\\nOperation completed:")
    print(f"Successfully created: {success_count} users")
    print(f"Errors: {error_count} users")

if __name__ == "__main__":
    add_users() 