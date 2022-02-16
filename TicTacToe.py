# tic tac toe between human and computer


import contextvars
from random import choice
from random import random
from tkinter import N, Y

from matplotlib.style import available
from Brain_class import Brain 

# global variables
available = []
selectedMoves = []
gameMoves = []
p1 = Brain('player1')                       # set up a player p1 for AI, nicname (filename)= 'player1'

def ResetGame():
    global available
    available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    global selectedMoves
    selectedMoves = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    global gameMoves                        # remembers move sequence of the game
    gameMoves = []

def printBoard(board):
    print()
    print(f'{board[0]} | {board[1]} | {board[2]} ')
    print('-'*9)
    print(f'{board[3]} | {board[4]} | {board[5]} ')
    print('-'*9)
    print(f'{board[6]} | {board[7]} | {board[8]} \n')


def playHuman(HUMAN):
    select = ''
    checkWin = False

    while select not in available:
        select = input('Choose a square... ')
    gameMoves.append(select)
    available.remove(select)

    selectedMoves[int(select)-1] = HUMAN
    printBoard(selectedMoves)

    checkWin = checkWinner()
    return checkWin


def playComputer(COMPUTER):
    select = ''
    checkWin = False
    
    input('Press Enter key for COMPUTER to take turn...')
    # get suggested move from Brain
    select = p1.SuggestMove(gameMoves)
    # check we have found an available tile
    if select not in available:
        #get a random square from avaialable
        select = choice(available)

    gameMoves.append(select)
    available.remove(select)

    selectedMoves[int(select)-1] = COMPUTER
    printBoard(selectedMoves)

    checkWin = checkWinner()
    return checkWin


def checkWinner():
    win = False
    row1 = (selectedMoves[0], selectedMoves[1], selectedMoves[2])
    row2 = (selectedMoves[3], selectedMoves[4], selectedMoves[5])
    row3 = (selectedMoves[6], selectedMoves[7], selectedMoves[8])
    col1 = (selectedMoves[0], selectedMoves[3], selectedMoves[6])
    col2 = (selectedMoves[1], selectedMoves[4], selectedMoves[7])
    col3 = (selectedMoves[2], selectedMoves[5], selectedMoves[8])
    diag1 = (selectedMoves[0], selectedMoves[4], selectedMoves[8])
    diag2 = (selectedMoves[2], selectedMoves[4], selectedMoves[6])
    winLines = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    
    while win == False:
        for each in winLines:
            if not ' ' in each:
                if each[0] == each[1] == each[2]:
                    win = True
                    break
        #default break if no winline found
        break

    return win    



def main():
    continue_playing = True
    while continue_playing == True:
        # initialisation
        ResetGame()
        winner = False
        game_over = False
        goFirst = input("Do you want to go first? (Y/N) ")
        if goFirst.capitalize() == 'Y':
            HUMAN = 'O'
            COMPUTER = 'X'
            player = 'HUMAN'
        else:
            HUMAN = 'X'
            COMPUTER = 'O'
            player = 'COMPUTER'

        printBoard(available)

        while not game_over:
            if player == 'HUMAN':
                game_over = playHuman(HUMAN)
                if  game_over:
                    print(f"\nPlayer {player} won")
                    winner = True
                    break
                else:
                    player = 'COMPUTER'
            else:
                game_over = playComputer(COMPUTER)
                if  game_over:
                    print(f"\nPlayer {player} won")
                    winner = True
                    break
                else:
                    player = 'HUMAN'
            if len(available) < 1:
                print('It is a draw')
                winner = False
                game_over = True

        if winner:
            p1.LearnMoves(gameMoves)
        
        continue_playing = input('Play again? (Y/N) ')
        if continue_playing.capitalize() == 'N':
            continue_playing = False
        else:
            continue_playing = True


    print()
    p1.Save()
    print('Thanks for playing')
    exit()

if __name__ == "__main__":
    main()
