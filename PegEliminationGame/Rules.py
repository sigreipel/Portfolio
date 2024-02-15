# Class for the Rules

class Rules:

    def __init__(self):  # empty map
        self.__board = []
        self.__start_row = -1
        self.__start_col = -1
        self.__eliminated_pegs = 0

    def starting_blank(self):  # starting location
        return self.__start_col, self.__start_row

    def num_rows(self):  # returns rows
        return len(self.__board)

    def num_columns(self):  # returns columns
        if self.num_rows == 0:
            return 0
        else:
            return len(self.__board[0])

    def load_from_file(self, filename):
        # stole from a CS066 Professor Manley lab homework
        self.__board = []
        self.__start_row = -1
        self.__start_col = -1
        with open(filename, 'r') as board:
            board = board.readlines()
            first_row_size = len(board[0]) - 1
            for line in board:
                line = line.rstrip()
                if len(line) != first_row_size:
                    raise Exception("Row and columns do not match.", filename)
                self.__board.append(list(line))

        for row in range(self.num_rows()):
            for col in range(self.num_columns()):
                if self.__board[row][col] == 'B':  # blank spot
                    self.__start_row = row
                    self.__start_col = col

    def __repr__(self):
        board = ""
        for row in range(self.num_rows()):
            for col in range(self.num_columns()):
                board += self.__board[row][col] + " "
            board += "\n"
        print("\nEliminated pegs: " + str(self.__eliminated_pegs))
        return board

    def clean_board(self):
        for row in range(self.num_rows()):
            for col in range(self.num_columns()):
                if self.__board[row][col] == "X":
                    self.__board[row][col] = "*"

    def peg_eliminator(self, col, row, direction):
        if not self.peg_identifier(col, row):
            print("\nNo peg exists in", col, ",", row)
            return False
        if direction == "":
            print("\nEnter a direction")
            return False
        if direction == "w":
            if self.legal_move(col, row, direction):
                print("Twas legal")
                self.__board[row - 2][col] = "X"
                self.__board[row - 1][col] = "B"
                self.__board[row][col] = "B"
                self.__eliminated_pegs += 1
        if direction == "a":
            if self.legal_move(col, row, direction):
                self.__board[row][col - 2] = "X"
                self.__board[row][col - 1] = "B"
                self.__board[row][col] = "B"
                self.__eliminated_pegs += 1
        if direction == "s":
            if self.legal_move(col, row, direction):
                self.__board[row + 2][col] = "X"
                self.__board[row + 1][col] = "B"
                self.__board[row][col] = "B"
                self.__eliminated_pegs += 1
        if direction == "d":
            if self.legal_move(col, row, direction):
                self.__board[row][col + 2] = "X"
                self.__board[row][col + 1] = "B"
                self.__board[row][col] = "B"
                self.__eliminated_pegs += 1

    def peg_identifier(self, col, row):
        if self.__board[row][col] == '*':
            return True
        else:
            return False

    def blank_identifier(self, col, row):
        if self.__board[row][col] == "B":
            return True
        else:
            return False

    def legal_move(self, col, row, direction):

        if row < 0 or row >= self.num_rows() or col < 0 or col >= self.num_columns():
            return False

        if direction == "w":
            if (row - 2 >= 0) and (self.peg_identifier(col, row - 1) == True) and (
                    self.blank_identifier(col, row - 2) == True):
                return True
        if direction == "a":
            if (col - 2 >= 0) and (self.peg_identifier(col - 1, row) == True) and (
                    self.blank_identifier(col - 2, row) == True):
                return True
        if direction == "s":
            if (row + 2 <= self.num_rows()) and (self.peg_identifier(col, row + 1) == True) and (
                    self.blank_identifier(col, row + 2) == True):
                return True
        if direction == "d":
            if (col + 2 <= self.num_columns()) and (self.peg_identifier(col + 1, row) == True) and (
                    self.blank_identifier(col + 2, row) == True):
                return True
        print("\nNot a legal move")
        return False

    def winning_condition(self):
        total_pegs = 0
        for row in range(self.num_rows()):
            for col in range(self.num_columns()):
                total_pegs += 1
        if self.__eliminated_pegs == total_pegs:
            return True

        return False
