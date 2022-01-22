import random
print("Who will walk with a dog today?")

names_string = input("Give everybody's names, separated by a comma: ")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items -1)
person_who_walk = names[random_choice]
print(person_who_walk + " is going to walk with a dog today.")

