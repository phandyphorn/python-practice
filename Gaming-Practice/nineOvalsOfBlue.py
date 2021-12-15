import tkinter as tk
grid = tk.Tk()
grid.geometry("600x600")
fByf = tk.Frame()
fByf.master.title("Hello PNC")
canvas = tk.Canvas(fByf)
def changeColorToRed(event):
    oval = canvas.create_oval(50+55*i,50,100+55*i,100,fill="red",tags="ovals")

def changeColorToYellow(event):
    oval = canvas.create_oval(50+55*i,50,100+55*i,100,fill="yellow",tags="ovals")

for i in range(9):
    canvas.create_oval(50+55*i,50,100+55*i,100,fill="blue",tags="ovals")

canvas.tag_bind("ovals","<Button-1>",changeColorToRed)
canvas.tag_bind("ovals","<Button-1>",changeColorToYellow)

canvas.pack(expand=True, fill= "both")
fByf.pack(expand=True, fill = "both")
grid.mainloop()

