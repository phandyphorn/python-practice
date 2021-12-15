# import to use function
import tkinter as tk
root = tk.Tk()
root.geometry("300x300")
frame = tk.Frame()
frame.master.title("Hello PNC Appear Circle")
canvas = tk.Canvas(frame)
# import to use random
import random
def drawCircle(event):
    randomColor = random.choice(colors)
    # we get random at the end of 300 because the size of this window is max in 300
    x1 = random.randrange(1,300)
    y1 = random.randrange(1,300)
    size = random.randrange(20,80)
    x2 = x1 + size
    y2 = y1 + size
    canvas.create_oval(x1,y1,x2,y2, fill = randomColor)

colors = ["#FFFF00","#00FF00","#FF00FF","#0000FF","#FF0000"]
root.bind('<Button-1>',drawCircle)
canvas.pack(expand=True, fill= "both")
frame.pack(expand=True, fill = "both")
root.mainloop()
