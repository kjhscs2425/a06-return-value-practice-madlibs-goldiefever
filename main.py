verb_ing1 = input("Give me a verb ending in -ing: ")
verb_ing2 = input("Give me a verb ending in -ing: ")
verb_ing3 = input("Give me a verb ending in -ing: ")
verb_ing4 = input("Give me a verb ending in -ing: ")

adj1 = input("Give me an adjective: ")
adj2 = input("Give me an adjective: ")
adj3 = input("Give me an adjective: ")

noun1 = input("Give me a noun: ")
noun2 = input("Give me a noun: ")
noun3 = input("Give me a noun: ")

pluralnoun1 = input("Give me a plural noun: ")
pluralnoun2 = input("Give me a plural noun: ")
pluralnoun3 = input("Give me a plural noun: ")
pluralnoun4 = input("Give me a plural noun: ")

plant1 = input("Give me a plant: ")

game1 = input("Give me a game: ")

bodypart1 = input("Give me a part of the body: ")

number1= input("Give me a number: ")

place1= input("Give me a place: ")

story = f('''A vacation is when you take a trip to some {adj1} place \n
with your {adj2} family. Usually you go to some place \n
that is near a/an {noun1} or up on a/an {noun2}. \n
A good vacation place is one where you can ride {pluralnoun1} \n
or play {game1} or go hunting for {pluralnoun2} . I like \n
to spend my time {verb_ing1} or {verb_ing2}. \n
When parents go on a vacation, they spend their time eating \n
three {pluralnoun3} a day, and fathers play golf, and mothers \n
sit around {verb_ing3}. Last summer, my little brother \n
fell in a/an {noun3} and got poison {plant1} all \n
over his {bodypart1}. My family is going to go to (the) {place1} \n
, and I will practice {verb_ing4}. Parents \n
need vacations more than kids because parents are always very \n
{adj3} and because they have to work {number1} \n
hours every day all year making enough {pluralnoun4} to pay \ n 
for the vacation.\n''')

print(story)