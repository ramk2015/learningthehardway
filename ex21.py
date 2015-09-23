
def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a+b
    
def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a-b
    
def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a*b
    
def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a/b
    

print "Let's do some maths with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it anyway.
print "Here is a puzzle"

what = add(age,subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?", "Will try: 35+74-4500", 35+74-4500


units_sold = int(raw_input("Enter number of units sold: "))
sale_price_of_units = int(raw_input("Enter sale price of each unit: "))
cogs = int(raw_input("Enter cost of each goods sold: "))
op_expenses = int(raw_input("Enter total operating costs to conduct biz: "))

revenue = multiply(units_sold, sale_price_of_units)
expenses = add(op_expenses, multiply(cogs, units_sold))
profit = subtract(revenue,expenses)

print "Your biz has generated total profits of %d dollars" % profit