from datetime import *

# Oliot ja metodit


def rivien_summat(matriisi: list):

    for i in range(len(matriisi)):
        summa = 0
        for j in range(len(matriisi)):
            summa += matriisi[i][j]
        matriisi[i].append(summa)

# Luokat ja oliot


def vuodet_listaan(paivamaarat: list):
    apulista = []
    for i in range(len(paivamaarat)):
        apulista.append(paivamaarat[i].year)
    apulista.sort()
    paivamaarat = apulista[:]
    return paivamaarat


if __name__ == "__main__":

    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)

    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1993, 5, 9)

    vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
    print(vuodet)


class Kirja:
    def __init__(self, nimi: str, kirjoittaja: str, genre: str, kirjoitusvuosi: int):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.genre = genre
        self.kirjoitusvuosi = kirjoitusvuosi


def vanhempi_kirja(kirja1: Kirja, kirja2: Kirja):
    if kirja1.kirjoitusvuosi < kirja2.kirjoitusvuosi:
        return (f"{kirja1.nimi} on vanhempi, se kirjoitettiin {kirja1.kirjoitusvuosi}")
    else:
        return (f"{kirja2.nimi} on vanhempi, se kirjoitettiin {kirja2.kirjoitusvuosi}")


def genren_kirjat(kirjat: list, genre: str):
    haluttugenre = []
    for i in range(len(kirjat)):
        if kirjat[i].genre == genre:
            haluttugenre.append(kirjat[i])
    return haluttugenre


python = Kirja("Fluent Python", "Luciano Ramalho", "ohjelmointi", 2015)
everest = Kirja("Huipulta huipulle", "Carina Räihä", "elämänkerta", 2010)
norma = Kirja("Norma", "Sofi Oksanen", "rikos", 2015)

kirjat = [python, everest, norma, Kirja("Lumiukko", "Jo Nesbø", "rikos", 2007)]

print("rikoskirjoja ovat")
for kirja in genren_kirjat(kirjat, "rikos"):
    print(f"{kirja.kirjoittaja}: {kirja.nimi}")

print(f"{python.kirjoittaja}: {python.nimi} ({python.kirjoitusvuosi})")
print(f"Kirjan {everest.nimi} genre on {everest.genre}")
print(vanhempi_kirja(python, everest))
