print "YOu enter a dark room with 2 doors. DO you go through door #1 or door #2?"

valid_input1 = ["1","2"]
door = None
while door not in valid_input1:
    door = raw_input("> ")
    
if door =="1":
    print"Theres a ginat bear here eating a cheese cake> WHat do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print " The bear eats your legs off. Good job!."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You starte into the endless abyss at Cthulhu's retina."
    print "1. Blueberries"
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "your body survives powered by a mind of jello. Good job!."
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!."
        
