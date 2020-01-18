import tkinter
from tkinter import messagebox
queue = 'X'

def info():
    text = 'xzGame a free Tic-Tac-Toe game'
    text += '\nVersion 1.0'
    text += '\nAuthor: Ilyosiddin Kalandar'
    text += '\nContact: ilyosiddin_kalandar@mail.ru'
    messagebox.showinfo('Info about xzGame',text)

def reset_board():
    global buttons
    for i in range(9):
        buttons[i]['text'] = ''
    
def check_board():
    # board is full?
    global buttons
    is_full = False
    for i in buttons:
        if i['text']:
            is_full = True
        else:
            is_full = False
            break
    if is_full:
        messagebox.showinfo('Board is full!','Your board is full,board has been reset!')
        reset_board()
    else:
        # check first line
        if buttons[0]['text'] == buttons[1]['text'] == buttons[2]['text']:
            if buttons[0]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[0]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
        elif buttons[3]['text'] == buttons[4]['text'] == buttons[5]['text']:
            if buttons[3]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[3]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
        elif buttons[6]['text'] == buttons[7]['text'] == buttons[8]['text']:
            if buttons[6]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[6]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
        elif buttons[0]['text'] == buttons[3]['text'] == buttons[6]['text']:
            if buttons[0]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[0]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
        elif buttons[1]['text'] == buttons[4]['text'] == buttons[7]['text']:
            if buttons[1]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[1]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
        elif buttons[2]['text'] == buttons[5]['text'] == buttons[8]['text']:
            if buttons[2]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[2]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
        elif buttons[0]['text'] == buttons[4]['text'] == buttons[8]['text']:
            if buttons[0]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[0]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
        elif buttons[2]['text'] == buttons[4]['text'] == buttons[6]['text']:
            if buttons[2]['text'] == 'X':
                messagebox.showinfo('xzGame','First player is win!')
                reset_board()
            elif buttons[2]['text'] == 'O':
                messagebox.showinfo('xzGame','Second player is win!')
                reset_board()
                
def click_button0():
    global queue
    if not buttons[0]['text']:
        buttons[0]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
        
def click_button1():
    global queue
    if not buttons[1]['text']:
        buttons[1]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
def click_button2():
    global queue
    if not buttons[2]['text']:
        buttons[2]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
    
def click_button3():
    global queue
    if not buttons[3]['text']:
        buttons[3]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
    
def click_button4():
    global queue
    if not buttons[4]['text']:
        buttons[4]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
    
def click_button5():
    global queue
    if not buttons[5]['text']:
        buttons[5]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
         messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
def click_button6():
    global queue
    if not buttons[6]['text']:
        buttons[6]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
    
def click_button7():
    global queue
    if not buttons[7]['text']:
        buttons[7]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()
    
def click_button8():
    global queue
    if not buttons[8]['text']:
        buttons[8]['text'] = queue
        if queue == 'X':
            queue = 'O'
        else:
            queue = 'X'
    else:
        messagebox.showerror('Error!','You are stupid? Can\'t move to this position!')
    check_board()

root = tkinter.Tk()
root.title('xzGame')
root.geometry('340x400+450+75')
root.resizable(False,False)
buttons = [tkinter.Button(text = '',font = 'Verdana 15',width = 8,height = 4) for i in range(9) ]

# initialiaze buttons

#First line of buttons
buttons[0].place(x = 0,y = 0)
buttons[0]['command'] = click_button0
buttons[1].place(x = 113,y = 0)
buttons[1]['command'] = click_button1
buttons[2].place(x = 226,y = 0)
buttons[2]['command'] = click_button2

# second line of buttons
buttons[3].place(x = 0,y = 117)
buttons[3]['command'] = click_button3
buttons[4].place(x = 113,y = 117)
buttons[4]['command'] = click_button4
buttons[5].place(x = 226,y = 117)
buttons[5]['command'] = click_button5

#third line of buttons
buttons[6].place(x = 0,y = 234)
buttons[6]['command'] = click_button6
buttons[7].place(x = 113,y = 234)
buttons[7]['command'] = click_button7
buttons[8].place(x = 226,y = 234)
buttons[8]['command'] = click_button8

super_buttons = [
    tkinter.Button(text = 'Info',font = 'Arial 15',width = 8,command = info),
    tkinter.Button(text = 'Reset',font = 'Arial 15',command=reset_board),
    tkinter.Button(text = 'Exit',font = 'Arial 15',command = exit)
]

super_buttons[0].place(x = 10,y = 355)
super_buttons[1].place(x = 135,y = 355)
super_buttons[2].place(x = 250,y = 355)

root.mainloop()
