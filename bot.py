from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

# Ваш токен от BotFather
TOKEN = "7756439379:AAFTcllKuFy2SpRdCoELAhRvP-zt6P1ZARA"

async def start(update: Update, context: CallbackContext):
    # Кнопка для запуска мини-приложения
    keyboard = [
        [KeyboardButton("Запустить игру", web_app={"url": "https://iriska074.github.io/Metal-Shift/"})]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "Нажмите на кнопку ниже, чтобы начать игру!", reply_markup=reply_markup
    )

def main():
    # Создаём приложение (новый способ с python-telegram-bot 20.x)
    application = Application.builder().token(TOKEN).build()

    # Обрабатываем команду /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
