"""#### Warsztat: Symulator LOTTO.
​
Jak wszystkim wiadomo, LOTTO to gra liczbowa polegająca na losowaniu 6 liczb z zakresu 1&ndash;49.
Zadaniem gracza jest poprawne wytypowanie losowanych liczb. Nagradzane jest trafienie 3, 4, 5 lub 6 poprawnych liczb.
​
Napisz program, który:
​
* zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
    * czy wprowadzony ciąg znaków jest poprawną liczbą,
    * czy użytkownik nie wpisał tej liczby już poprzednio,
    * czy liczba należy do zakresu 1-49,
* po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
* wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
* poinformuje gracza, czy trafił przynajmniej "trójkę"."""

from random import randint


def lotto():
    print("TROLOLOLOLOLOLO, witamy w LOTTO\n=================================")
    podane_liczby = []

    while len(podane_liczby) < 6:
        print(f"Pozstało do dodania {6 - len(podane_liczby)}")
        try:
            user_input = int(input("Podaj liczbę: "))
            if user_input in podane_liczby:
                print("Podałeś już tę liczbę")
            elif 1 <= user_input <= 49:
                podane_liczby.append(user_input)
            else:
                print("Liczba nie jest z zakresu 1 do 49.")

        except Exception as err:
            print("Coś się popsuło:", err)

    lottomat = [randint(1, 50) for each in range(6)]  # Lottomat losuje podane liczby.

    print(f"Twoje liczby: {sorted(podane_liczby)}")
    print("Liczby Lottomat:", lottomat)

    ile_trafione = len(set(lottomat) - set(podane_liczby))

    if ile_trafione <= 3:
        print(f"Brawo trafileś: {6 - ile_trafione} liczb.")
    else:
        print(f"Przykro mi, przegrałeś kolejne 5 zł. Trafiłeś: {6 - ile_trafione} liczb.")


lotto()
