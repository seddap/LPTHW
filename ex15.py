#Exercise 15: Reading Files

from sys import argv

script, filename = argv

#open creates a file object
txt = open(filename)

print ("Here's your file {}:".format(filename))
print (txt.read())

print ("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()

#open via pydoc open: open(name[, mode[, buffering]]) -> file object
#Open a file using the file() type, returns a file object.  This is the
#preferred way to open a file.  See file.__doc__ for further information.

#remember brackets after .read()

#not quite sure yet about .close in line 20/21
