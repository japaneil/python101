silver = {"spoon","fork","knife","knife"}

silver.add("napkin")
silver.remove("knife")
#silver.clear()

dishes = {"bowl","plate", "cup","knife"}
silver.update(dishes) #adds dishes to silver

dinner_table = silver.union(dishes) #creates new set with data of dishes and silver

for i in dinner_table:
    print(i)

print()

print(silver.difference(dishes))
print(silver.intersection(dishes)) #returns what is common in both sets