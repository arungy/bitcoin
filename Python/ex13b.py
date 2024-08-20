from sys import argv

script, question1, question2 = argv

yes_no = raw_input("%s? yes/no: " % question1)
addr = raw_input("%s: " % question2)

print "%s : %s" % (question1, yes_no)
print "%s : %s" % (question2, addr)
