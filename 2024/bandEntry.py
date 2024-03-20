# Get name for first member
Name1 = input("Please enter details of member 1:\nName: ")
# Get instrument for first member
Ins1 = input("Please enter details of member 1:\nInstrument: ")
# Get name for second member
Name2 = input("Please enter details of member 2:\nName: ")
# Get instrument for second member
Ins2 = input("Please enter details of member 2:\nInstrument: ")
# Get name for third member (if present)
Name3 = input("Please enter details of member 3:\nName: ")
# Get instrument for third member
Ins3 = input("Please enter details of member 3:\nInstrument: ")

mem1 = {
    "Name": Name1,
    "Instrument": Ins1
}
mem2 = {
    "Name": Name2,
    "Instrument": Ins2
}
mem3 = {
    "Name": Name3,
    "Instrument": Ins3
}

band = {
    "Member 1": mem1,
    "Member 2": mem2,
    "Member 3": mem3
}

print(band)  # Print out the band information
print("\nVariety of instruments are " +
      band["Member 1"]["Instrument"] + ", " +
      band["Member 2"]["Instrument"] + " and " +
      band["Member 3"]["Instrument"])
