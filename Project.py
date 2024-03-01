import random

songs = [
"song1 - artist 1",
"song2 - artist 2",
"song3 - artist 3",
"song4 - artist 4",
"song5 - artist 5",
]

username = "a"
password = "a"
songguess = ()
songanswer = ()
userguess1 = ()
userguess2 = ()
score = ()
usernameuserinput = ()
usernameuserinput = input("Please enter your username: ")

print("  ")

passworduserinput = ()
passworduserinput = input("Please enter your password: ")

while usernameuserinput != username:
    print("Username or Password Incorrect! Try Again.")
    usernameuserinput = input("Please enter your username: ")
    print("  ")
    passworduserinput = input("Please enter your password: ")

while passworduserinput != password:
    print("Username or Password Incorrect! Try Again.")
    usernameuserinput = input("Please enter your username: ")
    print("  ")
    passworduserinput = input("Please enter your password: ")
print("  ")

print("Game Starting...")

print("  ")

print(
    "There will be one letter and the Artist's name. You have to guess the song name."
)

print("  ")

print(random.choice(songs)[0])
