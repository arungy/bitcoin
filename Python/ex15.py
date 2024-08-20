from sys import argv

#parsing the command line arguments
script, filename = argv

#open the file from command line parameter "filename"
txt = open(filename)

#priting the filename
print "Here's your file %r:" % filename
print txt.read() #read the content of files using "read()" API and printing the content

txt.close()

print "I'll also ask you to type the filenamge again:"
file_again = raw_input("> ") #requesting to type the same file again

#opening the typed file again
txt_again = open(file_again)

#read the content of file and print in stdout screen
print txt_again.read()

txt_again.close()
