tabby_cat = "\tI'm tabbed in." #\t will tab the output ont he screen
persian_cat = "I'm split\non a line." #\n will split into next line
backslash_cat = "I'm \\ a \\ cat." #gives a backlash

fat_cat = """ 
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print persian_cat
print backslash_cat
print fat_cat

# while True:
# for i in ["?","-","|","\\","|"]:
#      print "%s\r" % i,
  
escape_sequences = """
Memorize all the escape sequences by putting them on flash cards.\n
Use ''' (triple-single-quote) instead. Can you see why you might\nse that instead of triplle double quotes ?
Combine escape sequences and format strings to create a more\nomplex format.
Remember the %r format? Combine %r with double-quote and single-quote\n
eapes and print them out. Compare %r with %s. Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
\\\ """
print escape_sequences
