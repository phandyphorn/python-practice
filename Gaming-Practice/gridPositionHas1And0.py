import tkinter as tk
root = tk.Tk()
root.geometry("300x300")
frame = tk.Frame()
frame.master.title("Hello PNC Appear Circle")
canvas = tk.Canvas(frame)

#==================== Step One
# function to make those grid:

# def arrayToPaintColorOnOnePosition():
#     global arrayAsGrid
#     for num in range(len(arrayAsGrid)):
#         if arrayAsGrid[num] == 1:
#             canvas.create_rectangle(20+40*num,60,60+40*num,100, fill="black")
#         elif arrayAsGrid[num] == 0:
#             canvas.create_rectangle(20+40*num,60,60+40*num,100,fill = "white")
# arrayAsGrid = [0,0,1,0,0,0]
# arrayToPaintColorOnOnePosition()

# ======================One more way:
arrayOfIntegers = [0,0,1,0,0]
def arrayToPaintColorOnOnePosition():
    global arrayAsGrid
    x1 = 20
    y1 = 60
    x2 = 60
    y2 = 100
    for i in range(len(arrayOfIntegers)):
        if arrayOfIntegers[i] == 1:
            canvas.create_rectangle(x1,y1,x2,y2,fill="black")
        elif arrayOfIntegers[i] == 0:
            canvas.create_rectangle(x1,y1,x2,y2,fill="white")
        x1 += 40
        x2 += 40
arrayToPaintColorOnOnePosition()

# ==================== Step Two
# Function to move when key are R and L.

def getIndexOf1(arrayOfIntegers):
    for index in range(len(arrayOfIntegers)):
        if arrayOfIntegers[index] == 1:
            indexOf1 = index
    return indexOf1

def moveToRight(event):
    onePosition = getIndexOf1(arrayOfIntegers)
    if onePosition < (len(arrayOfIntegers)-1) and arrayOfIntegers[onePosition] == 1:
        arrayOfIntegers[onePosition] = 0
        arrayOfIntegers[onePosition+1] = 1
    print(arrayOfIntegers)
    arrayToPaintColorOnOnePosition()

def moveToLeft(event):
    position = getIndexOf1(arrayOfIntegers)
    if position > 0 and arrayOfIntegers[position] == 1:
        arrayOfIntegers[position] = 0
        arrayOfIntegers[position-1] = 1
    print(arrayOfIntegers)
    arrayToPaintColorOnOnePosition()

root.bind("<r>", moveToRight)    
root.bind("<l>", moveToLeft)


canvas.pack(expand=True, fill= "both")
frame.pack(expand=True, fill = "both")
root.mainloop()