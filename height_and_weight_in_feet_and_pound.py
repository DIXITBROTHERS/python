# Q10:wap program to take input your height and weight in cm and kilogram and convert it into feet and pound
height=float(input("enter your height in cm:"))
weight=float(input("enter your weight in kilogram:"))
height_feet=height/30.48
weight_pound=weight*2.20462
print("your height in feet is:",height_feet)
print("your weight in pound is:",weight_pound)
