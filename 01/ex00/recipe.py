import sys
import string

class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if not name:
            sys.exit("Error: no recipe name")
        if not ingredients:
            sys.exit("Error: no ingredients")
        if not recipe_type or not recipe_type in {"starter", "lunch", "dessert"}:
            sys.exit("Error: no recipe type")
        if not cooking_lvl.isnumeric() or int(cooking_lvl) < 1 or int(cooking_lvl) > 5:
            sys.exit("Error: cooking level invalid")
        if not cooking_time.isnumeric() or int(cooking_time) < 1:
            sys.exit("Error: cooking time invalid")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients.split(' ')
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = "\nRecipe for " + self.name + ":\n"
        txt += "--> Type:\t\t" + self.recipe_type + "\n"
        txt += "--> Cooking level:\t" + self.cooking_lvl + "\n"
        txt += "--> Cooking time:\t" + self.cooking_time + "\n"
        txt += "--> Ingredients list:\t" + ", ".join(item for item in self.ingredients) + "\n"
        txt += "--> Description:\n\t" + self.description + "\n"
        return txt