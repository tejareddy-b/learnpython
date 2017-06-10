def print_two(*string):
	arg1, arg2 = string
	print "arg1: %r,arg2: %r" %(arg1,arg2)
def print_two_again(arg1 ,arg2):
	print "arg1: %r, arg2: %r" %(arg1,arg2)
def print_one(arg1):
	print "arg1: %r" %arg1
def print_none():
	print "I am in none"

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("first")
print_none()
