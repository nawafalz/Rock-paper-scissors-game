import random

# this is Rock , Paper , scissors Game |

# list of Rock , Paper , scissors #
elements = ['rock', 'paper', 'scissors']

# 2 player Game


still_playing = True
score_player1 = 0
score_player2 = 0

while still_playing:

    print('enter one of the three  > Rock , Paper , scissors')
    player1 = str(input('player 1 : '))
    player2 = random.choice(elements)
    print("player 2 :", player2)

    # description making
    # for rock
    if player1 == 'rock':
        if player2 == 'rock':
            print('\ndraw')
        elif player2 == 'paper':
            print('\nplayer 2 won\n')
            score_player2 += 1
        elif player2 == 'scissors':
            print('\nplayer 1 won \n')
            score_player1 += 1
    # description making
    # for paper
    if player1 == 'paper':
        if player2 == 'paper':
            print('\ndraw')
        elif player2 == 'rock':
            print('\nplayer 1 won \n')
            score_player1 += 1
        elif player2 == 'scissors':
            print('\nplayer 2 won\n')
            score_player2 += 1

    # description making
    # for scissors
    if player1 == 'scissors':
        if player2 == 'scissors':
            print('\ndraw')
        elif player2 == 'paper':
            print('\nplayer 1 won \n')
            score_player1 += 1
        elif player2 == 'rock':
            print('\nplayer 2 won\n')
            score_player2 +=1

    result = 'the score for player 1 : {}\nthe score for player 2 : {} \n'
    print(result.format(score_player1, score_player2))

    if score_player1 == 3:
        still_playing = False
    elif score_player2 == 3:
        still_playing = False
