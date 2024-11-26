
from aiogram.types import Message
from aiogram.types import Message
from loader import dp, db, get_user_language
from data.messages import MESSAGES
from filters import IsUser

@dp.message_handler(IsUser(), text=lambda msg: msg.text == MESSAGES[get_user_language(msg.from_user.id)]['delivery_status'])
async def process_delivery_status(message: Message):
    language = get_user_language(message.from_user.id)
    orders = db.fetchall('SELECT * FROM orders WHERE cid=?', (message.chat.id,))
    
    if len(orders) == 0:
        await message.answer(MESSAGES[language]['no_active_orders'])
    else:
        await delivery_status_answer(message, orders, language)

async def delivery_status_answer(message, orders, language):
    res = ''
    for order in orders:
        res += MESSAGES[language]['order_status'].format(order_number=order[3], status=MESSAGES[language]['status_in_warehouse'])
        res += '\n\n'
    await message.answer(res)