import copy, random

# Game mechanics engine. Used by both the UI and the simulator.
class Game:
    def __init__(self, init_matrix=None) -> None:
        self.row_count = 6
        self.col_count = 7
        self.set_state(init_matrix)

    # set the game state using given intial state of the board
    def set_state(self, init_matrix=None):
        self.undoMat = []
        if init_matrix is None:
            self.matrix = self.new_matrix()
        else:
            self.matrix = copy.deepcopy(init_matrix)

    # create a new blank matrix of the board where board = matrix[col][row]
    def new_matrix(self):
        return [[0 for i in range(self.row_count)] for j in range(self.col_count)]

    # get the current state of the board
    def current_state(self):
        return self.matrix

    # place piece in the board
    def place(self, position, player):
        # position = player's chosen column
        row = 0
        if self.can_place(position):
            for j in range(self.row_count-1, 0, -1):
                if self.matrix[position][j] == 0:
                    row = j
                    break
        if player == 1:
            self.matrix[position][row] = 1
        elif player == 2:
            self.matrix[position][row] = 2

    # check to see if we can place a piece in the board
    def can_place(self, position):
        for j in range(self.row_count-1, -1, -1):
            if self.matrix[position][j] == 0:
                return True
        return False

    # get the open slots of the board in tuple (col, row)
    def get_open_slots(self):
        slots = []
        for i in range(self.col_count):
            for j in range(self.row_count):
                if self.matrix[i][j] == 0:
                    slots.append((i, j))
        return slots

    # check to see if the game is over
    def game_over(self, player):
        # checking horizontal connect 4
        for i in range(self.col_count-3):
            for j in range(self.row_count):
                if self.matrix[i][j] == player and self.matrix[i+1][j] == player and self.matrix[i+2][j] == player and self.matrix[i+3][j] == player:
                    return True
        # checking vertical connect 4
        for i in range(self.col_count):
            for j in range(self.row_count-3):
                if self.matrix[i][j] == player and self.matrix[i][j+1] == player and self.matrix[i][j+2] == player and self.matrix[i][j+3] == player:
                    return True
        # checking for \ diagonal connect 4
        for i in range(self.col_count-3):
            for j in range(self.row_count-3):
                if self.matrix[i][j] == player and self.matrix[i+1][j+1] == player and self.matrix[i+2][j+2] == player and self.matrix[i+3][j+3] == player:
                    return True
        # checking for / diagonal connect 4
        for i in range(self.col_count-3):
            for j in range(3, self.row_count):
                if self.matrix[i][j] == player and self.matrix[i+1][j-1] == player and self.matrix[i+2][j-2] == player and self.matrix[i+3][j-3] == player:
                    return True
        return False

    # undo placed piece one state back (**optional**)
    # def undo(self):
    #    pass

    # save the current board state (**optional**)
    # def save_state(self, filename="savedata"):
    # pass

    # load the most recent and currrent board state (**optional**)
    # def load_state(self, filename="savedata"):
    # pass

    # when loading the most recent board state, read by state line (**optional**)
    # def load_state_line(self, line):
    # pass
