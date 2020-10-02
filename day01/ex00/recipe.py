
class Recipe:
    def __init__(self, name, cooking_level, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_level = cooking_level
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        txt = f"\nRecipe for {self.name}:\n\nThis is a {self.recipe_type} recipe for level {self.cooking_level} cooks.\nThis recipe takes {self.cooking_time} minutes.\nIngredients: {self.ingredients}\nDescription: \n'{self.description}'"
        return(txt)
