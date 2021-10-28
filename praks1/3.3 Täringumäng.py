täringuid = int(input("Täringute arv: "))
from random import randint
i = 0
while i < täringuid:
    r = randint(1, 6)
    i += 1
    print(str(r))
    
