import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import characters
import deck

class Character:
    def __init__(self, nume, own, pos, mainframe):
        #stats and effects
        self.name = nume
        self.owner = own
        self.lineUp = pos
        self.bHP = characters.char.get(nume)[0]
        self.ATK = characters.char.get(nume)[1]
        self.MP = characters.char.get(nume)[2]
        self.cHP = self.bHP
        self.physRes = 0
        self.magicRes = 0
        self.shieldEff = 0
        self.nilsaProtecc = False
        self.BACost = 3
        self.Ab1Cost = characters.char.get(nume)[3]
        self.Ab2Cost = characters.char.get(nume)[4]
        self.Ab1Name = characters.char.get(nume)[5]
        self.Ab2Name = characters.char.get(nume)[6]
        self.basicDesc = characters.char.get(nume)[7]
        self.Ab1Desc = characters.char.get(nume)[8]
        self.Ab2Desc = characters.char.get(nume)[9]
        self.shield = None
        self.antim = None
        self.wep = None
        self.alive = True
        self.determination = False
        self.expertise = False
        self.EORAdjustments = []

        # frame
        self.frame = tk.Frame(mainframe)
        self.frame.grid(row=self.owner, column=self.lineUp)
        self.mainframe = mainframe

        # tabs
        self.n = ttk.Notebook(self.frame, width=180, height=220)

        self.t1 = tk.Frame(self.n, bg='#a7c4a9')
        self.n.add(self.t1, text='Character Info')
        self.t1.rowconfigure((0, 1, 2), weight=1, uniform='b')
        self.t1.rowconfigure(3, weight=5, uniform='b')
        self.t1.columnconfigure((0, 1), weight=1, uniform='b')

        self.t2 = tk.Frame(self.n, bg='#a7c4a9')
        self.n.add(self.t2, text='Abilities')
        self.t2.rowconfigure((0, 2, 4), weight=1, uniform='b')
        self.t2.rowconfigure((1, 3, 5), weight=2, uniform='b')
        self.t2.columnconfigure(0, uniform='b')

        self.t3 = tk.Frame(self.n, bg='#a7c4a9')
        self.n.add(self.t3, text='Equipment')
        self.t3.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='b')
        self.t3.columnconfigure(0, uniform='b')

        """Skill Info"""

        self.skillBAName = ttk.Label(self.t2, style='CharLabel.TLabel', text='Basic Attack (' + str(self.BACost) + ')',
                                     wraplength=200, justify='left')
        self.skillBAName.grid(row=0, sticky='nw', ipady=5)
        self.skillBADesc = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.basicDesc, wraplength=200,
                                     justify='left')
        self.skillBADesc.grid(row=1, sticky='nw', ipady=5)
        self.skillAB1Name = ttk.Label(self.t2, style='CharLabel.TLabel',
                                      text=self.Ab1Name + ' (' + str(self.Ab1Cost) + ')', wraplength=200,
                                      justify='left')
        self.skillAB1Name.grid(row=2, sticky='nw', ipady=5)
        self.skillAB1Desc = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.Ab1Desc, wraplength=200,
                                      justify='left')
        self.skillAB1Desc.grid(row=3, sticky='nw', ipady=5)
        self.skillAB2Name = ttk.Label(self.t2, style='CharLabel.TLabel',
                                      text=self.Ab2Name + ' (' + str(self.Ab2Cost) + ')', wraplength=200,
                                      justify='left')
        self.skillAB2Name.grid(row=4, sticky='nw', ipady=5)
        self.skillAB2Desc = ttk.Label(self.t2, style='CharLabel.TLabel', text=self.Ab2Desc, wraplength=200,
                                      justify='left')
        self.skillAB2Desc.grid(row=5, sticky='nw', ipady=5)

        self.n.grid(row=0, column=0, sticky='nswe')

        """Char info"""
        self.hpLabel = ttk.Label(self.t1, text='  HP: ' + str(self.cHP), style='CharLabel.TLabel')
        self.hpLabel.grid(row=0, column=1, sticky='w', ipadx=25, ipady=5)

        self.atkLabel = ttk.Label(self.t1, text='   ATK: ' + str(self.ATK), style='CharLabel.TLabel')
        self.atkLabel.grid(row=1, column=0, ipadx=25, ipady=5, sticky='w')
        self.mpLabel = ttk.Label(self.t1, text='  MP: ' + str(self.MP), style='CharLabel.TLabel')
        self.mpLabel.grid(row=1, column=1, ipadx=25, ipady=5, sticky='w')

        self.pResLabel = ttk.Label(self.t1, text='   Phys Res: ' + str(self.physRes), style='CharLabel.TLabel')
        self.pResLabel.grid(row=2, column=0, ipadx=25, ipady=5, sticky='w')
        self.mResLabel = ttk.Label(self.t1, text='  Magic Res: ' + str(self.magicRes), style='CharLabel.TLabel')
        self.mResLabel.grid(row=2, column=1, ipadx=25, ipady=5, sticky='w')

        self.shieldLabel = ttk.Label(self.t1, text='  Shield:\n  ' + str(self.shieldEff) + ' HP',
                                     style='CharLabel.TLabel')
        self.shieldLabel.grid(row=3, column=1, ipadx=25, ipady=5, sticky='nw')

        self.nilsaLabel = ttk.Label(self.t1, text='', style='CharLabel.TLabel')
        self.nilsaLabel.grid(row=3, column=1, ipadx=25, ipady=5, sticky='sw')

        match self.name:
            case 'Alaya':
                self.charImgOriginal = Image.open('alaya.png').resize((100, 100))
            case 'Balom':
                self.charImgOriginal = Image.open('balom.png').resize((100, 100))
            case 'Moss':
                self.charImgOriginal = Image.open('moss.png').resize((100, 100))
            case 'Nilsa':
                self.charImgOriginal = Image.open('nilsa.png').resize((100, 100))
            case 'Kiave':
                self.charImgOriginal = Image.open('kiave.png').resize((100, 100))
            case 'Souset':
                self.charImgOriginal = Image.open('souset.png').resize((100, 100))
            case 'Phael':
                self.charImgOriginal = Image.open('phael.png').resize((100, 100))
            case _:
                self.charImgOriginal = Image.open('alaya.png').resize((100, 100))
        self.charImage = ImageTk.PhotoImage(self.charImgOriginal)
        self.pic = ttk.Label(self.t1, image=self.charImage)
        self.pic.grid(row=3, column=0, sticky='nswe', ipadx=5, ipady=5)

        """Equipment"""
        # Weapon
        self.eqWepName = ttk.Label(self.t3, style='CharLabel.TLabel', wraplength=180, justify='left')
        self.eqWepName.grid(row=0, sticky='nw', ipady=5)
        self.eqWepDesc = ttk.Label(self.t3, style='CharLabel.TLabel', wraplength=180, justify='left')
        self.eqWepDesc.grid(row=1, sticky='nw', ipady=5)

        # Shield
        self.eqShieldName = ttk.Label(self.t3, style='CharLabel.TLabel', wraplength=180, justify='left')
        self.eqShieldDesc = ttk.Label(self.t3, style='CharLabel.TLabel', wraplength=180, justify='left')
        self.eqShieldName.grid(row=2, sticky='nw', ipady=5)
        self.eqShieldDesc.grid(row=3, sticky='nw', ipady=5)

        # Anti-Magic
        self.eqAntimName = ttk.Label(self.t3, style='CharLabel.TLabel', wraplength=180, justify='left')
        self.eqAntimName.grid(row=4, sticky='nw', ipady=5)
        self.eqAntimDesc = ttk.Label(self.t3, style='CharLabel.TLabel', wraplength=180, justify='left')
        self.eqAntimDesc.grid(row=5, sticky='nw', ipady=5)

        self.refresh()


    def refresh(self):
        """Char Info"""
        self.hpLabel.configure(text='   HP: ' + str(self.cHP))
        self.atkLabel.configure(text='   ATK: ' + str(self.ATK))
        self.mpLabel.configure(text='  MP: ' + str(self.MP))
        self.pResLabel.configure(text='   Phys Res: ' + str(self.physRes))
        self.mResLabel.configure(text='  Magic Res: ' + str(self.magicRes))
        self.shieldLabel.configure(text='  Shield:\n  ' + str(self.shieldEff) + ' HP')
        if self.nilsaProtecc:
            self.nilsaLabel.configure(text='Protected\nby Nilsa')
        else:
            self.nilsaLabel.configure(text=' ')

        """Abilities"""
        self.skillBAName.configure(text='Basic attack (' + str(self.BACost) + ')')
        self.skillAB1Name.configure(text=self.Ab1Name + ' (' + str(self.Ab1Cost) + ')')
        self.skillAB2Name.configure(text=self.Ab2Name + ' (' + str(self.Ab2Cost) + ')')

        """Equipment"""
        if self.wep:
            self.eqWepName.configure(text='   ' + self.wep.name)
            self.eqWepDesc.configure(text='   ' + self.wep.desc)
        else:
            self.eqWepName.configure(text='   No weapon equipped')
            self.eqWepDesc.configure(text='   ')

        if self.shield:
            self.eqShieldName.configure(text='   ' + self.shield.name)
            self.eqShieldDesc.configure(text='   ' + self.shield.desc)
        else:
            self.eqShieldName.configure(text='   No shield equipped')
            self.eqWepDesc.configure(text='   ')

        if self.antim:
            self.eqAntimName.configure(text='   ' + self.antim.name)
            self.eqAntimDesc.configure(text='   ' + self.antim.desc)
        else:
            self.eqAntimName.configure(text='   No anti-magic equipped')
            self.eqAntimDesc.configure(text='   ')


    def takeDamage(self, type, value):
        postMit=value
        if self.determination:
            postMit = int(postMit*80/100)
        if self.nilsaProtecc:
            postMit = int(postMit*60/100)
            self.nilsaProtecc = False
        if postMit<self.shieldEff: self.shieldEff -= postMit
        else:
            self.shieldEff = 0
            if type=='m': postMit -= self.magicRes
            else: postMit -= self.physRes
            self.cHP -= postMit
        if self.cHP <=0: self.death()
        self.cHP = int(self.cHP)
        self.refresh()

    def gainShield(self, value):
        self.shieldEff += value

    def heal(self, value):
        if self.cHP+value >= self.bHP: self.cHP=self.bHP
        else: self.cHP += value

    def death(self):
        self.alive = False

    def equip(self, cardName):
        print(self.name, ' equipped ', end='')
        card = deck.Equipable(cardName)
        print(card.type)
        if card.type == 'shield':
            if self.shield:
                self.physRes -= self.shield.value
            self.shield = card
            self.physRes += self.shield.value
        elif card.type == 'antim':
            if self.antim:
                self.magicRes -= self.antim.value
            self.antim = card
            self.magicRes += self.antim.value
        elif card.type == 'wep':
            if self.wep:
                if self.wep.name == 'Simple grimoire' or self.wep.name == 'Advanced grimoire':
                    self.MP -= self.wep.value
                else: self.ATK -= self.wep.value
            self.wep = card
            if self.wep.name == 'Simple grimoire' or self.wep.name == 'Advanced grimoire':
                self.MP += self.wep.value
            else: self.ATK += self.wep.value
        self.refresh()

    def endOfRoundAdjustment(self):
        for i in self.EORAdjustments:
            match i[0]:
                case 'balom':
                    print(3)
                    self.MP -= i[1]
                case 'teollo':
                    self.ATK += i[1]; self.MP += i[1]
                case 'det':
                    self.determination = False
                case 'exp':
                    self.expertise = False
                case 'insp':
                    self.BACost += 1
                    self.Ab1Cost += 1
                    self.Ab2Cost += 1
        self.EORAdjustments = []
        self.refresh()

    #Abilities
    def Basic(self, enemy):
        match self.name:
            case 'Balom':
                value = self.MP
                if self.expertise: value = value * 120 / 100
                enemy.takeDamage('m', int(value))
            case 'Souset':
                value = 0.5*self.MP
                if self.expertise: value = value * 120 / 100
                enemy.takeDamage('m', int(value))
            case _:
                value = self.ATK
                if self.expertise: value = value * 120 / 100
                enemy.takeDamage('p', int(value))

    def Ab1(self, target=None):
        match self.name:
            case 'Alaya':
                value = 2*self.MP
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('m', int(value))
            case 'Balom':
                adjValue = self.MP
                self.MP += self.MP
                self.EORAdjustments.append(tuple({'balom', adjValue}))
                self.refresh()
            case 'Moss':
                value = int(self.cHP*0.25 + self.MP*2)
                target.gainShield(value)
            case 'Nilsa':
                for i in target:
                    if i.alive:
                        i.nilsaProtecc=True
            case 'Kiave':
                value = 2*self.ATK + 1*self.MP
                if self.expertise: value = value * 120 / 100
                target.takeDamage('p', int(value))
            case 'Souset':
                for i in target:
                    i.shielfEff = 0
            case 'Teollo':
                value = self.ATK
                if self.expertise: value = value * 120 / 100
                target.takeDamage('p', int(value))
                adjValue = int(0.5*self.MP)
                target.ATK -= adjValue; target.MP -= adjValue
                target.EORAdjustments.append(tuple({'teollo', adjValue}))
                target.refresh()
            case 'Phael':
                value = self.ATK+self.MP
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
            case 'Cirai':
                value = 2*self.ATK
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
            case 'Egwan':
                value = self.ATK
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
                self.heal(2*self.MP)
                self.refresh()

    def Ab2(self, target=None, sousetExtra=None):
        match self.name:
            case 'Alaya':
                value = 3*self.MP
                if self.expertise: value = value * 120 / 100
                target.takeDamage('m', int(value))
            case 'Balom':
                adjValue = 3*self.MP
                self.MP += adjValue
                self.EORAdjustments.append(tuple({'balom', adjValue}))
                self.refresh()
            case 'Moss':
                value = int(self.cHP*0.2 + self.MP*2)
                for i in target:
                    if i.alive:
                        i.gainShield(value)
            case 'Nilsa':
                value = int(0.2*self.cHP + 3*self.MP)
                target.heal(value)
            case 'Kiave':
                value = 3*self.ATK + 2*self.MP
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
            case 'Souset':
                value = 0
                for i in target:
                    if i.alive:
                        indValue = int(0.25*i.cHP)
                        i.takeDamage('m', indValue)
                        value += indValue
                value *= 0.25*self.MP
                if self.expertise: value = value * 120 / 100
                split = 0
                for i in sousetExtra:
                    if i.alive:
                        split += 1
                value = int(value/split)
                for i in sousetExtra:
                    if i.alive:
                        i.takeDamage('m', value)
            case 'Teollo':
                value = 2*self.ATK
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
                        adjValue = int(0.5*self.MP)
                        i.ATK -= adjValue; i.MP -= adjValue
                        i.EORAdjustments.append(tuple({'teollo', adjValue}))
            case 'Phael':
                value = 2*self.ATK+2*self.MP
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
            case 'Cirai':
                value = 0.2*self.cHP
                self.cHP -= int(value)
                self.refresh()
                value += 1.5*self.ATK
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
            case 'Egwan':
                value = self.ATK
                if self.expertise: value = value * 120 / 100
                for i in target:
                    if i.alive:
                        i.takeDamage('p', int(value))
                self.ATK +=1; self.MP += 1
                self.refresh()
