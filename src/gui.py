from tkinter import *

class SudokuGUI(Frame):
    
    grille = ""
    root = ""

    def __init__(self, grille):
        self.grille = grille
        self.initUI()
    
    def initUI(self):
        taille_rectanges = 50
        self.root = Tk(None, None, "Lines")
        self.root.geometry(str(self.root.winfo_screenwidth()) + "x" + str(self.root.winfo_screenheight()))

        canvas = Canvas(self.root)
        for i in range(len(self.grille.grid)):
            for j in range(len(self.grille.grid[0])):
                canvas.create_rectangle(100+j*taille_rectanges, 100+i*taille_rectanges, (100+j*taille_rectanges)+taille_rectanges, (100+i*taille_rectanges)+taille_rectanges)
                if self.grille.grid[i][j] == 0: continue
                label = Label(self.root, text=self.grille.grid[i][j])
                label.config(font=('Helvetica bold',20))
                label.place(x=100+taille_rectanges/2+j*taille_rectanges-10, y=100+taille_rectanges/2+i*taille_rectanges-15)
        canvas.create_line(100,100+3*taille_rectanges,100+9*taille_rectanges,100+3*taille_rectanges,width=2)
        canvas.create_line(100,100+6*taille_rectanges,100+9*taille_rectanges,100+6*taille_rectanges,width=2)
        canvas.create_line(100+3*taille_rectanges,100,100+3*taille_rectanges,100+9*taille_rectanges,width=2)
        canvas.create_line(100+6*taille_rectanges,100,100+6*taille_rectanges,100+9*taille_rectanges,width=2)
        canvas.pack(fill=BOTH, expand=1)
        
    def refresh(self):
        self.root.destroy()
        self.__init__(self.grille)