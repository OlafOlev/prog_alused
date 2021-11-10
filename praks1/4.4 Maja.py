from tkinter import *
raam = Tk()
raam.title("Maja")
tahvel = Canvas(raam, width = 1000, height = 1000, background="light blue")
#muru
tahvel.create_rectangle(0, 750, 1000, 1000,  fill = "green", outline="green", )
#maja kast
tahvel.create_rectangle(300, 500, 700, 900,  fill = "yellow",width = 5, outline="black", )
#maja katus
tahvel.create_polygon( 300, 500, 700, 500, 500, 300, 300, 500,   fill = "brown",width = 5, outline="black", )
#maja uks
tahvel.create_rectangle( 400, 700, 500, 900,  fill = "white",width = 5, outline="black", )
#maja aken
tahvel.create_rectangle( 550, 700, 650, 800,  fill = "white",width = 5, outline="black", )
#maja akna rist
tahvel.create_line( 600, 700, 600, 800, width = 5, )
tahvel.create_line( 550, 750, 650, 750, width = 5, )
tahvel.pack()
raam.mainloop()