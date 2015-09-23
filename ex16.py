from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that hit CTRL-C (^C)."
print "if you want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w') #'w' will remove all previous info in the file and start writing!
#open(name[, mode[, buffering]])
#Open a file, returning an object of the file type. If the file cannot be 
#opened, IOError is raised. 
#The first two arguments are the same as for 
#stdio's fopen(): name is the file name to be opened, and mode is a string 
#indicating how the file is to be opened.
#The most commonly-used values of mode are 'r' for reading, 
#'w' for writing (truncating the file if it already exists), and 
#'a' for appending (which on some Unix systems means that all writes append 
#to the end of the file regardless of the current seek position). 
#If mode is omitted, it defaults to 'r'. 


print "Truncating the file. Goodbye!"
target.truncate() 
#will only remove all info from the point it is in file
#With truncate(), you can declare how much of the file 
#you want to remove, based on where you're currently at 
#in the file. Without parameters, truncate() acts like w, whereas w always just wipes the whole file clean.

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
alltxt = line1 + "\n" + line2 + "\n" + line3  
print "I'm going to write these to the file."

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
target.write(alltxt)

print "And finally, we close it."
target.close()
