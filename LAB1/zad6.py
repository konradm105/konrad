droga = random.randint(1, 1000)
print(f"Wylosowana droga do pokonania wynosi: {droga} km")

spalanie = float(input("podaj średnie spalanie (w litrach na 100 km): "))

cena_paliwa = float(input("podaj cenę paliwa za litr (zł): "))

zuzycie_paliwa = (droga / 100) * spalanie
koszt_podrozy = zuzycie_paliwa * cena_paliwa

print(f"przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} l")
print(f"szacowany koszt podróży: {koszt_podrozy:.2f} zł")