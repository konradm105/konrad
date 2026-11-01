print(type(1+2))
print(type(1 + 4.5  ))
print(type(3 / 2  ))
print(type(4 / 2 ))
print(type(3 // 2))
print(type(-3 // 2  ))
print(type(11 % 2  ))
print(type(2 ** 10))
print(type(8 ** (1/3) ))

print("1. int(3.0) =", int(3.0))
#konwersja liczby zmiennoprzecinkowej (float) na całkowitą (int). Odcina część ułamkową.

print("2. float(3) =", float(3))
#konwersja liczby całkowitej (int) na zmiennoprzecinkową (float). Zwraca 3.0.

print("3. float(\"3\") =", float("3"))
#konwersja łańcucha znaków (str) na liczbę zmiennoprzecinkową (float).

print("4. str(12.4) =", repr(str(12.4)))
#konwersja liczby (float) na tekst (string). Zwraca "12.4". Użyto funkcji repr() w print, aby wyraźnie pokazać cudzysłowy w konsoli.

print("5. bool(0) =", bool(0))
#konwersja liczby na wartość logiczną (bool). Liczba 0 jest zawsze konwertowana na fałsz (False).