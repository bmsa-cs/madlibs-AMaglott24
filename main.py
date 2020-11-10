"""
MadLibs
Author: Alex Maglott
Period/Core: 6


"""
print("Madlib: Forest Hike\n")
name = input("Select a name: ")
adjective1 = input("Select an adjective: ")
weather = input("Select a type of weather ending in \"y\": ")
animal1 = input("Select an animal (Plural): ")
adjective2 = input("Select an adjective: ")
exclamation = input("Select an exclamation: ")
verb1 = input("Select a verb (Past Tense): ")
verb2 = input ("Select a verb ending in \"ing\": ")
adjective3 = input("Select an adjective: ")
animal2 = input("Select an animal: ")
motion = input("Select a type of motion ending in \"ing\": ")


print("\n" + name + " was taking a " + adjective1 + " stroll through the forest.")
print("The day was quite " + weather + ", so it was perfect for a walk.")
print(f"{name} remarked, \"It is so nice to see so many {animal1} \nin the woods today! They really {adjective2}-en the place up!\"")
print(f"Just then, one of the {animal1} {verb1} down onto {name}'s head! \n\"Oh {exclamation}!\" {name} exclaimed, {verb2} along with the {animal1}.")
print(f"Then, from the corner of their eye, {name} saw a\n{adjective3} {animal2} {motion} towards them! \"Oh my!\"")
print("\"Maybe today wasn't such a good day for a hike...\"")