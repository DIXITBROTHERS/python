'''print("Hello world")
print("hello,\n world")
print("hello,\t world")

a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

char=input()
print(ord(char))

ascii=int(input())
print(chr(ascii))

radius=float(input())
print(4/3*3.14*radius*radius*radius)


num = int(input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)

num_terms = int(input("Enter the number of terms for Fibonacci series: "))

fib_series = []
a, b = 0, 1

for _ in range(num_terms):
    fib_series.append(a)
    a, b = b, a + b

print("Fibonacci series up to", num_terms, "terms:")
print(fib_series)

num=int(input())
factorial=1
for i in range (1,num+1):
    factorial*=i
print(factorial)

str="KaranDixit"
print( str.count("a"))

number=int(input())
if number>=90:
    print("A")
elif number<90 and number>=80:
    print("B")
elif number <80 and number >=70:
    print("C")
else:
    print("D")'''
n=int(input())
if n%2!= 0:
    print("Weird")
elif  n%2==0 and n>1 and n<6:
    print("Not Weird")
elif n%2==0 and n>5 and n<21:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Weird")





