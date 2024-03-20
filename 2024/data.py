# STRING
# LITERAL ASSIGMENT
import math
first = "Neil"
last = "Arora"

print(type(first and last))
print(type(first and last) == str)
print(isinstance(first and last, str))
# -------------------------------------
print(" ")
# -------------------------------------
# CONSTRUCTOR FUNCTION
pizza = str("Cheese")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# CONCATENATION
fullname = first + " " + last
fullname += "!"
print(fullname)

# CASTING A NUM
year = str(2024)
year += " is the best year!"
print(year)

# MULTILINE
multiline = """
Hello   

hi     all good?

"""
print(multiline)

# Escapeing
sentence = 'I\'m back at work!\nHulu\\lulu!'
print(sentence)

# STRING METHODS
print(first)
print(first.lower())
print(first.upper())
print(first.capitalize())

print(multiline.title())
print(multiline.replace("good", "badiya"))
print(len(multiline))
print(multiline.strip())  # removes white space
# -------------------------------------
print(" ")
# -------------------------------------
# MENU PROJECT
title = "menu".upper()
print(title.center(22, "-"))
print("Coffee ".ljust(18, ".") + "$1".rjust(4))
print("Tea ".ljust(18, ".") + "$0.9".rjust(6, " "))
print("Cake ".ljust(18, ".") + "$7".rjust(4, " "))
# -------------------------------------
print(" ")
# -------------------------------------
# SRING INDEX VALUE
print(first[0].upper())
print(first[-1].upper())
print(first[1:-1].upper())
print(first[0:].upper())

# BOOLEAN DATA RETURN
print(first.startswith("n"))
print(first.endswith("l"))

# BOOLEAN
value = True
x = bool(False)
print(isinstance(value and x, bool))

# NUMERIC
# INT
price = 100
bestPrice = 90
print(price - bestPrice)

# FLOAT
gpa = 4
y = 1.119
print(isinstance(gpa and y, float))

# COMPLEX
comp = 5+3j
print(type(comp))
print(comp.real)
print(comp.imag)

# Builtin num func
print(abs(gpa * -1000))
print(round(gpa))
print(round(gpa, 10))


print(math.pi)
print(math.sqrt(65))
print(math.ceil(gpa))
print(math.floor(gpa))

# CASTING A STR TO NUM
zipcode = "110019"
zipcode = int(zipcode)
print(isinstance(zipcode, int))
