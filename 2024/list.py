from enum import Enum

class size(Enum):
    BIG = 3
    MID = 2
    SMALL = 1

users = ["Neil","Pranav"]
print("Neil" in users)
print(users[0])
print(users[-2])
print(users.index("Neil"))
print(str(users[0:]).replace(","," and").replace("'",""))
print(str(users[-1:]).replace(","," and").replace("'",""))
print("The size of your list is " + str(size(len(users))).replace("size.","").lower()+".")