# # Exercise One==========
# oldArray = eval(input())
# newArrayStoreNumBetweenOneAndZero = []
# isNumberOne = False
# isNumberOneBeforeZero = True
# index = 0
# while index < len(oldArray) and isNumberOneBeforeZero:
#     if isNumberOne and oldArray[index] != 0:
#         newArrayStoreNumBetweenOneAndZero.append(oldArray[index]) 
#     if oldArray[index]==1:
#         isNumberOne = True
#     if isNumberOne and oldArray[index] == 0:
#         isNumberOneBeforeZero = False
#     index += 1
# if isNumberOneBeforeZero:
#     newArrayStoreNumBetweenOneAndZero = []
# print(newArrayStoreNumBetweenOneAndZero)


# One More Way:
# array=eval(input())
# start=True
# end=False
# index=0
# newArray=[]
# for i in range(len(array)):
#     if array[i]==1 and start:
#         for j in range(i+1,len(array)):
#             if array[j]!=0:
#                 newArray.append(array[j])
#             else:
#                 index+=1
#                 start=False
# if index==0:
#     newArray=[]
# print(newArray)

# Exercise Two================
# text = input()
# isNotContainLetterAOrBOrCOrD = False
# for char in range(len(text)):
#     if text[char] == "A" or text[char] == "a" or text[char] == "B" or text[char] == "b" or text[char] == "C" or text[char] == "c" or text[char] == "D" or text[char] == "d":
#         isNotContainLetterAOrBOrCOrD = True
# print(isNotContainLetterAOrBOrCOrD)


# Exercise Three=============
# arrayOfNum = []
# for num in range(3):
#     number = int(input())
#     if number >= 10 and number <= 50:
#         arrayOfNum.append(number)
# print(arrayOfNum)


# Exercise Four================
# text = input()
# newText = ""
# for char in range(len(text)):
#     if text[char-1] == " " or char == 0:
#         newText += text[char].upper()
#     else:
#         newText += text[char]
# print(newText)




# Exercise One========================
allGoodThings = 0
eachGoodThings = 0
materials = [{'name':'Computer','quantity':20,'retail_price':400,'quality':'Good'},
{'name':'Computer','quantity':10,'retail_price':200,'quality':'Not good'},
{'name':'Monitor','quantity':20,'retail_price':1000,'quality':'Not good'},
{'name':'Keyboard','quantity':10,'retail_price':150,'quality':'Good'},
{'name':'Speaker','quantity':5,'retail_price':50,'quality':'Good'}]
for key in materials:
    if key["quality"] == "Good":
        eachGoodThings += key["retail_price"] * key["quantity"]
allGoodThings += eachGoodThings
print(allGoodThings)

# Exercise Two===================
array2D = eval(input())
result = False
for row in range(len(array2D)):
    for col in range(len(array2D[row])):
        if array2D[row][col] != array2D[row-1][col] or array2D[row][col] != array2D[row][col-1]:
            result = True
print(result)


# Exercise Three===============
arrayDictionary = eval(input())
studentClass = input()
minScore = 100
result = ''
for key in arrayDictionary:
    if key["class"] == studentClass and minScore > key['score']:
        minScore = key["score"]
        result = key['name']
print(result)
        
        





