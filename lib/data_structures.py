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
    spicy_names = []
    for data_set in spicy_foods:
        spicy_names.append(data_set["name"])
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for data_set in spicy_foods:
        if (data_set["heat_level"] > 5):
            spiciest_foods.append(data_set)
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for data_set in spicy_foods:
        message = f'{data_set["name"]} ({data_set["cuisine"]}) | Heat Level: {"🌶" * data_set["heat_level"]}'
        print(message)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for data_set in spicy_foods:
        if data_set["cuisine"] == cuisine:
            return data_set

def print_spiciest_foods(spicy_foods):
    for data_set in spicy_foods:
        if data_set["heat_level"] > 5:
            message = f'{data_set["name"]} ({data_set["cuisine"]}) | Heat Level: {"🌶" * data_set["heat_level"]}'
            print(message)

def get_average_heat_level(spicy_foods):
    heat_levels = []
    for data_set in spicy_foods:
        heat_levels.append(data_set["heat_level"])
    total = 0
    length = len(heat_levels)
    for num in heat_levels:
        total += num
    return total / length


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = []
    for dict in spicy_foods:
        new_spicy_foods.append(dict)
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods