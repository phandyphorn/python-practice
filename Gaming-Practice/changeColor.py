import tkinter as tk
grid = tk.Tk()
grid.geometry("600x600")
fByf = tk.Frame()
fByf.master.title("Hello PNC")
canvas = tk.Canvas(fByf)

def changeColorToYellow(event):
    print('Key pressed: ', event.char)
    oval = canvas.create_oval(50,50,300,300,fill="red",tags= "shape")
def changeColorToRed(event):
    oval = canvas.create_oval(50,50,300,300,fill="yellow",tags = "shape")

canvas.create_oval(50,50,300,300,fill="red",tags = "shape")

# Mouse Event
# left is Button-1
canvas.tag_bind("shape","<Button-1>",changeColorToYellow)
# right is Button-3
canvas.tag_bind("shape","<Button-3>",changeColorToRed)


# Keyboard Event
grid.bind('<Key>',changeColorToRed)
grid.bind('<Up>',changeColorToYellow)

canvas.pack(expand=True, fill= "both")
fByf.pack(expand=True, fill = "both")
grid.mainloop()
