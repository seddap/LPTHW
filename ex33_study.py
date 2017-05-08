#Exercise 33: While Loops

def fill_list_while(j, steps):
    i = 0
    numbers = []

    while i < j + 1:
        numbers.append(i)
        i += steps
        print ("Numbers now: ", numbers)

def fill_list_for(j, steps):
    numbers = []
    for i in range(0, j+1, steps):
        numbers.append(i)
        print ("Numbers now: ", numbers)

print ("Please enter an integer and the increments:")
val = int(input("Integer: "))
steps = int(input("Steps: "))

fill_list_while(val, steps)
print ("------------------------")
fill_list_for(val, steps)
