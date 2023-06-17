temp = int(input("what is the temperature outside?: "))

if not(temp>=0 and temp<=35):
    print("stay at home")
    print("temperature is bad")
elif not(temp<0 or temp>35):
    print("The temperature is good today")
