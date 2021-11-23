def mahlapakkide_arv():
    õun = int(input("Mitu kilogrammi õunu on? "))
    mahlapakkide_arv = round(õun*0.4/3)
    print(str(õun) + " kilogrammi õunte eest saab " + str(mahlapakkide_arv) + " mahlapakki")
mahlapakkide_arv()