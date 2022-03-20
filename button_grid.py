import tkinter as tk

def button_press(btnnum):
    #btn['text'] ="press"
    print(f'key pressed {btnnum}')

window = tk.Tk()    # create a tkinter window
# button_number=0
# button_array = [None] * 9   #this creates a list of 9 elements that will become the 9 buttons
# for i in range(3):
    
#     for j in range(3):
#         button_number += 1
#         frame = tk.Frame(master=window)
#         frame.grid(row=i, column=j)
#         #btn = tk.Button(master=frame, text=f"Row {i}\nCol {j}\nNum {button_number}", command=lambda: button_press(button_number))
#         button_array[button_number-1] = tk.Button(master=frame, text=f"Row {i}\nCol {j}\nNum {button_number}", command=lambda: button_press(str(button_number)))
#         button_array[button_number-1].pack()
#         #window.bind('<Button-1>', button_press)

window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)
frame = tk.Frame(master=window)
button1 = tk.Button(master=frame, text="1", command=lambda: button_press(1))
button1.grid(row=0, column=0)
button2 = tk.Button(master=frame, text="2", command=lambda: button_press(2))
button1.grid(row=1, column=2)
button3 = tk.Button(master=frame, text="3", command=lambda: button_press(3))
button1.grid(row=1, column=3)
button4 = tk.Button(master=frame, text="4", command=lambda: button_press(4))
button1.grid(row=2, column=1)
button5 = tk.Button(master=frame, text="5", command=lambda: button_press(5))
button1.grid(row=2, column=2)
button6 = tk.Button(master=frame, text="6", command=lambda: button_press(6))
button1.grid(row=2, column=3)
# button7 = tk.Button(master=frame, text="7", command=lambda: button_press(7))
# button8 = tk.Button(master=frame, text="8", command=lambda: button_press(8))
# button9 = tk.Button(master=frame, text="9", command=lambda: button_press(9))




window.mainloop()
exit()      # this closes the tk window

