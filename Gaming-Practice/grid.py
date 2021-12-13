import tkinter as tk
grid = tk.Tk()
grid.geometry("600x600")
fByf = tk.Frame()
fByf.master.title("Hello PNC")
canvas = tk.Canvas(fByf)
array2D = [[0,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,1,1]]
for row in range(len(array2D)):
    for num in range(len(array2D[row])):
        if array2D[row][num] == 1:
            canvas.create_rectangle(20+31*num,50+31*row,50+31*num,80+31*row,fill="#00FF00")   
        elif array2D[row][num] == 0:
            canvas.create_rectangle(20+31*num,50+31*row,50+31*num,80+31*row,fill="#FFFFFF")
canvas.pack(expand=True, fill= "both")
fByf.pack(expand=True, fill = "both")
fByf.mainloop()
