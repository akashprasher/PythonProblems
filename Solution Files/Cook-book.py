recipes = {
    "pasta": ["tomato", "basil", "garlic", "salt", "pasta", "olive oil"],
    "apple pie": ["apple", "sugar", "salt", "cinnamon", "flour", "egg", "butter"],
    "ratatouille": ["aubergine", "carrot", "onion", "tomato", "garlic", "olive oil", "pepper", "salt"],
    "chocolate cake": ["chocolate", "sugar", "salt", "flour", "coffee", "butter"],
    "omelette": ["egg", "milk", "bacon", "tomato", "salt", "pepper"]
}

user_input = str(input())

for w in recipes.items():
    if user_input in w[1]:
        print(w[0] + " time!")