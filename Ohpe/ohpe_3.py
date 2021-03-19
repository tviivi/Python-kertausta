#Ehdot silmukoissa

luku = int(input("Mihin asti: "))
summa = int(0)
apu = int(0)

print(f"Luku {luku}")
while luku > summa:
    apu += 1
    print(f"apu {apu}")
    summa += apu
print(summa)

#Merkkijonojen käsittely

sana = input("Anna merkkijono: ")
apu1 = int(0)
apu2 = int(len(sana))

while apu1 < len(sana):
    print(sana[apu2-1])
    apu2 -= 1
    apu1 += 1

merkkijono = input("Anna merkkijono: ")
merkki = input("Merkki: ")
kohta = merkkijono.find(merkki)
jono = kohta
kierroslaskuri = int(0)

if merkki in merkkijono:
    while int(len(merkkijono)) > jono:
        print(merkkijono[kohta])
        jono += 1
        kohta += 1
        kierroslaskuri +=1
        if kierroslaskuri == 3:
            break

#Lisää silmukoista

kayttajanluku = int(input("Anna luku: "))
i = int(1)
while i < kayttajanluku:
    print(i)
    print(kayttajanluku)
    i += 1
    kayttajanluku -= 1

#Omat funktiot

def risunelio(numba):
    i = 0
    while i < numba:
        j = 0
        while j < numba:
            j += 1
            print("#", end = "")
        i += 1
        print("")

if __name__ == "__main__":
    risunelio(3)