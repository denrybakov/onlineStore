from django.db import models
from django.contrib.auth.models import AbstractUser

# Create models
class User(AbstractUser):
  image = models.ImageField(upload_to='users_images', null=True, blank=True)