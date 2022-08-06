from re import I
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
root.geometry('600x400+650+300')
root.resizable(False, False)
root.title('Time Counter')
start_time = time.time()

data = open("results.txt", "w")
data.write("")
data.close

i=1


def pressed(event):
    global i

    print("Passed time: " + str("%.2f" % (time.time()-start_time)))
    data = open("results.txt", "a")
    data.write(str(i) + " " + "%.2f" % (time.time()-start_time) + "\n")

    i += 1


button_1 = ttk.Button(root, text='1', command=lambda: pressed(0))
button_1.bind('<KeyPress-c>', pressed)

button_1.focus()
button_1.pack(expand=True)


root.mainloop()
data.close
