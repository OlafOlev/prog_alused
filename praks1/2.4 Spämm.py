kirja_suurus = float(input("Sisestage kirja suurus: "))
pealkiri = input("Sisestage kirja teema pealkiri: ")
fail = input("Kas kirjaga on kaasas fail? ")
if pealkiri == "" or fail == "jah" and kirja_suurus > 1:
    print("Kiri on spämm")
else:
    print("Kiri ei ole spämm")