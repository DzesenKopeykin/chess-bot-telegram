from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, null=True)

    @classmethod
    def update_or_create(cls, tele_user):
        return cls.objects.update_or_create(
            id=tele_user.id,
            defaults=dict(
                is_bot=tele_user.is_bot,
                first_name=tele_user.first_name,
                last_name = tele_user.last_name or "",
                username=tele_user.username,
            )
        )
