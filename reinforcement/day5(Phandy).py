# =============================Food Management============================
# ====================Task1====================
# isNotStop = True
# while isNotStop:
#     mess = ["exit","add a food type","list all food types","add a food","list all foods","remove a food type"]
#     for m in range(len(mess)):
#         print(str(m) + ": " + mess[m])
#     choice = int(input("Your choice: "))
#     if choice == 0:
#         result = "Bye!"
#         isNotStop = False
#     elif choice > 0 and choice <= 5:
#         result = "Your choice is " + str(choice)
#     elif choice > 5:
#         result = "Wrong choice"
#     print(result)
#     print("\n")

# Add type of food
# ========================Task2=====================
# ============Function to add type in array
isNotStop = True
# Add type of food
def addType(arrayOfTypes,type):
    result = ""
    if type not in arrayOfTypes:
        arrayOfTypes.append(type)
        result = "OK, food type added to the database"
    else:
        result = "Error this food type already exists"
    return result
arrayOfTypes = []

def listOfFoods(arrayOfFoods):
    if len(arrayOfFoods) == 0:
        print("No food type for now")
    else:
        print("List of foods: "+"\n")
        for dictionaryOfEachType in arrayOfFoods:
            print(dictionaryOfEachType["Name"])
            print("Number of dishes: " + str(dictionaryOfEachType["Quanity"]))
            print("Food type: " + dictionaryOfEachType["Type"])
    return "\n"

# ====================Function to add food dictionary to arrayOfdictionary

def addFoodToEachType(arrayOfTypes,food,quanity,typeName):
    # message = "OK, food added to the database"
    if typeName in arrayOfTypes:
        dictionaryOfEachType = {}
        dictionaryOfEachType["Name"] = food
        dictionaryOfEachType["Quanity"] = quanity
        dictionaryOfEachType["Type"] = typeName
        arrayOfFoods.append(dictionaryOfEachType)
        return "Ok, food added to the database" 
    if typeName != type:
        return "Error this food type does not exist"
    
    return arrayOfFoods
arrayOfFoods = []
# ==================================Function to print type in arrayOfType========================

def listOfTypes(arrayOfTypes):
    nameOfType = ""
    nameOfType = "List of food types: " 
    if len(arrayOfTypes) == 0:
        nameOfType = "No type here"
    else:
        for type in arrayOfTypes:
            nameOfType += "\n"+ type
    return nameOfType

# ======================Function to remove==================
def removeDictionary(arrayOfFoods,typeToRemove):
    arrayOfTypes.remove(typeToRemove)
    # boolean = False
    # message = "No food type for now"
    for i in range(len(arrayOfFoods)):
        for key in arrayOfFoods:
            if key["Type"] == typeToRemove:
                arrayOfFoods.remove(key)
                # boolean = True
    # if boolean:
    #     message = "Ok, food type removed"
    return "Ok, food type removed"

while isNotStop:
    mess = ["exit","add a food type","list all food types","add a food","list all foods","remove a food type"]
    for m in range(len(mess)):
        print(str(m) + ": " + mess[m])
    choice = int(input("Your choice: "))
    if choice == 1:
        type = input("Name of the food type: ")
        print(addType(arrayOfTypes,type))
    if choice == 2:
        print(listOfTypes(arrayOfTypes))
    if choice == 3:
        food = input("Food name:")
        quanity = int(input("Number of dishes: "))
        typeName = input("food type: ")
        print(addFoodToEachType(arrayOfTypes,food,quanity,typeName))
    if choice == 4:
        print(listOfFoods(arrayOfFoods))
        
    if choice == 5:
        typeToRemove = input("Food type to remove: ")
        # arrayOfFoods = removeDictionary(typeToRemove)
        # arrayOfTypes.remove(typeToRemove)
        print(removeDictionary(arrayOfFoods,typeToRemove))

# ============: Tesk thre==========================
