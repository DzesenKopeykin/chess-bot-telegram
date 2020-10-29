from django.contrib import messages


def clear_game_data_action(modeladmin, request, queryset):

    for user in queryset:
        user.clear_game_data()

    message = (
        f"Successfully initiated clearing games data for {queryset.count()} users."
    )

    modeladmin.message_user(request, message, messages.SUCCESS)


clear_game_data_action.short_description = "Clear game data for selected users"