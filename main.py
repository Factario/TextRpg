import random
import time
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import items

# Creates black magic
Fire = Spell('Fire', 10, 100, 'black')
Thunder = Spell('Thunder', 25, 250, 'black')
Ice_Strike = Spell('Ice strike', 15, 150, 'black')
Meteor = Spell('Meteor', 40, 400, 'black')
Quake = Spell('Quake', 30, 300, 'black')

# Creates items
lesser_hp_potion = items('Lesser heal potion', 'heal potion', 'Heals 50 HP', 50)
hp_potion = items('Heal potion', 'heal potion', 'Heals 100 HP', 100)
greater_hp_potion = items('Greater heal potion', 'heal potion', 'Heals 250 HP', 250)
lesser_mp_potion = items('Lesser mana potion', 'mana potion', 'Restores 50 MP', 50)
mp_potion = items('Mana potion', 'mana potion', 'Restores 100 MP', 100)
greater_mp_potion = items('Greater mana potion', 'mana potion', 'Restores 250 MP', 250)
elixir = items('Elixir', 'elixir', 'Restores full HP and MP', 9999)
holy_grail = items('Holy grail', 'elixir', "Restores party's full HP and MP", 9999)

javelin = items('Javelin', 'attack', 'Deals 250 DMG', 250)

# Creates white magic

Lesser_Heal = Spell('Lesser_Blessing', 10, 100, 'white')
Cure = Spell('Cure', 15, 150, 'white')
Heal = Spell('Blessing', 18, 500, 'white')
zas_heal = Spell('Zas Koncertas', 25, 1000, 'white')

player_spells = [Fire, Thunder, Meteor, Cure]
enemy_spells = [Ice_Strike, Thunder, Quake, Heal]
enemy_spells1 = [Ice_Strike, Thunder, Quake, zas_heal]

# Kai reikia dar placiau aprasyt savo lista

player_items = [{'item': hp_potion, 'quantity': 5},
                {'item': mp_potion, 'quantity': 5},
                {'item': elixir, 'quantity': 2},
                {'item': javelin, 'quantity': 3},
                {'item': holy_grail, 'quantity': 1}]

# Player and evil, stats
player1 = Person('Vergil ', 750, 150, 60, 35, player_spells, player_items)
player2 = Person('Dante ', 750, 150, 60, 35, player_spells, player_items)
player3 = Person('Nero ', 750, 150, 60, 35, player_spells, player_items)

enemy1 = Person('Minion', 1000, 120, 120, 40, enemy_spells, [])
enemy2 = Person('Demon', 2500, 200, 100, 25, enemy_spells1, [])
enemy3 = Person('Minion', 1000, 120, 400, 34, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

while running:
    print('=========================================================================================================')
    print('        HP                                   MP')
    for player in players:
        player.get_stats()

    print('\n')
    print('          HP                                            MP')
    for enemy in enemies:
        enemy.enemy_stats()
    print('\n')

    for player in players:
        player.choose_action()
        choice = input('Choose action: ')

        if choice.isdigit() is False:
            print(bcolors.FAIL + bcolors.BOLD + 'Wrong choice' + bcolors.ENDC)
            continue

        if int(choice) > len(player.actions):
            print(bcolors.FAIL + bcolors.BOLD + 'Wrong choice' + bcolors.ENDC)
            continue

        else:
            index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(player.name + 'attacked:', enemies[enemy].name, 'for', dmg, "DMG",)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + ' has died')
                del enemies[enemy]
                time.sleep(0.33)

        if index == 1:
            player.choose_spells()
            spell_choice = input('\nChoose spell: ')
            time.sleep(0.33)

            if spell_choice.isdigit() is False:
                print(bcolors.FAIL + bcolors.BOLD + 'Wrong choice' + bcolors.ENDC)
                continue

            if int(spell_choice) > len(player.spell):
                print(bcolors.FAIL + bcolors.BOLD + 'Wrong choice' + bcolors.ENDC)
                continue

            else:
                spell_choice = int(spell_choice) - 1

            spell = player.spell[spell_choice]
            spell_dmg = spell.generate_damage()

            current_mp = player.get_mp()
            if spell.cost > current_mp:
                print(bcolors.FAIL + '\nNot enough mana\n' + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

    # str() neturi buti kaip str(spell.dmg()) o kaip str(spell.dmg)

            if spell.type == 'white':
                player = player.choose_allies(players)
                players[player].heal(spell.dmg)
                print(bcolors.OKGREEN + '\n' + spell.name + ' Healed ' + players[player].name + 'for: ' + str(spell.dmg)
                      + ' HP' + bcolors.ENDC)

            elif spell.type == 'black':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(spell.dmg)
                print(bcolors.OKBLUE + '\n' + spell.name + ' dealt ' + enemies[enemy].name, str(spell.dmg),
                      'damage' + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + ' has died')
                    del enemies[enemy]
                    time.sleep(0.33)

        if index == 2:
            player.choose_items()
            item_choice = input("\n Choose item: ")
            time.sleep(0.33)

            if item_choice.isdigit() is False:
                print(bcolors.FAIL + bcolors.BOLD + 'Wrong choice' + bcolors.ENDC)
                continue

            if int(item_choice) > len(player.items):
                print(bcolors.FAIL + bcolors.BOLD + 'Wrong choice' + bcolors.ENDC)
                continue

            else:
                item_choice = int(item_choice) - 1

            items = player.items[item_choice]['item']
            # skaiciuoti turi nuo cia nes kitaip uzskaityt 1 kaip 0
            if player.items[item_choice]['quantity'] <= 0:
                print(bcolors.WARNING + 'You are out of item' + bcolors.ENDC)
                continue
            player.items[item_choice]['quantity'] -= 1

            if items.type == 'heal potion':
                player = player.choose_allies(players)
                players[player].heal(items.property)
                print(bcolors.OKGREEN + '\n' + items.name + ' healed ' + players[player].name + 'for: '
                      + str(items.property) + ' HP ' +
                      bcolors.ENDC)
            if items.type == 'mana potion':
                player = player.choose_allies(players)
                players[player].restore_mana(items.property)
                print(bcolors.OKBLUE + '\n' + items.name + ' restored ' + players[player].name + 'mana for: ' + str(
                    items.property) + ' MP ' + bcolors.ENDC)
            if items.type == 'elixir':

                if items.name == 'Holy grail':
                    print('Your team are fully refreshed')
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player = player.choose_allies(players)
                    players[player].hp = players[player].maxhp
                    players[player].mp = players[player].maxmp
                    print(bcolors.OKBLUE + '\n' + items.name + ' fully refreshed ' + players[player].name
                          + bcolors.ENDC)

            if items.type == 'attack':
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(items.property)
                print('\n' + items.name + ' dealt ' + str(items.property) + ' DMG for ' + enemies[enemy].name
                      + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + ' has died')
                    del enemies[enemy]
                    time.sleep(0.33)


    if len(enemies) == 0:
        print(bcolors.OKGREEN + 'You win' + bcolors.ENDC)
        running = False

    # enemy ai
    print('\n')
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        if enemy_choice == 0:
            if len(players) == 0:
                print(bcolors.FAIL + bcolors.BOLD + 'Enemy won' + bcolors.ENDC)
                time.sleep(9)
                running = False
            target = random.randrange(0, len(players))
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)

            print(bcolors.FAIL + bcolors.BOLD + enemy.name + ' attacks: ' + players[target].name
                   + 'for ' + str(enemy_dmg) + ' DMG' + bcolors.ENDC)

            if players[target].get_hp() == 0:
                print(players[target].name + ' has died')
                del players[target]
                time.sleep(0.33)

        if enemy_choice == 1:
            try:
                spell, spell_dmg = enemy.enemy_choose_spell()
                enemy.reduce_mp(spell.cost)

                if spell.type == 'white':
                    enemy.choose_allies(enemies)
                    enemy.heal(spell.dmg)
                    print(bcolors.OKGREEN + enemy.name + ' ' + spell.name + ' Healed '
                          + enemy.name + ' for: ' + str(spell.dmg) + ' HP' + bcolors.ENDC)

                elif spell.type == 'black':
                    if len(players) == 0:
                        print(bcolors.FAIL + bcolors.BOLD + 'Enemy won' + bcolors.ENDC)
                        time.sleep(9)
                        running = False
                    target = random.randrange(0, len(players))
                    players[target].take_damage(spell.dmg)
                    print(bcolors.OKBLUE + enemy.name + ' ' + spell.name + ' dealt: '
                           + str(spell.dmg) + ' DMG for ' + players[target].name + bcolors.ENDC)

                    if players[target].get_hp() == 0:
                        print(players[target].name + ' has died')
                        del players[target]
                        time.sleep(0.33)

            except TypeError:
                if len(players) == 0:
                    print(bcolors.FAIL + bcolors.BOLD + 'Enemy won' + bcolors.ENDC)
                    time.sleep(9)
                    running = False
                target = random.randrange(0, len(players))
                enemy_dmg = enemy.generate_damage()

                players[target].take_damage(enemy_dmg)

                print(bcolors.FAIL + bcolors.BOLD + enemy.name + ' attacks: ' + players[target].name
                      + 'for ' + str(enemy_dmg) + ' DMG' + bcolors.ENDC)

                if players[target].get_hp() == 0:
                    print(players[target].name + ' has died')
                    del players[target]
                    time.sleep(0.33)
