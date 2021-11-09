import sys
import datetime

class Book:

    def __init__(self, name):
        if not name:
            sys.exit("Error: no book name")
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {'starter': [],
                             'lunch': [],
                             'dessert': []
                            }
        return

    def get_recipe_by_name(self, name):
        if not name:
            print("Error: no recipe name")
            return
        for type in self.recipes_list:
            for recipe in self.recipes_list.get(type):
                if recipe.name == name:
                    print(str(recipe))
                    return

    def get_recipes_by_types(self, recipe_type):
        if not recipe_type:
            print("Error: no recipe type")
            return
        lst = self.recipes_list.get(recipe_type)
        for recipe in lst:
            print(str(recipe))
        return

    def add_recipe(self, recipe):
        lst = self.recipes_list.get(recipe.recipe_type)
        lst.append(recipe)
        return