#Exercise 5: More Variables and Printing

name = "seddap"
age = 25
height = 74
weight = 180
eyes = "blue"
teeth = "white"
hair = "brown"
inch_to_cm = height * 2.54
lbs_to_kg = weight * 0.4536

print ("Let's talk about %s." % name)
print ("He's %d inches tall. That's %d centimeter." % (height, inch_to_cm))
print ("He's %d pounds heavy. That's %d kilogram" % (weight, lbs_to_kg))
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (eyes, hair))
print ("His teeth are usually %s depending on the coffee." % teeth)

#tricky line
print ("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

#test %r
print ("This is a test for percent r %r" % ("hello world 42"))

#round function
print ("This is a test for round. 42.2189412 rounded is %f" % round(42.2189412))

#old string formatting: https://docs.python.org/3/library/stdtypes.html#string-formatting (01.02.2017)
#new output: https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting (01.02.2017)
#explanation of %r:http://stackoverflow.com/questions/2354329/whats-the-meaning-of-r-in-python (01.02.2017)
