#Lisää funktioista

def samat(mjono, eka, toka):
    if len(mjono) < eka or len(mjono) < toka:
        return False
    if mjono[eka] == mjono[toka]:
        return True
    else:
        return False

#Listat

lukumaara = int(input("Kuinka monta lukua: "))
i = 0
lista = []

while i < lukumaara:
    uusiluku = int(input(f"Anna luku {i+1}: "))
    lista.append(uusiluku)
    uusiluku = 0
    i += 1
print(lista)

def keskiarvo(lista):
    i = 0
    summa = 0
    while i < len(lista):
        summa += lista[i]
        i += 1
    return summa/len(lista)

#Silmukat ja iterointi

def lista_tahtina(lista2):
    k = 0
    for k in range(len(lista2)):
        print(lista2[k]*"*")
        k += 1

#Tulostuksen muotoilu

def muotoile(lista3):
    j = 0
    for j in range(len(lista3)):
        return(round(lista3[j], 2))

#Lisää merkkijonoista ja listoista

def pisin_naapurijono(lista4):
    l = 1
    summa = 0
    for l in range(len(lista4)):
        edeltava = lista4[l-1]
        nykyinen = lista4[l]
        if nykyinen == edeltava + 1 or edeltava == nykyinen - 1:
            summa += 1
    print(summa)

if __name__ == "__main__":
    print(samat("koodari", 1, 10))
    print(keskiarvo([1, 2, 6, 4]))
    print(lista_tahtina([3, 4, 2]))
    print(muotoile([1.234, 0.333, 0.1111, 3.446]))
    print(pisin_naapurijono([1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]))