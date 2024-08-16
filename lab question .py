'''#Q1. write a program to sum all the number [ans: 26] 
list=[1,7,-10,34,2,-8]
sum=0
for i in list:
    sum+=int(i)
print(sum)

#Q2.wap to multiply all the item ina sample output  [ans: 1680]
list=[3,4,5,4,7]
sum=1 
for i in list:
    sum*=int(i)
print(sum)

#Q3. wap to get largest number from sample output [ans: 34]
#list=[1,7,10,34,2,8]
max=list[0]
for i in  list:
    if i>max:
        max=i
print(max)
        
# Q 4 .Write a Python program to get the smallest number from a list Sample Output [51,7,10,34,2,8] Smallest Number : 2        
      
list=[51,7,10,34,2,8]
min=list[0]
for i in list:
    if i<min:
       i=min
print(min)

#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

Sample Output

['abc', 'xyz', 'aba', '1221']

First and Last Character are same : 2

View Solution

list=['abc','xyz','aba','1221']
count=1
for i in list :'''


# if else
#wap to check the number is divisible by 7 

'''num=int(input())
if num%7==0:
    print("divisible")
else:
    print("not divisible")'''

#  wap to check the last digit is 4

'''num=int(input())
last_digit= num%10
if last_digit==4:
    print("the last digit is 4")
else:
    print("last digit is not 4")'''

# wap to check the  the number is divisable by 3 and last digit is 4

'''num=int(input())
if num%3==0 and num%10==4:
    print("the number is divisable by 3 and ends with 4")
else:
    print("the number is  not divisable by 3 and not ends with 4")'''

# wap to check the  the number is divisable by 7 and last digit is 5

'''num=int(input())
if num%7==0 and num%10==5:
    print("the number is divisable by 7 and ends with 5")
else:
    print("the number is  not divisable by 7 and not ends with 5")

# wap to check  input is divisiable by 5 or 11'''

'''num=int(input())
if num%5==0 and num%11==0:
    print("the number is divisable by both 5 and 7")
else:
    print("the number is not divisable by both 5 and 7")''' 

#read three number and print the highest number

'''a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print("a is greater ")
elif b>c and b>a:
    print("b is greater ")
else:
    print("c is greater" )'''

# wap to read three ange of triangle

'''a=int(input())
b=int(input())
c=int(input())
if'''










# leap year 

'''year=int(input())
if year%4==0 or year%100==0 or year%400==0:
    print("true")
else:
    print("false")'''



# class question
'''a = "VII "
b = "20"
c = "1"
print(a+b+c)'''

# find the value which does not exist in list


arr=[]
n=int(input("enter value"))
for i in range(n-1):
    x=int(input("enter value"))
    arr.append(x)
print(arr)
actualsum=n*((n+1)/2)
sum1=0
for i in range (n-1):
    sum1+=arr[i]
t=actualsum-sum
print(t)

    
    




    
    
    





