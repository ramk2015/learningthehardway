
def makelist(howbig):
    i = 0
    numbers = []
    while i < howbig:
        print "At the top is %d" % i 
        numbers.append(i)
        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num
        
def makelist_again(howbig):
    numbers=[]
    i = 0
    sublist = range(0, howbig)
    for i in sublist:
        print "At the top is %d" % i 
        numbers.append(i)
        i += 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num
    

user_input = None        
valid_input = range(1,100)
while user_input not in valid_input:
    try:
        user_input = int(raw_input("How large do you want to make your new list pls choose a value between[0-100]: "))
    except ValueError:
        print "numeric inputs only"
        
makelist(user_input)
makelist_again(user_input)