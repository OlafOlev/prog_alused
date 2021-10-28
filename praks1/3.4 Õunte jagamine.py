pöialpoissi = int(input("Mitu põialpoissi tahab õuna? "))
from random import randint
i = 0
õun = 14
while i < pöialpoissi:
    i += 1
    r = randint(1,2)
    õun = õun - r
    print(str(r))
print("Lumivalgekesele jäi " + str(õun))