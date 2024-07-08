import numpy as np
import time

# gun start
print("  _=---__________________-----------)           ")
print(" |______________________|  {‾‾‾‾‾‾} \  /‾       ")
print("  |_____________________|‾‾{------}‾ \(         ")
print("                        \ ‾{______}‾‾ ‾‾‾)      ")
print("                         \__________  /‾‾\      ")
print("                            \    )  \/    \     ")
print("                             \__/____)  o  \    ")
print("                                      \     \   ")
print("                                      |   o  \  ")
print("                                      |       \ ")
print("                                      ‾‾‾‾‾‾‾‾‾ ")
print("                    RUSSIAN ROULETTE")
print("__________________________________________________________")
print("Dealer: 'We'll be playing russian roulette. I expect you to know the rules. So first, what's your name?'")
time.sleep(1)
name = input("Enter your name: ")
print("Dealer: So",name,"huh. Okay...6 bullets, 5 blanks and 1 live. You're going first")
time.sleep(1)

bl = "'Blank'"
lv = "BANG! You are now dead because of skill issue"
Dlv = "BANG! Now the dealer is dead, you now won the prize"


# Player's turn
while True:
    st = input("Type 'start' to pull the trigger: ").lower() #accept any case
    if st != "start":
        continue

    bullet = np.random.randint(1, 6)
    dead = 4
    # place holder
    # print("Bullet number", bullet)
    # print("Live:", dead)
    if bullet == dead:
        print(".")
        time.sleep(0.5) #0.5sec timer 
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(lv)
        exit(0)
    else:
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5) 
        print(bl)
        time.sleep(1)
        print("Dealer: 'Okay now it's my turn'")


# Dealer's turns
    bullet = np.random.randint(1, 6)  # Generate a new number for the dealer
    dead = 4    # Generate a new number for the dealer
    # place holder
    # print("Bullet number", bullet)
    # print("Live:", dead)
    if bullet == dead:
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5) 
        print(Dlv)
        exit(0)
    else:
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5) 
        print(bl)
        time.sleep(1)
        print("Dealer: 'Now it's your turn'")








# add choice play or quit at the start
# add timer every word
# make the stakes higher or lower randomly