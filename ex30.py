people = 30
cars = 40
trucks = 15

if cars > people or trucks < cars:
    print "We should take the cars."
elif cars < people:
    print "we should not take the cars."
else:
    print "We cant decide"
    
if trucks > cars:
    print "thats too many trucks"
elif trucks < cars and people > trucks:
    print "Maybe we should take the trucks"
else:
    print "We still cant decide"
    
if people > trucks and cars > trucks:
    print "Alright lets just take the trucks."
else:
    print "Fine, lets stay home then."