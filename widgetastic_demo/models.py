from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    """Imports base user and adds other properties."""

    full_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField()
