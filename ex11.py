#Exercise 11: Asking Questions

print ("How old are you?", end =' '),
age = input()
print ("How tall are you?", end =' '),
height = input()
print ("How much do you weigh?", end = ' '),
weight = input()
print ("Give me number:", end = ' ')
number = int(input())
#gets number as string and converts it to int

print ("So you're {} old, {} tall and {} heavy.".format(age, height, weight))
print ("Your number was {}.".format(number))

#for python2: raw_input for accepting strings as an input.
#input takes expression and does an eval
