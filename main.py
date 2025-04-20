import random
'''
1 for "stone"
-1 for "paper"
0 for "scissor"
'''
computer = random.choice([-1,1,0])
print("Stone --> s\n","Paper --> p\n","Scissors-->sc")
youstr=input("Enter your choice:")
youDict={"s":1,"p":-1,"sc":0}
reverseDict={1:"Stone",-1:"Paper",0:"Scissor"}

you=youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("Its a draw.")
else:
    if(computer ==-1 and you==1):
        print("You lose! :( ")
    elif(computer==-1 and you==0):
        print("You win! :) ")
    elif(computer==1 and you==-1):
        print("You win! :) ")
    elif(computer==1 and you==0):
        print("You lose! :( ")
    elif(computer==0 and you==-1):
        print("You lose! :( ")
    elif(computer==0 and you==1):
        print("You win! :) ")

    else:
        print("Something went wrong :(")
