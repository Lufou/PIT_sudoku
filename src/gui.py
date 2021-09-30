from tkinter import *

class SudokuGUI(Frame):
    
    grille = ""
    root = ""

    def __init__(self, grille):
        self.grille = grille
        self.initUI()
    
    def initUI(self):
        taille_rectanges = 50
        window_width = taille_rectanges*len(self.grille.grid) + 20
        window_height = taille_rectanges*(len(self.grille.grid[0])) + 20
        self.root = Tk(None, None, "Lines")
        self.root.geometry(str(window_width) + "x" + str(window_height) + "+" + str(self.root.winfo_screenwidth()//2-window_width//2) + "+" + str(self.root.winfo_screenheight()//2-window_height//2))

        canvas = Canvas(self.root)
        for i in range(len(self.grille.grid)):
            for j in range(len(self.grille.grid[0])):
                canvas.create_rectangle(10+j*taille_rectanges, 10+i*taille_rectanges, (10+j*taille_rectanges)+taille_rectanges, (10+i*taille_rectanges)+taille_rectanges)
                if self.grille.grid[i][j] == 0: continue
                label = Label(self.root, text=self.grille.grid[i][j])
                label.config(font=('Helvetica bold',20))
                label.place(x=10+taille_rectanges/2+j*taille_rectanges-10, y=10+taille_rectanges/2+i*taille_rectanges-15)
        canvas.create_line(10,10+3*taille_rectanges,10+9*taille_rectanges,10+3*taille_rectanges,width=2)
        canvas.create_line(10,10+6*taille_rectanges,10+9*taille_rectanges,10+6*taille_rectanges,width=2)
        canvas.create_line(10+3*taille_rectanges,10,10+3*taille_rectanges,10+9*taille_rectanges,width=2)
        canvas.create_line(10+6*taille_rectanges,10,10+6*taille_rectanges,10+9*taille_rectanges,width=2)
        canvas.pack(fill=BOTH, expand=1)
        
    def refresh(self):
        self.root.destroy()
        self.__init__(self.grille)