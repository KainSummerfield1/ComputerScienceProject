import random
username = "user1"
password = "password"
song = ()
userguess1 = ()
userguess2 = ()
usernameuserinput = ()
usernameuserinput = input("Please enter your username: ")

passworduserinput = ()
passworduserinput = input("Please enter your password: ")

while usernameuserinput != username:
    print("Username or Password Incorrect! Try Again.")
    usernameuserinput = input(
        "Please enter your username: ")
    passworduserinput = input("Please enter your password: ")

while passworduserinput != password:
    print("Username or Password Incorrect! Try Again.")
    usernameuserinput = input(
        "Please enter your username: ")
    passworduserinput = input("Please enter your password: ")

print ("Game Starting...")

song = random.choice(open('songs.txt').readlines())

print(song)
