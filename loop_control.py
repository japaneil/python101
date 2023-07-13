while True:
    name = input("enter name:")
    if name != "":
        break

phone = "123432234"

for i in (phone):
    if i == "3":
        continue #skips to next iteration
    print(i, end="")

print()

for j in range(1,21):
    if j == 13:
        pass
    else:
        print(j)