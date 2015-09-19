name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_cm = height * 2.54
weight_in_kg = weight * 0.4536 
import datetime
d = datetime.date.today()
a = "time to goto bed"
print "today is %r and its %r" % (d,a) 
# print "today is %d " % d gives error : TypeError: %d format: a number is required, not datetime.date
print "today is %s and %s " % (d,a)

print "Let's talk about %s." % name
print "He's %d inches tall." % height #so use %d where you want a number to be printed using %
print "He's %d pounds heavy." % weight
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair) #use %s where you want a string to be printed using %
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d I get %d." % (
    age, height, weight, age + weight + height)
print "In India we would say he weighs %s kgs and is %s cms tall." % (weight_in_kg, height_in_cm)