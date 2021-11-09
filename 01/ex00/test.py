from recipe import Recipe
from book import Book

print("Choose a recipe name:")
name = input(">> ")
print("Choose a cooking level between 1 and 5:")
cooking_lvl = input(">> ")
print("Choose a cooking time:")
cooking_time = input(">> ")
print("List ingredients (separated by spaces):")
ingredients = input(">> ")
print("Give a description (facultative):")
description = input(">> ")
print('Recipe type (choose between "starter", "lunch" or "dessert"):')
recipe_type = input(">> ")
test = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
book = Book("name")
book.add_recipe(test)
book.get_recipes_by_types('dessert')