
import random
import time 
#import pyotp 
 

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
key = "NNQWS3TTOVWW2ZLSMZUWK3DE"
googleauth = ()
  
#uri = pyotp.totp.TOTP(key).provisioning_uri( 
    #name='Kain', 
    #issuer_name="Kain's Music Game")

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

# makes sure that the username & password is correct

while passworduserinput != password:
    print("Username or Password Incorrect! Try Again.")
    usernameuserinput = input("Please enter your username: ")
    print("  ")
    passworduserinput = input("Please enter your password: ")

print("  ")
#Google Authenticator OTP
#totp = pyotp.TOTP(key)
#two_factor_code = totp.now()
#googleauth = input("Please enter your Google Authenticator Code : ")

#while googleauth != two_factor_code:
    #print("Code Invalid. Try Again.")
    #print("")
    #googleauth = input("Please enter your Google Authenticator Code : ")
    
print("   ")

print("Game Starting...")

print("  ")

print(
    "There will be one letter and the Artist's name. You have to guess the song name."
)

print("   ")

songguess = random.choice(songs)

artist = songguess.split("-")
song = songguess.split("-")
print(artist[1])

print(song[0])

# picks a random song and displays the first letter

print("   ")

userguess1 = input("What do you think the song is? : ")

if userguess1 != song:
    print("Incorrect! You have one more chance!")
    print("  ")
    userguess2 = input("What do you think the song is? : ")
    print("  ")
    if userguess2 == song:
         print("Correct! Moving onto the next round...")
    if userguess2 !=song:
        print("Incorrect! Game Over!")
          


elif userguess1 == song:
    print("   ")
    print("Correct! Moving onto the next round...")
