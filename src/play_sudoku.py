import sys
instance = ""
if len(sys.argv)>1: # si il y a bien deux arguments
    inputfile = sys.argv[1]
    inputline = sys.argv[2]
    try:
        a = open(inputfile,"r")
        instance = SudokuGrid(a.readline(inputline))
            
    except:
        print("Impossible de lire le fichier")
else:
    grille = input("Veuillez saisir manuellement une grille : ")
    instance = SudokuGrid(grille)

while len(instance.get_empty_positions())!=0:
    for i in range(0,9):    
        for j in range(0,9):
            print(instance.grid[i][j]) #affichage de l'etat actuel de la grille
            position = tuple(input("Position de la valeur à ecrire"))
            valeur = int(input("Valeur à écrire : "))
            while position>=0 and position<80 and valeur>=0 and valeur<9:
            instance.write()