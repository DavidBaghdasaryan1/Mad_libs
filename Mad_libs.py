import random

template_choice = int(input("Please select a story template 1, 2 or 3: "))


if template_choice == 1:
    print("Please enter the following inputs:")
    words = [
        int(input("Number: ")),
        input("Measure of time: "),
        input("Mode of transportation: "),
        input("Adjective: "),
        input("Adjective 2: "),
        input("Noun: "),
        input("Color: "),
        input("Part of the body: "),
        input("Verb: "),
        int(input("Number 2: ")),
        input("Noun 2: "),
        input("Noun 3: "),
        input("Part of the body 2: "),
        input("Verb: "),
        input("Noun 4: "),
        input("Adjective 3: "),
        input("Silly word: "),
        input("Noun: ")
    ]
    template = "It was about {0} {1} ago when I arrived at the hospital in a {2}. The hospital is a/an {3} place, there are a lot of {4} {5} here. There are nurses here who have {6} {7}. If someone wants to come into my room I told them that they have to {8} first. I’ve decorated my room with {9} {10}. Today I talked to a doctor and they were wearing a {11} on their {12}. I heard that all doctors {13} {14} every day for breakfast. The most {15} thing about being in the hospital is the {16} {17}!"
    story = template.format(*words)
    print(story)

elif template_choice == 2:
    print("Please enter the following inputs:")
    words = [
        input("Proper noun (person's name): "),
        input("Noun: "),
        input("Adjective (feeling)1: "),
        input("Verb: "),
        input("Adjective (Feeling)2 : "),
        input("Animal: "),
        input("Verb 2: "),
        input("Color: "),
        input("Verb (ending in ing): "),                     
        input("Adverb (ending in ly): "),   
        int(input("Number: ")),   
        input("Measure of Time: "),
        input("Color: "),   
        input("Animal: "),   
        int(input("Number: ")),   
        input("Silly Word: "),
        input("Noun 2: "),
        
    ]
    template = "This weekend I am going camping with {0}. I packed my lantern, sleeping bag, and {1}. I am so {2} to {3} in a tent. I am {4} we might see a(n) {5}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {6}. I have heard that the {7} lake is great for {8}. Then we will {9} hike through the forest for {10} {11}. If I see a {12} {13} while hiking, I am going to bring it home as a pet! At night we will tell {14} {15} stories and roast {16} around the campfire!!"         
    story = template.format(*words)
    print(story)


elif template_choice == 3:
    print("Please enter the following inputs:")
    words = [
        input("Proper noun (person's name): "),
        input("Adjective: "),
        input("Color: "),
        input("Animal: "),
        input("Place: "),
        input("Adjective 2: "),
        input("Magical Creature (Plural): "),
        input("Adjective 3: "),
        input("Magical Creature (Plural)2: "),                     
        input("Room in a House: "),   
        input("Noun: "),   
        input("Noun2: "),   
        input("Noun(Plural) 3: "),   
        input("Adjective4: "),   
        input("Noun(Plural) 4: "),
        int(input("Number: ")),
        input("Measure of time: "),
        input("Verb(ending in ing): "),
        input("Adjective 5: "),
        input("Noun 5: "),
        ]
    template = "Dear {0}, I am writing to you from a {1} castle in an enchanted forest. I found myself here one day after going for a ride on a {2} {3} in {4}. There are {5} {6} and {7} {8} here! In the {9} there is a pool full of {10}. I fall asleep each night on a {11} of {12} and dream of {13} {14}. It feels as though I have lived here for {15} {16}. I hope one day you can visit, although the only way to get here now is {17} on a {18} {19}!!"
    story = template.format(*words)
    print(story)
else:
    quit()
