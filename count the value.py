# count the number of digit
n= int(input("enter any number"))
c=0
while n!=0:
    c+=1
    n//=10
print(c)


'''if int(n)<0:
    print(len(n)-1)
else:
    print(len(n))'''
    
    
