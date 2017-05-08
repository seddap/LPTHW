#Exercise 23: Strings, Bytes and Character Encodings

import sys
script, encoding, error = sys.argv

#called at the end of the script
def main(language_file, encoding, errors):
    line = language_file.readline() #read one line of the file given

    if line: #test if line is not empty
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) #ooh, recursion!

def print_line(line, encoding, errors):
    next_lang = line.strip() #stripping of the trailing \n on the line string
    raw_bytes = next_lang.encode(encoding, errors = errors) #encode into raw bytes
    cooked_string = raw_bytes.decode(encoding, errors = errors) #decode to get string

    print (raw_bytes, "<===>", cooked_string)

    #b'' = byte string
    #on the left shown on hex and on the right output as utf-8

languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, encoding, error)

#raw bytes -> use .decode() to get the string
#DBES "Decode Bytes, Encode Strings"
