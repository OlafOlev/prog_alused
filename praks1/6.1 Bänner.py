def reklaam():
    korda = int(input("Mitu korda soovite reklaamlauset kuvada? "))
    reklaamlause = lause()
    for i in range(0, korda):
        print(reklaamlause)
def lause():
    reklaamlause = input("Sisestage reklaamlause: ")
    return reklaamlause.upper()
reklaam()