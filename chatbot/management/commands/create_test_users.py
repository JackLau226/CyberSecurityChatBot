from django.core.management.base import BaseCommand
from chatbot.models import User

class Command(BaseCommand):
    help = 'Create test users for the application'

    def handle(self, *args, **options):
        # Create some test users
        test_users = [
            {'username': 'admin', 'password': 'admin123'},
            {'username': 'user1', 'password': 'password1'},
            {'username': 'user2', 'password': 'password2'},
            {'username': 'test', 'password': 'test123'},
        ]
        
        for user_data in test_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'password': user_data['password']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created user: {user.username}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'User already exists: {user.username}')
                )
        
        self.stdout.write(
            self.style.SUCCESS('Test users creation completed!')
        ) 