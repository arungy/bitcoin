from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you do't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#taking the input from user to delete the content the file or not
raw_input("?")

#opening the file got from argv
print "Opening the file..."
target = open(filename, 'w')

#remove all the text or content avaialbe in the file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#taking new lines to write on this file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#writing the lines in to files with newline character
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

#finally closing the file to store safely
print "And finally, we close it."
target.close()
