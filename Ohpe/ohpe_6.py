# Tiedostojen lukeminen

with open("esimerkki.txt") as tiedosto:
    sisalto = tiedosto.read()
    print(sisalto)


def suurin():
    suurin = 0

    with open("luvut.txt") as tiedosto2:
        for i in tiedosto2:
            i = int(i)
            if i > suurin:
                suurin = i
    return suurin

# Tiedostojen kirjoittaminen


omistus = input("Kenelle teos omistetaan: ")
tiedostonimi = input("Mihin kirjoitetaan: ")
with open(tiedostonimi, "w") as file:
file.write(f"Hei {omistus}")

# Virhetilanteisiin varautuminen


def uusi_henkilo(nimi: str, ika: int):
    if nimi == "":
        raise ValueError("Unohdit syöttää henkilön nimen")
    elif len(nimi) > 40:
        raise ValueError("Syöttämäsi nimi on liian pitkä")
    elif ika < 0 or ika > 150:
        raise ValueError("Virheellinen ikä: " + str(ika))
    else:
        henkilo = (nimi, ika)
        return henkilo


if __name__ == "__main__":
    print(suurin())
    print(uusi_henkilo("Veikko Veikkanen", 21))
    print(uusi_henkilo("Viisa Laatuska", -1))
