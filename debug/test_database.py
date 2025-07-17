#!/usr/bin/env python
"""
Test script to verify database and User model functionality
"""

import os
import sys
import django

# Add the project root directory to the Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cybersec_tutor.settings')
django.setup()

from chatbot.models import User

def test_database():
    """Test database connectivity and User model"""
    
    print("=== DATABASE TEST ===")
    
    try:
        # Test 1: Check if we can query the database
        print("1. Testing database connection...")
        user_count = User.objects.count()
        print(f"   ✓ Database connected. Total users: {user_count}")
        
        # Test 2: List all users
        print("\n2. Listing all users:")
        users = User.objects.all()
        if users:
            for user in users:
                print(f"   - {user.username} (ID: {user.id})")
        else:
            print("   No users found in database")
        
        # Test 3: Try to find a specific user
        print("\n3. Testing user lookup...")
        try:
            admin_user = User.objects.get(username='admin')
            print(f"   ✓ Found user: {admin_user.username}")
            print(f"   Password: {admin_user.password}")
        except User.DoesNotExist:
            print("   ✗ User 'admin' not found")
        
        # Test 4: Test password comparison
        print("\n4. Testing password comparison...")
        try:
            admin_user = User.objects.get(username='admin')
            test_password = 'admin123'
            if admin_user.password == test_password:
                print(f"   ✓ Password '{test_password}' matches for user 'admin'")
            else:
                print(f"   ✗ Password '{test_password}' does not match")
                print(f"   Stored password: {admin_user.password}")
        except User.DoesNotExist:
            print("   ✗ Cannot test password - user 'admin' not found")
        
        print("\n=== DATABASE TEST COMPLETED ===")
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_database() 