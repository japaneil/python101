Name1 = input("Please enter details of member 1:\nName: ")
Ins1 = input("Please enter details of member 1:\nInstrument: ")
Name2 = input("Please enter details of member 2:\nName: ")
Ins2 = input("Please enter details of member 2:\nInstrument: ")
Name3 = input("Please enter details of member 3:\nName: ")
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

print(band)
print("\nVariety of instruments are " +
      band["Member 1"]["Instrument"] + ", " +
      band["Member 2"]["Instrument"] + " and " +
      band["Member 3"]["Instrument"])
