import sqlite3
from pathlib import Path

from db_api import Database

from aiogram import Bot, Dispatcher
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db_path = Path('db_api', 'database', 'games_database.db')
db = Database(db_path=db_path)

try:
    db.create_table_tictactoe()
except sqlite3.OperationalError as e:
    print(e)
except Exception as e:
    print(e)