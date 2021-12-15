import tkinter as tk
grid = tk.Tk()
grid.geometry("600x600")
fByf = tk.Frame()
fByf.master.title("Hello PNC")
canvas = tk.Canvas(fByf)




canvas.pack(expand=True, fill= "both")
fByf.pack(expand=True, fill = "both")
grid.mainloop()