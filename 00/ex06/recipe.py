cookbook = {
    "sandwich" : {
        "ingredients" : ["ham","bread","cheese","tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
    },
    "cake" : {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
    },
    "salad" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : 15
    }
}

def getRecipe(recipe, arg):
    print("\nRecipe for", arg + ":")
    print("Ingredients list:", recipe.get("ingredients"))
    print("To be eaten for", recipe.get("meal"))
    print("Takes", recipe.get("prep_time"), "minutes of cooking")

def addRecipe():
    new = dict.fromkeys(("ingredients", "meal", "prep_time"), 0)
    print("\nPlease enter recipe name to add it to cookbook:")
    recipe = input(">> ")
    print("List of ingredients:")
    var = input(">> ")
    new.update({"ingredients": var})
    print("Type of meal:")
    var = input(">> ")
    new.update({"meal": var})
    print("Preparation time:")
    var = input(">> ")
    new.update({"prep_time": var})
    cookbook.update({recipe: new})
    

while 1:
    print("\nPlease select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    try:
        index = int(input(">> "))
    except:
        print("\nThis option does not exist, please type the corresponding number.")
    else:
        if index < 1 or index > 5:
            print("\nThis option does not exist, please type the corresponding number.")
        elif index == 1:
            addRecipe()
        elif index == 2:
            print("\nPlease enter recipe name to delete it:")
            arg = input(">> ")
            recipe = cookbook.get(arg)
            if not recipe:
                print("\n", arg, "not found")
            else:
                cookbook.pop(arg)
        elif index == 3:
            print("\nPlease enter the recipe's name to get its details:")
            arg = input(">> ")
            recipe = cookbook.get(arg)
            if not recipe:
                print("\n", arg, "not found")
            else:
                getRecipe(recipe, arg)
        elif index == 4:
            for key in cookbook.keys():
                getRecipe(cookbook.get(key), key)
        elif index == 5:
            print("\nCookbook closed")
            exit()