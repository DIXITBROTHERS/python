# WAP to input the electricity unit consume  based on the following and calculate the bill also when first 50 unit is 1.5 and next 100=1.75 next 100 1.75 next s250=2.5

unit=float(input("enter the unit consume:"))
if unit<=50:
    amount=unit*1.5
    tax=0.10*amount
    total_bill=amount+tax
    print("your total bill is:",total_bill)
elif unit<=100:
    amount=unit*1.75
    tax=0.10*amount
    total_bill=amount+tax
    print("your total bill is:",total_bill)
elif unit<=200:
    amount=unit*2
    tax=0.10*amount
    total_bill=amount+tax
    print("your total bill is:",total_bill)
else:
     amount=unit*2.5
     tax=0.10*amount
     total_bill=amount+tax
     print("your total bill is:",total_bill)
    
    


