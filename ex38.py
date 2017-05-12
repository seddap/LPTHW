#Exercise 38: Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    stuff.append(next_one)
    print ("There are {ls} items now.".format(ls = len(stuff)))

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1]) #shows last element
print (stuff.pop()) #shows last element
print (' '.join(stuff)) #joins list to string with spaces
print ('#'.join(stuff[3:5])) #joins list items 3 and 4 with a #
