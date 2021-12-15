
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
    centerOfCircle = random.randrange(20,300)
    # when we put event.anything it will clear at those point and those point is the position of the mouse.
    x1= event.x-centerOfCircle
    y1 = event.y-centerOfCircle
    x2= event.x+centerOfCircle
    y2 = event.y+centerOfCircle
    canvas.create_oval(x1,y1,x2,y2, fill = randomColor)

colors = ["#FFFF00","#00FF00","#FF00FF","#0000FF","#FF0000"]

root.bind('<Button-1>',drawCircle)
canvas.pack(expand=True, fill= "both")
frame.pack(expand=True, fill = "both")
root.mainloop()