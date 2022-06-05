import random
import colorama
colorama.init(autoreset=True)

class bcolors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, spell, items):

        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.spell = spell
        self.items = items
        self.actions = ['Attack', 'Spells', 'Items']
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def restore_mana(self, dmg):
        self.mp += dmg
        if self.mp > self.maxmp:
            self.mp = self.maxmp

    def get_hp(self):
        return self.hp

    def max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print('\n' + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.WARNING + bcolors.BOLD + 'Actions: ' + bcolors.ENDC)
        for item in self.actions:
            print('    ', str(i) + ':', item)
            i += 1

    def choose_spells(self):
        i = 1
        print('\n' + bcolors.OKBLUE + bcolors.BOLD + 'Spells' + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + 'Current Mana: ' + str(self.mp) + '/' + str(self.maxmp) + bcolors.ENDC)
        for spells in self.spell:
            if spells.type == 'black':
                print(str(i), ':', spells.name, '(cost: ', str(spells.cost), '| DMG: ', str(spells.dmg), ')')
                i += 1
            if spells.type == 'white':
                print(str(i), ':', spells.name, '(cost: ', str(spells.cost), '| Heal: ', str(spells.dmg), ')')
                i += 1

    def choose_items(self):
        i = 1
        print('\n' + bcolors.OKGREEN + bcolors.BOLD + 'Items: ' + bcolors.ENDC)
        for items in self.items:
            # Kai reikia rast ne pagal tipa o pagal aprasyma. naudojant test['test'].testing
            print('    ', str(i) + ' : ' + items['item'].name, ' - ', items['item'].description + ' │ ' +
                  str(items['quantity']) + 'x')
            i += 1

    def choose_allies(self, players):
        i = 1
        print(bcolors.BOLD + 'Players:' + bcolors.ENDC)
        for player in players:
            if player.get_hp() != 0:
                print('    ', str(i) + '.', player.name)
                i += 1
        choice = int(input('Choose target: ')) - 1
        return choice

    def choose_target(self, enemies):
        i = 1
        print(bcolors.FAIL + bcolors.BOLD + 'Target:' + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print('    ', str(i) + '.', enemy.name)
                i += 1
        choice = int(input('Choose target: ')) - 1
        return choice


    def enemy_stats(self):
        hp_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 100 / 3

        mp_bar = ''
        mp_ticks = (self.mp / self.maxmp) * 100 / 8

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        while mp_ticks > 0:
            mp_bar += '█'
            mp_ticks -= 1

        while mp_ticks > 0:
            mp_bar += '█'
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '

        hp_string = str(self.hp) + '/' + str(self.maxhp)
        current_hp = ''

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += ' '
                decreased -= 1

            current_hp += hp_string

        else:
            current_hp = hp_string

        mp_string = str(self.mp) + '/' + str(self.maxmp)
        current_mp = ''

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += ' '
                decreased -= 1

            current_mp = mp_string

        else:
            current_mp = mp_string

        print(bcolors.BOLD + self.name + '\n' +
              current_hp + '│' + bcolors.FAIL + hp_bar +
              bcolors.ENDC + '│   ' +
              current_mp + '│' + bcolors.OKBLUE + bcolors.BOLD + mp_bar +
              bcolors.ENDC + '│')

    def get_stats(self):
        hp_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ''
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += ' '

        while mp_ticks > 0:
            mp_bar += '█'
            mp_ticks -= 1

        while mp_ticks > 0:
            mp_bar += '█'
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += ' '

        hp_string = str(self.hp) + '/' + str(self.maxhp)
        current_hp = ''

        if len(hp_string) < 7:
            decreased = 7 - len(hp_string)

            while decreased > 0:
                current_hp += ' '
                decreased -= 1

            current_hp += hp_string

        else:
            current_hp = hp_string

        mp_string = str(self.mp) + '/' + str(self.maxmp)
        current_mp = ''

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += ' '
                decreased -= 1

            current_mp = mp_string

        else:
            current_mp = mp_string

        print(bcolors.BOLD + self.name + '\n' +
              current_hp + '│' + bcolors.OKGREEN + hp_bar +
              bcolors.ENDC + '│   ' +
              current_mp + '│' + bcolors.OKBLUE + bcolors.BOLD + mp_bar +
              bcolors.ENDC + '│')

    def enemy_choose_spell(self):
        spell_choice = random.randrange(0, len(self.spell))
        spell = self.spell[spell_choice]
        spell_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == 'white' and pct > 50:
            self.enemy_choose_spell()

        else:
            return spell, spell_dmg