#Exercise 13: Parameters, Unpacking, Variables

from sys import argv
#read the WYSS section from how to run this
script, first, second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)

#run with python3.4 ex13.py apple orange pear
#                            ^      ^     ^
#                           first second third
#needs 3 arguments, otherwise error -> need more values to unpack
#see ex13_study.py for more.
#argv to input in commandline, input for keyboard input while script is running
#argv = strings
