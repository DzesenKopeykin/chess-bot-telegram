from .decorators import command_handler


@command_handler("/start")
def handle_start_command(message):
    text = "Напиши username того с кем хочешь поиграть \(например `@my\_friend`\):"
    message.bot.sendMessage(message.chat.id, text, parse_mode="MarkdownV2")
