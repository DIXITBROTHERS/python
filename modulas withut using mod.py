# Q1:wap to find the value of mudulas without using mod operater
#take input in int form 
a=int(input("enter the value:"))
# takeing second input for divide the values 
b=int(input("enter any value:"))
# this is the formula for finding remainder 
r=a-b*(a//b)
# now print the remainder 
print("the remainder is:",r)
