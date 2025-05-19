# ARSENAL
pemain = {
    2: ("William Saliba", 23),
    3: ("Kieran Tierney", 27),
    4: ("Ben White", 27),
    6: ("Gabriel Magalhães", 27),
    7: ("Bukayo Saka", 23),
    8: ("Martin Ødegaard", 26),
    11: ("Gabriel Martinelli", 23),
    19: ("Leandro Trossard", 29),
    22: ("David Raya", 29),
    29: ("Kai Havertz", 25),
    41: ("Declan Rice", 26),
}


print("=" * 45)
print(f" {'Nomor Punggung':<12}  {'Nama':<20}  {'Umur':<5} ")
print("=" * 45)


for nomor, (nama, umur) in pemain.items():
    print(f" {nomor:<12}   {nama:<20}  {umur:<5} ")

print("=" * 45)