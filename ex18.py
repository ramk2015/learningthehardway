# this one is like your scripts with argv
def print_two(*args): #the * tells to take all input arguments and put them in args as a list
    arg1, arg2 = args #unpack input arguments
    print "arg1: %r, arg2: %r" % (arg1,arg2)
    
# ok, that *args is actually pointless, we can do just this
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)
    
#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this takes no arguments
def print_none():
    print "I got nothin'."
    
print_two("ram","khanna")
print_two_again("ram","khanna")
print_one("first!")
print_none()
