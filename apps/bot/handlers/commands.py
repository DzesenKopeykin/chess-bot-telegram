from .. import router


@router.command("/start")
def handle_start_command(bot, chat):
    text = "Напиши username того с кем хочешь поиграть \(например `@my\_friend`\):"
    bot.sendMessage(chat.id, text, parse_mode="MarkdownV2")
