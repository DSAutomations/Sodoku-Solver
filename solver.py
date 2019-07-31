# Sudoku Solver
# Author: Dylan Straub
#
# This is a Sudoku solver written in Python3 with no dependencies demonstrating
# object oriented programming and recursion.
#
# Inspired by a YouTube lecture series by Richard Buckland, UNSW
# https://www.youtube.com/user/BucklandRichard/videos
#
# This program consists of three classes:
#     Tile:   models an indivial square of the Sudoku board
#             aware of its own row/column position and value
#
#     Board:  a collection of 81 tile objects in a list
#             able to check if a move is valid
# 
#     Solve:  recursive solving logic
#             must instantiate with a board object which is then immediatley solved
#
# The Sudoku board is represented as a list indexed in a left-to-right, top-to-bottom order.
#
# A valid input string is an 81 character string indexed in this manner
# All blank spaces shall be represented by the '.' character.
#
# For example, the the following board:
#   ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
#   ║   │   │   ║ 9 │   │   ║   │ 2 │   ║
#   ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
#   ║   │   │ 3 ║   │   │   ║ 7 │ 9 │   ║
#   ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
#   ║ 8 │   │   ║   │   │ 6 ║ 5 │   │   ║
#   ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
#   ║ 6 │ 7 │   ║   │   │ 3 ║   │   │   ║
#   ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
#   ║   │   │ 1 ║   │   │   ║ 8 │   │   ║
#   ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
#   ║   │   │   ║ 1 │ 5 │ 4 ║   │   │ 3 ║
#   ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
#   ║ 7 │   │   ║   │ 4 │   ║   │   │   ║
#   ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
#   ║   │   │   ║   │ 7 │ 9 ║   │   │ 1 ║
#   ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
#   ║ 3 │   │ 8 ║   │   │ 2 ║   │   │   ║
#   ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
# would be represented by the following input string:
# '...9...2...3...79.8....65..67...3.....1...8.....154..37...4........79..13.8..2'
#
# You are expected to provide a valid and solvable input.
#
# This code will run as-is to produce a solution to the example above
# every attemptted solution will be printed on the console to visualize the
# recursive mechanism in action.

class Tile(object):
    """a tile to place on the board, knows its own x and y coords, its zone, and its value """
    def __init__(self, col, row, val = None):
        self.col = col
        self.row = row
        self.value = val
        self.zone = self.find_zone()

    def get_value(self):
        if self.value == None:
            return str('.')
        else:
            return self.value

    def find_zone(self):
        """ constructor helper, determines which 'ninth' of the board this tile is on"""
        if self.col in [0,1,2]:
            x_zone = 1
        elif self.col in [3,4,5]:
            x_zone = 2
        elif self.col in [6,7,8]:
            x_zone = 3
        if self.row in [0,1,2]:
            y_zone = 10
        elif self.row in [3,4,5]:
            y_zone = 20
        elif self.row in [6,7,8]:
            y_zone = 30
        return x_zone + y_zone

    def duplicate(self):
        return Tile(self.col, self.row, self.value)

    def __repr__(self):
        return '< Tile at ({},{}), Zone: {} Value:{} >'.format(self.col, self.row, self.zone, self.value)


class Board(object):
    """ houses a 9x9 array of tiles, will check if a move is valid """

    def __init__(self, board_in = []):
        self.board = [t.duplicate() for t in board_in]

    def initialize(self):
        """ populates a board with empty tiles """
        for row in range(9):
            for col in range(9):
                self.board.append(Tile(col, row))

    def fill_board(self, input_string):
        """ for inputting initial values into empty board """
        for t, i in zip(self.board, list(input_string)):
            if i == '.':
                continue
            t.value = int(i)

    def check_valid(self, index, value):
        """ returns true and places tile on board if valid, returns false if not """
        tile = self.board[index]
        if self.check_col(tile.col, value) and \
           self.check_row(tile.row, value) and \
           self.check_zone(tile.zone, value):
            return True
        else:
            return False

    def place_tile(self, index, value):
        """ places a tile on the board and returns a new board instance with that move in place """
        new_board = Board(self.board)
        new_board.board[index].value = value
        return new_board

    def check_col(self, column, value):
        """ helper function for check_valid() """
        if value in [t.value for t in self.board if t.col == column and t.value]:
            return False
        else:
            return True

    def check_row(self, row, value):
        """ helper function for check_valid() """
        if value in [t.value for t in self.board if t.row == row and t.value]:
            return False
        else:
            return True

    def check_zone(self, zone, value):
        """ helper function for check_valid() """
        if value in [t.value for t in self.board if t.zone == zone and t.value]:
            return False
        else:
            return True

    def is_full(self):
        """ determine if the board is full, used by the solver to check if finished """
        for t in self.board:
            if not t.value:
                return False
        return True

    def first_empty(self):
        """ returns the index of the lowest empty cell, used by solver """
        lowest_empty = 0
        while self.board[lowest_empty].value:
            lowest_empty += 1
        return lowest_empty

    def print_board(self):
        """ prints the board to the console """
        output = ['\n']
        for tile in self.board:
            output.append(str(tile.get_value()))
            if tile.col == 8:
                output.append('\n')
        print(' '.join(output))

    def tile_by_x_y(self, x, y):
        """ debugging function """
        array_value = (9 * y) + x
        print('Array value is: {}'.format(array_value))
        return self.board[array_value]

    def pprint_zone(self, zone):
        """ debugging function """
        zone = [t for t in self.board if t.zone == zone]
        print(zone[:3])
        print(zone[3:6])
        print(zone[6:])

class Solve(object):
    def __init__(self, board):
        self.board = board
        self.solution = self.solve(self.board)

    def solve(self, this_board):
        if this_board.is_full():
            return this_board
        first_empty = this_board.first_empty()
        for i in range(1,10):
            if this_board.check_valid(first_empty, i):
                next_board = this_board.place_tile(first_empty, i)
                next_board.print_board()
                returned_board = self.solve(next_board) # recursive call
                if returned_board == None:
                    continue
                if returned_board.is_full():
                    return returned_board

myboard = Board()
myboard.initialize()
myboard.fill_board('...9...2...3...79.8....65..67...3.....1...8.....154..37...4........79..13.8..2')
myboard.print_board()

mysolver = Solve(myboard)
mysolver.solution.print_board()


# '8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..'
# the preceeding string sample input string for the 'world's hardest' sodoku puzzle presented here:
# https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
