from sys import argv

script, filename = argv

raw_input("Do you want to print the file in screen? ")

#opening the file got from argv
print "Opening and reading the %r file." % filename
target = open(filename, 'r')

content = target.read()

print "Here is your content:\n"
print "%s" % content

#finally closing the file to store safely
target.close()
