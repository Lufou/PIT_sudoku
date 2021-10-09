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
            for i in range(1, 10):
                if not i in self.sudoku_grid.get_row(x[0]) and not i in self.sudoku_grid.get_col(x[1]) and not i in self.sudoku_grid.get_region(x[0]//3, x[1]//3):
                    self.possibles_val[(x[0], x[1])].append(i)
                    
    def reduce_domains(self, last_i, last_j, last_v):
        for i in range(9):
            if (last_i,i) in self.possibles_val:
                if last_v in self.possibles_val[(last_i,i)]:
                    self.possibles_val[(last_i,i)].remove(last_v)

            if (i,last_j) in self.possibles_val:
                if last_v in self.possibles_val[(i,last_j)]:
                    self.possibles_val[(i,last_j)].remove(last_v)
                    
            if (3*(last_i//3) + (i%3), 3*(last_j//3) + (i//3)) in self.possibles_val:
                if last_v in self.possibles_val[(3*(last_i//3) + (i%3), 3*(last_j//3) + (i//3))]:
                    self.possibles_val[(3*(last_i//3) + (i%3), 3*(last_j//3) + (i//3))].remove(last_v)

    def commit_one_var(self):
        for (i,j) in self.sudoku_grid.get_empty_positions():
            if len(self.possibles_val[(i,j)]) != 1: continue
            self.sudoku_grid.write(i, j, self.possibles_val[(i,j)][0])
            return (i,j,self.possibles_val[(i,j)][0])

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
            else:
                return False

    def is_solved(self):
        if len(self.sudoku_grid.get_empty_positions()) == 0 :
            return True
        else :
            return False

    def branch(self):
        branches = []
        first_empty_case = self.sudoku_grid.get_empty_positions()[0]
        for x in self.possibles_val[first_empty_case]:
            grid_copy = self.sudoku_grid.copy()
            grid_copy.write(first_empty_case[0], first_empty_case[1], x)
            temp_solver = self.__class__(grid_copy)
            branches.append(temp_solver)
        return branches

    def solve(self):
        self.solve_step()
        if self.is_solved():
            return self.sudoku_grid
        elif self.is_valid():
            for solver in self.branch():
                res = solver.solve()
                if res is not None:
                    return res
        return None