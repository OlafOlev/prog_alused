ringid = int(input("Sisesta ringide arv: "))
ringid += 1
porgandid = 0
for i in range(2, ringid, 2):
    porgandid += i
print("Porgandite kogu arv on " + str(porgandid) + ".")