from laskin import Laskin

print("--------------------------------------------------------------------------------------------")
print("Hei, olen laskin. Anna minulle pari numeroa niin lasken sinulle haluamasi laskutoimituksen!")
print("Laskin pysyy käynnissä, pyydetty vastaus tulee aina valintavaihtoehtojen yläpuolelle!")
print("---------------------------------------------------------------------------------------------")
a = int(input("Anna ensimmäinen numero:"))
b = int(input("Anna toinen numero:"))

lasku = Laskin(a,b)
valinta=1

while valinta != 0:
    print("0) Poistu","\n1)Summa","\n2)Vähennyslasku","\n3)Kertolasku","\n4)Jakolasku")
    valinta=int(input("Valitse haluamasi laskutoimitus:"))
    if valinta == 1:
        print("Valitsemasi laskutoimituksen vastaus:", lasku.summa())
    elif valinta == 2:
        print("Valitsemasi laskutoimituksen vastaus:",lasku.vahennys())
    elif valinta == 3:
        print("Valitsemasi laskutoimituksen vastaus:", lasku.kerto())
    elif valinta == 4:
        print("Valitsemasi laskutoimituksen vastaus:", round(lasku.jako(),2))
    elif valinta == 0:
        print("Laskin sulkeutuu...")
    else:
        print("Valitsethan numeron 0-4, kiitos")

print()
    