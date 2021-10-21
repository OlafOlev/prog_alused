inimeste_arv = int(input("Sisestage inimeste arv "))
kohtade_arv = int(input("Kohtade arv bussis on: "))
busside_arv = inimeste_arv // kohtade_arv
mahajääk = inimeste_arv % kohtade_arv
 
print("Maha jääb " + str(mahajääk) + " inimest ja ära sõidab " + str(busside_arv) + " bussi")