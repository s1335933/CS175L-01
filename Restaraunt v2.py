#Aidan Moxham
#CS-175L-01
#February 12th, 2023

    #Restaraunt V2
print("Is anyone in your party a vegetarian?")
vegetarian = input().lower()
print("Is anyone in your party a vegan?")
vegan = input().lower()
print("Is anyone in your party gluten-free?")
gluten_free = input().lower()

print("Here are your restaurant choices:")
restaurants = ["Joe's Gourmet Burgers", "Main Street Pizza Company", "Corner Cafe", "Mama's Fine Italian", "The Chef's Kitchen"]
veg_options = [False, True, True, True, True]
vegan_options = [False, False, True, False, True]
gluten_free_options = [False, True, True, False, True]

search = "yes"

i = 0
while i < len(restaurants):
    if veg_options[i] == True and vegan_options[i] == True and gluten_free_options[i] == True:
        if vegetarian == "yes" and vegan == "yes" and gluten_free == "yes":
            print("   ", restaurants[i])
    elif veg_options[i] == True and vegan_options[i] == False and gluten_free_options[i] == True:
        if vegetarian == "yes" and gluten_free == "yes":
            print("   ", restaurants[i])
    elif veg_options[i] == True and vegan_options[i] == True and gluten_free_options[i] == False:
        if vegetarian == "yes" and vegan == "yes":
            print("   ", restaurants[i])
    elif veg_options[i] == True and vegan_options[i] == False and gluten_free_options[i] == False:
        if vegetarian == "yes":
            print("   ", restaurants[i])
    elif veg_options[i] == False and vegan_options[i] == False and gluten_free_options[i] == False:
        print("   ", restaurants[i])
        
 # Ask the user if they would like to do another search
    search = input("\nEnter 'yes' if you would like to do another restaurant search (enter 'no' to end): ").lower()
    i += 1
    
