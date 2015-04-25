
from sys import argv

script, filename = argv


variable = open(filename)

print "Here's your file %r:" % filename
print variable.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()