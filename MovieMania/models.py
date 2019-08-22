from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class WishList(models.Model):
    wishist = models.CharField(max_length = 100)

class WatchLater(models.Model):
    watchlater = models.CharField(max_length = 100)
