#Exercise 32: Loops and Lists

#examples for lists
#   hairs = ['brown','blond','red']
#   eyes = ['brown','blue','green']
#   weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#first kind of for-loop goes through a list:
for number in the_count:
    print ("This is count {number}".format(number = number))

#same as above
for fruit in fruits:
    print ("A fruit of type: {fruit}".format(fruit = fruit))

#also we can go through mixed lists too
#notice we have to use {} since we don't know what's in it
for i in change:
    print ("I got {0}".format(i))

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print ("Adding {} to the list".format(i))
    #append is a function that lists understand
    elements.append(i)

#now we can print them out, too
for i in elements:
    print ("Element was: {}".format(i))

# 2D-lists: a = [[1, 2, 3][4, 5, 6]]
#range: range(start, stop[, step]) -> stop is j-1
#pydoc list:
#   append -- append object to end
#   count(value) -- return number of occurrences of value
#   index(value, [start, [stop]]) -- return first index of value
#   insert(index, object) -- insert object before index
#   pop([index]) -- remove and return item at index
#   remove(value) -- remove first occurrence of value
#   sort -- stable sort
