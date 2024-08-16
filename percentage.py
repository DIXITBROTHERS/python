''' WRITE A PROGRAM TO READ MARKS OF THREE SUBJECTS AND CALCULATE 
TOTAL MARKS AND PERCENT USING INPUT METHOD.'''

MATHS=float(input("enter your maths marks:"))
chemistry=float(input("enter your chemistry marks:"))
physics=float(input("enter your physics marks:"))
whole=(MATHS+chemistry+physics)
print("your percentage is",whole/300*100)
