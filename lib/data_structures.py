
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
        



def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get("name", "Food name not found!")
        cuisine = food.get("cuisine", "Cuisine not found!")
        heat_level= food.get("heat_level", 0)
        sum = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {sum}") 

# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if foods["cuisine"] == cuisine:
            return foods

# print(get_spicy_food_by_cuisine(spicy_foods, "American"))

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            levels = food.get("heat_level", 0)
            heat_level = "🌶" * levels
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

# print_spiciest_foods(spicy_foods)            

def get_average_heat_level(spicy_foods):
    sum = 0
    for food in spicy_foods:        
        if food["heat_level"] >= 0:
            sum += food["heat_level"]
    if len(spicy_foods) > 0:
        mean = sum// len(spicy_foods)
        return mean
    else:
        print("Nothing within the list")
def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]