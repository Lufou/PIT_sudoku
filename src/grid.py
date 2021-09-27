#-*-coding: utf8-*-

from os import error

class SudokuGrid:

    grid = [[0] * 9 for i in range(9)]

    def __init__(self, initial_values_str):
        try:
            for i in range(0,9):
                for j in range(0,9):
                    self.grid[i][j] = int(initial_values_str[i*9+j])
        except ValueError:
            print("Erreur : Le string d'entrée ne peut pas être interprété cmme une grille de Sudoku.")

    @staticmethod
    def from_file(filename, line):
        f = open(filename, "r")
        line = f.readline(line)
        f.close()
        return SudokuGrid(line)

    @staticmethod
    def from_stdin():
        res = ""
        while not res.isnumeric():
            input("Entrez la grille de Sudoku : ")
        
        return SudokuGrid(res)

    def __str__(self):
        res = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                res += str(self.grid[i][j])
        return res

    def get_row(self, i):
        res = []
        for j in range(len(self.grid)):
            res.append(self.grid[i][j])
        return res
        
    def get_col(self, j):
        res = []
        for i in range(len(self.grid)):
            res.append(self.grid[i][j])
        return res

    def get_region(self, reg_row, reg_col):
        res = []
        print(self.grid)
        for i in range(reg_row*3,reg_row*3+3):
            for j in range(reg_col*3,reg_col*3+3): 
                res.append(self.grid[i][j])
                print(self.grid[i][j])
        return res
        
    def get_empty_positions(self):
        res = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0:
                    res.append((i,j))
        return res

    def write(self, i, j, v, force=True):
        if i < 0 or i >= len(self.grid):
            raise ValueError()
        elif j < 0 or j >= len(self.grid[0]):
            raise ValueError()
        elif v < 1 or v > 9:
            raise ValueError()

        if self.grid[i][j] != 0 or force:
            self.grid[i][j] = v

    def copy(self):
        new_instance = self.__new__(self.__class__)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                new_instance.grid[i][j] = self.grid[i][j]
        return new_instance