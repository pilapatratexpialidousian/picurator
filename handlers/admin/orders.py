
from aiogram.types import Message
from loader import dp, db
from loader import dp, db, bot
from handlers.user.menu import orders
from filters import IsAdmin

@dp.message_handler(IsAdmin(), text=orders)
async def process_orders(message: Message):
    
    orders = db.fetchall('SELECT * FROM orders')
    
    if len(orders) == 0: await message.answer('У вас нет заказов.')
    else: await order_answer(message, orders)


@dp.message_handler(IsAdmin(), commands=['update_order_status'])
async def update_order_status(message: Message):
    args = message.get_args().split()
    
    if len(args) != 2:
        return await message.reply("Usage: /update_order_status <order_id> <new_status>")

    order_id, new_status = args

    # Update the order status
    db.query('UPDATE orders SET status = ? WHERE cid = ?', (new_status, order_id))
    await message.reply(f"Order {order_id} status updated to {new_status}.")

 # Fetch the customer's chat ID (cid)
    # The following line assumes that 'cid' in the 'orders' table is used as 'order_id'
    order = db.fetchone('SELECT cid FROM orders WHERE cid = ?', (order_id,))
    if order:
        cid = order[0]

        # Notify the customer if the status is 'dispatched'
        if new_status.lower() == 'dispatched':
            await bot.send_message(cid, f"Your order {order_id} has been dispatched and is on its way!")

        await message.reply(f"Order {order_id} status updated to {new_status} and the customer has been notified.")
    else:
        await message.reply(f"No order found with ID {order_id}.")




async def order_answer(message, orders):
    res = ''

    for order in orders:
        cid, name, address, products, status = order  # Update this line to include status
        product_details = ''

        # Existing code to process product details...
        # ...
         # Splitting the product string into individual products
        for product in products.split():
            idx, quantity = product.split('=')
            product_info = db.fetchone('SELECT title FROM products WHERE idx=?', (idx,))
            if product_info:
                product_title = product_info[0]
                product_details += f'{product_title} x {quantity}\n'
        # Include status in the response
        res += f'Order Number: {order[3]}\nStatus: {status}\nCustomer ID: {cid}\nName: {name}\nAddress: {address}\nProducts:\n{product_details}\n\n'

    await message.answer(res, parse_mode='HTML')




