#=====================================Array Lesson ===================
# ===>1
from abc import abstractproperty


array = [1,2,3,4]
for value in array:
    print(value,end=" ")


# ===>2
array = eval(input("Enter Value To Array: "))
for value in array:
    print(value)

# ===>3
array = eval(input("Enter Number: "))
print(array[0])

# ===>4
array = eval(input("Enter Array: "))
print([1][0])

# ===>5
array = ["phandy",20]
print(array[0])

# ===>6
array = [1,2,3,4,"phandy"]
for index in range(len(array)):
    value = array[index]
    print("hello " + str(value))

# ===Or======
array = [1,2,3,4,"sokchan"]
for value in array:
    print("hello " + str(value))

# ===>7
list1 = [2,4,6]
list2 = list1
list1[0] = 99
print(list1[0])
print(list2[0])
# result is the both are 99 because we update the both of them.


# ===>8
a = 5
b = a
a = 7
print(b)
# result is 5 because 7 is a new assign mean that if update it change but if we assign it doesn't change the old value


# ===>9
a = [18,24]
b = a
a[1] = 3
print(b[1])

# ===>10
a = [1,2,3]
b = a
a = [4,5,7]
print(b[0])

# ===>11
a = [1,2,3]
b = [a[0],a[1],a[2]]
a[0] = 7
print(b[0])
# it is assign so it can not change a the above


# ===>12
arrayString = ["ALGORITHM","PYTHON","HTML"]
arrayString.append("JS")
print(arrayString)


# ===>13
text = "RONAN"
arrayText = []
for char in range(len(text)):
    arrayText.append(text[char])
print(arrayText)

# ===>14
fruits = ["apple","banana","mango"]
fruits.insert(1,"orange")
print(fruits)


# ===>15
fruits = ["apple","banana"]
for index in range(5):
    if index % 2 == 1:
        fruits.insert(index ,"papaya " + str(index))
print(fruits)


# ===>16
numbers = [10,20,30]
numbers.pop(1)
print(numbers)


# ===>17
names = ["Phandy","Pheaktey","Keana","Vid"]
otherNames = names
names.pop(3)
print(otherNames)


# ===>18
a = [1,2,3]
b = 4
c = [a,b]
print(c)


# ===>19
a = [1,2,3]
b = [40,50]
c = [a,b]
print(c[0])


# ===>20
a = [0,1,2,3,4,5]
b = a[2:5]
print(b)

# ===>21
array = eval(input("Enter Number: "))
result = []
for value in array:
    if value not in result:
        result.append(value)
print(result)


# ====>22
array = eval(input("Enter Number: "))
newArray = []
for value in array:
    if value == int(value):
        newArray.append(value)
print(newArray)


# ===>23





# ===>24
array = eval(input("Enter word: "))
word = input("Enter: ")
array.append(word)
print(array)


# ===>25
arrayNumbers = eval(input("Enter Num: "))
countSmallToBig = 0
for number in range(1,len(arrayNumbers)):
    if arrayNumbers[number] > arrayNumbers[number-1]:
        countSmallToBig += 1
print(countSmallToBig)


# ===>26
numbers = eval(input("Enter Number: "))
for index in range(len(numbers)):
    if numbers[index] %  2 == 1:
        numbers[index] = 3
print(numbers)

# ===>27
array = [1,3,5,3,5]
for value in array:
    if value == 5:
        array.remove(value)
print(array)


#===>28
list1 = eval(input())
list2 = eval(input())
if len(list1) == len(list2):
    message = "EQUAL"
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            message = "NOT EQUAL"
else:
    message = "NOT EUQAL"
print(message)


#===>29
array = eval(input())
for i in range(len(array)):
    if array[i] < 10:
        array[i] = 10
print(array)

#===>30
numbers=[[1,2,3],[4,5,6],[7,8,9]]
print(numbers[1][1])

# one more way
# column is index of element in main array.
numbers=[
    [1,2,3],  #0 row is index of main array 
    [4,5,6],  
    [7,8,9]
]
print(numbers[1][1]) #numbers([row][column])

#===>31
a = [[1,7,3,4], [5,6,7,8],[9,1,1,1]]
result = ""
for element in a[0]:
    result += str(element) + "-"
print(result)


#===>32
a = [[1,7,3,4],[5,6,7,8],[9,1,1,1]]
result = ""
for value in range(len(a)):
    result += str(a[value][-1]) + "-"
print(result)
#=====================================Function Lesson ================
#===>1
def add10(array):
    array.append(99)
    return array
numbers = [1,2,3]
numbers = add10(add10(numbers))
print(numbers)


#===>2
def square(number):
    return number * number
number = int(input("Enter Number: "))
print(square(number))


#===>3
def addNumbers(number1,number2):
    return number1 + number2
number1 = int(input("Enter Num1: "))
number2 = int(input("Enter Num2: "))
print(addNumbers(number1,number2))


#===>4
def getNumberOfA(text):
    number = 0
    for i in range(len(text)):
        if text[i] == "A":
            number = number + 1
    return number
text = input("Enter Text: ")
print(getNumberOfA(text))


#===>5
# How to call function

def addNumbers(number1,number2):
    return number1 + number2

def banousNumbers(number1,number2):
    return number1 - number2

def muliplyNumbers(number1,number2):
    return number1 * number2

def devideNumbers(number1,number2):
    return number1/number2

number1 = int(input("Enter Number1: "))
number2 = int(input("Enter Number2: "))

print(addNumbers(number1,number2))
print(banousNumbers(number1,number2))
print(muliplyNumbers(number1,number2))
print(devideNumbers(number1,number2))


#===>6
def maxNumber(array):
    maxNumber = array[0]
    for value in array:
        if value > maxNumber:
            maxNumber = value
    return maxNumber
array = eval(input("Enter Number To Array: "))
print(maxNumber(array))


#===>7
array = eval(input("Enter Numbers: "))
def deleltDublicate(array):
    result = []
    for value in array:
        if value not in result:
            result.append(value)
    return result
print(deleltDublicate(array))


#===>8
def theSameArray(list1,list2):
    isNotEqualMustStop = True
    for num in range(len(list1)):
        if list1[num] == list2[num] and isNotEqualMustStop:
            result = "EQUAL"
        else:
            result = "NOT EQUAL"
            isNotEqualMustStop = False
    return result
list1 = eval(input("Enter value: "))
list2 = eval(input("Enter nums: "))
if len(list1) != len(list2):
    result = "NOT EQUAL"
else:
    result = theSameArray(list1,list2)
print(result)


#===>9
def printWelcome(name):
    print("Good Morning " + name + "!")
    print("How are you?")
    print("I really miss you!")
printWelcome ("Smey")  # all name which i write will be the value of name
printWelcome("Nuth")
printWelcome("Houy")
printWelcome("Crush")


#===>10
def fun1(name, age=20):
    print(name, age)
fun1('Emma', 25)

#===>11
def sentence(name,age):
    print(name + " " + age)
sentence("Phandy", "twenty")


#===>12
def addSen(*kids):
    print("The youngest child is " + kids[0])
addSen("Keana","Pheaktey","Phandy")


#===>13
def oddNumber(array):
    for value in array:
        if value % 2 == 1:
            oddNumbers.append(value)
    return oddNumbers
oddNumbers = []
for num in range(5):
    array = eval(input("Enter Number: "))
    result = oddNumber(array)
print(result)


#===>14
def whole(sibling):
    for x in sibling:
        print(x)
sibling = ["Phandy","Pheaktey","Keana"]
c = whole(sibling)

#===>15
def myFunc (n):
    result = 7 * n
    return result
n = int(input("Enter Number: "))
print(myFunc(n))


#===>16
def computMin(number1,number2):
    return min(number1,number2)
a = int(input("Enter Please:"))
b = int(input("Enter Mk :"))
minN = computMin(a,b)
print(minN)


#===>17
def computeMax(number1,number2,number3):
    return max(number1,number2,number3)
a = int(input("Enter :"))
b = int(input("Enter :"))
c = int(input("One more time :"))
maxN = computeMax(a,b,c)
print("The max number is : ",maxN)


#===>18
def sumOfN(start,end):
    sum = 0
    for i in range(start,end+1):
        sum += i
    return sum
start = int(input("Enter Start Number: "))
end = int(input("Enter Start Number: "))
if start > end:
    sum = 0
else:
    sum = sumOfN(start,end)
print(sumOfN(start,end))


#===>19
def numberOfUpperCases(word):
    return countUpperCases
word=input()
countUpperCases=0
for i in word:
    if i >="A" and i<="Z":
        countUpperCases+=1
print(numberOfUpperCases(word))


#===>20
def getComment(grade):
    grade = fGrade + sGrade
    return grade
grade = 0
fGrade = int(input("Enter First Grade: "))
sGrade = int(input("Enter Second Grade: "))
if getComment(grade) >= 10:
    result = "GOOD"
elif getComment(grade)<= 10:
    result = "BAD"
print(result)


#===>21
def reverseString(text1):    
    result = ""
    lastIndex = len(text1) - 1
    for i in range(len(text1)):
        result += text1[lastIndex-i]
    return result
text1 = input("Enter String: ")
print(reverseString(text1))


#===>22
def countSeven(array):
    totalSeven  = 0
    for element in range(len(array)):
        if array[element] == 7:
            totalSeven += 1
    return totalSeven
array = eval(input("Enter Number You Want And Contend 7 To See The Result: "))
print("In this array there are : " + str(countSeven(array)) + " time.")


#===>23
def countSmallToBig(arrayOfNumbers):
    totalOfSmallToBig = 0
    for i in range(1,len(arrayOfNumbers)):
        if arrayOfNumbers[i] > arrayOfNumbers[i-1]:
            totalOfSmallToBig += 1
    return totalOfSmallToBig
arrayOfNumbers = eval(input("Enter Nums: "))
print(countSmallToBig(arrayOfNumbers))


#===>24
def countAInArray(words):
    countA = 0
    for value in words:
        for element in range(len(value)):
            if value[element] == "A" or value[element] == "a":
                countA += 1
    return countA
words = eval(input("Enter Word In Words: "))
print(countAInArray(words))


#===>25
def numberOfEight(array):
    countNumber8 = 0
    for value in array:
        if value == 8:
            countNumber8 += 1
    return countNumber8
array = eval(input("Enter Number: "))
countNumber8 = numberOfEight(array)
if countNumber8 > 0:
    result = countNumber8
else:
    result = "NOT FOUND"
print(result)


#===>26
def sumArray(array):
    result = 0
    for i in range(len(array)):
        result += array[i]
    return result 
array1 = eval(input("Enter num: "))
array2 = eval(input("Enter num: "))
print(sumArray(array1))
print(sumArray(array2))


#===>27
def findValue(array,index):
    result = array[index]
    return result
array = eval(input("Enter value: "))
# array = ["ra","ry"]
index = int(input("Enter Index: "))
print(findValue(array,index))

#==No function==
stringOfArray = eval(input("Enter Here: "))
index = int(input("My Index: "))
print(stringOfArray[index])


#===>28
def countEven(array):
    numberOfEven = 0
    for value in array:
        if value % 2 == 0:
            numberOfEven += 1
    return numberOfEven 
def countOdd(array):
    numberOfOdd = 0
    for value in array:
        if value % 2 == 1:
            numberOfOdd += 1
    return numberOfOdd
array = eval(input("Enter Number: "))
print(countEven(array))
print(countOdd(array))


#===>29
def storeEven(array):
    arrayEven = []
    for value in array:
        if value % 2 == 0:
            arrayEven.append(value)
    return arrayEven
def storeOdd(array):
    arrayOdd = []
    for value in array:
        if value % 2 == 1:
            arrayOdd.append(value)
    return arrayOdd
array = eval(input("Enter Number: "))
print(storeEven(array))
print(storeOdd(array))


#===>30
def ExchangeDollarToKhmer (number):
    resultExchange = number * 4000
    return resultExchange
number = int(input("Enter Number:"))
AfteExchange = ExchangeDollarToKhmer(number)
print(AfteExchange)


#===>31
def rectangleOfX(number):
        rectangle = ""
        for h in range(number):
                for w in range(number):
                        rectangle += "X"
                rectangle += "\n"
        return rectangle
number = int(input("Enter Number: "))
print(rectangleOfX(number))
    

#===>32
def countLetterX(string):
        amountX = 0
        for i in range(len(string)):
                if string[i] == "X":
                        amountX += 1
        return amountX 
string = input("Enter String Mk: ")
print(countLetterX(string))


#===>33
def removeMinuses(word):
    newWord=""
    for i in range(len(word)):
        if word[i]!="-":
            newWord+=word[i]
    return newWord
yes=True
while yes:
    word=input("Enter Your String:")
    # r-o-n-a-n
    # Y we can enter more,it N we cannot enter anymore
    print(removeMinuses(word))
    restartAgain=input()
    if restartAgain=="N":
        yes=False

    
#===>34
def sum(value1,value2):
        return value1 + value2
value1 = 0 # value1 jam tro number and when we enter number2 jol so value1 gain those value and wait more value 2 enter
number = int(input("Enter Amount Of Enter: "))
for i in range(number):
        value2 = int(input("Value"+str(i+1)+": " )) 
        value1 = sum(value1,value2)
print(value1)


#===>35
def factorial(n):
    if n == 0:
        return 1   # factoral mean that * decrese. Ex 4 => 4X3X2X1 = 24
    else:
        return n * factorial(n-1)  # first it calulate n-1 until n == 0 that time it will return number1 mk.
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))


#===>36
def countChar(word,char):
        timeChar = 0
        for value in word:
                for i in range(len(value)):
                        if value[i] == char:
                                timeChar += 1
        return timeChar
word = eval(input("Enter array with store letter: "))
['a','b','c']
char = input("Enter char: ")
# a result is 1
print(countChar(word,char))



#===>37
def sum(number1,number2):
    resultOfSum = number1 + number2
    return resultOfSum
number1 = int(input("Take Value To parametter number1: "))
number2 = int(input("Take Value To parameter number2: "))
print("The sum is: " + str(sum(number1,number2)))


#===>38
def sum(totalOfV):
    count = 0
    for i in range(NumberOfValue):
        count += 1
        number = int(input("value "+ str(count) + ": "))
        totalOfV += number
    return totalOfV
totalOfV = 0
NumberOfValue = int(input("Number of value: "))
print("The sum is: "+str(sum(totalOfV)))



#===>39
def remove_duplicates(array):
    result=[]
    for i in array:
        if i not in result:
            result.append(i)
    return result
array=eval(input())
print(remove_duplicates(array))


#===>40
def replaceOne(array):
    firstChange = True
    for i in range(len(array)):
        if array[i] == 1  and firstChange: 
            array[i] = 0
        else:
            firstChange = False
    return array
array = eval(input())
print(replaceOne(array))


#===>41
