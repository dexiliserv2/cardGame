import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

import builder
import characters
import cards
import deck
import deckCards
# from tkinter import PhotoImage
# from PIL import Image, ImageTk

#sideAreaW = 230
#eAreaH = 315
#pAreaH = 415

#root
root = tk.Tk()
root.title('TCG')
# root.geometry('1200x750') # 1070x730 ?
root.attributes("-fullscreen", 1)
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#styles
s = ttk.Style()
s.theme_use('default')
s.configure('TFrame', background='#6495ED')
s.configure('Frame1.TFrame', background = 'yellow')
s.configure('TLabel', background='white')
s.configure('CharLabel.TLabel', background='#a7c4a9')
s.configure('InfoLabel.TLabel', background='#6495ED', foreground='white', font=('Arial', 14))
s.configure('InactiveLabel.TLabel', background='#c4d7ff')
s.configure('TButton', background='#a7c4a9')

mainframe = ttk.Frame(root)
menuMF = ttk.Frame(root)
dbMF = ttk.Frame(root)

menuActive = False
partyBuliderActive = False
gameActive = False

selectedChars = {1: None, 2: None, 3: None}

displayedCharacters = []

Deck = []
cardsInDeck = 0
cardsInHand = 0

gameOver = False

GameRound = 1
roundOver = 0
playerTurn = None
playerStart = True
playerCanAct = 1

enemyWaitTime = 3000

def Menu():
    global menuActive; menuActive = True
    global partyBuliderActive; partyBuliderActive = False
    global gameActive; gameActive = False
    mainframe.grid_remove()
    dbMF.grid_remove()
    menuMF.grid(row=0, column=0, sticky='nswe')
    menuMF.rowconfigure((0, 1), weight=1, uniform='m')
    menuMF.columnconfigure((0, 1, 2), weight=1, uniform='m')

    deckMenuB = ttk.Button(menuMF, text='Build party', command=PartyBuilder)
    deckMenuB.grid(row=0, column=1, sticky='s', ipadx=20, ipady=20)
    gameMenuB = ttk.Button(menuMF, text='Start game', command=Game)
    gameMenuB.grid(row=1, column=1, sticky='n', pady=70, ipadx=20, ipady=20)

    # howToPlayButton = ttk.Button(menuMF, text='How to play', command=HowToPlay)
    # howToPlayButton.grid(row=0, column=0, sticky='s', ipadx=20, ipady=20)
    #
    # aboutButton = ttk.Button(menuMF, text='About', command=About)
    # aboutButton.grid(row=0, column=2, sticky='s', ipadx=20, ipady=20)

    exitButton = ttk.Button(menuMF, text='Exit game', command=root.destroy)
    exitButton.grid(row=1, column=1, sticky='s', pady=70, ipadx=20, ipady=20)

# def HowToPlay():
#     htp = tk.Tk()
#     htp.title('TCG')
#     htp.geometry('1200x750')
#     htp.resizable(False, False)
#     htp.columnconfigure(0, weight=1)
#     htp.rowconfigure(0, weight=1)

def About():
    print(4)

def builderToMenu():
    global selectBtns
    for i in selectBtns: i.destroy()
    Menu()

def selectCharacter(n, buton):
    global displayedCharacters
    char = characters.charList[n]
    global selectedChars
    global selectBtns
    if selectedChars[1]==char:
        selectedChars[1]=None
        buton.configure(text='Select')
    elif selectedChars[2]==char:
        selectedChars[2]=None
        buton.configure(text='Select')
    elif selectedChars[3]==char:
        selectedChars[3]=None
        buton.configure(text='Select')
    elif not selectedChars[1]:
        selectedChars[1] = char
        buton.configure(text='Remove')
    elif not selectedChars[2]:
        selectedChars[2] = char
        buton.configure(text='Remove')
    elif not selectedChars[3]:
        selectedChars[3] = char
        buton.configure(text='Remove')
    else:
        deckFull = tk.Tk()
        deckFull.title('Warning')
        deckFull.geometry('350x150')
        deckFull.resizable(False, False)
        deckFull.columnconfigure(0, weight=1, uniform='z')
        deckFull.rowconfigure(0, weight=1, uniform='z')
        warningText = tk.Label(deckFull, text='Maximum characters selected.\nRemove a character if you wish to select another.')
        warningText.grid(row=0, column=0, sticky='n', pady=20)
        okButton = tk.Button(deckFull, text='OK', command=lambda: deckFull.destroy())
        okButton.grid(row=0, column=0, sticky='s', pady=20)

def PartyBuilder():
    global menuActive; menuActive = False
    global partyBuliderActive; partyBuliderActive = True
    global gameActive; gameActive = False
    menuMF.grid_remove(); mainframe.grid_remove()

    dbMF.grid(row=0, column=0, sticky='nswe')
    dbMF.rowconfigure((0, 1), weight=1, uniform='a')
    dbMF.columnconfigure(0, weight=1, uniform='a')
    dbMF.columnconfigure(( 1, 2, 3, 4, 5), weight=2, uniform='a')

    backToMenu = tk.Button(dbMF, text='\u2190 Menu', command=builderToMenu)
    backToMenu.grid(row=0, column=0, sticky='nw', padx=20, pady=20)

    global selectedChars
    global displayedChacters
    displayedChacters = []
    global selectBtns
    selectBtns = []

    butonAlaya = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(0, butonAlaya))
    if 'Alaya' in selectedChars.values(): butonAlaya.configure(text='Remove')
    butonBalom = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(1,butonBalom))
    if 'Balom' in selectedChars.values(): butonBalom.configure(text='Remove')
    butonMoss = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(2,butonMoss))
    if 'Moss' in selectedChars.values(): butonMoss.configure(text='Remove')
    butonNilsa = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(3,butonNilsa))
    if 'Nilsa' in selectedChars.values(): butonNilsa.configure(text='Remove')
    butonKiave = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(4,butonKiave))
    if 'Kiave' in selectedChars.values(): butonKiave.configure(text='Remove')

    butonSouset = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(5,butonSouset))
    if 'Souset' in selectedChars.values(): butonSouset.configure(text='Remove')
    butonTeollo = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(6, butonTeollo))
    if 'Teollo' in selectedChars.values(): butonTeollo.configure(text='Remove')
    butonPhael = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(7,butonPhael))
    if 'Phael' in selectedChars.values(): butonPhael.configure(text='Remove')
    butonCirai = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(8, butonCirai))
    if 'Cirai' in selectedChars.values(): butonCirai.configure(text='Remove')
    butonEgwan = tk.Button(dbMF, text='Select', command=lambda: selectCharacter(9, butonEgwan))
    if 'Egwan' in selectedChars.values(): butonEgwan.configure(text='Remove')

    selectBtns.extend([butonAlaya, butonBalom, butonMoss, butonNilsa, butonKiave, butonSouset, butonTeollo, butonPhael, butonCirai, butonEgwan])

    for i in range(1, len(characters.charList) + 1):
        currChar = builder.displayChar(dbMF, i)
        displayedCharacters.append(currChar)
        if i<6:
            selectBtns[i-1].grid(row=0, column=i, sticky='s', pady=50)
        else:
            selectBtns[i-1].grid(row=1, column=i-5, sticky='s', pady=50)

def GameToMenu(window):
    global basicButton; global Ab1Button; global Ab2Button
    basicButton.destroy()
    Ab1Button.destroy()
    Ab2Button.destroy()
    global roundCounter; global manaBars
    roundCounter.destroy(); manaBars.destroy()
    global Deck; global cardsInHand
    Deck = []; cardsInHand = 0
    Menu()
    window.destroy()

def exitGame():
    areYouSure = tk.Tk()
    areYouSure.title('Warning')
    areYouSure.geometry('300x180')
    areYouSure.resizable(False, False)
    areYouSure.columnconfigure((0, 1), weight=1, uniform='z')
    areYouSure.rowconfigure(0, weight=2, uniform='z')
    areYouSure.rowconfigure(1, weight=1, uniform='z')
    warningText = tk.Label(areYouSure, text='Are you sure you want to\nquit the game and return to the menu?\n\nYou will not be able to continue the game!')
    warningText.grid(row=0, column=0, columnspan=2, sticky='n', pady=20)
    okButton = tk.Button(areYouSure, text='OK', command=lambda:GameToMenu(areYouSure))
    okButton.grid(row=1, column=0)
    noButton = tk.Button(areYouSure, text='NO', command=lambda:areYouSure.destroy())
    noButton.grid(row=1, column=1)

def goToBuilder(window):
    window.destroy()
    PartyBuilder()

def returnToMenu(window):
    window.destroy()
    Menu()

def createDeck():
    global Deck
    global handCardArea
    Deck=[]
    for i in deckCards.equipable.keys():
        for j in range(deckCards.equipable.get(i)[4]):
            Deck.append(deck.Equipable(i))
    for i in deckCards.supp.keys():
        for j in range(deckCards.supp.get(i)[3]):
            Deck.append(deck.SuppCard(i))
    for i in deckCards.oneUse.keys():
        for j in range(deckCards.oneUse.get(i)[2]):
            Deck.append(deck.OneUse(i))
    global cardsInDeck
    cardsInDeck = 48

def viewDeck():
    deckViewer = tk.Tk()
    deckViewer.title('Deck')
    deckViewer.geometry('1000x600')
    deckViewer.resizable(False, False)

    deckViewer.rowconfigure((0, 1, 2), weight=1, uniform='v')
    deckViewer.columnconfigure((0, 1, 2, 3), weight=1, uniform='v')

    for i in range(0, 4):
        cardRow1 = Deck[i]; cardRow1.displayCard(deckViewer, 0, i); cardRow1.addName()
        # cardRow2 = Deck[i+4]; cardRow2.displayCard(deckViewer, 1, i); cardRow2.addName()
        # cardRow3 = Deck[i+8]; cardRow3.displayCard(deckViewer, 2, i); cardRow3.addName()

def DrawCards(n):
    global Deck
    global cardsInHand
    global handCardArea
    global handCards
    for i in range(n):
        drawnCard = Deck[random.randrange(0, 42)]
        if not handCards[0]:
            drawnCard.displayCard(handCardArea, 0, 0)
            handCards[0] = drawnCard
        elif not handCards[1]:
            drawnCard.displayCard(handCardArea, 0, 1)
            handCards[1] = drawnCard
        elif not handCards[2]:
            drawnCard.displayCard(handCardArea, 0, 2)
            handCards[2] = drawnCard
        else:
            drawnCard.displayCard(handCardArea, 0, 3)
            handCards[3] = drawnCard
        drawnCard.addButton()
        cardsInHand += 1

def cardsSelectable():
    global handCards; global cardsInHand
    if handCards[0]:
        handCards[0].nameButton.configure(state='normal')
        handCards[0].nameButton.configure(command=lambda: cardAction(0))

    if handCards[1]:
        handCards[1].nameButton.configure(state='normal')
        handCards[1].nameButton.configure(command=lambda: cardAction(1))

    if handCards[2]:
        handCards[2].nameButton.configure(state='normal')
        handCards[2].nameButton.configure(command=lambda: cardAction(2))

    if handCards[3]:
        handCards[3].nameButton.configure(state='normal')
        handCards[3].nameButton.configure(command=lambda: cardAction(3))

def cardsUnselectable():
    global handCards; global cardsInHand
    for i in handCards:
        if i!=False:
            i.nameButton.configure(state='disabled')

def suppCard(cardName, pos):
    global playerMana
    global handCards
    global cardsInHand
    global playerSupp
    global playerCharacters
    playerMana -= deckCards.supp.get(cardName)[0]
    refreshManabars()
    handCards[pos].removeCard()
    handCards[pos] = False
    cardsInHand -= 1
    if not playerSupp[0]:
        playerSupp[0] = [cardName, deckCards.supp.get(cardName)[2]]
        global pSup1
        pSup1.configure(text = '       ' + cardName)
    else:
        playerSupp[1] = [cardName, deckCards.supp.get(cardName)[2]]
        global pSup2
        pSup2.configure(text='       ' + cardName)
    match cardName:
        case 'Determination':
            for i in playerCharacters:
                if i.alive:
                    i.determination = True
                    i.EORAdjustments.append(tuple({'det', 0}))
        case 'Expertise':
            for i in playerCharacters:
                if i.alive:
                    i.expertise = True
                    i.EORAdjustments.append(tuple({'exp', 0}))
        case 'Inspiration':
            for i in playerCharacters:
                if i.alive:
                    i.BACost -= 1
                    i.Ab1Cost -= 1
                    i.Ab2Cost -= 1
                    i.EORAdjustments.append(tuple({'insp', 0}))
                    i.refresh()
        case _:
            print('Mana supp card')

def immediateCard(cardName, pos):
    global actionLog
    actionLog.configure(text='P1: played ' + cardName)
    global playerMana
    global playerCharacters
    global HandCards
    global cardsInHand
    match cardName:
        case 'Swiftness':
            handCards[pos].removeCard()
            handCards[pos] = False
            cardsInHand -= 1
            playerMana -= deckCards.oneUse.get(cardName)[0]
            global playerCanAct
            playerCanAct += 1
        case 'Mana Potion':
            handCards[pos].removeCard()
            handCards[pos] = False
            cardsInHand -= 1
            playerMana += 1
        case 'Newfound Strength':
            handCards[pos].removeCard()
            handCards[pos] = False
            cardsInHand -= 1
            playerMana += 2
        case 'Health Potion (S)':
            selectAllyHeal(cardName, pos)
        case 'Health Potion (L)':
            selectAllyHeal(cardName, pos)
        case 'Resourcefulness':
            handCards[pos].removeCard()
            handCards[pos] = False
            cardsInHand -= 1
            DrawCards(2)
    refreshManabars()

def cardAction(pos):
    global actionLog
    global playerMana
    global handCards
    global cardsInHand
    cardName = handCards[pos].name
    if cardName in deckCards.equipable.keys():
        if deckCards.equipable.get(cardName)[0] <= playerMana:
            selectAllyEquip(cardName, pos)
        else:
            warningMessage('noMana')
    elif cardName in deckCards.supp.keys():
        global playerSupp
        if deckCards.supp.get(cardName)[0] > playerMana:
            warningMessage('noMana')
        elif playerSupp[0] and playerSupp[1]:
            warningMessage('slotsFull')
        else:
            actionLog.configure(text='P1: played '+cardName)
            suppCard(cardName, pos)
    else:
        if deckCards.oneUse.get(cardName)[0] > playerMana:
            warningMessage('noMana')
        match cardName:
            case 'Newfound Strength':
                if playerMana!=0:
                    warningMessage('conditions')
                else:
                    immediateCard(cardName, pos)
            case 'Resourcefulness':
                if cardsInHand>3:
                    warningMessage('conditions')
                else:
                    immediateCard(cardName, pos)
            case _:
                immediateCard(cardName, pos)

def addChars():
    selectMoreChars = tk.Tk()
    selectMoreChars.title('Warning')
    selectMoreChars.geometry('350x150')
    selectMoreChars.resizable(False, False)
    selectMoreChars.columnconfigure(0, weight=1, uniform='z')
    selectMoreChars.rowconfigure(0, weight=1, uniform='z')
    warningText = tk.Label(selectMoreChars, text='Your party is incomplete.\nPlease select more characters.')
    warningText.grid(row=0, column=0, sticky='n', pady=20)
    okButton = tk.Button(selectMoreChars, text='Go to Party Builder', command=lambda: goToBuilder(selectMoreChars))
    okButton.grid(row=0, column=0, sticky='sw', pady=20, padx=30)
    noButton = tk.Button(selectMoreChars, text='Return to Menu', command=lambda: returnToMenu(selectMoreChars))
    noButton.grid(row=0, column=0, sticky='se', pady=20, padx=30)

def refreshManabars():
    global playerMana
    global opponentMana
    global manaBars
    manaBars.configure(
        text=opponentMana * '\u2588 ' + str(opponentMana) + '\n' + playerMana * '\u2588 ' + str(playerMana))

def enableButtons():
    global selectCharBtns
    for i in selectCharBtns: i.configure(state='normal')

def disableButtons():
    global selectCharBtns
    for i in selectCharBtns: i.configure(state='disabled')
    global basicButton
    global Ab1Button
    global Ab2Button
    basicButton.configure(state='disabled')
    Ab1Button.configure(state='disabled')
    Ab2Button.configure(state='disabled')
    global endRound
    endRound.configure(state='disabled')

def reduceSuppRounds():
    global playerSupp; global enemySupp
    if playerSupp[0]:
        playerSupp[0][1] -= 1
        if playerSupp[0][1]==0:
            global pSup1; pSup1.configure(text='       Support\n       Card\n       Slot 1')
            playerSupp[0] = False
    if playerSupp[1]:
         playerSupp[1][1] -= 1
         if playerSupp[1][1] == 0:
             global pSup2; pSup2.configure(text='       Support\n       Card\n       Slot 2')
             playerSupp[1] = False
    if enemySupp[0]:
        enemySupp[0][1] -= 1
        if enemySupp[0][1]==0:
            global eSup1; eSup1.configure(text='       Support\n       Card\n       Slot 1')
            enemySupp[0] = False
    if enemySupp[1]:
        enemySupp[1][1] -= 1
        if enemySupp[1][1]==0:
            global eSup2; eSup2.configure(text='       Support\n       Card\n       Slot 2')
            enemySupp[1] = False

def RoundSetup():
    global GameRound; global playerTurn; global playerStart; global roundOver; global playerCanAct; global oppCanAct
    GameRound += 1
    roundOver = 0
    if playerStart:
        playerTurn = 'Your turn'
        playerCanAct = True
        oppCanAct = False
    else:
        playerTurn = 'Opponent\'s turn'
        playerCanAct = False
        oppCanAct = True
    global playerMana; global opponentMana; playerMana = opponentMana = 12
    global playerSupp; global enemySupp
    global playerCharacters; global enemyCharacters

    reduceSuppRounds()
    if ('Siphon', 1) in playerSupp: opponentMana-=1
    if ('Siphon', 1) in enemySupp: playerMana-=1
    if ('Mana Fountain', 1) in playerSupp: playerMana+=1
    if ('Mana Fountain', 1) in enemySupp: opponentMana+=1

    global roundCounter
    roundCounter.configure(text='Round: ' + str(GameRound) + '\nTurn: ' + playerTurn)

    global endRound
    endRound.configure(state='normal')

    refreshManabars()

    global cardsInHand; global opponentCards
    while cardsInHand<3:
        DrawCards(1)
    while opponentCards<3:
        opponentDraw(1)

    global oppExtraTurn
    oppExtraTurn = 0
    startTurn()

def playerEndRound():
    global roundOver; global playerStart; global playerCanAct; global endRound
    global playerCharacters
    for i in playerCharacters:
        if i.alive:
            i.endOfRoundAdjustment()
    endRound.configure(state='disabled')
    roundOver += 1
    if roundOver<2: playerStart = True
    else: playerStart = False
    playerCanAct = 0
    endTurn()

def startTurn():
    global playerCanAct
    if playerCanAct:
        enableButtons()
        global endRound
        endRound.configure(state='normal')
        global playerTurn; playerTurn = 'Your turn'
        global roundCounter
        roundCounter.configure(text='Round: ' + str(GameRound)+'\nTurn: ' + playerTurn)
        global manaBars
        manaBars.configure(text=opponentMana * '\u2588 '+str(opponentMana)+'\n'+playerMana * '\u2588 '+str(playerMana))
        cardsSelectable()
    else:
        opponentAct()

def endTurn():
    refreshAll()
    global playerCanAct
    playerCanAct -= 1
    if playerCanAct>0:
        startTurn()
    else:
        if playerCanAct < 0: playerCanAct = 1
        disableButtons()
        global playerTurn; playerTurn = 'Opponent\'s turn'
        global roundCounter
        roundCounter.configure(text='Round: ' + str(GameRound) + '\nTurn:\n' + playerTurn)
        refreshManabars()
        cardsUnselectable()
        opponentAct()

def warningMessage(type):
    window = tk.Tk()
    window.title('No Mana')
    window.geometry('300x150')
    text = tk.Label(window)
    custom = None
    match type:
        case 'noMana':
            custom = 'You don\'t have enough mana to play this ability or card.'
        case 'slotsFull':
            custom = 'Both support card slots are occupied.'
        case 'conditions':
            custom = 'The conditions necessary to use this card are not met.'
    general = '\nPlease choose another action or end the round.'
    text.configure(text=custom + general)
    text.grid()

def checkMana(ability, character):
    global playerMana
    global playerSupp
    match ability:
        case 1:
            if character.BACost > playerMana:
                warningMessage('noMana')
                return False
        case 2:
            if character.Ab1Cost > playerMana:
                warningMessage('noMana')
                return False
        case 3:
            if character.Ab2Cost > playerMana:
                warningMessage('noMana')
                return False
    return True

def lockTarget(ability, char, target):
    global enemySelectBtns
    global playerMana
    for i in enemySelectBtns:
        i.destroy()
    match ability:
        case 1:
            char.Basic(target)
            playerMana -= char.BACost
            actionLog.configure(text='P1: used '+char.name+'\'s Basic')
        case 2:
            char.Ab1(target)
            playerMana -= char.Ab1Cost
            actionLog.configure(text='P1: used ' + char.name + '\'s Ability1')
        case 3:
            char.Ab2(target)
            playerMana -= char.Ab2Cost
            actionLog.configure(text='P1: used ' + char.name + '\'s Ability2')
    endTurn()

def selectTarget(ability, char):
    if checkMana(ability, char):
        global enemyCharacters
        global enemySelectBtns
        enemySelectBtns = []
        if enemyCharacters[0].alive:
            char1Button = tk.Button(enemyCharacters[0].t1, text=enemyCharacters[0].name, bg='#a7c4a9',
                                state='normal', command=lambda: lockTarget(ability, char, enemyCharacters[0]))
            enemySelectBtns.append(char1Button)
        if enemyCharacters[1].alive:
            char2Button = tk.Button(enemyCharacters[1].t1, text=enemyCharacters[1].name, bg='#a7c4a9',
                                state='normal', command=lambda: lockTarget(ability, char, enemyCharacters[1]))
            enemySelectBtns.append(char2Button)
        if enemyCharacters[2].alive:
            char3Button = tk.Button(enemyCharacters[2].t1, text=enemyCharacters[2].name, bg='#a7c4a9',
                                state='normal', command=lambda: lockTarget(ability, char, enemyCharacters[2]))
            enemySelectBtns.append(char3Button)
        for i in enemySelectBtns:
            i.grid(row=0, column=0, sticky='w', ipady=5, ipadx=25)

def healPot(char, cardName, pos):
    global playerMana
    global handCards
    global cardsInHand
    global actionLog
    playerMana -= deckCards.oneUse.get(cardName)[0]
    refreshManabars()
    handCards[pos].removeCard()
    handCards[pos] = False
    cardsInHand -= 1
    if cardName == 'Health Potion (S)': value = 5
    else: value = 10
    char.heal(value)
    actionLog.configure(text='P1: healed ' + cardName + ' for ' + str(value)+'HP')
    configSelectButtons()

def selectAllyHeal(card, pos):
    global selectCharBtns
    global playerCharacters
    if playerCharacters[0].alive:
        selectCharBtns[0].configure(command=lambda: healPot(playerCharacters[0], card, pos))
    else:
        selectCharBtns[0].configure(state='disabled')
    if playerCharacters[1].alive:
        selectCharBtns[1].configure(command=lambda: healPot(playerCharacters[1], card, pos))
    else:
        selectCharBtns[1].configure(state='disabled')
    if playerCharacters[2].alive:
        selectCharBtns[2].configure(command=lambda: healPot(playerCharacters[2], card, pos))
    else:
        selectCharBtns[2].configure(state='disabled')

def equip(char, cardName, pos):
    global playerMana
    global handCards
    global cardsInHand
    global actionLog
    playerMana -= deckCards.equipable.get(cardName)[0]
    refreshManabars()
    handCards[pos].removeCard()
    handCards[pos] = False
    cardsInHand -= 1
    char.equip(cardName)
    actionLog.configure(text='P1: equipped ' + cardName + ' on '+char.name)
    configSelectButtons()

def selectAllyEquip(card, pos):
    global selectCharBtns
    global playerCharacters
    if playerCharacters[0].alive:
        selectCharBtns[0].configure(command=lambda: equip(playerCharacters[0], card, pos))
    else:
        selectCharBtns[0].configure(state='disabled')
    if playerCharacters[1].alive:
        selectCharBtns[1].configure(command=lambda: equip(playerCharacters[1], card, pos))
    else:
        selectCharBtns[1].configure(state='disabled')
    if playerCharacters[2].alive:
        selectCharBtns[2].configure(command=lambda: equip(playerCharacters[2], card, pos))
    else:
        selectCharBtns[2].configure(state='disabled')

def lockAlly(ability, char, target):
    global playerMana
    match ability:
        case 2:
            char.Ab1(target)
            actionLog.configure(text='P1: used ' + char.name + '\'s Ability1')
            playerMana -= char.Ab1Cost
        case 3:
            char.Ab2(target)
            actionLog.configure(text='P1: used ' + char.name + '\'s Ability2')
            playerMana -= char.Ab2Cost
    configSelectButtons()
    endTurn()

def selectAlly(ability, char):
    if checkMana(ability, char):
        global selectCharBtns
        global playerCharacters
        if playerCharacters[0].alive:
            selectCharBtns[0].configure(command=lambda: lockAlly(ability, char, playerCharacters[0]))
        else:
            selectCharBtns[0].configure(state='disabled')
        if playerCharacters[1].alive:
            selectCharBtns[1].configure(command=lambda: lockAlly(ability, char, playerCharacters[1]))
        else:
            selectCharBtns[1].configure(state='disabled')
        if playerCharacters[2].alive:
            selectCharBtns[2].configure(command=lambda: lockAlly(ability, char, playerCharacters[2]))
        else:
            selectCharBtns[2].configure(state='disabled')

def AbNoTarget(ability, char):
    global playerMana
    if checkMana(ability, char):
        global playerCharacters
        global enemyCharacters
        if ability == 2:
            match char.name:
                case 'Balom': char.Ab1()
                case 'Nilsa': char.Ab1(playerCharacters)
                case _: char.Ab1(enemyCharacters)
            actionLog.configure(text='P1: used ' + char.name + '\'s Ability1')
            playerMana -= char.Ab1Cost
        else:
            match char.name:
                case 'Balom': char.Ab2()
                case 'Moss': char.Ab2(playerCharacters)
                case 'Souset': char.Ab2(playerCharacters, enemyCharacters)
                case _: char.Ab2(enemyCharacters)
            actionLog.configure(text='P1: used ' + char.name + '\'s Ability2')
            playerMana -= char.Ab2Cost
        endTurn()

def configButtons(i):
    global playerCharacters; global enemyCharacters
    char = playerCharacters[i]

    global basicButton; global Ab1Button; global Ab2Button

    basicButton.configure(command=lambda: selectTarget(1, char))

    Ab1Button.configure(text=char.Ab1Name)
    if char.name in ['Kiave', 'Teollo']:
        Ab1Button.configure(command=lambda: selectTarget(2, char))
    elif char.name == 'Moss':
        Ab1Button.configure(command=lambda: selectAlly(2, char))
    else:
        Ab1Button.configure(command=lambda: AbNoTarget(2, char))

    Ab2Button.configure(text=char.Ab2Name)
    if char.name == 'Alaya':
        Ab2Button.configure(command=lambda: selectTarget(3, char))
    elif char.name == 'Nilsa':
        Ab2Button.configure(command=lambda: selectAlly(3, char))
    else:
        Ab2Button.configure(command=lambda: AbNoTarget(3, char))

def configSelectButtons():
    global selectCharBtns
    global playerCharacters
    if playerCharacters[0].alive:
        selectCharBtns[0].configure(state='normal', command=lambda: configButtons(0))
    else:
        selectCharBtns[0].configure(state='disabled')
    if playerCharacters[1].alive:
        selectCharBtns[1].configure(state='normal', command=lambda: configButtons(1))
    else:
        selectCharBtns[1].configure(state='disabled')
    if playerCharacters[2].alive:
        selectCharBtns[2].configure(state='normal', command=lambda: configButtons(2))
    else:
        selectCharBtns[2].configure(state='disabled')

def refreshAll():
    global playerCharacters; global enemyCharacters
    for i in playerCharacters:
        if i.alive:
            i.refresh()
    for i in enemyCharacters:
        if i.alive:
            i.refresh()


def opponentEndRound():
    global roundOver; global playerCanAct
    global enemyCharacters
    for i in enemyCharacters:
        if i.alive:
            i.endOfRoundAdjustment()
    roundOver += 1
    playerCanAct = 0
    opponentEndTurn()

def opponentAct():
    global oppCanAct
    if oppCanAct:
        oppCheckCards()
        oppCheckChars()
    else:
        startTurn()

def opponentEndTurn():
    global oppCanAct
    oppCanAct -= 1
    if oppCanAct > 0:
        opponentAct()
    else:
        if oppCanAct < 0: oppCanAct = 1
        global playerTurn; playerTurn = 'Your turn'
        global roundCounter
        roundCounter.configure(text='Round: ' + str(GameRound) + '\nTurn:\n' + playerTurn)
        refreshManabars()
        startTurn()

def oppAbility(char, ability, target=None):
    global opponentMana; global actionLog; global oppExtraTurn
    match ability:
        case 0:
            char.Basic(target)
            opponentMana -= char.BACost
            actionLog.configure(text='P2: used '+char.name+'\'s Basic')
        case 1:
            char.Ab1(target)
            opponentMana -= char.Ab1Cost
            actionLog.configure(text='P2: used ' + char.name + '\'s Ability1')
        case 2:
            char.Ab2(target)
            opponentMana -= char.Ab2Cost
            actionLog.configure(text='P2: used ' + char.name + '\'s Ability2')
    refreshManabars()
    oppExtraTurn -= 1

def oppCheckChars():
    global enemyCharacters; global playerCharacters; global opponentMana
    if enemyCharacters[1].alive:
        if opponentMana >= enemyCharacters[1].Ab2Cost and enemyCharacters[1].cHP > enemyCharacters[1].bHP*40/100:
            root.after(enemyWaitTime, oppAbility, enemyCharacters[1], 2, playerCharacters)
        elif opponentMana >= enemyCharacters[1].Ab1Cost and enemyCharacters[1].shieldEff > 0 and enemyCharacters[1].nilsaProtecc:
            root.after(enemyWaitTime, oppAbility, enemyCharacters[1], 1, playerCharacters)
        elif opponentMana >= enemyCharacters[2].Ab2Cost and enemyCharacters[2].alive:
            if enemyCharacters[1].cHP <= enemyCharacters[1].bHP*40/100:
                root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 2, enemyCharacters[1])
            elif enemyCharacters[2].alive and \
                    not enemyCharacters[1].nilsaProtecc and \
                    ((enemyCharacters[0].alive and not enemyCharacters[0].nilsaProtecc) or not enemyCharacters[0].alive) and \
                    not enemyCharacters[2].nilsaProtecc:
                root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 1, enemyCharacters)
            elif enemyCharacters[0].alive:
                if enemyCharacters[0].shieldEff == 0 and \
                        enemyCharacters[1].shieldEff == 0 and \
                        ((enemyCharacters[2].alive and enemyCharacters[2].shieldEff == 0) or not enemyCharacters[2].alive):
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 2, enemyCharacters)
                elif enemyCharacters[1].alive and enemyCharacters[1].shieldEff == 0:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[1])
                elif enemyCharacters[2].alive and enemyCharacters[2].shieldEff == 0:
                    if enemyCharacters[2].nilsaProtecc:
                        if enemyCharacters[0].shieldEff == 0 and not enemyCharacters[0].nilsaProtecc:
                            root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[0])
                        else:
                            root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[2])
                    else:
                        root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[2])
                elif enemyCharacters[2].cHP <= enemyCharacters[2].bHP*40/100:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 2, enemyCharacters[2])
                elif enemyCharacters[0].cHP <= enemyCharacters[0].bHP*40/100:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 2, enemyCharacters[0])
                elif opponentMana >= enemyCharacters[1].BACost:
                    min = 0; pos = 0
                    for i in playerCharacters:
                        if i.alive and i.cHP < min:
                            min = i.cHP
                            pos = i.lineUp
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[1], 0, playerCharacters[pos])
                else:
                    opponentEndRound()
            else:
                if enemyCharacters[2].cHP <= enemyCharacters[2].bHP*40/100:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 2, enemyCharacters[2])
                elif opponentMana >= enemyCharacters[1].BACost:
                    min = 0; pos = 0
                    for i in playerCharacters:
                        if i.alive and i.cHP < min:
                            min = i.cHP
                            pos = i.lineUp
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[1], 0, playerCharacters[pos])
                else:
                    opponentEndRound()
        else:
            if enemyCharacters[0].alive:
                if enemyCharacters[1].shieldEff == 0 and enemyCharacters[0].shieldEff==0:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 2, enemyCharacters)
                elif enemyCharacters[1].shieldEff == 0:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[1])
                elif enemyCharacters[0].cHP < enemyCharacters[0].bHP*40/100 and enemyCharacters[0].shieldEff == 0:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[0])
                elif opponentMana >= enemyCharacters[1].BACost:
                    min = 0; pos = 0
                    for i in playerCharacters:
                        if i.alive and i.cHP < min:
                            min = i.cHP
                            pos = i.lineUp
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[1], 0, playerCharacters[pos])
                else:
                    opponentEndRound()
            elif opponentMana >= enemyCharacters[1].BACost:
                min = 0; pos = 0
                for i in playerCharacters:
                    if i.alive and i.cHP < min:
                        min = i.cHP
                        pos = i.lineUp
                root.after(enemyWaitTime, oppAbility, enemyCharacters[1], 0, playerCharacters[pos])
            else:
                opponentEndRound()
    else:
        if enemyCharacters[0].alive and enemyCharacters[2].alive:
            if opponentMana >= enemyCharacters[2].Ab2Cost:
                if enemyCharacters[2].cHP < enemyCharacters[2].bHP*40/100:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 2, enemyCharacters[2])
                elif enemyCharacters[2].shieldEff == 0 and enemyCharacters[0].cHP >= enemyCharacters[0].bHP*40/100:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[2])
                elif enemyCharacters[0].cHP < enemyCharacters[0].bHP*40/100:
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 2, enemyCharacters[0])
                elif opponentMana >= enemyCharacters[0].BACost:
                    min = 0; pos = 0
                    for i in playerCharacters:
                        if i.alive and i.cHP < min:
                            min = i.cHP
                            pos = i.lineUp
                    root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 0, playerCharacters[pos])
                else:
                    opponentEndRound()
        elif enemyCharacters[0].alive:
            if enemyCharacters[0].cHP < enemyCharacters[0].bHP*40/100 and opponentMana >= enemyCharacters[0].Ab1Cost:
                root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 1, enemyCharacters[0])
            if enemyCharacters[0].cHP >= enemyCharacters[0].bHP*40/100 and opponentMana >= enemyCharacters[0].BACost:
                min = 0; pos = 0
                for i in playerCharacters:
                    if i.alive and i.cHP < min:
                        min = i.cHP
                        pos = i.lineUp
                root.after(enemyWaitTime, oppAbility, enemyCharacters[0], 0, playerCharacters[pos])
            else:
                opponentEndRound()
        else:
            if enemyCharacters[2].cHP < enemyCharacters[2].bHP*40/100 and opponentMana >= enemyCharacters[2].Ab2Cost:
                root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 2, enemyCharacters[2])
            if enemyCharacters[2].cHP >= enemyCharacters[2].bHP*40/100 and opponentMana >= enemyCharacters[2].BACost:
                min = 0; pos = 0
                for i in playerCharacters:
                    if i.alive and i.cHP < min:
                        min = i.cHP
                        pos = i.lineUp
                root.after(enemyWaitTime, oppAbility, enemyCharacters[2], 0, playerCharacters[pos])
            else:
                opponentEndRound()

def oppEquip(char, pos):
    global opponentHand; global opponentCards; global opponentMana
    char.equip(opponentHand[pos].name)
    actionLog.configure(text='P2: equipped ' + opponentHand[pos].name + ' on ' + char.name)
    print(opponentHand[pos].name)
    opponentMana -= opponentHand[pos].cost
    refreshManabars()
    opponentHand[pos] = False
    opponentCards -= 1

def oppSupp(slot, pos):
    global opponentHand; global opponentCards
    global enemyCharacters; global opponentMana
    cardName = opponentHand[pos].name
    match slot:
        case 0:
            enemySupp[0] = [cardName, deckCards.supp.get(cardName)[2]]
            global eSup1
            eSup1.configure(text='       ' + cardName)
        case 1:
            enemySupp[1] = [cardName, deckCards.supp.get(cardName)[2]]
            global eSup2
            eSup2.configure(text='       ' + cardName)
    actionLog.configure(text='P2: played ' + opponentHand[pos].name)
    print(opponentHand[pos].name)
    opponentMana -= opponentHand[pos].cost
    refreshManabars()
    opponentHand[pos] = False
    opponentCards -= 1

    match opponentHand[pos]:
        case 'Determination':
            for i in enemyCharacters:
                if i.alive:
                    i.determination = True
                    i.EORAdjustments.append(tuple({'det', 0}))
        case 'Expertise':
            for i in enemyCharacters:
                if i.alive:
                    i.expertise = True
                    i.EORAdjustments.append(tuple({'exp', 0}))
        case 'Inspiration':
            for i in enemyCharacters:
                if i.alive:
                    i.BACost -= 1
                    i.Ab1Cost -= 1
                    i.Ab2Cost -= 1
                    i.EORAdjustments.append(tuple({'insp', 0}))
                    i.refresh()
        case _:
            print('opp mana card')

def oppOneUse(pos):
    global opponentHand; global opponentCards; global opponentMana; global enemyCharacters
    global actionLog
    match opponentHand[pos].name:
        case 'Swiftness':
            global oppExtraTurn
            oppExtraTurn += 1
            opponentMana -= opponentHand[pos].cost
            refreshManabars()
            actionLog.configure(text='P2: played Swiftness')
            print(opponentHand[pos].name)
            opponentHand[pos] = False
            opponentCards -= 1
        case 'Mana Potion':
            opponentMana += 1
            refreshManabars()
            actionLog.configure(text='P2: played Mana Potion')
            print(opponentHand[pos].name)
            opponentHand[pos] = False
            opponentCards -= 1
        case 'Health Potion (S)':
            for i in enemyCharacters:
                if i.bHP - i.cHP > 5:
                    i.heal(5)
                    opponentMana -= opponentHand[pos].cost
                    refreshManabars()
                    actionLog.configure(text='P2: played Health Potion (S)')
                    print(opponentHand[pos].name)
                    opponentHand[pos] = False
                    opponentCards -= 1
                    break
        case 'Health Potion (L)':
            for i in enemyCharacters:
                if i.bHP - i.cHP > 10:
                    i.heal(10)
                    opponentMana -= opponentHand[pos].cost
                    refreshManabars()
                    actionLog.configure(text='P2: played Health Potion (L)')
                    print(opponentHand[pos].name)
                    opponentHand[pos] = False
                    opponentCards -= 1
                    break
        case 'Resourcefulness':
            if opponentCards<=3:
                opponentMana -= opponentHand[pos].cost
                refreshManabars()
                actionLog.configure(text='P2: played Resourcefulness')
                print(opponentHand[pos].name)
                opponentHand[pos] = False
                opponentCards -= 1
                opponentDraw(2)
        case 'Newfound Strength':
            if opponentMana == 0:
                opponentMana += 2
                refreshManabars()
                actionLog.configure(text='P2: played Newfound Strength')
                print(opponentHand[pos].name)
                opponentHand[pos] = False
                opponentCards -= 1

def oppCheckCards():
    global opponentCards; global opponentHand; global enemySupp; global enemyCharacters; global opponentMana
    for i in range(4):
        # root.after(5000, print, 2)
        if opponentHand[i]:
            if opponentMana >= opponentHand[i].cost:
                cardType = type(opponentHand[i]).__name__
                match cardType:
                    case 'SuppCard':
                        if not enemySupp[0]:
                            root.after(enemyWaitTime, oppSupp, 0, i)
                        elif not enemySupp[1]:
                            root.after(enemyWaitTime, oppSupp, 1, i)
                    case'Equipable':
                        if opponentHand[i].type == 'shield':
                            for j in enemyCharacters:
                                if j.alive and j.name in characters.tankChar and (not j.shield or j.shield.value < opponentHand[i].value):
                                    root.after(enemyWaitTime, oppEquip, j, i)
                                    break
                        elif opponentHand[i].type == 'antim':
                            for j in enemyCharacters:
                                if j.alive and j.name in characters.tankChar and (not j.antim or j.antim.value < opponentHand[i].value):
                                    root.after(enemyWaitTime, oppEquip, j, i)
                                    break
                        elif opponentHand[i].name in ['Simple grimoire', 'Advanced grimoire']:
                            for j in enemyCharacters:
                                if j.alive and j.name in characters.magicChar and (not j.wep or j.wep.value < opponentHand[i].value):
                                    root.after(enemyWaitTime, oppEquip, j, i)
                                    break
                        elif opponentHand[i].name in ['Basic Bow/Sword', 'Mastercraft Bow/Sword']:
                            for j in enemyCharacters:
                                if j.alive and j.name in characters.physChar and (not j.wep or j.wep.value < opponentHand[i].value):
                                    root.after(enemyWaitTime, oppEquip, j, i)
                                    break
                    case _:
                        root.after(enemyWaitTime, oppOneUse, i)

def opponentDraw(n):
    global opponentCards; global opponentHand
    for i in range(n):
        drawnCard = Deck[random.randrange(0, 42)]
        if not opponentHand[0]:
            opponentHand[0] = drawnCard
        elif not opponentHand[1]:
            opponentHand[1] = drawnCard
        elif not opponentHand[2]:
            opponentHand[2] = drawnCard
        else:
            opponentHand[3] = drawnCard
        opponentCards += 1

def Game():
    partyOK = True
    global selectedChars
    for i in selectedChars.values():
        if not i:
            addChars()
            partyOK = False
            break

    if partyOK:
        global menuActive; menuActive = False
        global partyBuliderActive; partyBuliderActive = False
        global gameActive; gameActive = True

        global GameRound; global gameOver; global playerTurn; global roundOver; global playerStart
        global playerMana; global opponentMana; playerMana = opponentMana = 12

        #mainframe config
        menuMF.grid_remove()
        mainframe.grid(row=0, column=0, sticky='nsew')
        mainframe.columnconfigure(0, weight=4, uniform='a')
        mainframe.columnconfigure(1, weight=9, uniform='a')
        mainframe.columnconfigure(2, weight=3, uniform='a')
        mainframe.rowconfigure(0, weight=3, uniform='a')
        mainframe.rowconfigure(1, weight=1, uniform='a')

        #left sidebar
        sidebar = ttk.Frame(mainframe, style='TFrame')
        sidebar.columnconfigure((0, 1), weight=1, uniform='a')
        sidebar.rowconfigure(0, weight=1, uniform='a')
        sidebar.rowconfigure((1, 2), weight=3, uniform='a')
        sidebar.grid(row=0, column=0, sticky='nswe')

        backToMenu = ttk.Button(sidebar, text='\u2190 Menu', command=exitGame)
        backToMenu.grid(row=0, column=0, sticky='nw', padx=20, pady=20)

        #Play Area
        playArea = ttk.Frame(mainframe, style='TFrame')
        playArea.columnconfigure((0, 1, 2), weight=1, uniform='a')
        playArea.rowconfigure((0, 1), weight=1, uniform='a')
        playArea.grid(row=0, column=1, sticky='nswe')

        #right sidebar
        sidebarR = ttk.Frame(mainframe, style='TFrame')
        sidebarR.columnconfigure(0, weight=1, uniform='a')
        sidebarR.rowconfigure(0, weight=4, uniform='a')
        sidebarR.rowconfigure(1, weight=3, uniform='a')
        sidebarR.grid(row=0, rowspan=2, column=2, sticky='nswe')

        #Round and Turn details
        roundFrame = ttk.Frame(sidebarR, style='TFrame')
        roundFrame.rowconfigure((0, 1, 2), weight=1, uniform='a')
        roundFrame.columnconfigure(0, weight=1, uniform='a')
        roundFrame.grid(row=0, column=0, sticky='nswe')

        #Deck
        # pDeck = ttk.Button(mainframe, text='View deck', style='TButton', command=viewDeck)
        # pDeck.grid(row=1, column=0, ipadx=60, ipady=60)

        #Action Log
        logFrame = ttk.Frame(mainframe, style='TFrame')
        logFrame.rowconfigure(0, weight=1, uniform='a')
        logFrame.rowconfigure(1, weight=2, uniform='a')
        logFrame.grid(row=1, column=0, sticky='nswe')
        logHeader = ttk.Label(logFrame, text='Last action: ', style='InfoLabel.TLabel')
        logHeader.grid(row=0, column=0, padx=40, sticky='w')
        global actionLog
        actionLog = ttk.Label(logFrame, style='InfoLabel.TLabel', text='Started game')
        actionLog.grid(row=1, column=0, padx=40, sticky='w')

        #Hand Cards
        global handCardArea
        handCardArea = tk.Frame(mainframe, background='#6495ED')
        handCardArea.grid(row=1, column=1, sticky='nswe')
        handCardArea.columnconfigure((0, 1, 2, 3), weight=1, uniform='a')

        createDeck()

        global opponentHand; global opponentCards
        opponentCards = 0
        opponentHand = [False, False, False, False]

        global handCards; global cardsInHand
        cardsInHand = 0
        handCards = [False, False, False, False]

        #Enemy Support Card Slots
        global eSup1; global eSup2
        eSup1 = ttk.Label(sidebar, text='       Support\n       Card\n       Slot 1', style='InactiveLabel.TLabel', justify='center')
        eSup2 = ttk.Label(sidebar, text='       Support\n       Card\n       Slot 2', style='InactiveLabel.TLabel', justify='center')
        eSup1.grid(row=1, column=0, ipadx=30, ipady=50)
        eSup2.grid(row=1, column=1, ipadx=30, ipady=50)

        # Player Support Card Slots
        global pSup1; global pSup2
        pSup1 = ttk.Label(sidebar, text='       Support\n       Card\n       Slot 1', style='InactiveLabel.TLabel', justify='center')
        pSup2 = ttk.Label(sidebar, text='       Support\n       Card\n       Slot 2', style='InactiveLabel.TLabel', justify='center')
        pSup1.grid(row=2, column=0, ipadx=30, ipady=50)
        pSup2.grid(row=2, column=1, ipadx=30, ipady=50)

        # Ability Buttons Area
        abilities = ttk.Frame(sidebarR, style='TFrame')
        abilities.rowconfigure((0, 1, 2), weight=1, uniform='a')
        abilities.columnconfigure(0, weight=1, uniform='a')
        abilities.grid(row=1, column=0, sticky='nswe')
        global basicButton
        global Ab1Button
        global Ab2Button
        basicButton = tk.Button(abilities, text='Basic attack')
        Ab1Button = tk.Button(abilities, text='Ability 1')
        Ab2Button = tk.Button(abilities, text='Ability 2')
        basicButton.grid(row=0, column=0, ipady=5, ipadx=25)
        Ab1Button.grid(row=1, column=0, ipady=5, ipadx=25)
        Ab2Button.grid(row=2, column=0, ipady=5, ipadx=25)

        global playerSupp; global enemySupp
        playerSupp = [False, False]; enemySupp = [False, False]

        global enemyCharacters; global playerCharacters
        playerCharacters = [
            cards.Character(selectedChars[1], 1, 0, playArea),
            cards.Character(selectedChars[2], 1, 1, playArea),
            cards.Character(selectedChars[3], 1, 2, playArea)]
        enemyCharacters = [
            cards.Character('Moss', 0, 0, playArea),
            cards.Character('Cirai', 0, 1, playArea),
            cards.Character('Nilsa', 0, 2, playArea)]

        #Character Select Buttons
        global selectCharBtns
        selectCharBtns = []
        char1Button = tk.Button(playerCharacters[0].t1, text=playerCharacters[0].name, bg='#a7c4a9',
                                             state='normal', command=lambda: configButtons(0))
        char2Button = tk.Button(playerCharacters[1].t1, text=playerCharacters[1].name, bg='#a7c4a9',
                                state='normal', command=lambda: configButtons(1))
        char3Button = tk.Button(playerCharacters[2].t1, text=playerCharacters[2].name, bg='#a7c4a9',
                                state='normal', command=lambda: configButtons(2))
        selectCharBtns.extend([char1Button, char2Button, char3Button])
        for i in selectCharBtns:
            i.grid(row=0, column=0, sticky='we', ipady=5, ipadx=15)

        for i in range(len(enemyCharacters)):
            label = ttk.Label(enemyCharacters[i].t1, text='   '+enemyCharacters[i].name, style='CharLabel.TLabel')
            label.grid(row=0, column=0, sticky='w', ipady=5, ipadx=25)


        # Round & Turn
        global roundCounter
        playerTurn = 'Your turn'
        roundCounter = ttk.Label(roundFrame, text='Round: ' + str(GameRound) + '\nTurn: ' + playerTurn,
                                 background='#6495ED', foreground='white', font=('Arial', 20))
        roundCounter.grid(row=0, column=0, sticky='n', pady=20)

        global endRound
        endRound = tk.Button(roundFrame, text='End round', command=playerEndRound)
        endRound.grid(row=2, column=0, sticky='n', pady=20, ipadx=10, ipady=5)

        global manaBars
        manaBars = ttk.Label(roundFrame,
                             text=opponentMana * '\u2588 ' + str(opponentMana) + '\n' + playerMana * '\u2588 ' + str(playerMana),
                             background='#6495ED', foreground='white')
        manaBars.grid(row=1, column=0, sticky='n', pady=30)

        GameRound = 0
        RoundSetup()

        # while not gameOver:
        #
        #     while roundOver != 2:
        #         playerTurn = True
        #         for i in playerCharacters:
        #             i.selectable = True
        #             i.refresh()

        #first round start
        # for i in playerCharacters:
        #     i.selectable = True
        #     i.refresh()

        # root.after(100, playerCharacters[1].equip, exCard)
        # root.after(100, playerCharacters[2].Ab1, playerCharacters)
        # root.after(3000, playerCharacters[0].Ab1, 0)
        # root.after(6000, playerCharacters[0].Basic, enemyCharacetrs[0])
        # root.after(9000, playerCharacters[1].takeDamage, 'p', 10, playerCharacters)

Menu()

root.mainloop()