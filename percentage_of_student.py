# take input percentage of student and give grade according to it

percentage=float(input("enter the percentage of student:"))

if percentage>80 and percentage<=100:
    print("very good")
elif percentage>60 and percentage<=80:
    print("good")
elif percentage>40 and percentage<=60:
    print("average")
else:
    print("fail")

