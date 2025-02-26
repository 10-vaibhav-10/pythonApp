import random
import time

OPERATOR=["+","-","*"]
Min_Operand=2
Max_Operand=9
Total_Problems=10

def gen_problem():
    left=random.randint(Min_Operand,Max_Operand)
    right=random.randint(Min_Operand,Max_Operand)
    operator=random.choice(OPERATOR)
    
    expression=str(left)+" "+operator+" " +str(right)
    ans=eval(expression)    #evaluates any statement in python as expression
    return expression, ans

wrong=0

input("Press any key to start: ")
print("--------------------------")

start_time=time.time()
for i in range(Total_Problems):
    expression,ans=gen_problem()
    while True:
        print("Problem no:"+str(i+1)+ " : ")
        write_answer=input(expression+ " = ")
        if write_answer==str(ans):
            break
        wrong=wrong+1
end_time=time.time()
print("--------------------------")
time_Taken=round(end_time-start_time,2) #rounding off to last 2 digits
print("You took total of ",time_Taken," to attempt the questions.")
print("You also committed total of "+str(wrong)+ " mistakes")    
    
    
    
    
    