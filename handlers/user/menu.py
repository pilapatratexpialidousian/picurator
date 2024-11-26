# handlers/user/menu.py
from aiogram.types import Message, ReplyKeyboardMarkup
from loader import dp, get_user_language
from filters import IsAdmin, IsUser
from data.messages import MESSAGES

@dp.message_handler(IsAdmin(), commands='menu')
async def admin_menu(message: Message):
    language = get_user_language(message.from_user.id)
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(MESSAGES[language]['settings'])
    markup.add(MESSAGES[language]['questions'], MESSAGES[language]['orders'])

    await message.answer(MESSAGES[language]['menu'], reply_markup=markup)

@dp.message_handler(IsUser(), commands='menu')
async def user_menu(message: Message):
    language = get_user_language(message.from_user.id)
    markup = ReplyKeyboardMarkup(selective=True)
    markup.add(MESSAGES[language]['catalog'])
    markup.add(MESSAGES[language]['balance'], MESSAGES[language]['cart'])
    markup.add(MESSAGES[language]['delivery_status'])

    await message.answer(MESSAGES[language]['menu'], reply_markup=markup)
