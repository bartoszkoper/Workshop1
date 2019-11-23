"""#### Warsztat: Kostka do gry
​
W grach planszowych i papierowych RPG używa się wielu rodzajów kostek do gry, nie tylko tych dobrze znanych, sześciennych.
Jedną z popularniejszych kości jest np. kostka dziesięciościenna, a nawet stuścienna!
Jako że w grach kośćmi rzuca się często, pisanie za każdym razem np. _"rzuć dwiema kostkami dziesięciościennymi,a do wyniku dodaj 20"_
byłoby nudne, trudne i marnowałoby ogromne ilości papieru. W takich sytuacjach używa się kodu _"rzuć 2D10+20"_.
​
Kod takiej kostki wygląda następująco:
​
### xDy+z
​
gdzie:
* __y__ &ndash; rodzaj kostek, których należy użyć (np. D6, D10),
* __x__ &ndash; liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
* __z__ &ndash; liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).
​
__Przykłady:__

* __2D10+10__: 2 rzuty D10, do wyniku dodaj 10,
* __D6__: zwykły rzut kostką sześcienną,
* __2D3__: rzut dwiema kostkami trójściennymi,
* __D12-1__: rzut kością D12, od wyniku odejmij 1.
​
Napisz funkcję, która:
​
* przyjmie w parametrze taki kod w postaci stringa,
* rozpozna wszystkie dane wejściowe:
    * rodzaj kostki,
    * liczbę rzutów,
    * modyfikator,
* wykona symulację rzutów i zwróci wynik.
​
Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.   """

from random import randint

kostki = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']


def rzut(string: str) -> None:
    for each in kostki:
        if each in string:
            podzial = string.partition(each)
            liczba_rzutow,rodzaj_kostki,modyfikator = podzial

        else:
            pass

    try:
        if "" == liczba_rzutow:
            liczba_rzutow = 1
        elif int(liczba_rzutow) < 0:
            liczba_rzutow = 0
        else:
            liczba_rzutow = int(liczba_rzutow)

        if "" == modyfikator:
            modyfikator = 0
        else:
            modyfikator = int(modyfikator)

        print("===============================" * 5)
        print(f"Podzieliłem stringa na: {podzial}")
        print(f"Znalazłem kostkę: {rodzaj_kostki}, type {type(rodzaj_kostki)}.")
        print(f"Liczba rzutów: {liczba_rzutow}, type {type(liczba_rzutow)}.")
        print(f"Modyfikator: {modyfikator}, type {type(modyfikator)}")

    except ValueError:
        print("===============================" * 5)
        print("Nie ma takiej kostki", string, podzial)




rzut("2D10+10")
rzut("D6")
rzut("D12-1")
rzut("4D100-20")
rzut("3D6")
rzut("1D4+2")
rzut("2D3")
rzut("2D42+2")
rzut("-2D42+2") # uwaga: ujemna ilość kości