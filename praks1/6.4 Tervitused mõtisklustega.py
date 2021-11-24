def tervitus(kord):
    for i in range(0 , kord):
        print("""Võõrustaja: "Tere!" """)
        print("Täna " + str(i + 1) + ". kord tervitada, mõtiskleb võõrustaja.")
        print("""Külaline: "Tere, suur tänu kutse eest!" """)
tervitus(int(input("Sisestage külaliste arv:")))