# class to hold tic tac toe board

from tkinter import *

class tttGUI(Frame):
    '''GUI implimentation or Tic-Tac-Toe'''
    def __init__(self, master) -> None:
        super(tttGUI, self).__init__(master)
        self.grid()
        self.buttons = []
        self.create_widgets()
        
    def button_press(self, btn):
        #print(f'button pressed {btn}')
        #print(self.buttons[btn-1])
        # update the text on button when button is pressed.
        self.buttons[btn-1].config(text='newtext')


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