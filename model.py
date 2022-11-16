import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def new_game_dict():
    dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    return dict

def possible_moves_list(dict):
    return list(dict.values())

def string_to_dict(string: str) -> dict:
    list_1 = string[1:].split(' ')
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return dict(zip(list_2, list_1))

def string_to_list(string: str) -> list:
    return string[1:].split(' ')

def create_file(id, dict, moves, move, game = 'tictactoe'):
    path = f'{str(id)}.txt'
    with open(path, 'w') as file:
        file.write(str(game)+'\n')
        file.write(str(id)+'\n')
        file.write(str(dict)+'\n')
        file.write(str(moves)+'\n')
        file.write(str(move)+'\n')

def edit_file(id, dict, moves, move, game = 'tictactoe'):
    path = f'{str(id)}.txt'
    with open(path, 'w') as file:
        file.write(str(game)+'\n')
        file.write(str(id)+'\n')
        file.write(str(dict)+'\n')
        file.write(str(moves)+'\n')
        file.write(str(move)+'\n')

def what_game(id):
    path = f'{str(id)}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        return lines[0]        

def take_id(id):
    path = f'{str(id)}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        return lines[1]

def take_dict(id):
    path = f'{str(id)}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        return lines[2][:-1]

def take_moves(id):
    path = f'{str(id)}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        return lines[3]

def take_first(id):
    path = f'{str(id)}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        return lines[4]

def take_comp_move(id):
    path = f'{str(id)}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i] == 'O':
                return lines[i-4]

def dict_to_2D_list(dict):
    single = list(dict.values())
    list1 = []
    list2 = []
    list3 = []
    superlist = []
    list1.append(single[0])
    list1.append(single[1])
    list1.append(single[2])
    list2.append(single[3])
    list2.append(single[4])
    list2.append(single[5])
    list3.append(single[6])
    list3.append(single[7])
    list3.append(single[8])
    superlist.append(list1)
    superlist.append(list2)
    superlist.append(list3)

    return superlist

def keyboard_change(list_2D: list, process_keyboard: list):
    for i in range(len(list_2D)):
        for j in range(len(list_2D[i])):
            if list_2D[i][j] == 'X':
                process_keyboard[i][j] = InlineKeyboardButton(text = '❌', callback_data='X')
            elif list_2D[i][j] == 'O':
                process_keyboard[i][j] = InlineKeyboardButton(text = '⭕', callback_data='O')
            else:
                process_keyboard[i][j] = InlineKeyboardButton(text = ' ', callback_data=list_2D[i][j])
    
    return process_keyboard

def convert_to_dict(string):
    list_1 = []
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(string)):
        if string[i] == "'":
            list_1.append(string[i+1])
        for i in range(len(list_1)):
            if list_1[i] == ',':
                list_1.remove(list_1[i])
        for i in range(len(list_1)):
            if list_1[i] == '}':
                list_1.remove(list_1[i])
    
    return dict(zip(list_2, list_1))

def convert_to_moveslist(string):
    list_1 = []
    for i in range(len(string)):
        if string[i].isdigit():
            list_1.append(string[i])
    
    return list_1

def first_move():
    return random.randint(0, 1)

def check_win(dict):
    if dict[1] == dict[2] == dict[3] \
    or dict[4] == dict[5] == dict[6] \
    or dict[7] == dict[8] == dict[9] \
    or dict[1] == dict[4] == dict[7] \
    or dict[2] == dict[5] == dict[8] \
    or dict[3] == dict[6] == dict[9] \
    or dict[1] == dict[5] == dict[9] \
    or dict[3] == dict[5] == dict[7]:
        return True

def check_draw(moves):
    if len(moves) == 0:
        return True

def check_clear(dict):
    if 'X' in dict.values() or 'O' in dict.values():
        return True

def comp_logic(dict, moves):
    if not 'O' in dict.values() and not 'X' in dict.values():
        return '5'
    elif dict[1] == dict[4] == 'O' and (dict[7] != 'X' and dict[7] != 'O'):
        return '7'
    elif dict[4] == dict[7] == 'O' and (dict[1] != 'X' and dict[1] != 'O'):
        return '1'
    elif dict[2] == dict[5] == 'O' and (dict[8] != 'X' and dict[8] != 'O'):
        return '8'
    elif dict[5] == dict[8] == 'O' and (dict[2] != 'X' and dict [2] != 'O'):
        return '2'
    elif dict[3] == dict[6] == 'O' and (dict[9] != 'X' and dict[9] != 'O'):
        return '9'
    elif dict[6] == dict[9] == 'O' and (dict[3] != 'X' and dict[3] != 'O'):
        return '3'
    elif dict[1] == dict[2] == 'O' and (dict[3] != 'X' and dict[3] != 'O'):
        return '3'
    elif dict[2] == dict[3] == 'O' and (dict[1] != 'X' and dict[1] != 'O'):
        return '1'
    elif dict[4] == dict[5] == 'O' and (dict[6] != 'X' and dict[6] != 'O'):
        return '6'
    elif dict[5] == dict[6] == 'O' and (dict[4] != 'X' and dict[4] != 'O'):
        return '4'
    elif dict[7] == dict[8] == 'O' and (dict[9] != 'X' and dict[9] != 'O'):
        return '9'
    elif dict[8] == dict[9] == 'O' and (dict[7] != 'X' and dict[7] != 'O'):
        return '7'
    elif dict[1] == dict[5] == 'O' and (dict[9] != 'X' and dict[9] != 'O'):
        return '9'
    elif dict[5] == dict[9] == 'O' and (dict[1] != 'X' and dict[1] != 'O'):
        return '1'
    elif dict[3] == dict[5] == 'O' and (dict[7] != 'X' and dict[7] != 'O') :
        return '7'
    elif dict[5] == dict[7] == 'O' and (dict[3] != 'X' and dict[3] != 'O'):
        return '3'
    elif dict[1] == dict[3] == 'O' and (dict[2] != 'X' and dict[2] != 'O'):
        return '2'
    elif dict[4] == dict[6] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'
    elif dict[7] == dict[9] == 'O' and (dict[8] != 'X' and dict[8] != 'O'):
        return '8'
    elif dict[1] == dict[7] == 'O' and (dict[4] != 'X' and dict[4] != 'O'):
        return '4'
    elif dict[2] == dict[8] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'
    elif dict[3] == dict[9] == 'O' and (dict[6] != 'X' and dict[6] != 'O'):
        return '6'
    elif dict[1] == dict[9] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'
    elif dict[3] == dict[7] == 'O' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'                      
    elif dict[1] == dict[4] == 'X' and (dict[7] != 'X' and dict[7] != 'O'):
        return '7'
    elif dict[4] == dict[7] == 'X' and (dict[1] != 'X' and dict[1] != 'O'):
        return '1'
    elif dict[2] == dict[5] == 'X' and (dict[8] != 'X' and dict[8] != 'O'):
        return '8'
    elif dict[5] == dict[8] == 'X' and (dict[2] != 'X' and dict [2] != 'O'):
        return '2'
    elif dict[3] == dict[6] == 'X' and (dict[9] != 'X' and dict[9] != 'O'):
        return '9'
    elif dict[6] == dict[9] == 'X' and (dict[3] != 'X' and dict[3] != 'O'):
        return '3'
    elif dict[1] == dict[2] == 'X' and (dict[3] != 'X' and dict[3] != 'O'):
        return '3'
    elif dict[2] == dict[3] == 'X' and (dict[1] != 'X' and dict[1] != 'O'):
        return '1'
    elif dict[4] == dict[5] == 'X' and (dict[6] != 'X' and dict[6] != 'O'):
        return '6'
    elif dict[5] == dict[6] == 'X' and (dict[4] != 'X' and dict[4] != 'O'):
        return '4'
    elif dict[7] == dict[8] == 'X' and (dict[9] != 'X' and dict[9] != 'O'):
        return '9'
    elif dict[8] == dict[9] == 'X' and (dict[7] != 'X' and dict[7] != 'O'):
        return '7'
    elif dict[1] == dict[5] == 'X' and (dict[9] != 'X' and dict[9] != 'O'):
        return '9'
    elif dict[5] == dict[9] == 'X' and (dict[1] != 'X' and dict[1] != 'O'):
        return '1'
    elif dict[3] == dict[5] == 'X' and (dict[7] != 'X' and dict[7] != 'O') :
        return '7'
    elif dict[5] == dict[7] == 'X' and (dict[3] != 'X' and dict[3] != 'O'):
        return '3'
    elif dict[1] == dict[3] == 'X' and (dict[2] != 'X' and dict[2] != 'O'):
        return '2'
    elif dict[4] == dict[6] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'
    elif dict[7] == dict[9] == 'X' and (dict[8] != 'X' and dict[8] != 'O'):
        return '8'
    elif dict[1] == dict[7] == 'X' and (dict[4] != 'X' and dict[4] != 'O'):
        return '4'
    elif dict[2] == dict[8] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'
    elif dict[3] == dict[9] == 'X' and (dict[6] != 'X' and dict[6] != 'O'):
        return '6'
    elif dict[1] == dict[9] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'
    elif dict[3] == dict[7] == 'X' and (dict[5] != 'X' and dict[5] != 'O'):
        return '5'                  
    else:
        return random.choice(moves)

def human(sweets):
    recommended = sweets % 29
    if not recommended == 0:
        a = int(input(f"Введите количество конфет (1-28). Может быть, {recommended}?: "))
    else:
        a = int(input(f"Введите количество конфет (1-28): "))
    while a > 28 or a < 1:
        a = int(input("Вы ввели недопустимое кол-во. Введите количество конфет (1-28): "))
    sweets -= a
    if sweets == 0:
        print("Игрок победил!")
    else:
        print(f"Игрок забрал {a} конфет. Осталось {sweets}.")

    return sweets

def candies_logic(sweets):
    b = sweets % 29
    while b < 1 or b > 28:
        b = random.randint(1, 28)
    else:
        sweets -= b
    return sweets

def create_candies_file(id, candies, first_move, game = 'candies'):
    path = f'{str(id)}.txt'
    with open(path, 'w') as file:
        file.write(str(game)+'\n')
        file.write(str(id)+'\n')
        file.write(str(candies)+'\n')
        file.write(str(first_move)+'\n')

def get_candies_quantitiy(id):
    path = f'{str(id)}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        return lines[2][:-1]

def check_candies_win(candies):
    if candies <= 0:
        return True

def dict_values_to_string(table_dict: dict) -> str:
    string = ''
    for i in table_dict.values():
        string = string + ' ' + i
    return str(string)

def list_to_string(possible_moves: list) -> str:
    string = ''
    for i in possible_moves:
        string = string + ' ' + str(i)
    return str(string)
