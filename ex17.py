#Exercise 17: More Files

#ex17_sample.txt (FROM) and ex17_sample2.txt (TO)

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("Copying from {} to {}".format(from_file, to_file))

indata = open(from_file).read()

print ("The input file is {} bytes long".format(len(indata)))

print ("Does the output file exist? {}".format(exists(to_file)))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Done.")

out_file.close()
