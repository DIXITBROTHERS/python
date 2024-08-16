'''i=1
while i<=100:
    print(i)
    i+=1

i=100
while i>=1:
    print(i)
    i-=1

n=int(input())
i=1
while i<=10:
    print(n*i)
    i+=1

i=1
while i<=10:
    print(i*i)
    i+=1

n=[24,34,54,34,65,90,86,98,45,]
for el in n:
    print(el)
n=[24,34,54,34,65,90,86,98,45,90]
x=90
index=0
for el in n:
    if el==x:
        print("number found at index",index )
    index+=1


#palendrome

m=input()
n=m[::-1]
print(n)

#fabonaci series
n=int(input())
a=0
b=1
ls = [0,1]
for i in range(0,n):
    c = a + b
    ls.append(c)
    a = b
    b = c
    
for i in ls:
    print(i, end = " ")

#prime number
num = int(input("Enter the NUmber : "))
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count +=1
    else:
        pass

print(count == 2)'''



    
    
    

