from sys import argv
import datetime

script, user_name, age = argv
current_year = (datetime.date.today().year)
birth_year = current_year - int(age)
prompt = '--->'

print "Hi %s, Im the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives= raw_input(prompt)

print   "What kind of computer do you have?"
computer = raw_input(prompt)

valid_month = [1,2,3,4,5,6,7,8,9,10,11,12]
birth_month = None
while birth_month not in valid_month:
    print "What month is your birthday [1-12]:"
    try:
        birth_month = int(raw_input(prompt))
    except ValueError:
        print("I do  not understand why you would type that")
        
if birth_month > datetime.date.today().month:
    birth_year = birth_year-1
    switch = 1
elif birth_month == datetime.date.today().month:
    switch = 0
else: switch = 1 

if switch == 1:
    print """
The prophecy had declared that the one and his army 
was born in the year %r, you could be one of them.
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
Now we know more about you than before.
And will keep a close eye on you.
Better not do something foolish
""" % (birth_year,likes,lives,computer)
else:
    print """
Hello %s, there is a %r chance that you are the ONE
resistance is futile, we like the odds for authorizing your elimination
and know everything about you.
""" % (user_name, 11/12.0)
