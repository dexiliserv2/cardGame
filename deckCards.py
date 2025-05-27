equipable = {
	'Wood Shield' : (1, 'shield', 2, '+2 Phys Res', 2),
	'Metal Shield' : (2, 'shield', 4, '+4 Phys Res', 2),
	'Anti Magic Ring' : (1, 'antim', 2, '+2 Magic Res', 2),
	'Anti Magic Amulet' : (2, 'antim', 4, '+4 Magic Res', 2),
	'Simple grimoire' : (1, 'wep', 1, '+1 MP', 2),
	'Advanced grimoire' : (2, 'wep', 2, '+2 MP', 2),
	'Basic Bow/Sword' : (1, 'wep', 1, '+1 ATK', 2),
	'Mastercraft Bow/Sword' : (2, 'wep', 2, '+2 ATK', 2)
}

supp = {
	'Siphon': (1, 'At the start of the round, drain 1 point of Mana from the opponent. 2 Rounds', 3, 2),
	'Mana Fountain': (1, 'At the start of the round, gain 1 point of Mana. 3 Rounds', 4, 2),
	'Determination': (1, 'Ignore 20% of incoming damage. 1 Round', 1, 2),
	'Expertise': (1, 'Increase outgoing damage by 20%. 1 Round', 1, 2),
	'Inspiration': (2, 'Reduce all ability costs by 1. 1 Round', 1, 2)
}

oneUse = {
	'Swiftness': (1, 'The next action does not consume a turn.', 3),
	'Mana Potion': (0, 'Gain 1 point of Mana.', 3),
	'Newfound Strength': (0, 'Gain 2 points of Mana. Can only be used if the player has 0 points of mana left.', 3),
	'Health Potion (S)': (0, 'Restore 5 HP to one character.', 3),
	'Health Potion (L)': (1, 'Restore 10 HP to one character.', 3),
	'Resourcefulness': (1, 'Draw 2 cards from the deck. Each player can only hold a maximum of 4 cards at once.', 2)
	# 'Cull': (1, 'Remove one of the opponent\'s support cards.', 3),
	# 'Disarm': (2, 'Remove one equippable item from one enemy.', 2)
}