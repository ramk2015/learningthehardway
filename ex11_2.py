## Show Meu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Backkup")
print ("2. User management")
print ("3. Reboot the server")
print (30 * '-')

## Get input ##
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
elif choice == 3:
    print ("Rebooting the server...")
else: ##default##
    print ("Invalid number. Try again....")