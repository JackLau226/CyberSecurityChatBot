#!/usr/bin/env python3
"""
Script to backup database and optionally wipe it clean.
"""

import os
import sys
import django
import shutil
from datetime import datetime

# Add project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from chatbot.models import User

def backup_and_wipe_db():
    print("=== Database Backup and Wipe Script ===")
    print("-" * 40)
    
    try:
        # Get current database path
        db_path = 'db.sqlite3'
        
        if not os.path.exists(db_path):
            print(f"Error: Database file '{db_path}' not found")
            return
        
        # Create backup filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f'db_backup_{timestamp}.sqlite3'
        
        print(f"Creating backup: {backup_filename}")
        
        # Create backup
        try:
            shutil.copy2(db_path, backup_filename)
            print(f"Success: Database backed up to '{backup_filename}'")
        except Exception as e:
            print(f"Error creating backup: {e}")
            return
        
        # Ask if want to wipe
        print("\nBackup completed successfully.")
        response = input("Do you want to wipe the database clean? (yes/no): ").strip().lower()
        
        if response in ['yes', 'y']:
            print("\nWARNING: This will delete ALL data in the database!")
            confirm = input("Are you absolutely sure? Type 'CONFIRM' to proceed: ").strip()
            
            if confirm == 'CONFIRM':
                try:
                    # Delete all users
                    user_count = User.objects.count()
                    User.objects.all().delete()
                    
                    print(f"Success: Database wiped clean. Deleted {user_count} users.")
                    print("Note: The backup file is still available if you need to restore data.")
                    
                except Exception as e:
                    print(f"Error wiping database: {e}")
            else:
                print("Operation cancelled. Database remains unchanged.")
        else:
            print("Database wipe cancelled. Database remains unchanged.")
    
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    backup_and_wipe_db() 