from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

process_keyboard = [[InlineKeyboardButton(text = ' ', callback_data='1'), InlineKeyboardButton(text = ' ', callback_data='2'), InlineKeyboardButton(text = ' ', callback_data='3')],
                [InlineKeyboardButton(text = ' ', callback_data='4'), InlineKeyboardButton(text = ' ', callback_data='5'), InlineKeyboardButton(text = ' ', callback_data='6')],
                [InlineKeyboardButton(text = ' ', callback_data='7'), InlineKeyboardButton(text = ' ', callback_data='8'), InlineKeyboardButton(text = ' ', callback_data='9')],
                [InlineKeyboardButton(text = 'Главное меню', callback_data='Главное меню')]]

tictactoe_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=process_keyboard)

start_keyboard = [[InlineKeyboardButton(text = 'Перезапуск бота', callback_data='Перезапуск бота')],
                [InlineKeyboardButton(text = 'Крестики-нолики', callback_data='Крестики-нолики')]]

game_start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=start_keyboard)