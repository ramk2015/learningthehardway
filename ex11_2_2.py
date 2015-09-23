## Show Menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Backkup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')

valid_choices = [1,2,3]
choice = None # is frequently used to represent the absence of a value, as when default arguments are not passed to a function.
## Get input ##
while choice not in valid_choices:
    choice = raw_input('Enter your choice [1-3] : ')
### Convert string to int type ##
    try: 
        choice = int(choice)
    except ValueError:
        print("You have not entered a numeric choice.")

###Take action as per selected menu-option ###
if choice ==1:
    print("Starting backup ......")
elif choice ==2:
    print ("Starting user management .....")
else:
    print ("Rebooting the server...")
