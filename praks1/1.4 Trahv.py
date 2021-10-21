nimi = str(input("Sisestage oma nimi: "))
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
if lubatud_kiirus >= tegelik_kiirus:
    print("Tubli, et ei kiirusta")
if lubatud_kiirus < tegelik_kiirus:
    trahv = tegelik_kiirus - lubatud_kiirus 
    trahv = trahv * 3
    if trahv >= 190:
        trahv = 190
    print(nimi + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot")
    
    
    
    