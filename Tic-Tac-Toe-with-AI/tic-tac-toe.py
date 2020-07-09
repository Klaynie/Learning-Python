from enum import IntEnum
import random

class GameSession():
    
    def __init__(self, cells):
        global symbol_for_x, symbol_for_o
        self.cells = cells.replace('_',empty_cell_symbol)
        self.symbol_for_x = symbol_for_x
        self.symbol_for_o = symbol_for_o
        self.turn = self.count_symbol(self.get_symbol_for_x()) + self.count_symbol(self.get_symbol_for_o())
        self.scope = [1, 2, 3]
    
    def get_game_state(self):
        global error_messages, game_continues_messages, game_final_messages, symbol_for_x, symbol_for_o, empty_cell_symbol
        field_states = self.convert_field_to_states()
        count_o = self.count_symbol(symbol_for_o)
        count_x = self.count_symbol(symbol_for_x)
        count_win_conditions, count_x_wins, count_o_wins = self.count_field_states(field_states)
        if count_win_conditions > 1:
            result = error_messages[ErrorMessage.IMPOSSIBLE]
        elif count_o > count_x + 1 or count_x > count_o + 1:
            result = error_messages[ErrorMessage.IMPOSSIBLE]
        elif count_x_wins == 1:
            result = game_final_messages[GameFinaleMessage.X_WINS]
        elif count_o_wins == 1:
            result = game_final_messages[GameFinaleMessage.O_WINS]
        elif empty_cell_symbol in self.cells:
            result = game_continues_messages[GameContinueMessage.NOT_FINISHED]
        else:
            result = game_final_messages[GameFinaleMessage.DRAW]
        return result
    
    def get_symbol_for_x(self):
        return self.symbol_for_x
    
    def get_symbol_for_o(self):
        return self.symbol_for_o
    
    def set_turn(self):
        self.turn = self.count_symbol(self.get_symbol_for_x()) + self.count_symbol(self.get_symbol_for_o())
    
    def get_turn(self):
        return self.turn
    
    def get_game_scope(self):
        return self.scope
    
    def print_field(self):
        print("---------")
        print("| " + self.cells[0] + " " + self.cells[1] + " " + self.cells[2] + " |")
        print("| " + self.cells[3] + " " + self.cells[4] + " " + self.cells[5] + " |")
        print("| " + self.cells[6] + " " + self.cells[7] + " " + self.cells[8] + " |")
        print("---------")
        
    def count_symbol(self, symbol_to_count):
        result = 0
        for symbol in self.cells:
            if symbol == symbol_to_count:
                result += 1
        return result
    
    def convert_field_to_rows(self):
        return [self.cells[0] + self.cells[1] + self.cells[2]\
               ,self.cells[3] + self.cells[4] + self.cells[5]\
               ,self.cells[6] + self.cells[7] + self.cells[8]]

    def convert_field_to_columns(self):
        return [self.cells[0] + self.cells[3] + self.cells[6]\
               ,self.cells[1] + self.cells[4] + self.cells[7]\
               ,self.cells[2] + self.cells[5] + self.cells[8]]

    def convert_field_to_diagonals(self):
        return [self.cells[0] + self.cells[4] + self.cells[8]\
               ,self.cells[6] + self.cells[4] + self.cells[2]]

    def convert_field_to_states(self):
        rows = self.convert_field_to_rows()
        columns = self.convert_field_to_columns()
        diagonals = self.convert_field_to_diagonals()
        return [rows, columns, diagonals]
    
    def update_cell_with_value(self, cell_to_update, value):
        self.cells = self.cells[:cell_to_update] + value + self.cells[cell_to_update+1:]

    def count_field_states(self, field_states):
        global symbol_for_x, symbol_for_o
        win_condition_x = 3 * symbol_for_x
        win_condition_o = 3 * symbol_for_o
        count_win_conditions = 0
        count_x_wins = 0
        count_o_wins = 0
        for lists in field_states:
            for items in lists:
                if items == win_condition_x:
                    count_x_wins += 1
                    count_win_conditions += 1
                elif items == win_condition_o:
                    count_o_wins += 1
                    count_win_conditions += 1
        return count_win_conditions, count_x_wins, count_o_wins
    
    def return_cell_content(self, cell_number):
        return self.cells[cell_number]
    
    def cell_is_empty(self, cell_number):
        global empty_cell_symbol
        result = True
        if self.return_cell_content(cell_number) != empty_cell_symbol:
            result = False
        return result

class UserPrompt(IntEnum):
    INPUT_CELL = 0
    INPUT_COORDINATES = 1

class ErrorMessage(IntEnum):
    IMPOSSIBLE = 0
    INCORRECT_FIELD_AMOUNT = 1
    NON_NUMBER = 2
    OUT_OF_RANGE = 3
    OCCUPIED = 4

class GameContinueMessage(IntEnum):
    NOT_FINISHED = 0

class GameFinaleMessage(IntEnum):
    X_WINS = 0
    O_WINS = 1
    DRAW = 2

class AiTurnMessage(IntEnum):
    EASY = 0

symbol_for_x = 'X'
symbol_for_o = 'O'
empty_cell_symbol = ' '
user_input_prompts = ["Enter cells: ", "Enter the coordinates: "]
game_continues_messages = ["Game not finished"]
game_final_messages = [symbol_for_x + " wins", symbol_for_o + " wins", "Draw"]
error_messages = ["Impossible"\
                 ,"Please provide the correct amount of fields!"\
                 ,"You should enter numbers!"\
                 ,"Coordinates should be from 1 to 3!"\
                 ,"This cell is occupied! Choose another one!"]
ai_turn_messages = ['Making move level "easy"']

def is_correct_length(field_input):
    result = True
    if len(field_input) != 2:
        result = False
    return result

def is_number(field_input):
    result = True
    if not field_input[0].isdigit() or not field_input[1].isdigit():
        result = False
    return result

def is_in_scope(game_session, field_input):
    game_scope = game_session.get_game_scope()
    result = True
    if field_input[0] not in game_scope or field_input[1] not in game_scope:
        result = False
    return result

def is_valid_turn(game_session, new_field_input):
    global error_messages
    result = True
    if not is_number(new_field_input):
        print(error_messages[ErrorMessage.NON_NUMBER])
        result = False
    elif not is_correct_length(new_field_input):
        print(error_messages[ErrorMessage.INCORRECT_FIELD_AMOUNT])
        result = False
    elif is_number(new_field_input):
        new_field_input[0], new_field_input[1] = int(new_field_input[0]), int(new_field_input[1])
        if not is_in_scope(game_session, new_field_input):
            print(error_messages[ErrorMessage.OUT_OF_RANGE])
            result = False
        elif is_in_scope(game_session, new_field_input):
            cell_number = convert_input_to_cell(new_field_input)
            if not game_session.cell_is_empty(cell_number):
                print(error_messages[ErrorMessage.OCCUPIED])
                result = False
    return result

def convert_input_to_cell(new_field_input):
    if new_field_input == [1, 3]:
        return 0
    elif new_field_input == [1, 2]:
        return 3
    elif new_field_input == [1, 1]:
        return 6
    elif new_field_input == [2, 3]:
        return 1
    elif new_field_input == [2, 2]:
        return 4
    elif new_field_input == [2, 1]:
        return 7
    elif new_field_input == [3, 3]:
        return 2
    elif new_field_input == [3, 2]:
        return 5
    elif new_field_input == [3, 1]:
        return 8

def ai_turn(game_session):
    global ai_turn_messages
    print(ai_turn_messages[AiTurnMessage.EASY])
    keep_generating = True
    while keep_generating:
        field_1 = random.randint(1,3)
        field_2 = random.randint(1,3)
        new_field_input = [field_1, field_2]
        cell_number = convert_input_to_cell(new_field_input)
        if game_session.cell_is_empty(cell_number):
            result = [str(field_1), str(field_2)]
            keep_generating = False
    return result

def game_loop(game_session):
    global user_input_prompts
    stay_in_game = True
    while stay_in_game:
        stay_in_turn = True
        turn_counter = game_session.get_turn()
        while stay_in_turn:
            if turn_counter % 2 == 0:
                new_field_input = input(user_input_prompts[0]).split()
            elif turn_counter % 2 != 0:
                new_field_input = ai_turn(game_session)
            if is_valid_turn(game_session, new_field_input):
                stay_in_turn = False
                cell = convert_input_to_cell(new_field_input)
                if turn_counter % 2 == 0:
                    game_session.update_cell_with_value(cell, game_session.get_symbol_for_x())
                    game_session.set_turn()
                elif turn_counter % 2 != 0:
                    game_session.update_cell_with_value(cell, game_session.get_symbol_for_o())
                    game_session.set_turn()
        game_session.print_field()
        game_state = game_session.get_game_state()
        print(game_state)
        if game_state not in game_continues_messages:
            stay_in_game = False

if __name__ == "__main__":
    cells = '_________'
    new_game_session = GameSession(cells)
    new_game_session.print_field()
    game_loop(new_game_session)