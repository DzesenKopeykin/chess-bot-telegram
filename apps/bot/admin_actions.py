from django.contrib import messages


def finish_game_action(modeladmin, request, queryset):
    users_in_game = queryset.filter(in_game=True)
    num_of_not_in_game_users = queryset.filter(in_game=False).count()

    for user in users_in_game:
        user.finish_game()

    message = f"Successfully initiated finishing games for {users_in_game.count()} users."
    if num_of_not_in_game_users:
        message += f" {num_of_not_in_game_users} users not in game are ignored."

    modeladmin.message_user(request, message, messages.SUCCESS)


finish_game_action.short_description = "Finish games for selected users"