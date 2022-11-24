from django.db import models

# Create your models here.
class UserSignIn(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.email