print("Tere!")
print("Arva ära mis arvu ma mõtlen?")
from random import randint
rand = randint (1,10000)
kordumine = True
while(kordumine):
    suvaline = int(input("Sinu pakkumine: "))
    if suvaline > rand:
        print("See arv, mis mu pead vaevab on väiksem.")
    if suvaline < rand:
        print("See arv, mis mu pead vaevab on suurem.")
    if suvaline == rand:
        kordumine = False
    if(kordumine == False):
        break
print("Tubli oled! Vastus tõesti oli " + str(rand) + ".")