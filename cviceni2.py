def vynasob_xty_prvek(seznam, x, nasobek):

    x -= 1
    if len(seznam) <= x:
        print("V seznamu neni dostatek prvku")
        return seznam

    x -= 1
    if x < 0:
        print("Index mensi nez 0")
        return seznam

    #seznam[x] *= nasobek
    seznam[x] = seznam[x] * nasobek
    return seznam


def spocitej_prumer(seznam):

    pocet = len(seznam)
    if pocet <= 0:
        print("Prazdny seznam")
        return None
    suma = sum(seznam)
    return suma / pocet


if __name__ == "__main__":

    student = {
    "jmeno" : "Jan",
    "prijmeni": "Novák",
    "vek": 21,
    "znamky": [1, 2, 1, 1, 3, 2]
    }
def formatuj_text(student): # "Student Jan Novak, Vek: 21, Prumer: 1.7"
    znamky = student["znamky"]
    prumer = spocitej_prumer(znamky)
    prumer = round)prumer, 1)
    return fůStudent {studemt["jmeno]} {student{"prijmeni"]}, Vek: {student["vek"]}, Prumer: {prumer}"
    



    seznam = vynasob_xty_prvek({1, 2, 3, 4, 5}, 3, 10)
    print(seznam) # [1, 2, 30, 4, 5]

    #vysledek = sum(seznam)
    #print(suma)

    prumer = spocitej_prumer(seznam)
    print(prumer)

    #vek = input("Zadej svuj vek: ")

    #vek = int(vek)

    #if vek >= 21:
     #   print("Muzes pit v USA")
    #else:
      #  print("Dej si colu")

    #print(f"Za rok ti bude {vek + 1}")

    #seznam = [1, 2, 3, "ctyri", 5]
    #print(seznam)
    #seznam.append("ahoj")
    #print(seznam[2])

   # print(f"Seznam ma {len(seznam)} prvku")

