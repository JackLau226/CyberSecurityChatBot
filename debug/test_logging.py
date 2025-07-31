#!/usr/bin/env python
"""
Test script for the logging system
"""

import os
import sys
import django
import re
from datetime import datetime

# Add root directory to Python path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from chatbot.models import User

def count_tokens(text):
    # Count total characters in the text, then div by 4, round up
    """Count tokens based on character count: 1 token = 4 characters - copied from views.py"""
    char_count = len(text)
    tokens = char_count / 4
    return int(tokens) + (1 if tokens % 1 > 0 else 0)

def log_token_request(username, message, token_count):
    """Log token request to token log file and update user's token count in database"""
    # Update user's token count in database
    try:
        user = User.objects.get(username=username)
        user.tokens += token_count
        user.save()
    except User.DoesNotExist:
        pass  
    
    # Log to token log file
    logs_dir = os.path.join(PROJECT_ROOT, 'log')
    os.makedirs(logs_dir, exist_ok=True)
    token_log_path = os.path.join(logs_dir, 'token_log.txt')
    
    with open(token_log_path, 'a', encoding='utf-8') as f:
        now = datetime.now()
        formatted_now = now.strftime('%Y-%m-%d %H:%M:%S')
        # Shorten message if too long
        truncated_message = message[:100] + "..." if len(message) > 100 else message
        f.write(f"{formatted_now} - User {username} sent message: '{truncated_message}' (Token count: {token_count})\n")

def test_logging():
    """Test the new logging functions"""
    
    print("=== TESTING NEW LOGGING SYSTEM ===")
    
    # Token counting
    print("\n1. Testing token counting:")
    test_messages = [
        "Hello, how are you?",
        "What is cybersecurity?",
        "This is a longer message with more words to test the token counting functionality.",
        "Short.",
        "Multiple   spaces   test",
        "Special@#$%^&*() characters test"
    ]
    
    for message in test_messages:
        token_count = count_tokens(message)
        print(f"   Message: '{message}'")
        print(f"   Token count: {token_count}")
        print()
    
    # Token logging
    print("2. Testing token logging:")
    test_username = "test_user"
    test_message = "This is a test message for token logging."
    token_count = count_tokens(test_message)
    
    print(f"   Logging token request for user: {test_username}")
    print(f"   Message: '{test_message}'")
    print(f"   Token count: {token_count}")
    
    log_token_request(test_username, test_message, token_count)
    print("   ✓ Token request logged successfully")
    
    # Check log files
    print("\n3. Checking log files:")
    log_dir = os.path.join(PROJECT_ROOT, 'log')
    
    if os.path.exists(log_dir):
        print(f"   ✓ Log directory exists: {log_dir}")
        
        login_log_path = os.path.join(log_dir, 'login_log.txt')
        token_log_path = os.path.join(log_dir, 'token_log.txt')
        
        if os.path.exists(login_log_path):
            print(f"   ✓ Login log file exists: {login_log_path}")
            with open(login_log_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"   Login log content:\n{content}")
        else:
            print(f"   ✗ Login log file not found: {login_log_path}")
        
        if os.path.exists(token_log_path):
            print(f"   ✓ Token log file exists: {token_log_path}")
            with open(token_log_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"   Token log content:\n{content}")
        else:
            print(f"   ✗ Token log file not found: {token_log_path}")
    else:
        print(f"   ✗ Log directory not found: {log_dir}")
    
    print("\n=== LOGGING TEST COMPLETED ===")

if __name__ == '__main__':
    test_logging() 