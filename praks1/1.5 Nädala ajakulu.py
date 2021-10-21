ainepunktide_arv = int(input("Sisestage ainepunktide arv: "))
nädalate_arv = int(input("Sisestage nädalate arv: "))
tunnid = ainepunktide_arv * 26
nädala_ajakulu = round(tunnid / nädalate_arv)
print("Teie ajakulu nädalas on " + str(nädala_ajakulu))
