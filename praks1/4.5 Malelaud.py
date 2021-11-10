from tkinter import *
raam = Tk()
raam.title("Malelaud")
tahvel = Canvas(raam, width = 800, height = 800,)
#x1 ja y1 on kasti ülemise vasaku nurga koordinaadid
x1 = 0
y1 = 0
#x2 ja y2 on kasti alumise parema nurga koordinaadid
x2 = 100
y2 = 100
#i on vaja meil valgede ja mustade kastide vahetamiseks
i = 0
#j on vaja meil selleks et algus kast vahektuks iga rida, et oleks esimesel real valge, teisel must, kolmandal valge, jne
j = 1
#esimeses tsüklis me vahetame mis real program joonistab kaste 
while y2 <= 800:
    #teises tsüklis me vahetame kuhu program joonistab kasti vasakult paremale
    while x2 <= 800:
        #Siin vahetame mis värvi kasti program joonistab
        if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            tahvel.create_rectangle(x1, y1, x2, y2,  fill = "white", outline="white", )
        if i == 1 or i == 3 or i == 5 or i == 7:
            tahvel.create_rectangle(x1, y1, x2, y2,  fill = "black", outline="black", )
        #lisame i-le 1 juurde et järgmine kast oleks teist värvi
        i += 1
        #lisame x koordinaadidele 100 juurde, et järgmine kast oleks ühe ruudu võrra paremal
        x1 += 100
        x2 += 100
    #lisame y koordinaadidele 100 juurde, et joonistada uut rida
    y1 += 100
    y2 += 100
    #paneme x koordinaadid tagasi mis enne olid, et alustaks vaskult uuesti
    x1 = 0
    x2 = 100
    #siin vahetame mis värviga ruut järgmine rida hakkab
    if j == 0 or j == 2 or j == 4 or j == 6:
       i = 0
    if j == 1 or j == 3 or j == 5 or j == 7:
       i = 1
    j += 1
    
tahvel.pack()
raam.mainloop()