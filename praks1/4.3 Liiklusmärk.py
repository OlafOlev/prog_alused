from tkinter import *
raam = Tk()
raam.title("Peatee märk")
tahvel = Canvas(raam, width = 1000, height = 1000)
#välis must ruut
tahvel.create_polygon(500, 0, 1000, 500, 500, 1000, 0, 500, 500, 0, fill = "white",width = 10, outline="black", )
#sise must ruut kollane sisem
tahvel.create_polygon(500, 100, 900, 500, 500, 900, 100, 500, 500, 100, fill = "yellow",width = 8, outline="black", )
tahvel.pack()
raam.mainloop()