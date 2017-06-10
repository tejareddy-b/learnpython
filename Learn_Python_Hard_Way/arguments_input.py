from sys import argv
script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script talking." %(user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %(user_name)
likes = raw_input(prompt)
print "So you said %s about liking me" %(likes)
