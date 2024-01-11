from aiogram.types import Message
from loader import dp, db
from .menu import delivery_status
from filters import IsUser

@dp.message_handler(IsUser(), text=delivery_status)
async def process_delivery_status(message: Message):
    # Fetch orders with their status
    orders = db.fetchall('SELECT * FROM orders WHERE cid=?', (message.chat.id,))
    
    if len(orders) == 0: 
        await message.answer('У вас нет активных заказов.')
    else: 
        await delivery_status_answer(message, orders)

async def delivery_status_answer(message, orders):
    res = ''

    for order in orders:
        order_id, _, _, _, status = order  # Assuming order structure includes status at the end
        res += f'Заказ <b>№{order_id}</b>: {status}\n\n'

    await message.answer(res)
