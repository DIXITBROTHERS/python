# wap to calculate profit and loss and also percentage of profit or loss

cp=int(input("enter the cost price "))
sp=int(input("enter the selling price"))
if cp>sp:
    loss=cp-sp
    print( " you have loss of ",loss)
    loss_percentage=loss/cp*100
    print("the loss percentage is:",loss_percentage)
else :
    profit=sp-cp
    print("you have profit of ",profit)
    profit_percentage=profit/cp*100
    print("the profit percentage is:",profit_percentage)
    
