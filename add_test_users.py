#!/usr/bin/env python
"""
Script to add test users to the database
Run this script from the project root directory
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cybersec_tutor.settings')
django.setup()

from chatbot.models import User

def create_test_users():
    """Create test users for the application"""
    
    # Test users data
    test_users = [
        {'username': 'admin', 'password': 'admin123'},
        {'username': 'user1', 'password': 'password1'},
        {'username': 'user2', 'password': 'password2'},
        {'username': 'test', 'password': 'test123'},
        {'username': 'demo', 'password': 'demo123'},
    ]
    
    print("Creating test users...")
    
    for user_data in test_users:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={'password': user_data['password']}
        )
        
        if created:
            print(f"✓ Created user: {user.username}")
        else:
            print(f"⚠ User already exists: {user.username}")
    
    print("\nTest users creation completed!")
    print("\nYou can now login with any of these credentials:")
    for user_data in test_users:
        print(f"  Username: {user_data['username']}, Password: {user_data['password']}")

if __name__ == '__main__':
    create_test_users() 