import requests
kuu = input("Sisestage kuu: ").replace("ä","a")
päev = int(input("Sisestage päev: "))
url = "http://kodu.ut.ee/~eno/mooc/" + kuu
output = requests.get(url).text
data = output.splitlines()
x = 0
for rida in data:
    x += 1
    if x == päev:
        print("Kuupäeval " + str(päev) + ". " + str(kuu) + " on nimepäevad jõrgmiste nimedega inimestel:")
        print(rida)
