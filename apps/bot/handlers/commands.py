from .decorators import command_handler
from ..models import User


@command_handler("/start")
def handle_start_command(message):
    tele_user = message.from_user
    User.update_or_create(tele_user)
    help_text = (
        "Здравствуйте\! Здесь вы можете поиграть в шахматы с реальными людьми\. "
        "Для того чтобы начать партию напишите `@username` пользователя с которым "
        "вы желаете играть\.\n\n*Важно\! Бот должен знать вашего оппонента, "
        f"попросите его перейти к @dev\_chess\_bot и нажать /start*"
    )
    message.bot.sendMessage(message.chat.id, help_text, parse_mode="MarkdownV2")
    if not tele_user.username:
        text = (
            "Я вижу что у вас не установлен `@username`\.\n"
            "*Другие игроки не смогут предложить вам сыграть партию\!*\n"
            "О том как установить `@username` и что это такое вы можете прочитать "
            "[здесь](https://telegram.org/faq#q-what-are-usernames-how-do-i-get-one)\."
            "\n\nПосле того как вы установили или изменили `@username` "
            "запустите снова команду /start чтобы я запомнил его\."
            "\n\nЕсли вы не хотите устанавливать себе `@username`, "
            "то напишите `@username` соперника\."
        )
        message.bot.sendMessage(
            message.chat.id,
            text,
            parse_mode="MarkdownV2",
            disable_web_page_preview=True,
        )
