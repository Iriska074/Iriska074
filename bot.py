from telegram import Update, Bot, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler

# Ваш токен от BotFather
TOKEN = "7756439379:AAFTcllKuFy2SpRdCoELAhRvP-zt6P1ZARA"

# Ссылка на игру
WEB_APP_URL = "https://iriska074.github.io/Metal-Shift/"

# Функция для команды /start
def start(update: Update, context):
    # Кнопка для запуска мини-приложения
    keyboard = [
        [KeyboardButton("Запустить игру", web_app={"url": WEB_APP_URL})]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем сообщение с кнопкой
    update.message.reply_text(
        "Нажмите на кнопку ниже, чтобы начать игру!", reply_markup=reply_markup
    )

# Основная функция
def main():
    # Создаём бота
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Обрабатываем команду /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
