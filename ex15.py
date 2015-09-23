from sys import argv #from built in moduile sys import object argv
#This module provides access to some objects used or maintained by the
#interpreter and to functions that interact strongly with the interpreter.
# argv -- command line arguments; argv[0] is the script pathname if known
# so argv[0] will say "ex15.py" and argv[1] will say ex_sample.txt

script,filename = argv # assigning value of argv[0] to variable script and value of argv[1] to variable filename

txt = open(filename) #returns a file object to variable txt
#open is  abuilt in function in module __builtin__:open(...)
#open(name[, mode[, buffering]]) -> file object
#Open a file using the file() type, returns a file object.  This is the
#preferred way to open a file.

print "Here's your file %r:" % filename #prints text and embedded variable filename
print txt.read() #
#To read a file's contents, call f.read(size), which reads some quantity of
#data and returns it as a string. size is an optional numeric argument. 
#When size is omitted or negative, the entire contents of the file will be 
#read and returned; it's your problem if the file is twice as large as 
#your machine's memory. Otherwise, at most size bytes are read and returned. 
#If the end of the file has been reached, f.read() will return an empty string ("").

print "Type the filename again:" 
file_again = raw_input(" >") # takes input from user on filename and assigns to variable 

txt_again= open(file_again) #file pbject to txt_again

print txt_again.read() #print entire file

txt.close()
txt_again.close()
#When you're done with a file, call f.close() to close it and free up any 
#system resources taken up by the open file
# After calling f.close(), attempts to use the file object will automatically fail.