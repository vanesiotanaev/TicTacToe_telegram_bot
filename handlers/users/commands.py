from loader import dp, bot, db
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards import process_keyboard, game_start_inline_keyboard, tictactoe_inline_keyboard
import time
import view
import model
from classes import Tictactoe

@dp.message_handler(commands='start') 
async def start(message: types.Message):
    await message.answer(text = f'Привет, {message.from_user.first_name}! 🖖' + '\nТы находишься в Главном меню.' + '\nВыбери действие...', 
    reply_markup = game_start_inline_keyboard)

@dp.callback_query_handler(text = ['Главное меню', 'Перезапуск бота'])
async def main_menu(callback: types.CallbackQuery):
    await bot.edit_message_text(text = f'Привет, {callback.from_user.first_name}! 🖖' + '\nТы находишься в Главном меню.' + '\nВыбери действие...', 
    chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
    reply_markup = game_start_inline_keyboard)

@dp.callback_query_handler(text = ['Крестики-нолики'])
async def tictactoe(callback: types.CallbackQuery):
    if callback.data == "Крестики-нолики":
        new_game = Tictactoe(callback.from_user.id, model.new_game_dict(), list(model.new_game_dict().values()), model.first_move())
        
        db.add_tictactoe_session(db.get_tictactoe_sessions_count()+1, new_game.user_id, model.dict_values_to_string(new_game.table_dict),
        model.list_to_string(new_game.possible_moves), new_game.first_move)

        await bot.edit_message_text(text = 'Игра "Крестики-нолики"!', chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
        reply_markup = tictactoe_inline_keyboard)
        time.sleep(1)

        user_current_session_id = db.tictactoe_sessions_by_user_id(new_game.user_id)[-1][0]

        if db.tictactoe_first_move(user_current_session_id)[0][0] == 1:
            print(user_current_session_id)

            await bot.edit_message_text(text = f'{callback.from_user.first_name}, ты ходишь первым! 👈',
            chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
            reply_markup = tictactoe_inline_keyboard)       
        else:
            await bot.edit_message_text(text = f'Начинает компьютер! 🤖',
            chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
            reply_markup = tictactoe_inline_keyboard)

            user_current_session_id = db.tictactoe_sessions_by_user_id(callback.from_user.id)[-1][0]
            user_current_table_dict = model.string_to_dict(db.tictactoe_table_dict(user_current_session_id)[0][0])
            user_current_possible_moves = model.string_to_list(db.tictactoe_possible_moves(user_current_session_id)[0][0])

            time.sleep(1)
            comp = model.comp_logic(user_current_table_dict, user_current_possible_moves)
            user_current_table_dict[int(comp)] = 'O'
            user_current_possible_moves.remove(comp)

            to_be_converted_user = user_current_table_dict
            list_2D = model.dict_to_2D_list(to_be_converted_user)
            small_current = model.keyboard_change(list_2D, process_keyboard)
            current_keyboard = InlineKeyboardMarkup(inline_keyboard=small_current)

            await bot.edit_message_text(text = f'{callback.from_user.first_name}, твой ход! 👈',
            chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
            reply_markup = current_keyboard)
            
            db.update_tictactoe_session(user_current_session_id,
            model.dict_values_to_string(user_current_table_dict),
            model.list_to_string(user_current_possible_moves))

@dp.callback_query_handler()
async def tictactoe_proccess(callback: types.CallbackQuery):

    user_current_session_id = db.tictactoe_sessions_by_user_id(callback.from_user.id)[-1][0]
    user_current_table_dict = model.string_to_dict(db.tictactoe_table_dict(user_current_session_id)[0][0])
    user_current_possible_moves = model.string_to_list(db.tictactoe_possible_moves(user_current_session_id)[0][0])

    to_be_converted_user = user_current_table_dict
    list_2D = model.dict_to_2D_list(to_be_converted_user)
    small_current = model.keyboard_change(list_2D, process_keyboard)
    current_keyboard = InlineKeyboardMarkup(inline_keyboard=small_current)

    if model.check_win(user_current_table_dict) or model.check_draw(user_current_possible_moves):
                await bot.edit_message_text(text = f'Игра окончена! ⛔',
                chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                reply_markup = current_keyboard)
    else:                
        move = callback.data
        if model.check_win(user_current_table_dict) or model.check_draw(user_current_possible_moves):
            await bot.edit_message_text(text = f'Игра окончена! ⛔',
            chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
            reply_markup = current_keyboard)
                
        if not move in user_current_possible_moves:
            await bot.edit_message_text(text = f'Ошибка ввода! 🤌',
            chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
            reply_markup = current_keyboard)
        else:
            user_current_table_dict[int(move)] = 'X'
            user_current_possible_moves.remove(move)
            
            db.update_tictactoe_session(user_current_session_id,
            model.dict_values_to_string(user_current_table_dict),
            model.list_to_string(user_current_possible_moves))

            user_current_session_id = db.tictactoe_sessions_by_user_id(callback.from_user.id)[-1][0]
            user_current_table_dict = model.string_to_dict(db.tictactoe_table_dict(user_current_session_id)[0][0])
            user_current_possible_moves = model.string_to_list(db.tictactoe_possible_moves(user_current_session_id)[0][0])
                    
            to_be_converted_user = user_current_table_dict
            list_2D = model.dict_to_2D_list(to_be_converted_user)
            small_current = model.keyboard_change(list_2D, process_keyboard)
            current_keyboard = InlineKeyboardMarkup(inline_keyboard=small_current)
                
            if model.check_win(user_current_table_dict):
                await bot.edit_message_text(text = f'Ура! Победа!!! 🎉',
                chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                reply_markup = current_keyboard)
            elif model.check_draw(user_current_possible_moves):
                await bot.edit_message_text(text = 'Ничья! 🤝', 
                chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                reply_markup = current_keyboard)
            else:
                await bot.edit_message_text(text = f'Ход компьютера! 🤖',
                chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                reply_markup = current_keyboard)
                time.sleep(1)
                comp = model.comp_logic(user_current_table_dict, user_current_possible_moves)
                user_current_table_dict[int(comp)] = 'O'
                user_current_possible_moves.remove(comp)

                db.update_tictactoe_session(user_current_session_id,
                model.dict_values_to_string(user_current_table_dict),
                model.list_to_string(user_current_possible_moves))

                to_be_converted_user = user_current_table_dict
                list_2D = model.dict_to_2D_list(to_be_converted_user)
                small_current = model.keyboard_change(list_2D, process_keyboard)
                current_keyboard = InlineKeyboardMarkup(inline_keyboard=small_current)

                if model.check_win(user_current_table_dict):
                    await bot.edit_message_text(text = 'Победa компьютера! 🤖',
                    chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                    reply_markup = current_keyboard)
                elif model.check_draw(user_current_possible_moves):
                    await bot.edit_message_text(text = 'Ничья! 🤝', 
                    chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                    reply_markup = current_keyboard)
                else:
                    await bot.edit_message_text(text = f'{callback.from_user.first_name}, твой ход! 👈',
                    chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                    reply_markup = current_keyboard)

# @dp.message_handler(text = ['Конфеты'])
# @dp.message_handler(commands='candies')
# async def candies_start(message: types.Message):
#     candies = 150
#     first_move = model.first_move()
#     model.create_candies_file(message.from_user.id, candies, first_move)
#     await message.answer(text = f'Правила игры "Конфеты":\n\nНа столе лежит 150 конфет. Игрок и компьютер по очереди забирают конфеты себе. За один ход можно забрать не менее 1 и не более 28 конфет. Выигрывает тот, кто сделал последний ход и забрал все оставшиеся конфеты. Удачи!')
#     await message.answer(text = f"Итак, есть {candies} конфет.")
#     if first_move == 0:
#         recommended = candies % 29
#         if not recommended == 0:
#             await message.answer(text = (f"Сколько конфет хотите забрать (1-28)? Может быть, {recommended}?"))
#         else:
#             await message.answer(text = (f"Сколько конфет хотите забрать (1-28)? "))
#     else:
#         candies = model.candies_logic(candies)
#         model.create_candies_file(message.from_user.id, candies, first_move)
#         await message.answer(text = (f"После хода компьютера осталось {candies} конфет."))
#         recommended = candies % 29
#         if not recommended == 0:
#             await message.answer(text = (f"Сколько конфет хотите забрать (1-28)? Может быть, {recommended}?"))
#         else:
#             await message.answer(text = (f"Сколько конфет хотите забрать (1-28)? "))


#     if model.what_game(message.from_user.id) == 'candies\n':
#         candies = int(model.get_candies_quantitiy(message.from_user.id))
#         if not message.text.isdigit() or int(message.text) > 28 or int(message.text) < 1 or int(message.text) > candies:
#             await message.answer(text = (f"Вы ввели что-то не то!"))
#         else:
#             candies = int(model.get_candies_quantitiy(message.from_user.id))
#             user = int(message.text)
#             candies -= user
#             if candies == 0:
#                 await message.answer(text = (f"{message.from_user.first_name} победил(a)! Осталось {candies} конфет!"))
#             else:
#                 await message.answer(text = (f"{message.from_user.first_name} забрал(a) {user} конфет! Осталось {candies}!"))
#                 model.create_candies_file(message.from_user.id, candies, '1')
#                 candies = model.candies_logic(candies)
#                 model.create_candies_file(message.from_user.id, candies, '1')
#                 await message.answer(text = (f"После хода компьютера осталось {candies} конфет."))
#                 if candies == 0:
#                     await message.answer(text = (f"Победил компьютер!"))
#                 else:
#                     recommended = candies % 29
#                     if not recommended == 0:
#                         await message.answer(text = (f"Сколько конфет хотите забрать (1-28)? Может быть, {recommended}?"))
#                     else:
#                         await message.answer(text = (f"Сколько конфет хотите забрать (1-28)?"))
            