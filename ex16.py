#Exercise 16: Reading and Writing Files

#close          --closes the file (like file->save)
#read           --reads the contents of the file and can be assigned to VAR
#readline       --reads just one line of a txt file
#truncate       --empties the file
#write("stuff") --wirtes "stuff" to file
#seek(0)        --moves the r/w location to the beginning of the file

from sys import argv

script, filename = argv

#Studydrill 2
show_txt = open(filename)
print (show_txt.read())
show_txt.close

print ("We're going to erase {}.".format(filename))
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

#Studydrill 3
target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print ("And finally, we close it.")
target.close()

#4
#'w' opens the file in a "write" state and truncates any existing data in the file
#'a' opens the file in a state to be appended to, preserving the existing data

#5
#truncate in line 29 is redundant since the 'w' parameter truncates the file upon call
