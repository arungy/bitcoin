def delivery_fooditems_and_food(apple, mango, rice, dal, milk, curd):
    print "Hi da, I got %d fresh apples & %d mangos" % (apple, mango)
    print "As per list, I bought %d kg rice & %d kg dal" % (rice, dal)
    print "You mentioned to get %d litre milk & %d litre curd" % (milk, curd)
    print "Call Bigbasket customer care and order these items!!!!!\n"

print "Just passing as numbers:"
delivery_fooditems_and_food(12, 7, 5, 3, 2, 1)

print "Just passing through variables:"
apple = 22
mango = 5
rice  = 10
dal   = 20
milk  = 7
curd  = 3

delivery_fooditems_and_food(apple, mango, rice, dal, milk, curd)

print "Passing as variable with numbers:"
delivery_fooditems_and_food(apple+100, mango+70, rice+15, dal+25, milk+2, curd+4)

