def elutee(s):
    n = 0
    for i in s:
        if i != ".":
            n += int(i)
    if n < 10:
        return n
    else:
        return elutee(str(n))
a = 1
while a < 10:
    fail1 = open("eluteenumber" + str(a) + ".txt", "x")
    fail1.close()
    a += 1
fail = open("sunnikuupaevad.txt")
o = 1
for rida in fail:
    eluteenumber = elutee(rida[:-1])
    while eluteenumber != o:
        o += 1
    failinimi = "eluteenumber" + str(o)
    fail2 = open(failinimi + ".txt", "a", encoding = "UTF-8")
    fail2.write(rida +"\n")
    fail2.close()
    o = 1