#Studydrills

def clothing(shirt_count, pants_count):
    print ("You have {} shirts.".format(shirt_count))
    print ("You have {} pants.\n".format(pants_count))

clothing(21, 12)

print ("How many shirts and pants do you have?")
amount_of_shirts = int(input('> Shirts: '))
amount_of_pants = int(input('> Pants: '))
clothing(amount_of_shirts, amount_of_pants)

print ("Bit of math with int() conversion:")
clothing(amount_of_shirts + 42, amount_of_pants - 5)

#float
clothing(4214/2, 100*2)

#negative
clothing(1-2, 1+1)
