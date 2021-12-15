import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
surface = tk.Frame()
surface.master.title("Hello PNC")
canvas = tk.Canvas(surface)
import random

colors = ["#FFFF00","#800080","#00FF00","#FF00FF","#0000FF","#FF0000"]
for h in range(10):
    canvas.create_rectangle(30,30+35*h,60,60+35*h, fill=random.choice(colors))
    canvas.create_rectangle(30+35*9,30+35*h,60+35*9,60+35*h, fill=random.choice(colors))
    for w in range(10):
        canvas.create_rectangle(30+35*w,30,60+35*w,60, fill=random.choice(colors))
        canvas.create_rectangle(30+35*w,30+35*9,60+35*w,60+35*9, fill=random.choice(colors))

        if w < 4:
            canvas.create_rectangle(65+70*w,60+5*1,130+70*w,125+5*1,fill=random.choice(colors))
        elif h < 3 and w > 5:
            canvas.create_rectangle(65+70*(w-6),65+70*(h+1),130+70*(w-6),130+70*(h+1),fill=random.choice(colors))    
canvas.pack(expand=True, fill= "both")
surface.pack(expand=True, fill = "both")
surface.mainloop()
