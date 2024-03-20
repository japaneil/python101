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

users.append("Satvik")

users += ["Jason","Dave","Mia"]
print(users)

users.extend(["Robets","Jimmy"])
print(users)

users.insert(0,"Alice")
print(users)

users.remove("Satvik")
print("\n" + str(users))

# del users
# print(users)

# users.clear()
# print(users)
users.insert(0,"alice")
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [1,2,3,4,5,6,7]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums))

numscopy = nums.copy()
mynums = list(nums)
myset = nums[0:]

print(numscopy)
print(sorted(mynums))
print(myset)

mylist = list([0,1,2,3,4,5,6,7,8,9])
print(len(mylist), mylist[:3], mylist[-3:]) 