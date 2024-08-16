# basic python program

'''print("hello")
print("world")
print(end="hello ")
print("world")

p=12
t=15
print(p+t)
print(p-t)
print(p*t)
print(p/t)
print(p%t)'''

#Q6 
'''num1=int(input())
num2=int(input())
print(num1**num2)'''

#Q7

'''length=int(input())
width=int(input())
print("the are of rectangle is", length*width)
print("the paremeter of rectangle is",(length+width)*2)'''

#Q8

'''radius=float(input())
print("the area of circle is",3.14*radius*radius)
print("the circumference is",2*3.14*radius)'''

#Q9

'''base=float(input())
height=float(input())
hypotaneous=(base**2+height**2)**0.5
print("the hypotaneous is ",hypotaneous)'''

#Q10

'''a,b=10,15
a,b=b,a
print("a=",a,"b=",b)'''

#Q11

'''lower_limit=int(input())
upper_limit=int(input())
sum=0
for i in range (lower_limit,upper_limit+1):
    sum+=i
print(sum)'''

'''num=int(input())
s=0
for i in range (1,num+1):
    s+=i
print(s)'''

#Q12 celsius to fahrenheit
# temperature=float(input())
# print((temperature*9/5)+32)



# a =[1, 2, 3]
# a =list(a)
# a[0] = 2
# print(a)

# print(type(5 / 2))
# print(type(5 // 2))

# a =[1, 2, 3, 4, 5]
# sum = 0
# for ele in a:
#    sum += ele
# print(sum)

# a =3
# b =1
# print(a, b)
# a, b = b, a
# print(a, b)


# a =[1, 2]
# print(a * 3)

# a=[1,2,3,4]
# b=[3,4,5,6]
# c=[x for x in a if x not in b]
# print(c)

# # print a prime number

# l=int(input())
# u=int(input())
# for i in range (l,u+1,1):
#     if i>1:
#         for j in range (2,i):
#             if i%j==0:
#                 break
#             else:
#                 print(i)

# num=int(input())
# count=0
# for i in range (1,num+1):
#     if num%i==0:
#         count+=1
#     else:
#         pass
# print(count==2)

# num=int(input())
# a=0
# b=1
# l=[0,1]
# for i in range (0,num):
#     c=a+b
#     l.append(c)
#     a=b
#     b=c
# for i in l:
#     print(i, end=" ")

# num=int(input())
# a=0
# b=1
# l=[0,1]
# for i in range(0,num+1):
#     c=a+b
#     l.append(c)
#     a=b
#     b=c
# for i in l:
#     print(i,end=" ")
# # reverse the given value 
# n=input()
# l=n[::-1]
# print(l)
# # febonacci series
# num=int(input())
# a=0
# b=1
# l=[0,1]
# for i in range(0,num+1):
#     c=a+b
#     l.append(c)
#     a=b
#     b=c
# for i in l:
#     print(i,end=" ")
#  # prime number    
# num=int(input())
# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count+=1
#     else:
#         pass
# print(count==2)

# table 
# num=int(input("enter your value"))
# for i in range (1,11):
#     m=i*num
#     print(m)
# tuple practice

 
#Q1Write a Python program to create a tuple.
'''this=("karan",30,30.55,)'''
#Q2Write a Python program to create a tuple with different data types.
'''this=("karan",30,30.55,)
print(this)'''
#Q3Write a Python program to create a tuple with numbers and print one item
'''d=("karan",80,90.67)
(x,y,z)=d
print(x)'''

# print a tuple by taking input
'''kd=tuple(input("enter value"))
print(kd)''' 
#Q4 Write a Python program to unpack a tuple in several variables.
'''pack=("karan","dixit",25,100,"hello","world")
for i in range pack:
        print(i)'''
        
# d=("karan",80,90.67)
# (x,y,z)=d
# print(x)    

# a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# ls1 = []
# for i in a:
#     ls = list(i)
#     ls1.append(ls)
# for j in ls1:
#     j[2] = 100
# ls2 = []
# for e in ls1:
#     ls3 = tuple(e)
#     ls2.append(ls3)
# print(ls2)  

  

# list



# ls=[1,2,3,4,5,6,7,8,9,10]
# for i in ls:
#     if i%2==0:
#         print(i)

# ls=[1,2,3,4,5,6,7,8,9,10]
# print(ls)
# print(type(ls))
# print(len(ls))
# if 11 not in ls:
#     print("11 is not in list ")
# if 4 in ls:
#     print("4 in list")
# print(ls[5])



# ls=[1,3,2,3,3,4,3,5,3,6,3,7,8,3,9,10]
# ls.append(100)
# print(ls)
# ls.insert(2,10)
# print(ls)
# ls1=[15,16,17,18]
# print(ls)
# ls.extend(ls1)
# print(ls)
# ls.remove(10)
# print(ls)
# ls.pop(5)
# print(ls)
# ls.index(3)
# print(ls)
# ls.count(3)
# print(ls)
# ls.sort()
# print(ls)
# ls.sort(reverse=True)
# print(ls)
# ls.reverse()
# print(ls)
# ls.clear()
# print(ls)
# del ls
# print(ls)

# ls=[50,49,30,20,39,27,25,12,23,22,9,85,90]
# newls=[i for i in ls if i>25]
# print(newls)

# size=int(input())
# ls=[]
# for i in range(size):
#     num=int(input())
#     ls.append(num)

# idx1=int(input())
# idx2=int(input())
# print(ls)

# temp=ls[idx1]
# ls[idx1]=ls[idx2]
# ls[idx2]=temp
# print(ls)



#function



# def sum(a,b):
#     s=a+b
#     m=a*b
#     su=a-b
#     d=a/b
#     return s,m,su,d
# a=int(input())
# b=int(input())
# m=input()
# if m=='+':
#     print(a+b)
# elif m=='-':
#     print(a-b)
# elif m=='*':
#     print(a*b)
# elif m=='/':
#     print(a/b)
# else:
#     print("This sign is not defined")
    
# sum(a,b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
    
# def calculator(num1, num2, operation):
#     if operation == 'add':
#         return num1 + num2
#     elif operation == 'subtract':
#         return num1 - num2
#     elif operation == 'multiply':
#         return num1 * num2
#     elif operation == 'divide':
#         if num2 == 0:
#             return "Error: Division by zero is not allowed."
#         else:
#             return num1 / num2
#     else:
#         return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."





# import


# import math
# x=45
# y=math.cbrt(x)
# print(y)

# import random

# def generate_random_number():
#     return random.randint(1, 100)

# print(generate_random_number())


# file handaling 

# f = open("file123.txt", "r")
# lines = f.readlines(),
# print(f.read())

# f1 = open("file123.txt", "w+")
# f1.write("aditya varshney")
# print(f1.read())



# n = int(input())
# temp=0
# for i in range(0,9,1):
#     temp = n+temp
# print(temp)


# number = int(input("Enter a number: "))
# result = int(input("enter a number "))
# print(result(number))

# number1=int(input())
# number2=int(input())
# result=number1<<number2
# print(result)


# number=int(input()) 
# number1=int(input())
# temp=0
# for i in range (1,number+1):
#     temp=number1+temp
# print(temp)
    
# def multiplication(a,b):
#      temp=0
#      for i in range(1,a+1):
#          temp=b+temp
#      return temp
# a=int(input())
# b=int(input())
# print(multiplication(a,b))  

#     table   

# num=int(input())
# for i in range(1,11):
#     m=num*i
#     print(f"{num} x {i} = {m}")

#    patern printing
    
 
# num1=int(input())
# for i in range(0,num1):
#     print("* "*num1)

    
      
# num1=int(input())
# for i in range(1,num1+1):
#     print(" * " *i)
    

# num=int(input())
# for i in range(num,0,-1):
#     print(" * " *i)
    
# num1=int(input())
# for i in range(1,num1+1):
#     print("*"*i)
# for i in range(num1,0,-1):
#     print("*"*i)


# num=int(input())
# for i in range(num,):
#     print(i,end=" ")
    
# num=int(input())
# for i in range(1,num+1):
#     if i%2==0:


# num=int(input())
# for i in range(1,num+1):
#      if i%2!=0:
#         print(i,end=" ") 

# dict={ 
      
#     'a':100,
#     'b':200,
#     'c':300
# }

# print(sum(dict.values()))

# dict3,dict2=map(eval,input().split())
# print(dict3,dict2)
# print(type(dict3))
# print(type(dict2))

# f = None
# for i in range (5):
#     with open("data.txt", "w") as f:
# if  i > 2:
#     break
# else:
#     print(f.closed)

# print(4.00/(2.0+2.0))
# X = 2+9*((3*12)-8)/10
# print( X)

# x=24//6%3, 24//4//2
# print(x)

# x=float(4+int(2.39)%2)
# print(x)

# x=4+2**5//10
# print(x)

# x=2**(3**2)
# y=(2**3)**2
# z=2**3**2
# print(x,y,z)

# x = ['ab', 'cd']
# for i in x:
#     i.upper()
# print(x)

# i = 1
# while True:
#     if i%3 == 0:
#         break
# print(i)
# i + = 1

# i = 1
# while True:
#     if i%0O7 == 0:
#         break
# print(i)
# i += 1

# i = 1
# while True:
#     if i%0O7 == 0:
#         break
#     print(i)
# i += 1

# x = "abcdef"
# while i in x:
#     print(i, end=" ")

# x = 'abcd'
# for i in x:
#     print(i)
#     x.upper()

# x = 123
# for i in x:
#     print(i)

# print(ord( "b" ) - ord( "a" )  )

# print("xyyzxyzxzxyy".count('yy'))

# print('Ab!2'.swapcase())
# print('ab'.zfill(6))

# a=list(map(int,input().split()))
# b=int(input())
# for i in a:
#     c=b+i
# print(c)
def f(x, y, z): 
    return x + y + z
f(2, 30, 400)