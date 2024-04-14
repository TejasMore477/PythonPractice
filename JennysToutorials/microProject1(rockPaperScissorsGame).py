import random

print("THE ROCK-PAPER-SCISSORS GAME \n YOU VS COMPUTER ")
print()
print("enter 0 for rock \n enter 1 for paper \n enter 2 for scissor")
print()
value = int(input("enter your choice :"))

computerChoice = random.randint(0, 2)
print(f"computerChoice = {computerChoice}")
if computerChoice == 0 and value == 0:
    print("match draw")
elif computerChoice == 0 and value == 1:
    print("you win")
elif computerChoice == 0 and value == 2:
    print("you loose")
elif computerChoice == 1 and value == 0:
    print("you loose")
elif computerChoice == 1 and value == 1:
    print("match draw")
elif computerChoice == 1 and value == 2:
    print("you win")
elif computerChoice == 2 and value == 0:
    print("you win")
elif computerChoice == 2 and value == 1:
    print("you loose")
elif computerChoice == 2 and value == 2:
    print("match draw")
else:
    print(f"invalid input :{value}")


