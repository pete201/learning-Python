from tkinter import *

class GUI_ttt(Frame):
    '''GUI implimentation or Tic-Tac-Toe'''
    def __init__(self, master) -> None:
        super(GUI_ttt, self).__init__(master)
        self.grid()
        self.buttons = []
        self.create_widgets()
        
    def button_press(self, btn):
        print(f'button pressed {btn}')



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

    myGUI = GUI_ttt(root)

    root.mainloop()




if __name__ == '__main__':
    main()