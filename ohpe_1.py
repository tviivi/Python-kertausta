from math import sqrt

#Tietoa käyttäjältä

nimi = input("Anna nimi: ")
vuosi = input("Anna vuosi: ")

print(f"{nimi} on urhea ritari, syntynyt vuonna {vuosi}. Eräänä aamuna {nimi} heräsi kovaan meluun: lohikäärme lähestyi kylää. Vain {nimi} voisi pelastaa kylän asukkaat.")

#Lisää muuttujista

nimi = "Teppo Testaaja"
ika = 20
taito1 = "python"
taso1 = "aloittelija"
taito2 = "java"
taso2 = "veteraani"
taito3 = "ohjelmointi"
taso3 = "puoliammattilainen"
ala = 2000
yla = 3000

print(f"nimeni on {nimi}, olen {ika}-vuotias")
print("taitoihini kuuluvat")
print(f"- {taito1} ({taso1})")
print(f"- {taito2} ({taso2})")
print(f"- {taito3} ({taso3})")
print(f"haen työtä, josta maksetaan palkkaa {ala}-{yla} euroa kuussa")

#Laskentaa luvuilla

tulo = int(1)

tulo *= int(input("Anna luku 1: "))
tulo *= int(input("Anna luku 2: "))
tulo *= int(input("Anna luku 3: "))

print(f"Tulo on {tulo}")

#Ehtorakenne

print("Kerro huominen sääennuste:")
lampo = int(input("Lämpötila: "))
sade = input("Sataako (kyllä/ei): ")

print("Pue housut ja t-paita")
if lampo<20 and lampo>10:
    print("Ota myös pitkähihainen paita")
if lampo<10 and lampo>5:
    print("Pue päälle myös takki")
if lampo<5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")
if sade == "kyllä":
    print("Muista sateenvarjo!")

a = int(input("Anna a: "))
b = int(input("Anna b: "))
c = int(input("Anna c: "))

x1 = (-b+(sqrt(b*b-(4*a*c))))/(2*a)
x2 = (-b-(sqrt(b*b-(4*a*c))))/(2*a)

print(x1)
print(x2)