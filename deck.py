import deckCards
import tkinter as tk
from tkinter import ttk

class Equipable:
    def __init__(self, card):
        self.name = card
        self.cost = deckCards.equipable.get(card)[0]
        self.type = deckCards.equipable.get(card)[1]
        self.value = deckCards.equipable.get(card)[2]
        self.desc = deckCards.equipable.get(card)[3]

    def displayCard(self, frame, row, col):
        self.frame = tk.Frame(frame, bg='#a7c4a9')
        self.frame.rowconfigure((0, 2), weight=1, uniform='c')
        self.frame.rowconfigure(1, weight=3, uniform='c')
        self.frame.columnconfigure(0, weight=3, uniform='c')
        self.frame.columnconfigure(1, weight=1, uniform='c')
        self.frame.grid(row=row, column=col, sticky='nswe', padx=20, pady=20)
        self.costLabel = ttk.Label(self.frame, text='Cost: ' + str(self.cost), background='#c5e3c7')
        self.costLabel.grid(row=2, column=1, sticky='swe')
        self.descLabel = ttk.Label(self.frame, text=self.desc, wraplength=200, justify='left', background='#a7c4a9')
        self.descLabel.grid(row=1, column=0, sticky='nwe', pady=20, padx=20)

    def removeCard(self):
        self.frame.grid_remove()

    def addName(self):
        self.nameLabel = ttk.Label(self.frame, text=self.name, background='#a7c4a9')
        self.nameLabel.grid(row=0, column=0, columnspan=2, sticky='nswe')

    def addButton(self):
        self.nameButton = tk.Button(self.frame, text=self.name, background='#a7c4a9', state='disabled')
        self.nameButton.grid(row=0, column=0, columnspan=2, sticky='nw', ipadx=5, ipady=5)

class SuppCard:
    def __init__(self, card):
        self.name = card
        self.cost = deckCards.supp.get(self.name)[0]
        self.desc = deckCards.supp.get(self.name)[1]
        self.rounds = deckCards.supp.get(self.name)[2]

    def displayCard(self, frame, row, col):
        self.frame = tk.Frame(frame, bg='#a7c4a9')
        self.frame.rowconfigure((0, 2), weight=1, uniform='c')
        self.frame.rowconfigure(1, weight=3, uniform='c')
        self.frame.columnconfigure(0, weight=3, uniform='c')
        self.frame.columnconfigure(1, weight=1, uniform='c')
        self.frame.grid(row=row, column=col, sticky='nswe', padx=20, pady=20)
        self.costLabel = ttk.Label(self.frame, text='Cost: ' + str(self.cost), background='#c5e3c7')
        self.costLabel.grid(row=2, column=1, sticky='swe')
        self.descLabel = ttk.Label(self.frame, text=self.desc, wraplength=200, justify='left', background='#a7c4a9')
        self.descLabel.grid(row=1, column=0, sticky='nwe', pady=20, padx=20)

    def removeCard(self):
        self.frame.grid_remove()

    def addName(self):
        self.nameLabel = ttk.Label(self.frame, text=self.name, background='#a7c4a9')
        self.nameLabel.grid(row=0, column=0, columnspan=2, sticky='nswe')

    def addButton(self):
        self.nameButton = tk.Button(self.frame, text=self.name, background='#a7c4a9', state='disabled')
        self.nameButton.grid(row=0, column=0, columnspan=2, sticky='nw', ipadx=5, ipady=5)

class OneUse:
    def __init__(self, card):
        self.name = card
        self.cost = deckCards.oneUse.get(self.name)[0]
        self.desc = deckCards.oneUse.get(self.name)[1]

    def displayCard(self, frame, row, col):
        self.frame = tk.Frame(frame, bg='#a7c4a9')
        self.frame.rowconfigure((0, 2), weight=1, uniform='c')
        self.frame.rowconfigure(1, weight=3, uniform='c')
        self.frame.columnconfigure(0, weight=3, uniform='c')
        self.frame.columnconfigure(1, weight=1, uniform='c')
        self.frame.grid(row=row, column=col, sticky='nswe', padx=20, pady=20)
        self.costLabel = ttk.Label(self.frame, text='Cost: ' + str(self.cost), background='#c5e3c7')
        self.costLabel.grid(row=2, column=1, sticky='swe')
        self.descLabel = ttk.Label(self.frame, text=self.desc, wraplength=200, justify='left', background='#a7c4a9')
        self.descLabel.grid(row=1, column=0, sticky='nwe', pady=20, padx=20)

    def removeCard(self):
        self.frame.grid_remove()

    def addName(self):
        self.nameLabel = ttk.Label(self.frame, text=self.name, background='#a7c4a9')
        self.nameLabel.grid(row=0, column=0, columnspan=2, sticky='nswe')

    def addButton(self):
        self.nameButton = tk.Button(self.frame, text=self.name, background='#a7c4a9', state='disabled')
        self.nameButton.grid(row=0, column=0, columnspan=2, sticky='nw', ipadx=5, ipady=5)