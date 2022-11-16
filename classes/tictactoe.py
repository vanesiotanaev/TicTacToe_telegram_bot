class Tictactoe:
    user_id: int
    table_dict: dict
    possible_moves: list
    first_move: int

    def __init__(self, user_id: int, table_dict: dict, possible_moves: list, first_move: int):
        self.user_id = user_id
        self.table_dict = table_dict
        self.possible_moves = possible_moves
        self.first_move = first_move

    def show_object(self):
        return(self.user_id, self.table_dict, self.possible_moves, self.first_move)
