# Program is running but I still need to develop the dinamic of fight
# to define who wins and who loses

from fighter import Fighter, Fight
'''
First, define the fighters with name, nationality, age, height, weight,
wins, losses, draws
Then, define the fight like: fight_one = Fight()
After, tell who are the players: 
    fight.player1 = fighter
    fight.player2 = fighter
fight.setChallenge()
    Important!! Fighter's categories must match
fight.fight()
'''

fighter1 = Fighter('Pretty Boy', 'France', 31, 1.75, 68.9, 11, 2, 1)

fighter2 = Fighter('Putscript', 'Brazil', 29, 1.68, 57.8, 14, 2, 3)

fighter3 = Fighter('Snapshadow', 'EUA', 35, 1.65, 80.9, 12, 2, 1)

fighter4 = Fighter('Dead Code', 'Australia', 28, 1.93, 81.6, 13, 0, 2)

f01 = Fight()

f01.player1 = fighter1
f01.player2 = fighter2

f01.setChallenge()
f01.fight()
