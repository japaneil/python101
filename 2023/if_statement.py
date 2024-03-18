age = int(input("how old are you?: "))

if age >= 18:
    if age == 100:
        print("You are old")
        exit()
    print("You are an adult")

elif age<0:
    print("You are not born yet")
else:
    print("You are a child")