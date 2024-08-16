# nested if else Q: take positive integer input and tell if it is divisible by 3 or 5 but not divisable by 15
# by taking 3 ,5,15 , saperately
number=int(input("enter any number:"))
'''if number%5==0:
   print("the number is divisible by 5")
else:
    print("the number is not divisable by 5")
if number%3==0:
    print("the number is not divisiable by 3")
else:
    print("the number is not divisable by 3")
if number%15==o:
    print("the number is divisable by 15")
else:
    print("the number is not divisable by 15")'''

# by taking 3 and 5 both

if number%15==0:
    print("the number is divisable by 15")
else:
    print("the number is not divisable by 15")
if number%3==0 or number%5==0:
    print("the number is divisable by 3 and 5")
else:
    print("the number is not divisable by 3 and 5")
                 
