import random


us=0
cs=0
list=["Rock","Paper","Scissor"]

x=4
print("This game will repeat 3 times and will count the score to check who wins:")
for i in range(1,x):
        r=random.choice(list)
        print(r)
        user=input("Choose your form:\n 1.Rock \n 2.Paper \n.3.Scissor\n")


        if(user=="Rock" and r=="Scissor"):
            print("User wins with Rock against Scissor ")
            us=us+1
        # elif(r=="Rock" and user=="Scissor"):
        #     print("Computer wins against User Rock")
        #     cs=cs+1
        elif(user=="Paper" and r=="Rock"):
            print("User wins with paper against Rock")
            us=us+1
        # elif(r=="Paper" and user=="Rock"):
        #     print("Computer wins with paper against Rock")
        #     cs=cs+1
        elif(user=="Scissor" and r=="Paper"):
            print("User wins with Scissor against Paper")
            us=us+1
        # elif(r=="Scissor" and user=="Paper"):
        #     print("Computer wins with Scissor against Paper")
        #     cs=cs+1
        elif(r==user):
            print("Tied as both chose the same thing")
            us=us+1
            cs=cs+1
            x=x+1
        else:
            print("Computer wins")
            cs=cs+1
          
print("Game Ended")  
if(cs>us):
    print("Computer wins with score of ",cs)
elif(cs==us):
    print("Game Tied")
else:
    print("User wins with score of ",us)
