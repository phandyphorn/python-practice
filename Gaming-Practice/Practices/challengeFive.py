
# import to use function
import tkinter as tk
root = tk.Tk()
root.geometry("300x300")
frame = tk.Frame()
frame.master.title("Hello PNC")
canvas = tk.Canvas(frame)
# import to use random
import random

pointsToMakeShape = []
def makePoint(event):
    global pointsToMakeShape
    x = event.x
    y = event.y
    canvas.create_oval(x+5,y+5,x-5,y-5,tags="delete-point")
    pointsToMakeShape.append(x)
    pointsToMakeShape.append(y)
root.bind('<Button-1>',makePoint)

def makePolygon(event):
    global pointsToMakeShape
    colors = ["#FFFF00","#00FF00","#FF00FF","#0000FF","#FF0000"]
    color = random.choice(colors)  
    canvas.create_polygon(pointsToMakeShape,fill=color)
    canvas.delete("delete-point")
    pointsToMakeShape = []
root.bind('<Button-3>',makePolygon)

canvas.pack(expand=True, fill= "both")
frame.pack(expand=True, fill = "both")
root.mainloop()