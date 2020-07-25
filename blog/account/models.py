from django.db import models
from django.contrib.auth.models import AbstractUser

class signIn(AbstractUser):
    GENDER = (
        ("M","남자"),
        ("W", "여자"),
        ("O", '그 밖의 성')
    )
    birthday = models.DateField(blank = True)
    gender =  models.CharField(max_length = 10, blank = True, choices = GENDER)

# Create your models here.