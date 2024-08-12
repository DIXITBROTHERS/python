# wap for making calculater by match

num1=int(input("enter the value of num1:"))
num2=int(input("enter the value of num2:"))

# take operater input

operater=input("enter your operater:")

match operater:
    case  "+":
           print("the addition of the given values is:",num1+num2)
    case"-":
           print("the subtraction of the given values:",num1-num2)
    case "*":
          print("the multiplication of the given values",num1*num2)
    case "/":
          print("the divison of the given values",num1/num2)
    case _:
          print("the operater is not valid correct")

