charList = ['Alaya', 'Balom', 'Moss', 'Nilsa', 'Kiave', 'Souset', 'Teollo', 'Phael', 'Cirai', 'Egwan']

physChar = ['Kiave', 'Teollo', 'Phael', 'Cirai', 'Egwan']

magicChar = ['Alaya', 'Balom', 'Moss', 'Nilsa', 'Souset', 'Teollo', 'Phael']

tankChar = ['Moss', 'Nilsa', 'Cirai', 'Egwan']

targetedAb1 = ['Moss', 'Kiave', 'Teollo']

targetedAb2 = ['Alaya']

char = {
    'Alaya': (30, 3, 3, 6, 6, 'Scorch the Earth', 'Flaming Missile',
              'Deal 1x ATK physical damage to one enemy',
              'Deal 2x MP magic damage to all enemies',
              'Deal 3x MP magic damage to one enemy'),
    'Balom': (35, 2, 4, 3, 8, 'Aquaflow', 'Surging Torrent',
               'Deal 1x MP magic damage to one enemy',
               'Increase MP by 1xMP for this round',
               'Increase MP by 3xMP for this round'),
    'Moss': (40, 3, 0, 4, 4, 'Vine Armor', 'Force of Nature',
             'Deal 1x ATK physical damage to one enemy',
             'Create a shield worth 0.25x Moss\'s current HP + 2x MP for one ally',
             'Create a shield worth 0.2x Moss\'s current HP + 2x MP for all allies'),
    'Nilsa': (50, 2, 2, 4, 4, 'Protector\'s Vow', 'Rejuvenation',
              'Deal 1x ATK physical damage to one enemy',
              'Create a special barrier for each ally, reducing the next instance of damage received by 40%',
              'Heal one ally for 0.2x Nilsa\'s current HP + 3x MP'),
    'Kiave': (30, 4, 0, 5, 10, 'Unflinching Focus', 'Distributed Fire',
              'Deal 1x ATK physical damage to one enemy',
              'Deal 2x ATK + 1x MP physical damage to one enemy',
              'Deal 3x ATK + 2x MP physical damage to all enemies'),
    'Souset': (20, 2, 5, 6, 10, 'Torn Defenses', 'Sacrifice',
               'Deal 0.5x MP magic damage to one enemy',
               'Remove all enemy shields',
               'Consume 0.5x current HP from all allies and deal 0.25x MP x consumed HP magic damage to all enemies, distributed evenly'),
    'Teollo': (35, 2, 3, 5, 10, 'Stagger', 'Fall',
                'Deal 1x ATK physical damage to one enemy',
                'Deal 1x ATK physical damage to one enemy and reduce the target\'s ATK and MP by 0.5x MP for this round',
                'Deal 2x ATK physical damage to all enemies and reduce the targets\' ATK and MP by 0.5x MP for this round'),
    'Phael': (35, 4, 1, 4, 7, 'Fierce Cleave', 'Decimating Slash',
              'Deal 1x ATK physical damage to one enemy',
              'Deal 1x ATK + 1x MP physical damage to all enemies',
              'Deal 2x ATK + 2x MP physical damage to all enemies'),
    'Cirai': (40, 5, 0, 6, 6, 'Overwhelming Force', 'Absolute Determination',
              'Deal 1x ATK physical damage to one enemy',
              'Deal 2x ATK physical damage to all enemies',
              'Consume 0.2x current HP and deal 1x consumed HP + 1.5x ATK physical damage to all enemies'),
    'Egwan': (40, 3, 2, 6, 6, 'Soothing tremor', 'Rumbling Strike',
              'Deal 1x ATK physical damage to one enemy',
              'Deal 2x ATK physical damage to all enemies and heal self for 2x MP health',
              'Deal 2x ATK physical damage to all enemies and permanently increase self ATK and MP by 1')
    }

