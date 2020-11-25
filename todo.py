# let's create a simple todo list app in python and then we'll port it to other languages

import sys

# check to see if there are no arguments (always one because it is the file running)
n = len(sys.argv)

if n == 1:
    print ("For Help: python3 todo.py -help")

if n == 2 and sys.argv[1] == '-help':
    print ("Usage:")
    print ("todo -list (lists all elements)")
    print ("todo -push 'something to do'")
    print ("todo -pop 3 (removes element 3 from list)")

if n == 2 and sys.argv[1] == '-list':
    # read todolist file and display it here in a loop
    print("reading todolist file and displaying it...")

if n > 2 and sys.argv[1] == '-push':
    # append sys.argv[2] to todolist file
    print("appending " + sys.argv[2] + " to the todolist file")

if n > 2 and sys.argv[1] == '-pop':
    # remove element sys.argv[2] from todolist file
    print("removing element " + sys.argv[2] + " from todolist file")
    
   
