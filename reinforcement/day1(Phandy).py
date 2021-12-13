# # Exercise Start Practice=============
# array1 = eval(input())
# array2 = []
# for num in array1:
#     if num > 50:
#         array2.append(num)
# print(array2)


# # Exercise One================
# number = int(input())
# result = False
# if (number > 1 and number < 10) or (number > 30 and number < 50) or (number < 77 and number > 100):
#     result = True
# print(result)
   

# # Exercise Two================
# array = eval(input())
# result = False
# for num in array:
#     if num < 0:
#         result = True
# print(result)

# # One more==========
# array = eval(input())
# isNotMinus = False
# index = 0
# while not isNotMinus and index < len(array):
#     if array[index] < 0:
#         isMinus = True
#     index += 1
# print(isNotMinus)

# # Exercise Three
# array = eval(input())
# isBetween = True
# index = 0
# while isBetween and index < len(array):
#     if array[index] < 8 or array[index] > 12:
#         isBetween = False
#     index += 1
# print(isBetween)

# # Exercise Four==============
# string = input()
# isNotSign = False
# index = 0
# while not isNotSign and index<len(string):
#     if string[index] == "!":
#         isNotSign = True
#     index += 1
# print(isNotSign)

# # Exercise Five============
# arrayOfNum = eval(input())
# result = "Pass"
# amountNum = len(arrayOfNum)
# sumNum = 0
# average = 0
# for num in arrayOfNum:
#     sumNum += num
#     average = sumNum/amountNum
# if average < 50:
#     result = "Fail"
# print(result)


# # Exercise Six============
# arrayOfBoolean = eval(input())
# numberOfBooleanTrue = 0
# for boolean in arrayOfBoolean:
#     if boolean == True:
#         numberOfBooleanTrue += 1
# print(numberOfBooleanTrue)

# # Exercise Seven=============
# number = int(input())
# stringOfNum = ""
# betweenNum = 0
# for num in range(0,number+1,2):
#     stringOfNum += str(num) + " "
# print(stringOfNum)

# # =============================================================

firstArrayOfInteger = eval(input())
secondArrayOfInteger = eval(input())
sumOfFirstArray = 0
sumOfSecondArray = 0
for num in firstArrayOfInteger:
    sumOfFirstArray += num
print(sumOfFirstArray)