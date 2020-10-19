from django.db import models


class User(models.Model):
    COLORS = (
        ("w", "white"),
        ("b", "black"),
    )

    id = models.IntegerField(primary_key=True)
    is_bot = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, null=True)

    in_game = models.BooleanField(default=False)
    board = models.CharField(max_length=255, null=True, blank=True)
    opponent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    color = models.CharField(max_length=1, choices=COLORS, null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.mention}"

    @property
    def full_name(self):
        full_name = self.first_name
        if self.last_name:
            full_name += " " + self.last_name
        return full_name

    @classmethod
    def update_or_create(cls, tele_user):
        return cls.objects.update_or_create(
            id=tele_user.id,
            defaults=dict(
                is_bot=tele_user.is_bot,
                first_name=tele_user.first_name,
                last_name=tele_user.last_name or "",
                username=tele_user.username,
            ),
        )
