import characters
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class displayChar:
    def __init__(self, dbMF, position):
        self.name = characters.charList[position-1]
        self.bHP = characters.char.get(self.name)[0]
        self.ATK = characters.char.get(self.name)[1]
        self.MP = characters.char.get(self.name)[2]
        self.BACost = 3
        self.Ab1Cost = characters.char.get(self.name)[3]
        self.Ab2Cost = characters.char.get(self.name)[4]
        self.Ab1Name = characters.char.get(self.name)[5]
        self.Ab2Name = characters.char.get(self.name)[6]
        self.basicDesc = characters.char.get(self.name)[7]
        self.Ab1Desc = characters.char.get(self.name)[8]
        self.Ab2Desc = characters.char.get(self.name)[9]

        self.frame = tk.Frame(dbMF, bg='#a7c4a9')
        self.n = ttk.Notebook(self.frame, width=180, height=220)
        self.n.grid(row=0, column=0, sticky='nswe')

        self.t1 = tk.Frame(self.n, bg='#a7c4a9')
        self.n.add(self.t1, text='Base stats')
        self.t1.rowconfigure((0, 1), weight=1, uniform='b')
        self.t1.rowconfigure(3, weight=5, uniform='b')
        self.t1.columnconfigure(0, weight=1, uniform='b')

        self.line1 = ttk.Label(self.t1, text='   ' + self.name + '\t\t  HP: ' + str(self.bHP), style='CharLabel.TLabel')
        self.line1.grid(row=0, sticky='w', ipadx=25, ipady=5)
        self.line2 = ttk.Label(self.t1, text='   ATK: ' + str(self.ATK) + '\t\t  MP: ' + str(self.MP), style='CharLabel.TLabel')
        self.line2.grid(row=1, sticky='w', ipadx=25, ipady=5)

        self.charImgOriginal = Image.open('alaya.png').resize((100, 100))
        self.charImage = ImageTk.PhotoImage(self.charImgOriginal)
        self.pic = ttk.Label(self.t1, image=self.charImage)
        self.pic.grid(row=3, sticky='nswe', ipadx=5, ipady=5)

        self.t2 = tk.Frame(self.n, bg='#a7c4a9')
        self.n.add(self.t2, text='Abilities')
        self.t2.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='b')
        self.t2.columnconfigure(0, uniform='b')

        self.skillBAName = ttk.Label(self.t2, style='CharLabel.TLabel', text='Basic Attack (' + str(self.BACost) + ')')
        self.skillBAName.grid(row=0, sticky='sw', ipady=5)
        self.skillBADesc = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.basicDesc)
        self.skillBADesc.grid(row=1, sticky='nw', ipady=5)
        self.skillAB1Name = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.Ab1Name + ' (' + str(self.Ab1Cost) + ')')
        self.skillAB1Name.grid(row=2, sticky='sw', ipady=5)
        self.skillAB1Desc = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.Ab1Desc)
        self.skillAB1Desc.grid(row=3, sticky='nw', ipady=5)
        self.skillAB2Name = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.Ab2Name + ' (' + str(self.Ab2Cost) + ')')
        self.skillAB2Name.grid(row=4, sticky='sw', ipady=5)
        self.skillAB2Desc = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.Ab2Desc)
        self.skillAB2Desc.grid(row=5, sticky='nw', ipady=5)

        if position < 6:
            self.frame.grid(row=0, column=position, padx=20, pady=20, sticky='n')
        else:
            self.frame.grid(row=1, column=position-5, padx=20, pady=20, sticky='n')