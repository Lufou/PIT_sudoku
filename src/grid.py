#-*-coding: utf8-*-

from os import error


class SudokuGrid:

    grid = [[0]*9]*9

    def __init__(self, initial_values_str):
        try:
            count = 1
            for i in range(0,9):
                for j in range(0,9):
                    self.grid[i][j] = int(initial_values_str[count-1])
                    count += 1
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
        for i in range(self.grid.__len__):
            for j in range(self.grid[0].__len__):
                res += str(self.grid[i][j])
        return res

    def get_row(self, i):
        res = []
        for j in range(self.grid[i].__len__):
            res.append(self.grid[i][j])
        return res
        
    def get_col(self, j):
        res = []
        for i in range(self.grid.__len__):
            res.append(self.grid[i][j])
        return res

    def get_region(self, reg_row, reg_col):
        """À COMPLÉTER!
        Cette méthode extrait les valeurs présentes dans une région donnée de la grille de Sudoku.
        *Variante avancée: Renvoyez un générateur sur les valeurs au lieu d'une liste*
        :param reg_row: Position verticale de la région à extraire, **entre 0 et 2**
        :param reg_col: Position horizontale de la région à extraire, **entre 0 et 2**
        :type reg_row: int
        :type reg_col: int
        :return: La liste des valeurs présentes à la colonne donnée
        :rtype: list of int
        """
        

    def get_empty_positions(self):
        res = []
        for i in range(self.grid.__len__):
            for j in range(self.grid[0].__len__):
                if self.grid[i][j] == 0:
                    res.append((i,j))
        return res

    def write(self, i, j, v, force=True):
        if i < 0 or i >= self.grid.__len__:
            raise ValueError()
        elif j < 0 or j >= self.grid[0].__len__:
            raise ValueError()
        elif v < 1 or v > 9:
            raise ValueError()

        if self.grid[i][j] != 0 or force:
            self.grid[i][j] = v

    def copy(self):
        new_instance = self.__new__(self.__class__)
        for i in range(self.grid.__len__):
            for j in range(self.grid[0].__len__):
                new_instance.grid[i][j] = self.grid[i][j]
        return new_instance
        
       