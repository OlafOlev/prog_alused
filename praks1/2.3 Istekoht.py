iseloos = input("Kas soovite istekohta ise valida (ise) või loosida (loos)?")
if iseloos == "ise":
    valikoht = input("Kas soovite istuda akna ääres(aken) või mitte (muu)?")
    if valikoht == "aken":
        print("Valisite ise. Aknakoht")
    elif valikoht == "muu":
        print("Valisite ise. Vahekäigukoht")

elif iseloos == "loos":
    from random import randint
    r1 = randint(1, 3)
    if (r1 >= 2):
        print("Istekoht loositi. Vahekäigukoht")
    else:
        print("Istekoht loositi. Aknakoht")
    