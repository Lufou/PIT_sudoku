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
        """À COMPLÉTER
        Cette méthode devrait être appelée à chaque mise à jour de la grille,
        et élimine la dernière valeur affectée à une case
        pour toutes les autres cases concernées par cette mise à jour (même ligne, même colonne ou même région).
        :param last_i: Numéro de ligne de la dernière case modifiée, entre 0 et 8
        :param last_j: Numéro de colonne de la dernière case modifiée, entre 0 et 8
        :param last_v: Valeur affecté à la dernière case modifiée, entre 1 et 9
        :type last_i: int
        :type last_j: int
        :type last_v: int
        """
        

    def commit_one_var(self):
        empty = []
        empty.extend(self.sudoku_grid.get_empty_positions())

        for case_vide in empty:
            if len(self.possibles_val[case_vide]) != 1: continue
            self.sudoku_grid.write(self.possibles_val[case_vide])
            return (case_vide[0],case_vide[1],self.possibles_val[case_vide])

        return None

    def solve_step(self):
        """À COMPLÉTER
        Cette méthode alterne entre l'affectation de case pour lesquelles il n'y a plus qu'une possibilité
        et l'élimination des nouvelles valeurs impossibles pour les autres cases concernées.
        Elle répète cette alternance tant qu'il reste des cases à remplir,
        et correspond à la résolution de Sudokus dits «simple».
        *Variante avancée: en plus de vérifier s'il ne reste plus qu'une seule possibilité pour une case,
        il est aussi possible de vérifier s'il ne reste plus qu'une seule position valide pour une certaine valeur
        sur chaque ligne, chaque colonne et dans chaque région*
        """
        

        raise NotImplementedError()

    def is_valid(self):
        """À COMPLÉTER
        Cette méthode vérifie qu'il reste des possibilités pour chaque case vide
        dans la solution partielle actuelle.
        :return: Un booléen indiquant si la solution partielle actuelle peut encore mener à une solution valide
        :rtype: bool
        """
        raise NotImplementedError()

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
        """
        Cette méthode implémente la fonction principale de la programmation par contrainte.
        Elle cherche d'abord à affiner au mieux la solution partielle actuelle par un appel à ``solve_step``.
        Si la solution est complète, elle la retourne.
        Si elle est invalide, elle renvoie ``None`` pour indiquer un cul-de-sac dans la recherche de solution
        et déclencher un retour vers la précédente solution valide.
        Sinon, elle crée plusieurs sous-problèmes pour explorer différentes possibilités
        en appelant récursivement ``solve`` sur ces sous-problèmes.
        :return: Une solution pour la grille de Sudoku donnée à l'initialisation du solver
        (ou None si pas de solution)
        :rtype: SudokuGrid or None
        """
        raise NotImplementedError()
