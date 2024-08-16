# sum of  the enter digit 
n=int(input("enter any number "))
s=0
while n>0:
    r=n%10
    s=s+r
    n//=10
print(s)


# second way

n= int(input())
s=0
if n isdigit():
    for i in n:
        s+=int(i)
    print(s)
else:
    print("invalid input")
    
