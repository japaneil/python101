mytuple = tuple(("Neil",1,True))
newlist = list(mytuple)

(one, two, *hey) = mytuple
print(one)
print(two)
print(hey)

print(mytuple.count('Neil')) # count the number of times 'Neil' appears in the tuple
print(mytuple.index('Neil')) # start  looking for 'Neil' from index position