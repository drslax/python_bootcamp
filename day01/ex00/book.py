from recipe import Recipe
import datetime


class Book:

    def __init__(self):
        self.name = ''
        self.last_update = 0
        self.creation_date = 0
        self.recipe_list = {'starter': [], 'lunch': [], 'dessert': []}

    def get_recipe_by_name(self, name):
        # """Print a recipe with the name `name` and return the instance"""
        for i in self.recipe_list:
            for j in self.recipe_list[i]:
                if j.name == name:
                    print(str(j))
                    return
        pass

    def get_recipes_by_types(self, recipe_type):
        # """Get all recipe names for a given recipe_type """
        for i in self.recipe_list[recipe_type]:
            print(i.name)
        pass

    def add_recipe(self, recipe):
        # """Add a recipe to the book and update last_update"""
        for i in self.recipe_list:
            if recipe.recipe_type == i:
                self.recipe_list[i].append(recipe)
                self.last_update = datetime.datetime.now()
        pass


book = Book()
recipe = Recipe(name="Couscous", cooking_level=1, cooking_time=90, ingredients=[
                'smida', 'khizo', 'left'], description='khalet lqlawi', recipe_type='lunch')
recipe2 = Recipe(name="bobo", cooking_level=1, cooking_time=90, ingredients=[
    'smida', 'khizo', 'left'], description='khalet lqlawi', recipe_type='starter')
book.add_recipe(recipe)
book.add_recipe(recipe)
book.add_recipe(recipe)
book.add_recipe(recipe)
book.add_recipe(recipe2)

book.get_recipes_by_types('lunch')
