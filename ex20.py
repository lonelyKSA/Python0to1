from sys import argv

script, input_file = argv

def print_all(f):
   print f.read()
 #define a function to read all the file and print it.  
def rewind(f):
    f.seek(0)
#define a function to  rewind the file to the start position.  
def print_a_line(line_count,f):
    print line_count, f.readline()
# define a function to read files by line    

current_file = open(input_file)
#open the file and assign it to 'variable' current_file 
print "First let's print the whole file:\n"

print_all(current_file)
# print all the file.
print "Now let's rewind, kind of like a tape."

rewind(current_file)
#back to the start position.
print "Let's print three lines:"

current_line = 1
#assign 1 to variable current_line
print_a_line(current_line,current_file)
#print current_line and the first line in the file
current_line = current_line + 1
#add 1 to variable current_line
print_a_line(current_line,current_file)
#print current_line and the second line in the file.
current_line = current_line + 1
#add 1 to variable current_line
print_a_line(current_line,current_file)
#print current_line and the third line in the file.