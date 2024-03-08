import random

# importing random for chosing random song

songs = [
"1test - artist1",
"2test - artist2",
"3test - artist3",
"4test - artist4",
"5test - artist5",
]

# list of songs

username = "a"
password = "a"
songguess = ()
songanswer = ()
userguess1 = ()
userguess2 = ()
score = ()
usernameuserinput = ()

# required variables

usernameuserinput = input("Please enter your username: ")

print("  ")

passworduserinput = ()
passworduserinput = input("Please enter your password: ")

while usernameuserinput != username:
    print("Username or Password Incorrect! Try Again.")
    usernameuserinput = input("Please enter your username: ")
    print("  ")
    passworduserinput = input("Please enter your password: ")

# makes sure that the username + password is correct

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


songguess = random.choice(songs)

print(songguess[0])

# picks a random song and displays the first letter

print("   ")

userguess1 = input("What do you think the song is? : ")

if userguess1 != songguess:
    print("Incorrect! You have one more chance!")
    print("  ")
    userguess2 = input("What do you think the song is? : ")
    print("  ")
    if userguess2 == songguess:
         print("Correct! Moving onto the next round...")
    if userguess2 !=songguess:
        print("Incorrect! Game Over!")
          


elif userguess1 == songguess:
    print("")
    print("Correct! Moving onto the next round...")




















