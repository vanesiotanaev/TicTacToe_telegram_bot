import sqlite3

class Database: 
    def __init__(self, db_path: str = 'games_database.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)
    
    def execute(self, sql: str, parameters: tuple = tuple(),
            fetchone = False, fetchall = False, commit = False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()

        return data
    
    def create_table_tictactoe(self):
        sql = """
        CREATE TABLE Tictactoe(
        session_id int NOT NULL,
        user_id int NOT NULL,
        table_dict text NOT NULL,
        possible_moves text NOT NULL,
        first_move int NOT NULL,
        PRIMARY KEY (session_id)
        );
        """
        self.execute(sql, commit=True)
    
    def update_user_phone(self, user_id: int, phone: str):
        sql = 'UPDATE Users SET phone=? WHERE user_id=?'
        return self.execute(sql, parameters=(phone, user_id), commit=True)
    
    def add_tictactoe_session(self, session_id: int, user_id: int, table_dict: str, possible_moves: str, first_move: int):
        sql = 'INSERT INTO Tictactoe(session_id, user_id, table_dict, possible_moves, first_move) VALUES(?, ?, ?, ?, ?)'
        parameters = (session_id, user_id, table_dict, possible_moves, first_move)
        self.execute(sql, parameters, commit = True)

    def delete_tictactoe_session(self, **kwargs):
        sql = 'DELETE FROM Tictactoe WHERE '
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def update_tictactoe_session(self, session_id: int, table_dict: str, possible_moves: str):
        sql = 'UPDATE Tictactoe SET table_dict=?, possible_moves=? WHERE session_id=?'
        return self.execute(sql, parameters=(table_dict, possible_moves, session_id), commit=True)
    
    def tictactoe_first_move(self, session_id: int):
        sql = 'SELECT first_move FROM Tictactoe WHERE session_id=?'
        return self.execute(sql, parameters = (session_id,), fetchall = True)
    
    def tictactoe_table_dict(self, session_id: int):
        sql = 'SELECT table_dict FROM Tictactoe WHERE session_id=?'
        return self.execute(sql, parameters = (session_id,), fetchall = True)
    
    def tictactoe_possible_moves(self, session_id: int):
        sql = 'SELECT possible_moves FROM Tictactoe WHERE session_id=?'
        return self.execute(sql, parameters = (session_id,), fetchall = True)

    def get_tictactoe_sessions_count(self) -> int:
        sql = 'SELECT * FROM Tictactoe'
        return len(self.execute(sql, fetchall=True))
    
    def tictactoe_sessions_by_user_id(self, user_id) -> int:
        sql = 'SELECT session_id FROM Tictactoe WHERE user_id=?'
        return self.execute(sql, parameters = (user_id,), fetchall=True)
    
    def add_item(self, id: int, name: str = None, count: int = 0, photo_path: str = ''):
        sql = 'INSERT INTO Items(id, name, count, photo_path) VALUES(?, ?, ?, ?)'
        parameters = (id, name, count, photo_path)
        self.execute(sql, parameters, commit = True)
    
    def add_user(self, user_id: int, username: str = None, first_name: str = None, second_name: str = None, phone: str = None):
        sql = 'INSERT INTO Users(user_id, username, first_name, second_name, phone) VALUES(?, ?, ?, ?, ?)'
        parameters = (user_id, username, first_name, second_name, phone)
        self.execute(sql, parameters, commit = True)

    def select_items_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM Items WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall = True)

    def select_all_items(self) -> list:
        sql = 'SELECT * FROM Items'
        return self.execute(sql, fetchall = True)
    
    def update_item_count(self, id: int, count: str):
        sql = 'UPDATE Items SET count=? WHERE id=?'
        return self.execute(sql, parameters=(count, id), commit=True)
    
    def get_items_count(self) -> int:
        sql = 'SELECT * FROM Items'
        return len(self.execute(sql, fetchall=True))
    
    def delete_user(self, **kwargs):
        sql = 'DELETE FROM Users WHERE '
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def delete_all(self):
        self.execute('DELETE FROM Users WHERE True', commit = True)
        self.execute('DELETE FROM items WHERE True', commit = True)

    def drop_all(self):
        self.execute('DROP TABLE Users', commit = True)
        self.execute('DROP TABLE Items', commit = True)

    def get_id(self) -> list:
        sql = 'SELECT id FROM Users'
        return self.execute(sql, fetchall = True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += ' AND '.join(
            [
                f'{item} = ?' for item in parameters
            ]
        )
        return sql, tuple(parameters.values())