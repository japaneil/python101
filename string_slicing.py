name = "Neil Arora"
f_name = name[:4] #stopping index is exclusive
print(f_name)
l_name = name[5:]
print(l_name)
funk = name[::2]
print(funk)
reverse = name[::-1]
print(reverse)

#slice function

website = "www.youtube.com"
website1 = "www.google.com"
name1 = slice(4,-4)
print(website[name1])
print(website1[name1])