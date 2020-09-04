from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, null=True)
