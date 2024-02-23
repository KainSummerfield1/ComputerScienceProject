import random

login1 = ("user1:password1")


loginuserinput = ()
loginuserinput = input("Please enter your login (must be seperated with a colon) : ")

while login1 !=loginuserinput:
    print("wrong login! try again!")
    loginuserinput = input("Please enter your login (must be seperated with a colon) : ")
print("game starting!")
    
        
file = open("songs.txt","r")
