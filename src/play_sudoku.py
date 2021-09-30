import sys
from grid import SudokuGrid

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
        print("-------------------")
        line = "|"
        for j in range(0,9):
            line += (str(instance.grid[i][j]) + "|")
        print(line)
    print("--------------------")

    position = input("Position de la valeur à ecrire sous la forme 0,0 : ")
    sep = position.split(",")
    while not sep[0].isnumeric() or not sep[1].isnumeric() or int(sep[0]) < 0 or int(sep[0]) >= 9 or int(sep[1]) < 0 or int(sep[1]) >= 9:
        position = input("Position de la valeur à ecrire sous la forme 0,0 : ")
        sep = position.split(",")

    valeur = input("Valeur à écrire (de 1 à 9) : ")
    while not valeur.isnumeric() or int(valeur) <= 0 or int(valeur) > 9 or instance.get_row(int(sep[0])).__contains__(int(valeur)) or instance.get_col(int(sep[1])).__contains__(int(valeur)) or instance.get_region(int(sep[0]),int(sep[1])).__contains__(int(valeur)):
        valeur = input("Vous n'êtes pas autorisé à mettre cette valeur, entrez une nouvelle valeur (de 1 à 9) : ")

    instance.write(int(sep[0]),int(sep[1]),int(valeur))