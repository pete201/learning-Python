# class to hold tic tac toe board

from tkinter import *
from Brain_class import Brain 


class player():
    def __init__(self, genus, token) -> None:
        self.genus = genus  # legal values are 'HUMAN' and 'COMPUTER'
        self.token = token

        # if a COMPUTER, we need to set up a Brian:
        if self.genus == 'COMPUTER':
            self.brain = Brain('Brian')
            

class game():
    def __init__(self) -> None:
        self.player1 = player('HUMAN','X')
        self.player2 = player('COMPUTER','O')
        self.current_player = self.player1
        self.ResetGame()


    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player =self.player2
        else:
            self.current_player = self.player1


    def swap_who_goes_first(self):
        '''whoever is assigned 'X' went first last time'''
        if self.player1.token == 'X':
            self.player1.token = 'O'
            self.player2.token = 'X'
            self.current_player = self.player2
        else:
            self.player1.token = 'X'
            self.player2.token = 'O'
            self.current_player = self.player1


    def ResetGame(self):
        # reset the available moves and the selected moves so far...
        self.available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.selectedMoves = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        # remembers move sequence of the game
        self.gameMoves = []


    def play_move(self, tile_number = None):
        '''if a tile number is passed, play that, otherwise look up suggestion from Brain'''
        if tile_number == None: # indicates COMPUTER player
            '''no tile number required for COMPUTER turn'''
            # get suggested move from Brain
            tile_number = self.player2.brain.SuggestMove(self.gameMoves)
        # update available and game arrays
        self.gameMoves.append(str(tile_number))
        self.available.remove(str(tile_number))
        self.selectedMoves[int(tile_number)-1] = self.current_player.token # use tile_number-1 here as we are refering to an array index

        winner = self.checkWinner()
        if winner:
            print(self.current_player.token,"wins !!!")
            self.player2.brain.Learn8from1(self.gameMoves)
            return 'WINNER'

        # check if draw
        elif len(self.gameMoves) > 8:
            print("We have a draw!!")
            #self.player2.gameStats("COMPUTER", '\tdraw')
            return 'DRAW'
        else:
            return 'PLAY-ON'
      

    def checkWinner(self):
        win = False
        row1 = (self.selectedMoves[0], self.selectedMoves[1], self.selectedMoves[2])
        row2 = (self.selectedMoves[3], self.selectedMoves[4], self.selectedMoves[5])
        row3 = (self.selectedMoves[6], self.selectedMoves[7], self.selectedMoves[8])
        col1 = (self.selectedMoves[0], self.selectedMoves[3], self.selectedMoves[6])
        col2 = (self.selectedMoves[1], self.selectedMoves[4], self.selectedMoves[7])
        col3 = (self.selectedMoves[2], self.selectedMoves[5], self.selectedMoves[8])
        diag1 = (self.selectedMoves[0], self.selectedMoves[4], self.selectedMoves[8])
        diag2 = (self.selectedMoves[2], self.selectedMoves[4], self.selectedMoves[6])
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


class Board(Frame):
    '''GUI implementation of Tic-Tac-Toe'''
    def __init__(self, master) -> None:
        super(Board, self).__init__(master)
        self.grid()
        self.buttons = []
        self.create_widgets()
        
        self.ticTacToe = game()     # tk can access game logic functions
        self.gameState = 'PLAY-ON'  # possible values are 'PLAY-ON', 'WINNER', 'DRAW'


    def button_press(self, btn):
        print(f'button pressed: {btn}')
        # update the text on button when button is pressed.  use btn-1 since array index is 0-8 and btn numbers are 1-9 (to maintain Brain functionality)
        # play HUMAN turn
        #check if tile is vaccant else return without doing anything
        if self.gameState == 'PLAY-ON':
            if self.buttons[btn-1]['text'] == '':
                # update btn txt wit player character
                self.buttons[btn-1]['text'] = self.ticTacToe.current_player.token
                self.gameState = self.ticTacToe.play_move(btn) 
                #################################################
                # on retun from play we can get:
                # WINNER
                # DRAW
                # PLAY-ON
                #################################################
                self.ticTacToe.switch_turn()
            else:
                return
        else:
            # if a button is pressed when game-over, restart game and reset board
            self.ticTacToe.ResetGame()
            self.ticTacToe.swap_who_goes_first()
            for tile in range(9):
                self.buttons[tile]['text'] = ''
            self.gameState = 'PLAY-ON'

        if self.gameState == 'PLAY-ON' and self.ticTacToe.current_player.genus == 'COMPUTER':
            self.gameState = self.ticTacToe.play_move()  # no value passed for player.genus = COMPUTER
            # update btn with COMPUTER token
            # get tile_number from last play_move... which is the last entry in gameMoves[]
            self.buttons[int(self.ticTacToe.gameMoves[-1])-1]['text'] = self.ticTacToe.current_player.token # get tile from last gameMoves[] stored
            self.ticTacToe.switch_turn()


    def create_widgets(self):
        '''create button and text widgets'''
        #create welcome label
        self.welcome_lbl = Label(self, text="Welcome to Tic-Tac-Toe")
        self.welcome_lbl.grid(row=0, column=0, columnspan=3, sticky=W)

        # create buttons
        count=0
        for r in range(3):
            for c in range(3):
                count += 1
                self.buttons.append(Button(self, text='', width=14, height=6, bg="blue", fg="yellow", relief=GROOVE, command=lambda x=count: self.button_press(x)))
                self.buttons[-1].grid(row=r+1, column=c)



def main():

    root = Tk()
    root.title('Tic-Tac-Toe')

    myGUI = Board(root)
    root.mainloop()

    # after games have ended, save Brain to file:
    print('Saving brain to file, please wait...')
    myGUI.ticTacToe.player2.brain.Save()
   


if __name__ == '__main__':
    main()