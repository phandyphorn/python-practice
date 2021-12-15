import tkinter as tk
root = tk.Tk()
root.geometry("600x600")
surface = tk.Frame()
surface.master.title("Hello PNC")
canvas = tk.Canvas(surface)
import random

colors = ["#FFFF00","#800080","#00FF00","#FF00FF","#0000FF","#FF0000"]
for h in range(10):
    for w in range(10):
        canvas.create_rectangle(30+35*w,60+35*h,60+35*w,90+35*h, fill=random.choice(colors))
canvas.pack(expand=True, fill= "both")
surface.pack(expand=True, fill = "both")
surface.mainloop()
