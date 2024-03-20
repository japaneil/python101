import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


print("\n")
cpu = int(random.choice("123"))
choice = int(
    input("Enter your choice ...\n1 for rock\n2 for paper\n3 for scissors!\n"))

print("\nYou chose " + str(RPS(choice)).replace("RPS.", ""))
print("Python chose " + str(RPS(cpu)).replace("RPS.", ""))
if choice == cpu:
    print("Draw")
elif (choice == 2 and cpu == 1) or (choice == 1 and cpu == 3) or (choice == 3 and cpu == 2):
    print("You win")
else:
    print("You lost!")
