from sys import argv

script, hours, rate = argv


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheeses!" % cheese_count
    print "you have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
    
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)


print "OR, we can use variables from our scrip:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10+6-4,7*23)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)

def wages(hours_worked,hourly_rate):
    money = hours_worked*hourly_rate
    print "your bank has been credited with %d dollars for your hard work\n" % money
    print "With this we will go shopping for our party"
    shop_cheese = money * .5 / 4
    shop_crackers = money *.5 / 2
    print "We have now bought %r packs of cheese and %r boxes of crakcers\n" % (shop_cheese,shop_crackers)
    
print "assigning values from command line inputs"
wages(int(hours),int(rate))

print "Calling it from script"
wages(40,100)

print "assigning values from from user input"
x=int(raw_input("Enter hours_worked: "))
y = int(raw_input("Enter hourly rate: "))


wages(x, y)