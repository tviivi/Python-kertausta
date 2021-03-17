# Lisää listoista

def pisin(merkkijonot: list):
    i = 0
    pisinmerkkijono = ""
    for i in range(len(merkkijonot)):
        if len(merkkijonot[i]) > len(pisinmerkkijono):
            pisinmerkkijono = merkkijonot[i]
    return pisinmerkkijono


def kumpivoitti(pelilauta: list):
    nollat = 0
    ykkoset = 0

    for i in range(len(pelilauta)):
        for j in range(len(pelilauta)):
            if pelilauta[i][j] == 0:
                nollat += 1
            if pelilauta[i][j] == 1:
                ykkoset += 1

    if nollat > ykkoset:
        return 0
    if ykkoset > nollat:
        return 1

# Viittaukset


def transponoi(matriisi: list):
    n = len(matriisi)
    uusimatriisi = [[0]*n for i in range(n)]
    print(uusimatriisi)
    for i in range(len(matriisi)):
        for j in range(len(matriisi)):
            uusimatriisi[j][i] = matriisi[i][j]

    for k in range(len(matriisi)):
        matriisi[k] = uusimatriisi[k]

# Sanakirja


def kertaa_kymmenen(alku: int, loppu: int):
    lista = {}
    for i in range(alku, loppu+1):
        lista[i] = 10*i
    return lista


def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):
    elokuva = {"nimi": nimi, "ohjaaja": ohjaaja,
               "vuosi": vuosi, "pituus": pituus}
    rekisteri.append(elokuva)

# Tuple


def vanhin(henkilot: list):
    for i in range(len(henkilot)):
        print(henkilot[i])
# Miten päästään käsiksi henkilön kahteen eri parametriin?


if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    pelilauta = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 1, 0]
    ]
    matriisi = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(pisin(jonot))
    print(kumpivoitti(pelilauta))
    print(transponoi(matriisi))

    d = kertaa_kymmenen(3, 6)
    print(d)

    rekisteri = []
    lisaa_elokuva(rekisteri, "Pythonin viemää", "Pekka Python", 2017, 116)
    lisaa_elokuva(rekisteri, "Python lentokoneessa",
                  "Renny Pytholin", 2001, 94)
    print(rekisteri)

    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]
    print(vanhin(hlista))
