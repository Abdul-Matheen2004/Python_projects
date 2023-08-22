from functools import partial
import tkinter as tk
import re
window = tk.Tk()
labeles= ['C', '1','4','7','','CE','2','5','8','0','+/-','3','6','9','.','/','*','+','-','=']
count = 0
numOfClicks = 0
radio = 0
def inserting(position):
    global numOfClicks
    global radio
    numOfClicks+=1
    match labeles[position]:
        case "CE":
            numOfClicks = 0
            inp.delete(0, tk.END)
            return
        case "C":
            numOfClicks-=2
            inp.delete(numOfClicks, tk.END)
            return
        case "+/-":
            if radio == 0:
                radio = 1
                inp.insert(0, "-")
            elif radio == 1:
                radio = 0
                inp.delete(0, 1)
            return
        case "=":
            culcution()
            return
    inp.insert(numOfClicks, labeles[position]) 

    
def culcution():
    raw = inp.get()
    verification = 0
    pattern = r'[\+\-\*\/]+'
    saparation = re.split(pattern,raw)
    for i in range(len(saparation)):
        if saparation[i].isdigit() == True:
            verification = 0
        else:
            verification = 1
    if verification == 0:
        inp.delete(0, tk.END)
        inp.insert(0,eval(raw))
    else:
        inp.delete(0, tk.END)
        inp.insert(0,"enter number")

table = tk.Frame()
inp = tk.Entry(master=window, width=30)
inp.pack()
for i in range(4):
    for j in range(5):
        frame = tk.Frame(master=table, borderwidth=1)
        frame.grid (column=i, row=j, padx=3, pady=3)
        position = labeles[count]
        label = tk.Button(master=frame, text=(position) ,pady=10 ,padx=10, command=partial(inserting, count))
        count += 1
        label.pack()
table.pack()
window.mainloop()