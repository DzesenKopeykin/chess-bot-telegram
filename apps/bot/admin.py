from django.contrib import admin

from . import models, admin_actions
from .admin_utils import build_changelist_link


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "username",
        "is_bot",
        "in_game",
        "color",
        "get_opponent_link",
    )
    readonly_fields = (
        "id",
        "first_name",
        "last_name",
        "username",
        "is_bot",
    )
    search_fields = (
        "id",
        "first_name",
        "last_name",
        "username",
    )
    list_filter = (
        "in_game",
        "is_bot",
    )
    actions = (admin_actions.clear_game_data_action,)

    def get_opponent_link(self, obj):
        if obj.opponent is None:
            return "-"
        return build_changelist_link(
            "bot_user", f"id__exact={obj.opponent.id}", obj.opponent.first_name
        )

    get_opponent_link.allow_tags = True
    get_opponent_link.short_description = "Opponent"
