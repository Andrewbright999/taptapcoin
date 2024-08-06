import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
import asyncio

API_TOKEN = '6954511946:AAGNJmo48ElQ9zRceJQQCmoMbihkl2Da1Hk'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    user = message.from_user
    user_info = (
        f"User ID: {user.id}\n"
        f"Username: {user.username}\n"
        f"First Name: {user.first_name}\n"
        f"Last Name: {user.last_name}\n"
        f"Language Code: {user.language_code}"
    )
    await message.reply(user_info)

    web_app_info = WebAppInfo(url='https://habr.com/ru/articles/706446/')
    ikb = InlineKeyboardButton(text="Перейти", web_app=web_app_info)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[ikb]])
    await message.reply("Нажми на кнопку, чтобы перейти в веб-приложение:", reply_markup=keyboard)

# Обработчик текстовых сообщений
@dp.message()
async def echo(message: Message):
    await message.reply(message.text)

async def main():
    # Регистрация диспетчера
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
