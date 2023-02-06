#Aidan Moxham
#Professor Eckert 
#CS-175L-01
#February 5th, 2023

    #Restaraunt Selector Program

restaurant_options = {
    "Joe's Gourmet Burgers": {"vegetarian": False, "vegan": False, "gluten-free": False},
    "Main Street Pizza Company": {"vegetarian": True, "vegan": False, "gluten-free": True},
    "Corner Cafe": {"vegetarian": True, "vegan": True, "gluten-free": True},
    "Mama's Fine Italian": {"vegetarian": True, "vegan": False, "gluten-free": False},
    "The Chef's Kitchen": {"vegetarian": True, "vegan": True, "gluten-free": True}
}

def choose_restaurants(vegetarian, vegan, gluten_free):
    suitable_restaurants = []
    for restaurant, restrictions in restaurant_options.items():
        if restrictions["vegetarian"] >= vegetarian and restrictions["vegan"] >= vegan and restrictions["gluten-free"] >= gluten_free:
            suitable_restaurants.append(restaurant)
    return suitable_restaurants

def main():
    is_vegetarian = input("Is anyone in your party a vegetarian? ") == "yes"
    is_vegan = input("Is anyone in your party a vegan? ") == "yes"
    is_gluten_free = input("Is anyone in your party gluten-free? ") == "yes"

    suitable_restaurants = choose_restaurants(is_vegetarian, is_vegan, is_gluten_free)

    if suitable_restaurants:
        print("Here are your restaurant choices:")
        for restaurant in suitable_restaurants:
            print(f"   {restaurant}")
    else:
        print("Sorry, there are no restaurants that meet your criteria.")

if __name__ == "__main__":
    main()
