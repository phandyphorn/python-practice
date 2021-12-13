# =====================Function use to add type to arrayOfTypes=========================

# ======Show the 5 message =================First Function
def printMessages(messages):
    for mess in range(len(messages)):
        print(str(mess) + ": " + messages[mess])
    return "\n"
messages = ["exit","add a food type","list all food","add a food","list all foods","remove a food type"]

# =====Add Type Of Food To An Array=========Second Function
def addType(arrayOfTypes,typeName):
    message = ""
    if typeName not in arrayOfTypes:
        arrayOfTypes.append(typeName)
        message = "OK, food type added to the database"
    else:
        message = "Error this food type already exists"
    return message
arrayOfTypes = []

# =====Output all types in arrayOfType======Third Function
def printTypeInArrayOfTypes(arrayOfTypes):
    messageAsType = ""
    messageAsType = "List of food types: "
    if len(arrayOfTypes) == 0:
        messageAsType = "No type here"
    else:
        for typeName in arrayOfTypes:
            messageAsType += "\n" + typeName
    return messageAsType

# =====Add food to dictionary which dictionary=====Fourth Function
def addFoodToEachTypeInDictionary(arrayOfTypes,food,quantity,typeFood):
    if typeFood in arrayOfTypes:
        dictionary = {}
        dictionary["Name"] = food
        dictionary["Quantity"] = quantity
        dictionary["Type"] = typeFood
        arrayOfDics.append(dictionary)
        return "Ok, food added to the database"
    if typeFood != typeName:
        return "Error this food type does not exist"
    return arrayOfDics
arrayOfDics = []

# =====list of foods from arrayofdics====Fifth Func
def listOfFoods(arrayOfDics):
    if len(arrayOfDics) == 0:
        print("No food type for now")
    else:
        print("List of foods: "+"\n")
        for dictionary in arrayOfDics:
            print(dictionary["Name"])
            print("Number of dishes: " + str(dictionary["Quantity"]))
            print("Food type: " + dictionary["Type"])
    return "\n"

# =====Remove type from arrayOfTypes and dictionary which has this type===Sixth func
def removeDictionary(arrayOfDics,typeToRemove):
    arrayOfTypes.remove(typeToRemove)
    for index in range(len(arrayOfDics)):
        for key in arrayOfDics:
            if key["Type"] == typeToRemove:
                arrayOfDics.remove(key)
    return "Ok, food type removed"
isNotStop = True
while isNotStop:
    print(printMessages(messages))

    choice = int(input("Your Choice: "))
    if choice == 0:
        print("Bye")
        isNotStop = False
    if choice == 1:
        typeName = input("Name of the food type: ")
        print(addType(arrayOfTypes,typeName))

    if choice == 2:
        print(printTypeInArrayOfTypes(arrayOfTypes))

    if choice == 3:
        food = input("Food Name:")
        quantity = int(input("Number of dishes: "))
        typeFood = input("food type: ")
        print(addFoodToEachTypeInDictionary(arrayOfTypes,food,quantity,typeFood))

    if choice == 4:
        print(listOfFoods(arrayOfDics))

    if choice == 5:
        typeToRemove = input("Food type to remove: ")
        print(removeDictionary(arrayOfDics,typeToRemove))
    

# ===============================================================================================