# messages.py

MESSAGES = {
    'en': {
        # General messages
        'start': '''Hi! 👋

🤖 I'm a marketplace bot to buy products from any category.

🛍️ To access the catalog and see the products, use the /menu command.

💰 For deposits, you can use Yandex, Sber, and Qiwi.

❓ Have questions? Not a problem! Use the /sos command to contact the admins.

🤝 Want to order a similar bot? Contact the developer <a href="https://t.me/NikolaySimakov">Nikolay Simakov</a>, he doesn't bite)))''',

        'user_mode_on': 'User mode is on.',
        'admin_mode_on': 'Admin mode is on.',
        'menu': 'Menu',

        # User menu items
        'catalog': '🛍️ Catalog',
        'balance': '💰 Balance',
        'cart': '🛒 Cart',
        'delivery_status': '🚚 Order status',

        # Admin menu items
        'settings': '⚙️ Catalog settings',
        'orders': '🚚 Orders',
        'questions': '❓ Questions',

        # Cart messages
        'cart_empty': 'Your cart is empty.',
        'cart_product_info': '<b>{title}</b>\n\n{body}\n\nPrice: {price}$.',
        'enter_name': 'Enter your name.',
        'enter_address': 'Specify your address.',
        'change_name': 'Change the name from <b>{name}</b>?',
        'change_address': 'Change the address from <b>{address}</b>?',
        'order_confirmed': 'Your order is on its way 🚀\nName: <b>{name}</b>\nAddress: <b>{address}</b>',
        'not_enough_funds': 'You don\'t have enough funds. Make a deposit!',

        # Catalog messages
        'choose_category': 'Choose the category to see the products:',

        # SOS messages
        'sos_prompt': 'What\'s the problem? Describe it in detail and the operator will respond soon.',
        'sos_sent': 'Sent!',
        'sos_limit_exceeded': 'The limit for questions is exceeded.',
        'no_questions': 'No questions.',

        # Delivery status messages
        'no_active_orders': 'You don\'t have active orders.',
        'order_status': 'Order <b>№{order_number}</b>{status}',
        'status_in_warehouse': ' in a warehouse.',
        'status_on_the_way': ' on its way!',
        'status_arrived': ' arrived at the post office!',

        # Confirmation messages
        'make_sure_correct': 'Make sure everything is correct.',
        'ready': 'Ready!',
        'cancelled': 'Canceled!',
        'sent': 'Sent!',
        'no_such_choice': 'There is no such choice.',

        # Keyboard buttons
        'back': '👈 Back',
        'confirm_order': '✅ Confirm the order',
        'all_correct': '✅ All is correct',
        'cancel': '🚫 Cancel',
        'answer': 'Answer',
    },
    'ru': {
        # General messages
        'start': '''Привет! 👋

🤖 Я бот-магазин для покупки товаров из любой категории.

🛍️ Чтобы получить доступ к каталогу и посмотреть товары, используйте команду /menu.

💰 Для пополнения можно использовать Яндекс, Сбер и Киви.

❓ Есть вопросы? Не проблема! Команда /sos поможет вам связаться с администраторами.

🤝 Хотите заказать похожего бота? Свяжитесь с разработчиком <a href="https://t.me/NikolaySimakov">Николаем Симаковым</a>, он не кусается)))''',

        'user_mode_on': 'Режим пользователя включен.',
        'admin_mode_on': 'Режим администратора включен.',
        'menu': 'Меню',

        # User menu items
        'catalog': '🛍️ Каталог',
        'balance': '💰 Баланс',
        'cart': '🛒 Корзина',
        'delivery_status': '🚚 Статус заказа',

        # Admin menu items
        'settings': '⚙️ Настройки каталога',
        'orders': '🚚 Заказы',
        'questions': '❓ Вопросы',

        # Cart messages
        'cart_empty': 'Ваша корзина пуста.',
        'cart_product_info': '<b>{title}</b>\n\n{body}\n\nЦена: {price}₽.',
        'enter_name': 'Введите ваше имя.',
        'enter_address': 'Укажите ваш адрес.',
        'change_name': 'Изменить имя с <b>{name}</b>?',
        'change_address': 'Изменить адрес с <b>{address}</b>?',
        'order_confirmed': 'Ваш заказ в пути 🚀\nИмя: <b>{name}</b>\nАдрес: <b>{address}</b>',
        'not_enough_funds': 'У вас недостаточно средств. Пополните баланс!',

        # Catalog messages
        'choose_category': 'Выберите категорию, чтобы увидеть товары:',

        # SOS messages
        'sos_prompt': 'В чём проблема? Опишите её подробно, и оператор скоро ответит.',
        'sos_sent': 'Отправлено!',
        'sos_limit_exceeded': 'Превышен лимит вопросов.',
        'no_questions': 'Нет вопросов.',

        # Delivery status messages
        'no_active_orders': 'У вас нет активных заказов.',
        'order_status': 'Заказ <b>№{order_number}</b>{status}',
        'status_in_warehouse': ' на складе.',
        'status_on_the_way': ' в пути!',
        'status_arrived': ' прибыл на почту!',

        # Confirmation messages
        'make_sure_correct': 'Убедитесь, что всё правильно.',
        'ready': 'Готово!',
        'cancelled': 'Отменено!',
        'sent': 'Отправлено!',
        'no_such_choice': 'Такого выбора нет.',

        # Keyboard buttons
        'back': '👈 Назад',
        'confirm_order': '✅ Подтвердить заказ',
        'all_correct': '✅ Всё верно',
        'cancel': '🚫 Отмена',
        'answer': 'Ответить',
    }
}