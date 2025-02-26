import random


r=random.randrange(0,101)
#print(r)
tt=0            #takes count of the attempt
x=int(input("Enter any number you think of:"))
while(x!=r):  
    if(x>r and x<101):
        print("Your number is greater than the guessed number") 
    elif(x<r and x>=0):
        print("Your number is smaller than the guessed number")  
    else:
        print("You number doesn't full within the limit it is asked") 
    tt=tt+1
    x=int(input("Enter any number you think of:"))


if(x==r):
     tt=tt+1
     print("You guessed the correct number")
    

print("You took",tt,"chances to get correct answer")
    
    