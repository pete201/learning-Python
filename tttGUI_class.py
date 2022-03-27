# class to hold tic tac toe board

from tkinter import *

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


    def ResetGame(self):
        #global available
        self.available = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        #global selectedMoves
        self.selectedMoves = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        #global gameMoves                        # remembers move sequence of the game
        self.gameMoves = []


    def button_press(self, btn):
        #print(f'button pressed {btn}')
        #print(self.buttons[btn-1])
        # update the text on button when button is pressed.
        #self.buttons[btn-1].config(text='newtext')
        self.buttons[btn-1]['text']='newtext'

        # play HUMAN turn
            #check if tile is vaccant
            # update btn txt wit HUMAN character
            # check if win
            # get COMPUTER move
            # update btn with COMUTER  char
            # check win


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
                self.buttons.append(Button(self, text=f'button {r},{c}', width=14, height=6, bg="blue", fg="yellow", relief=GROOVE, command=lambda x=count: self.button_press(x)))
                self.buttons[-1].grid(row=r+1, column=c)
                #self.buttons[-1].bind('<Button-1>', self.button_press())



def main():
    root = Tk()
    root.title('Tic-Tac-Toe')

    myGUI = tttGUI(root)

    root.mainloop()




if __name__ == '__main__':
    main()