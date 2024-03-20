mytuple = tuple(("Neil", 1, True))
newlist = list(mytuple)

(one, two, *hey) = mytuple
print(one)
print(two)
print(hey)

# count the number of times 'Neil' appears in the tuple
print(mytuple.count('Neil'))
print(mytuple.index('Neil'))  # start  looking for 'Neil' from index position
