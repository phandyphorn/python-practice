points = []
# def drawCicle():
#     points.append(5)
#     points.append(10)
#     print(points)
# drawCicle()

# Use Global a (a nov kang krov)
# a = 0
# def myFunction():
#     print(a)
# myFunction()

# # Use Local a
# a = 0
# def myFunction():
#     a = 5
#     print(a)
# myFunction()
# print(a)

# We can knonea global
a = 5
def myFunction():
    global a
    a += 5
    print(a)
myFunction()
print(a)