# let's create a simple todo list app in python and then we'll port it to other languages

import sys

# check to see if there are no arguments (always one because it is <python3 todo.py>
n = len(sys.argv)

if n == 1:
    print ("For Help: python3 todo.py -help")

if n == 2 and sys.argv[1] == '-help':
    print ("Usage:")
    print ("todo -list (lists all elements)")
    print ("todo -add 'something to do'")
    print ("todo -rm 3 (removes element 3 from list)")

if n == 2 and sys.argv[1] == '-list':
    # check to see if list file exists, if not then print error
    # read list file and display it here in a loop
    print("[TODO LIST]\n")
    todoFile = open("list", "r")
    todoList = todoFile.readlines()
    for i in todoList:
        print (i)
        todoFile.close()

if n > 2 and sys.argv[1] == '-add':
    # append sys.argv[2] to list file
    print("appending " + sys.argv[2] + " to the list file")
    todoFile = open("list", "a")
    todoFile.write(sys.argv[2] + "\n")
    todoFile.close()

if n > 2 and sys.argv[1] == '-rm':
    # Remove element sys.argv[2] from list file
    # So we need to read the file, store all the lines in an array, copy the array but
    # remove the selected element, and then write (not append) to 'list' file
    print("removing element " + sys.argv[2] + " from list file")
    todoFile = open("list", "r")
    todoList = todoFile.readlines()
    todoFile.close()
    choice = int(sys.argv[2])
    # add out of bounds checking in future version, dont' just assume -1 will be valid (could be negative if person entered element 0
    if choice > 0 and choice <= len(todoList):
        print("Removing Entry #" + sys.argv[2] + " -> " + todoList[choice-1])
        todoFile = open("list", "w")
        for idx, val in enumerate(todoList):
            if idx + 1 != choice:
                todoFile.write(val)
        todoFile.close()

    
