'''list=[]
e=int(input())
for i in range(1,e):
    list.insert(i,e)
print(list)
list.remove(e)
print(list)
list.append(e)
print(list)
list.sort()
print(list)
list.pop(-1)
print(list)
list.reverse()
print(list)'''

# Initialize the list
list = []

# Read the value of n
n = int(input())

# Read the commands
for _ in range(n):
    command = input().split()
    operation = command[0]

    if operation == 'insert':
        i = int(command[1])
        e = int(command[2])
        list.insert(i, e)
    elif operation == 'print':
        print(list)
    elif operation == 'remove':
        e = int(command[1])
        if e in list:
            list.remove(e)
    elif operation == 'append':
        e = int(command[1])
        list.append(e)
    elif operation == 'sort':
        list.sort()
    elif operation == 'pop':
        list.pop()
    elif operation == 'reverse':
        list.reverse()
