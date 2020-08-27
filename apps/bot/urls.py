from django.urls import path

from .views import telegram_update

urlpatterns = [
    path("<str:bot_token>", telegram_update, name="update"),
]
