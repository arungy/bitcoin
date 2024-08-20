name = 'Zed A. Shaw'
age = 35 #not a lie serious
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inche (i.e. %d centimeter) tall." % (height, (height * 2.54))
print "He's %d pound (i.e. %d kilogram) heavy." % (weight, (weight * 0.45359))
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
