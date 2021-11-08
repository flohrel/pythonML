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
    
getRecipe()