import random

print("let's play rock paper scissors!")
n=int(input("how many times do you want to play?"))
cu=0
cc=0
for i in range(n):
    c=random.choice(["rock","paper","scissors"])
    b = input("Enter rock, paper, or scissors: ").lower()
    if c=="rock" and b=="paper":
        print(" 1 points to each")
    elif c==b:
        print(" 0 points to you")
        cu+=1
    elif c=="rock" and b=="scissors":
        print(" 1 points to me")
        cc+=1
    elif c=="paper" and b=="rock":
        print(" 1 points to me")
        cc+=1
    elif c=="paper" and b=="scissors":
        print(" 1 points to you")
        cu+=1
    elif c=="scissors" and b=="paper":
        print(" 1 points to me")
        cc+=1
    elif c=="scissors" and b=="rock":
        print(" 1 points to you")
        cu+=1
    else:
        print("invalid input")
        break
if cu==cc:
    print("both wins")
elif cu>cc:
    print("you win")
else:
    print("you lose")
