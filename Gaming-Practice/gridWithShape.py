import tkinter as tk
grid = tk.Tk()
grid.geometry("600x600")
fByf = tk.Frame()
fByf.master.title("Hello PNC")
canvas = tk.Canvas(fByf)

for x in range(100):
    canvas.create_rectangle(0+11*x,0,10+11*x,10)
    # if x % 2 == 0:
    #     canvas.create_rectangle(0+11*x,0,10+11*x,10,fill="#000FFF")
for y in range(100):
    canvas.create_rectangle(0,0+11*y,10,10+11*y)
canvas.pack(expand=True, fill= "both")
fByf.pack(expand=True, fill = "both")
fByf.mainloop()
