from fractions import *
from random import *
from datetime import *

# Moduulit


def jaa_palasiksi(maara: int):
    lista = []
    for p in range(maara):
        lista.append(Fraction(1, maara))
    return lista

# Satunnaisuus


def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    kaikki_luvut = list(range(alaraja, ylaraja))
    rivi = sample(kaikki_luvut, maara)
    rivi.sort()
    return rivi

# Aikojen käsittely


tiedosto = input("Mihin kirjoitetaan: ")
aloituspaiva = input("Aloituspäivä: ")
aloitus = datetime.strptime(aloituspaiva, "%d.%m.%Y")
aloitus.strftime("%d.%m.%Y")
paivia = int(input("Montako päivää: "))
# ok
aikavali = aloitus + timedelta(days=paivia)
aikavali.strftime("%d.%m.%Y")
print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite)")
pvmlista = []
for i in range(paivia):
    paiva = aloitus + timedelta(days=i)
    ruutuaika = input(f"Ruutuaika {paiva}: ")
    pvmlista.append(f"{paiva}: {ruutuaika}")
print(pvmlista)
with open(tiedosto, "w") as file:
file.write(f"Ajanjakso: {aloitus.strftime(" % d. % m. % Y")}\n")
file.write(pvmlista)

if __name__ == "__main__":
    print(jaa_palasiksi(5))
    print(lottonumerot(7, 1, 41))
