import tkinter
from tkinter import messagebox
from AlphaBeta import alpha_beta_rac
from Node import Node
import sys


choice = 'x'
root = Node(choice)
buttons = [[None, None, None],[None, None, None],[None, None, None]]

def checker(btn, x, y):
    if(btn['text'] != ' '):
        return
    global root
    btn['text'] = choice.upper()
    root.grid[x][y] = choice
    root.generate_tree()
    succ = alpha_beta_rac(root, 'max')
    for i in succ.grid:
        print(i)
    for i in range(0,3):
        for j in range(0,3):
            if(succ.grid[i][j] and buttons[i][j]['text'] == ' '):
                buttons[i][j]['text'] = succ.grid[i][j].upper()
    root = succ
    root.level = root.inverse_level()
    root.XorO = root.inverse_XorO()
    if root.check_win():
        messagebox.showinfo('Results', 'You win')
        sys.exit()
    elif root.check_win(root.inverse_XorO()):
        messagebox.showinfo('Results', 'You lost')
        sys.exit()
    elif root.nb_none() == 0:
        messagebox.showinfo('Results', "It's a tie")
        sys.exit()    

def gui_builder():
    window = tkinter.Tk()
    window.title('Tic Tac Toe')
    window.resizable(False, False)

    buttons[0][0] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[0][0],0,0)})
    buttons[0][0].grid({'row': '0', 'column': '0', 'sticky': 'NSEW', 'in': window})

    buttons[0][1] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[0][1],0,1)})
    buttons[0][1].grid({'row': '0', 'column': '1', 'sticky': 'NSEW', 'in': window})

    buttons[0][2] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[0][2],0,2)})
    buttons[0][2].grid({'row': '0', 'column': '2', 'sticky': 'NSEW', 'in': window})
    
    buttons[1][0] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[1][0],1,0)})
    buttons[1][0].grid({'row': '1', 'column': '0', 'sticky': 'NSEW', 'in': window})

    buttons[1][1] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[1][1],1,1)})
    buttons[1][1].grid({'row': '1', 'column': '1', 'sticky': 'NSEW', 'in': window})

    buttons[1][2] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[1][2],1,2)})
    buttons[1][2].grid({'row': '1', 'column': '2', 'sticky': 'NSEW', 'in': window})

    buttons[2][0] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[2][0],2,0)})
    buttons[2][0].grid({'row': '2', 'column': '0', 'sticky': 'NSEW', 'in': window})

    buttons[2][1] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[2][1],2,1)})
    buttons[2][1].grid({'row': '2', 'column': '1', 'sticky': 'NSEW', 'in': window})

    buttons[2][2] = tkinter.Button(window, {'text': ' ', 'height': '4', 'width': '8', 'font': '10', 'command': lambda: checker(buttons[2][2],2,2)})
    buttons[2][2].grid({'row': '2', 'column': '2', 'sticky': 'NSEW', 'in': window})

    window.mainloop()

if __name__ == "__main__":
    gui_builder()