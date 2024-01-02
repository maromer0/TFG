print("Welcome to pizzeria Bella Napoli.\n\t1-Pizza Vegetarian.\n\t2-Pizza Non Vegetarian.")
pizza = input("Select your favourite pizza: ")
if pizza == "1":
    print("ingredients:\n\t1-Pepper\n\t2-tofu")
    ingredients = input("Select your favourite ingredient: ")
    if ingredients == "1":
        print("Pizza vegetarian with mozarrella, tomato and pepper")
    else:
        print("Pizza vegetarian with mozarrella, tomato and tofu")
else:
    print("ingredients:\n\t1-Peperoni\n\t2-Ham\n\t3-Salmon")
    ingredients = input("Select your favourite ingredient: ")
    if ingredients == "1":
        print("Pizza non vegetarian with mozarrella, tomato and peperoni")
    elif ingredients == "2":
        print("Pizza non vegetarian with mozarrella, tomato and ham")
    else:
        print("Pizza non vegetarian with mozarrella, tomato and salmon")
