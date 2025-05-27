# cardGame

![image](https://github.com/user-attachments/assets/ec3e6de8-c25e-4d82-a206-9a006f14d5a4)

This is a simple fantasy themed card game developed as part of the Algorith Design course at the FACE UCV - https://ace.ucv.ro .


# How to play
On starting a new game, the player must build a party using the Build Party button. A party must consist of no more and no less than three characters. Once a party has been assembled, the player may begin a game.

![htp](https://github.com/user-attachments/assets/2e7c21a4-aa86-45f2-a774-a8b16e2c67f5)

The player must use their characters' abilities and additional cards to defeat the opponents' characters first. The game is divided in rounds, at the beginning of which mana is reset to a default of 12 points for each player (which may be affected by card effects) and cards are automatically drawn so as to have a minimum of three. Each round is divided into turns, alternating between the player and the opponent. Using a card is a quick action, and does not consume a turn. Character abilities are slower actions, which will consume a turn (unless a specific card has been used).

In the dark red window the player can see the current round and turn, as well as their mana points (bottom bar) and the opponent's mana points (top bar).

The yellow window represents the play area, displaying the opponent's party (top) and the player's party (bottom). The player can view each character's stats, skill information, and equipment information by cycling through the card tabs.

The purple window is the area where the player can see the cards in their hand. These cards can be equipment cards, support cards, or instant use cards. Cards can be used by clicking on the name. Equpment cards also require a character to be selected afterwards, who will equip it. Each player can hold a maximum of four cards at any point.

The green window represents the support card area, where the player and oppenent's support cards will be displayed. These cards take effect at the beginning of the round, for a limited amount of rounds. Each player can have a maximum of two support cards active at any point.

The orange window contains the buttons respnsible for the characters' abilities. The abilities will change with the selected character. Certain abilities require a target, which will have to be selected after the ability. All information related to a character's abilities is included in that character's ability information tab.

The bright red window contains an action log, displaying the last action taken by either the player or the opponent. The player is P1, while the opponent is P2.

# Known faults

Occasionally, at the beginning of a new game, one random card in the player's hand may have an inactive button. Returning to menu and starting a new game fixes this.

The enemy's behaviour uses a limited set of actions, which may lead to repetitive gameplay.

The enemy's behavior may break in specific scenarios.

Some character images may not display the correct avatar.
