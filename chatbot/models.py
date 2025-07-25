from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    tokens = models.IntegerField(default=0)  # Track total tokens used by the user
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
