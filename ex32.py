the_count = [1,2,3,4,5]
fruits =['apples','oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number
    
#same as above
for fruit in fruits:
    print "A fruits of type: %s" % fruit
    
#also we can go through mixed lists too
# notice we have to use %r since we dont know whats in it
for i in change:
    print"I got %r" % i
    
# we can also build lists, first start with an empty one
# then use the range function to do 0 to 5 counts 
# now we can print them out too

new_list = []
for i in range(0,6): #range does >=min value and <max value
    new_list.append(i)
    print "added %r to new list" % i
    
for i in new_list:
    print "The new element in new list was: %r" % i

new_list2=[]    
new_list2 = range(0,6)
print new_list2