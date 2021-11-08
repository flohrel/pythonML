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

def getRecipe():
    print("Please enter the recipe's name to get its details:")
    arg = input(">> ")
    recipe = cookbook.get(arg)
    if not recipe:
        print(arg, "not found")
        return
    print("Recipe for", arg + ":")
    print("Ingredients list", recipe.get("ingredients"))
    print("To be eaten for", recipe.get("meal"))
    print("Takes", recipe.get("prep_time"), "minutes of cooking")
    
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
        print("\nInvalid argument")
    else:
        if index < 1 or index > 5:
            print("\nInvalid option")
        elif index == 5:
            print("\nCookbook closed")
            exit()