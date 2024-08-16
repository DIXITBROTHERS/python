# wap to check the enter character is alphbatic , number or special character

character=input("enter any character you want: ")

if character.isnumeric() == True:
    print("the character is number  ")
    
elif character.isalpha() == True:
    print(" the character is alphabate")
    
else:
    print("special character")
    
