#Ohjelmoinnin termejä

sana = input("Anna sana: ")

if len(sana)>1:
    print(f"Sanassa {sana} on {len(sana)} kirjainta")
else:
    pass

#Lisää ehtolauseita

sana1 = input("Anna 1. sana: ")
sana2 = input("Anna 2. sana: ")

if sana1>sana2:
    print(f"{sana1} on aakkosjärjestyksessä viimeinen.")
elif sana1<sana2:
    print(f"{sana2} on aakkosjärjestyksessä viimeinen")
else:
    print("Annoit saman sanan kahdesti.")

#Ehtojen yhdistäminen

luku = int(input("Luku: "))
if luku % 3 == 0 and luku % 5 == 0:
    print("FizzBuzz") 
elif luku % 3 == 0:
    print("Fizz")
elif luku % 5 == 0:
    print("Buzz")

#Yksinkertainen silmukka

luvut = 0
summa = int(0)
neg = 0
pos = 0

while True:
    lukukysely = int(input("Lukuu: "))
    if lukukysely < 0:
        neg += 1
    if lukukysely > 0:
        pos += 1
    if lukukysely == 0:
        break
    summa += int(lukukysely)
    luvut += 1
print(f"Lukuja yhteensä {luvut}")
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa/luvut}")
print(f"Positiivisia {pos}")
print(f"Negatiivisia {neg}")