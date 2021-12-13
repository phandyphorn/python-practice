# Exercise One==============================
# number = int(input())
# result = "NOT BETWEEN"
# if number >=1 and number <= 10 or number >= 30 and number <= 50 or number >=70 and number <= 100:
#     result = "BETWEEN"
# print(result)

# Exercise Two===============================
# password = input()
# isTheSame = False
# result = ""
# while not isTheSame:
#     stringToTypePw = input()
#     if stringToTypePw == password:
#         result = "Password confirmed"
#         isTheSame = True
#     else:
#         result = "Password don't match"
#         issubclass = False
#     print(result)

# Exercise Three============================
# isBanana = True
# arrayOfFruit = []
# index = 0
# while index < 5 and isBanana:
#     fruitName = input()
#     if fruitName == "Banana":
#         arrayOfFruit.append(fruitName)
#         isBanana = False
#     else:
#         arrayOfFruit.append(fruitName)
#     index +=1
# print(arrayOfFruit)

# Exercise Four==========================
# oldString= input()
# newString = ""
# isNotSOrD = True
# char = 0
# while char < len(oldString):
#     if (oldString[char] == "'" or oldString[char] == '"') and isNotSOrD:
#         isNotSOrD = False
#     elif (oldString[char] == "'" or oldString[char] == '"') and not isNotSOrD:
#         isNotSOrD = True
#     elif isNotSOrD:
#         newString += oldString[char]
#     char += 1
# print(newString)
    

# Exercise One========================
# allGoodThings = 0
# eachGoodThings = 0
# materials = [{'name':'Computer','quantity':20,'retail_price':400,'quality':'Good'},
# {'name':'Computer','quantity':10,'retail_price':200,'quality':'Not good'},
# {'name':'Monitor','quantity':20,'retail_price':1000,'quality':'Not good'},
# {'name':'Keyboard','quantity':10,'retail_price':150,'quality':'Good'},
# {'name':'Speaker','quantity':5,'retail_price':50,'quality':'Good'}]
# for key in materials:
#     if key["quality"] == "Good":
#         eachGoodThings += key["retail_price"] * key["quantity"]
# allGoodThings += eachGoodThings
# print(allGoodThings)

# Exercise Two===================
# array2D = eval(input())
# result = False
# for row in range(len(array2D)):
#     for col in range(len(array2D[row])):
#         if array2D[row][col] != array2D[row-1][col] or array2D[row][col] != array2D[row][col-1]:
#             result = True
# print(result)

# Exercise Two Use Function============
# def numberInRowOfA(array2D):
#     for row in range(len(array2D)):
#         storageNum = []
#         for col in range(len(array2D[row])):
#             if array2D[row][col] in storageNum:
#                 return False
#             else:
#                 storageNum.append(array2D[row][col])
#     return True

# def numberInColOfA(array2D):
#     for row in range(len(array2D)):
#         storageNum = []
#         for col in range(len(array2D[row])):
#             if array2D[col][row] in storageNum:
#                 return False
#             else:
#                 storageNum.append(array2D[col][row])
#     return True
# array2D = eval(input())
# result = False
# if numberInRowOfA(array2D) and numberInColOfA(array2D):
#     result = True
# print(result)




# Exercise Three===============
# arrayDictionary = eval(input())
# studentClass = input()
# minScore = 100
# result = ''
# for key in arrayDictionary:
#     if key["class"] == studentClass and minScore > key['score']:
#         minScore = key["score"]
#         result = key['name']
# print(result)
        
        






