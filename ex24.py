print "Let's practice everything."
print 'You\'d nned to know \'bout escapes with \\ that do \n newlines and \t tab.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print (30 * '-')
print poem
print (30*'-')


five = 10-2+3-6
print "This should be %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
    
    
start_point = 10000
beans,jars, crates = secret_formula(start_point)

print "With a starting pont of: %d" % start_point
print "We;d have %d beans, %d jars, %d crates." % (beans,jars,crates)

start_point /=  10 # /= 10 did not work

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
