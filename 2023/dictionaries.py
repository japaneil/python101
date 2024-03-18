capitals = {"USA":"Washington DC","India":"Delhi","China":"Bejing"}

print(capitals["India"])
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"NYC (Just Kidding)"})
capitals.pop("China")
#capitals.clear()
for key,value in capitals.items():
    print("The capital of "+key+" is "+value+".")