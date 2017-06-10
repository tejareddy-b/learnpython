from sys import argv
script, filename = argv
txt = open(filename, 'w')
txt.truncate()
file_again = raw_input("> ")
txt.write(file_again)
txt.write("\n")
txt.close()
