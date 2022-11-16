from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Перезапуск бота'),
            KeyboardButton(text = 'Конфеты'),
            KeyboardButton(text = 'Крестики-нолики')
        ],
        [
            KeyboardButton(text = 'Подтвердить номер телефона', request_contact=True)
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выбери действие'
)

user_move_keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = '1'),
            KeyboardButton(text = '2'),
            KeyboardButton(text = '3')
        ],
        [
            KeyboardButton(text = '4'),
            KeyboardButton(text = '5'),
            KeyboardButton(text = '6')
        ],
        [
            KeyboardButton(text = '7'),
            KeyboardButton(text = '8'),
            KeyboardButton(text = '9')
        ],
        [
            KeyboardButton(text = 'Главное меню')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выбери действие'
)