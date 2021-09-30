#-*-coding: utf8-*-
from grid import SudokuGrid

class SudokuSolver:
    
    sudoku_grid = ""
    possibles_val = {}

    def __init__(self, sudoku_grid):
        self.sudoku_grid = sudoku_grid
        self.reduce_all_domains()

    def reduce_all_domains(self):
        for x in self.sudoku_grid.get_empty_positions():
            self.possibles_val[(x[0], x[1])] = []
            print((x[0],x[1]))
            for i in range(10):
                if not self.sudoku_grid.get_row(x[0]).__contains__(i) and not self.sudoku_grid.get_col(x[1]).__contains__(i) and not self.sudoku_grid.get_region(x[0], x[1]).__contains__(i):
                    self.possibles_val[(x[0], x[1])].append(i)
                    
    def reduce_domains(self, last_i, last_j, last_v):
        # same line
        for j in range(len(self.sudoku_grid.grid[0])):
            if j == last_j: continue
            case = (last_i,j)
            if self.possibles_val[case].__contains__(last_v):
                self.possibles_val[case].remove(last_v)
        # same col
        for i in range(len(self.sudoku_grid.grid)):
            if i == last_i: continue
            case = (i,last_j)
            if self.possibles_val[case].__contains__(last_v):
                self.possibles_val[case].remove(last_v)
        # same region
        for i in range((last_i//3)*3,(last_i//3)*3+3):
            for j in range((last_j//3)*3,(last_j//3)*3+3):
                case = (i,j)
                if case == (last_i, last_j): continue
                if self.possibles_val[case].__contains__(last_v):
                    self.possibles_val[case].remove(last_v)

    def commit_one_var(self):
        empty = []
        empty.extend(self.sudoku_grid.get_empty_positions())

        for (i,j) in empty:
            if len(self.possibles_val[(i,j)]) != 1: continue
            self.sudoku_grid.write(self.possibles_val[(i,j)])
            return (i,j,self.possibles_val[(i,j)])

        return None

    def solve_step(self):
        while len(self.sudoku_grid.get_empty_positions()) > 0:
            res = self.commit_one_var()
            if res != None:
                (i, j, v) = res
                self.reduce_domains(i, j, v)
            else:
                break

    def is_valid(self):
        for (i,j) in self.sudoku_grid.get_empty_positions():
            if len(self.possibles_val[(i,j)]) > 0:
                return True
        return False

    def is_solved(self):
        if len(self.sudoku_grid.get_empty_positions()) == 0 :
            return True
        else :
            return False

    def branch(self):
        """À COMPLÉTER
        Cette méthode sélectionne une variable libre dans la solution partielle actuelle,
        et crée autant de sous-problèmes que d'affectation possible pour cette variable.
        Ces sous-problèmes seront sous la forme de nouvelles instances de solver
        initialisées avec une grille partiellement remplie.
        *Variante avancée: Renvoyez un générateur au lieu d'une liste.*
        *Variante avancée: Un choix judicieux de variable libre,
        ainsi que l'ordre dans lequel les affectations sont testées
        peut fortement améliorer les performances de votre solver.*
        :return: Une liste de sous-problèmes ayant chacun une valeur différente pour la variable choisie
        :rtype: list of SudokuSolver
        """
        raise NotImplementedError()

    def solve(self):
        for solver in self.branch():
            solver.solve_step()
            if solver.is_solved():
                return solver.grid
            else:
                s = solver.solve()
                if s != None:
                    return s
        return None
