# fibonacci series
# n=int(input())
# a=0
# b=1
# ls = [0,1]
# for i in range(0,n):
#     c = a + b
#     ls.append(c)
#     a = b
#     b = c
    
# for i in ls:
#     print(i, end = " ")

# n=int(input())
# a=0
# b=1
# ls=[0,1]
# for i in range(0,n):
#     c=a+b
#     ls.append(c)
#     a=b 
#     b=c
# for i in ls:
#     print(i,end=" ")

num = int(input("Enter the NUmber : "))
count = 0

for i in range(1,num+1):
    if num % i == 0:
        count +=1
    else:
        pass

print(count == 2)
    


