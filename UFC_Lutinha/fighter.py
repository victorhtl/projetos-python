from random import randint


class Fight:
    ''' Class were two objects (fighters) will fight '''

    def __init__(self):
        self.__player1 = None
        self.__player2 = None
        self.__situation = False

    @property
    def player1(self):
        return self.__player1

    @player1.setter
    def player1(self, value):
        self.__player1 = value

    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, value):
        self.__player2 = value

    def setChallenge(self):
        if self.player1.category() == self.player2.category():
            self.__situation = True
            print('Challenge is setted')
        else:
            print("Categories doesn't match")
            print("Fight cannot be setted")

    def fight(self):
        print('\nPlayer 1:')
        self.player1.intro()
        print('\nPlayer 2: ')
        self.player2.intro()
        if self.__situation:
            pass
        else:
            print("Fight is not approved")


class Fighter:
    '''Class that defines players'''

    def __init__(self, name, nationality, age, height, weight,
                 wins, losses, draws):
        self.__name = name
        self.__nationality = nationality
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__wins = wins
        self.__losses = losses
        self.__draws = draws

    # Methods
    def category(self):
        if self.__weight < 52.2:
            self.__category = 'invalid'
        elif self.__weight <= 70.3:
            self.__category = 'light'
        elif self.__weight <= 83.3:
            self.__category = 'medium'
        elif self.__weight <= 120.2:
            self.__category = 'heavy'
        else:
            self.__category = 'invalid'
        return self.__category

    def intro(self):
        print(f'Fighter: {self.__name}')
        print(f'From: {self.__nationality}')
        print(f'{self.__age} years old')
        print(f'{self.__height} meters high')
        print(f'Weighing {self.__weight} Kg')
        print(f'With {self.__wins} wins', end=', ')
        print(f'{self.__losses} losses', end=', ')
        print(f'and {self.__draws} draws')

    def status(self):
        print(f'\n{self.__name}')
        print(f'Category: {self.category()}')
        print(f'{self.__wins} wins')
        print(f'{self.__losses} losses')
        print(f'{self.__draws} draws')

    def winFight(self):
        self.__wins += 1

    def looseFight(self):
        self.__losses += 1

    def drawFight(self):
        self.__draws += 1
