import sys
instance = ""
if len(sys.argv)>1: # si il y a bien deux arguments
    inputfile = sys.argv[1]
    inputline = sys.argv[2]
    try:
        a = open(inputfile,"r")
        instance = SudokuGrid(a.readline(inputline))
            for i in range(0,9):
                for j in range(0,9):
                    print(instance.grid[i][j]) #affichage de l'etat actuel de la grille
    except:
        print("Impossible de lire le fichier")
else:
    input("Veuillez saisir manuellement une grille : ")


    position = int(input("Position de la valeur à ecrire"))
    valeur = int(input("Valeur à écrire : "))
    try:
        #verification de la validité de la saisie
    except: 
        print("Veuillez rentrer une saisie valide !")