import datetime
import numpy

# ini namanya list
waktutempat = str(datetime.date.today())
mahasiswa = [
    'ananta',
    2022071028,
    'informatika',
    'DesainAnalisisAlgoritma',
    waktutempat,
    'UniversitasPembangunanJaya'
]

for i in mahasiswa:
    print(f"{i} UPJ")