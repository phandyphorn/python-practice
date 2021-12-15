import tkinter as tk
grid = tk.Tk()
grid.geometry("600x600")
fByf = tk.Frame()
fByf.master.title("Hello PNC")
canvas = tk.Canvas(fByf)
import random

def myEventTrigger(event):
    print("User have clicked at position: ", event.x, event.y)
    randomColor = random.choice(colors)
    canvas.itemconfig(oval, fill = randomColor)
    canvas.move(oval, 10,10)
canvas = tk.Canvas(fByf)
colors = ["#00FFFF","#0000FF","#FFFF00","#FF00FF","#800080"]
oval = canvas.create_oval(50,50,300,300,fill="red",tags = "PNCTarget")
canvas.tag_bind("PNCTarget","<Button-1>",myEventTrigger)

canvas.pack(expand=True, fill= "both")
fByf.pack(expand=True, fill = "both")
grid.mainloop()