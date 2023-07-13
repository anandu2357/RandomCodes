import random 
import time
lst=["Rock","Paper","Scissor"]
scp1,scp2=0,0
maxValue=int(input("Enter the maxpoints for winning :"))

while(scp1<=maxValue or scp2<=maxValue):
    plr1=random.choice(lst)
    plr2=random.choice(lst)
    time.sleep(3)
    if(plr1==plr2):
        print(f"Player 1 : {plr1}")
        print(f"Player 2 : {plr2}")
        print(f"TIE.....! TOTAL POINTS [PLAYER 1 :{scp1} PLAYER 2 :{scp2} ]")
    elif((plr1=='Rock' and plr2=='Scissor') or (plr1=='Paper' and plr2=='Rock') or (plr1=='Scissor' and plr2=='Paper')):
        print(f"Player 1 : {plr1}")
        print(f"Player 2 : {plr2}")
        scp1+=1
        print(f"PLAYER 1 GOT THE POINT ....! [PLAYER 1 :{scp1} PLAYER 2 :{scp2} ]")
    elif((plr2=='Rock' and plr1=='Scissor') or (plr2=='Paper' and plr1=='Rock') or (plr2=='Scissor' and plr1=='Paper')):
        scp2+=1
        print(f"Player 1 : {plr1}")
        print(f"Player 2 : {plr2}")
        print(f"PLAYER 2 GOT THE POINT ....! [PLAYER 1 :{scp1} PLAYER 2 :{scp2} ]")
    if(scp1==maxValue):
        print("PLAYER 1 WON")
        break
    elif(scp2==maxValue):
        print("PLAYER 2 WON")
        break
        