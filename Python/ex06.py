#assign string to with integer format character to variable
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#assign string within string using format character to variable
y = "Those who know %s and those who %s." % (binary, do_not)

#printing the variable
print x
print y

#priting the variable as it is, quoted string 
print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny!? %r"

#printing the string  with rexp string i.e. without using quotes
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with right side."

#concatinating the strings using '+' operator
print w + e
