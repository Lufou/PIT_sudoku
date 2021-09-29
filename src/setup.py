from cx_Freeze import setup, Executable
base = None
#Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("play_sudoku.py", base=base)]
#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "play_sudoku.py",
    options = options,
    version = "1.0",
    description = 'Programme permettant d\' exécuter play_sudoku.py',
    executables = executables
)