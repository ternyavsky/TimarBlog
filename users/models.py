from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    count_state = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

