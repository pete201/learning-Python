# class to hold tic tac toe board

from tkinter import *
from Brain_class import Brain 
from random import choice


class tttGUI(Frame):
    '''GUI implementation of Tic-Tac-Toe'''
    def __init__(self, master) -> None:
        super(tttGUI, self).__init__(master)
        self.grid()
        self.buttons = []
        self.create_widgets()

        self.available = []
        self.selectedMoves = []
        self.gameMoves = []
        self.ResetGame()

        goFirst = False     # this allows HUMAN to go first
        # switch player
        self.HUMAN, self.COMPUTER, self.player, goFirst = self.switchPlayer(goFirst)

        # set up a learning brain
        self.p1 = Brain('player1')                       # set up a player p1 for AI, nicname (filename)= 'player1'

    def ResetGame(self):
        #global available
        self.available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        #global selectedMoves
        self.selectedMoves = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        #global gameMoves                        # remembers move sequence of the game
        self.gameMoves = []
        #TODO assign buttons to respond to clicks


    def switchPlayer(self, goFirst):
        first = not goFirst
            
        if first == True:
            HUMAN = 'O'
            COMPUTER = 'X'
            player = 'HUMAN'
        else:
            HUMAN = 'X'
            COMPUTER = 'O'
            player = 'COMPUTER'
            
        return HUMAN, COMPUTER, player, first

    
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


    def button_press(self, btn):
        print(f'button pressed {btn}')
        # update the text on button when button is pressed.  use btn-1 since array index is 0-8 and btn numbers are 1-9 (to maintain Brain functionality)

        # play HUMAN turn
        #check if tile is vaccant
        if self.buttons[btn-1]['text'] != '':
            # if button has text then return without doing anything
            return      
        else:
            # update available and game arrays
            self.gameMoves.append(str(btn))
            self.available.remove(str(btn))

            self.selectedMoves[btn-1] = self.HUMAN 

            # update btn txt wit HUMAN character
            self.buttons[btn-1]['text'] = self.HUMAN
            
            # check if win
            gameOver = self.checkWinner()   # checkWinner returns TRUE if last move was a winning move
            if  gameOver:
                winner = True

                print('HUMAN won')
                #TODO GameOver: assign buttons to do nothing if clicked
                #TODO GameOver: update game stats file e.g. player.csv
                return
            else:
                print(f'no winner yet, gameMoves: {self.gameMoves} , and selectedMoves: {self.selectedMoves} ')
                #play COMPUTER turn
                # get suggested move from Brain
                select = self.p1.SuggestMove(self.gameMoves)
                print(type(select))
                # check we have found an available tile
                #if select not in self.available:
                    #get a random square from avaialable
                    #select = choice(self.available)

                self.gameMoves.append(select)
                self.available.remove(select)

                self.selectedMoves[int(select)-1] = self.COMPUTER
                # update btn with COMPUTER  char
                self.buttons[int(select)-1]['text'] = self.COMPUTER
                # check if win
                gameOver = self.checkWinner()   # checkWinner returns TRUE if last move was a winning move
                if  gameOver:
                    winner = True
                    print('COMPUTER won')
                    #TODO GameOver: assign buttons to do nothing if clicked
                    #TODO GameOver: update game stats file e.g. player.csv
                    return

            #if WINNER
                #learn game moves 
                #NOTE i could learn moves when window is closed - back in main prog.
                #TODO this version throws an error on a draw!!


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
                #self.buttons.append(Button(self, text=f'button {r},{c}', width=14, height=6, bg="blue", fg="yellow", relief=GROOVE, command=lambda x=count: self.button_press(x)))
                self.buttons.append(Button(self, text='', width=14, height=6, bg="blue", fg="yellow", relief=GROOVE, command=lambda x=count: self.button_press(x)))
                self.buttons[-1].grid(row=r+1, column=c)
                #self.buttons[-1].bind('<Button-1>', self.button_press())



def main():
    root = Tk()
    root.title('Tic-Tac-Toe')

    myGUI = tttGUI(root)

    root.mainloop()




if __name__ == '__main__':
    main()