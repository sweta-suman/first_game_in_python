import random as r
list=['snake','water','gun']
comp_win=0
user_win=0
num=1
while(num!=5):
    m=r.choice(list)
    n=input("Enter your choice from snake,water or gun->")
    if m=="snake" and n=="water":
        print("Computer choice is--",m,"\nyour choice is--",n)
        print("snake will drink water and \nCOMPUTER wins here")
        comp_win+=1
    elif m=="water" and n=="gun":
        print("Computer choice is--",m,"\nyour choice is--",n)
        print("gun will sink water and \nCOMPUTER win here")
        comp_win+=1
    elif m=="snake" and n=="gun":
        print("Computer choice is--",m,"\nyour choice is--",n)
        print("gun will kill the snake and\n YOU win here")
        user_win+=1
    elif m=="water" and n=="snake":
        print("Computer choice is--",m,"\nyour choice is--",n)
        print("snake will drink water and\n YOU win here")
        user_win+=1
    elif m=="gun" and n=="water":
        print("Computer choice is--",m,"\nyour choice is--",n)
        print("gun will sink water and \nYOU win here")
        user_win+=1
    elif m=="gun" and n=="snake":
        print("Computer choice is--",m,"\nyour choice is--",n)
        print("gun will kill the snake and \nCOMPUTER win here")
        comp_win+=1
    else:
        print("Computer choice is--",m,"\nyour choice is--",n)
        print("NOONE WINS")        
    num+=1
print("Computer wins-->>",comp_win,"times")
print("YOU win-->>",user_win,"times")






    

