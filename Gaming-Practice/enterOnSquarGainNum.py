import tkinter as tk
grid = tk.Tk()
grid.geometry("600x600")
fByf = tk.Frame()
fByf.master.title("Hello PNC")
canvas = tk.Canvas(fByf)

def enterOnSquare(event):
    canvas.create_text(50,50,text="countAmountOfEnter",font="Porisal, 30")
canvas.create_rectangle(100,150,200,250,fill="#FF0000",tags = 'enterOnSquare')
canvas.tag_bind("enterOnSquare","<Button-1>",enterOnSquare)



canvas.pack(expand=True, fill= "both")
fByf.pack(expand=True, fill = "both")
grid.mainloop()