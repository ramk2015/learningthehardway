x = "There are %d types of people." % 10 # initializes x as string value and puts value of 10 within string
binary = "binary" # initializes binary as a string value
do_not = "don't" # initializes do_not as a string value
y = "Those who know %s and those who %s." % (binary,do_not) #1. intitalizes y as a string value with value of binary and value of do_not within it

print x
print y

print "I said: %r." % x #2. shows the inherent format (characters) of x within string print
print "I also said: '%s'." % y #3. shows value of string y as characters within string print

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # here %r seems to be doing nothing as nothing passed

print joke_evaluation % hilarious #4. prints values of hilarious inside joke_evaluation

w = "This is the left side of ..."
e = "a string with a right side."

print w + e # + concatenates 
# %r best for debugging its the raw format