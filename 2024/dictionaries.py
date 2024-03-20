band = {
    "Vocals": "Plant",
    "guitar": "Page"
}

print(band)
print(len(band))

# Access items
print(band["Vocals"])  # Access item by key
print(band.get("guitar"))

print(str(band.keys()).replace("dict_keys" and "(" and "[" and "]" and ")" and "'", "").lower(
).replace(",", " and"))   # Get all keys as a string without the dict_key part
print(band.values())  # Returns a view object of all the values in the dictionary
# Returns a view object of tuples containing the key and value pairs
print(band.items())

print(bool("guitar" in band))

band["Vocals"] = "Neil"
band.update({"drums": "Dave"})
print(band)

# Removes and returns an item with specified key (if present).
print(band.pop("drums"))
# If not provided, it removes and return an arbitrary (implementation-defined) item.
print(band)  # KeyError: 'drums'
band["drums"] = "John"
print(band)

# Returns and remove a (key, value) pair from the dictionary.
print(band.popitem())
print(band)

band["drums"] = "John"
del band["drums"]       # Deleting an item using its key
print(band)  # KeyError: 'drums'

mydic = dict(band)
print(mydic)

band2 = band  # Making another reference to the same dictionary

band3 = band.copy()
print(band3 == band2)      # True
print(band is band2)           # True

# Nested  dictionaries

member1 = {
    "Name":  "Tom",
    "Instrument": "Guitar"
}
member2 = {
    "Name":  "Neil",
    "Instrument": "Sax"
}
member3 = {
    "Name":  "Pranav",
    "Instrument": "Violin"
}
band = {
    "1": member1,
    "2": member2,
    "3": member3
}

print(band)
print(band["1"]["Name"])   # Accessing a nested value

band["1"]["Name"] = "New Tom"     # Changing a nested value
print(band)                          # KeyError
print(band["2"]["Instrument"] == "Sax")
