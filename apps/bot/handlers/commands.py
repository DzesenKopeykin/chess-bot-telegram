from .decorators import command_handler


@command_handler("/start")
def handle_start_command(message):
    send_help_text(message.bot, message.chat.id)


@command_handler("/help")
def handle_start_command(message):
    send_help_text(message.bot, message.chat.id)


def send_help_text(bot, chat_id):
    text = (
        "Привет\! Здесь ты можешь поиграть в шахматы с реальными людьми\. "
        "Для того чтобы начать партию напиши _`@username`_ пользователя с которым "
        "ты желаешь играть\.\n\n*Важно\! Бот должен знать твоего оппонента, "
        f"попроси его перейти к @dev\_chess\_bot и нажать /start*"
    )
    bot.sendMessage(chat_id, text, parse_mode="MarkdownV2")
