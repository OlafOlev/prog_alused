iseloos = input("Kas soovite istekohta ise valida (ise) või loosida (loos)?")
if iseloos == "ise":
    valikoht = input("Kas soovite istuda akna ääres(aken) või mitte (muu)?")
    if valikoht == "aken":
        print("Valisite ise. Aknakoht")
    if valikoht == "muu":
        print("Valisite ise. Vahekäigukoht")

if iseloos == "loos":
    import random
    r1 = random.randint(1, 3)
    if (r1 == 1) or (r1 == 2):
        print("Istekoht loositi. Vahekäigukoht")
    else:
        print("Istekoht loositi. Aknakoht")
    