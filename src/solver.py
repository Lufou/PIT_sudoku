#-*-coding: utf8-*-

class SudokuSolver:
    
    grid = [[0] * 9 for i in range(9)]

    def __init__(self, grid):
        self.grid = grid
        print(self.grid)
        #self.reduce_all_domains()
        
        """À COMPLÉTER
        Ce constructeur initialise une nouvelle instance de solver à partir d'une grille initiale.
        Il construit les ensembles de valeurs possibles pour chaque case vide de la grille,
        en respectant les contraintes définissant un Sudoku valide.
        Ces contraintes seront appliquées en appelant la méthode ``reduce_all_domains``.
        :param grid: Une grille de Sudoku
        :type grid: SudokuGrid
        """
        #raise NotImplementedError()

    def reduce_all_domains(self):
        """À COMPLÉTER
        Cette méthode devrait être appelée à l'initialisation
        et élimine toutes les valeurs impossibles pour chaque case vide.
        *Indication: Vous pouvez utiliser les fonction ``get_row``, ``get_col`` et ``get_region`` de la grille*
        """


        raise NotImplementedError()

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
        raise NotImplementedError()

    def commit_one_var(self):
        """À COMPLÉTER
        Cette méthode cherche une case pour laquelle il n'y a plus qu'une seule possibilité.
        Si elle en trouve une, elle écrit cette unique valeur possible dans la grille
        et renvoie la position de la case et la valeur inscrite.
        :return: Le numéro de ligne, de colonne et la valeur inscrite dans la case
        ou ``None`` si aucune case n'a pu être remplie.
        :rtype: tuple of int or None
        """
        res = [] 
        empty = []
        empty.extend(self.grid.get_empty_positions()) #récupère les positions des cases vides et les stocke dans la liste "empty"
        #les 3 listes suivantes sont destinées à contenir la colone, ligne et région qui possède la case vide
        row = []
        col = []
        reg = []
        if len(empty) == 0 : #si il n'y a plus de cases vides
            res.append("None")
        else :
            row.extend(self.grid.get_row(empty[0][0]))#récupère les lignes de la première case vide fournie par get_empty_positions()
            col.extend(self.grid.get_col(empty[0][1]))#récupère les colonnes de la première case vide fournie par get_empty_positions()
            reg.extend(self.grid.get_region(empty[0][0]//3,empty[0][1]//3))
            print(row, "|",col, "|", reg)
            res.append(empty[0][0]) 
            res.append(empty[0][1]) 
            c1 = sum(row)
            c2 = sum(col)
            c3 = sum(reg)
             #36 est la somme minimale d'une ligne/colonne/région pour laquelle on ait qu'une seule possibilité de valeur
            if row.count(0) == 1 :
                res.append(45 - c1)
            elif col.count(0) == 1 :
                res.append(45 - c2)

            elif reg.count(0) == 1 :
                res.append(45 - c3)
            else :
                res.clear()
                res.append("None")
        return res     

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
        if len(self.grid.get_empty_positions()) == 0 :
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
