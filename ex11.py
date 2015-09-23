print "How old are you",
age = int(raw_input())
print "How tall are you",
height = raw_input()
print "How much do you weigh?",
weight = raw_input('--> ')

print "So you're %d old,%r tall and %r heavy." % (age, height, weight)

note = """
We put a comma at the end of each print line 
this is so print doesnt end the line with a 
new line character and take the input on the next line
ex. with comma --> 
How old are you 35
wo comma -->
How old are you
35 """

print note