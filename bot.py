from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7756439379:AAFTcllKuFy2SpRdCoELAhRvP-zt6P1ZARA"

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("Запустить игру", web_app={"url": "https://iriska074.github.io/Metal-Shift/game.html"})]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text("Нажмите на кнопку ниже, чтобы начать игру!", reply_markup=reply_markup)

def main():
    # Создание приложения
    application = Application.builder().token(TOKEN).build()

    # Добавление обработчика команд
    application.add_handler(CommandHandler("start", start))

    # Запуск polling
    application.run_polling()

if __name__ == "__main__":
    main()
