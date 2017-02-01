#Exercise 6: Strings and Text

#string with %d formatting
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#string with %s formatting and two variables
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#string with %r which prints var hilarious
# %r displays "raw" data of the variable
print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

#string concat
print (w + e)
