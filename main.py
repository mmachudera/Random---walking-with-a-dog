import random
print("Who will walk with a dog today?")

names_string = input("Give everybody's names, separated by a comma: ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items -1)
person_who_walk = names[random_choice]
print(person_who_walk + " is going to walk with a dog today.")

plastic_bag = input(person_who_walk + ", do you have a plactic bag?  Y or N ? ")
if plastic_bag == "Y":
  print("Great! In case of rain, take also an umbrella.")
else:
  print("Do you want to pay a ticket? Take a bag, please.")

water = input("Did you pack some water? Y or N ? ")
if water == "Y":
  print("You are a good guardian! Have fun.")
else:
  print("Take water and harry up. Your doggy doesn't like to wait too long!")

