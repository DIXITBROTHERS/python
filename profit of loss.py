# Q: wap to for profit or loss through cp and sp by taking input

cp=int(input("enter your cost price:"))
sp=int(input("enter your selling price:"))
# when ther is loss

if cp>sp:
 print("you have loss of:",cp-sp)

#when there is profit

elif sp>cp:
 print("you have profit of:",sp-cp)

# when there is no profit no loss

else:

 print("you have no profit no loss:",cp-sp)




       
