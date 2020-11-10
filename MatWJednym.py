# zmienne globalne

plansza = [['--' for i in range(8)]for j in range(8)]
biale = ['--' for i in range(16)]
czarne = ['--' for i in range(16)]


# podstawowe funkcje:

def pokaz_plansze(plansza):
    for i in range(0, 8):
        for j in range(0, 8):
            print(plansza[i][j] + str(i) + str(j), end=" ")
        print()

def wypelnij_plansze(plansza):
    flaga = False
    for i in range(0, 8):

        if flaga == True:
            break

        for j in range(0, 8):

            if flaga == True:
                break

            podana = input("Podaj figure, jeśli chcesz skończyć wciśnij 'z': ")
            if podana != 'z':
                x = int(input("Podaj xWspółrzedną: "))
                y = int(input("Podaj yWspółrzedną: "))
                plansza[x][y] = podana
            elif str(podana) == 'z':
                flaga = True

def rozpoznaj_figure(podana):

    figura = podana.lower()

    if figura == 'p':
        figura = 'pion'

    elif figura == 'r':
        figura = 'wieza'

    elif figura == 'k':
        figura = 'skok'

    elif figura == 'b':
        figura = 'goniec'

    elif figura == 'q':
        figura = 'krolowa'

    elif figura == 'w':
        figura = 'krol'

    return figura

def czyja_figura(podana):

    wynik = podana.lower()

    if wynik == 'w':
        wynik = 'bialy'
    else:
        wynik = 'czarny'

    return wynik

def wez_figury():

    l = 0
    l2 = 0

    for i in range(8):
        for j in range(8):
            if plansza[i][j] != '--':
                if plansza[i][j][0] == 'b':
                    czarne[l] = plansza[i][j] + str(i) + str(j)
                    l = l + 1
                else:
                    biale[l2] = plansza[i][j] + str(i) + str(j)
                    l2 = l2 + 1
# i daj graczom do tablic

# ruch figur:

def ruch(figura, xPodany, yPodany):

    x = int(figura[2])
    y = int(figura[3])

    if xPodany >= 0 and xPodany <= 8 and yPodany >= 0 and yPodany <= 8:             # czy nie wyjdziemy poza plansze

        if figura[1] == 'W':                                                        # ten pionek w koronie
            if abs(x-xPodany) <= 1 and abs(y-yPodany) <= 1:
                plansza[xPodany,yPodany] = figura




wypelnij_plansze(plansza)
pokaz_plansze(plansza)
wez_figury()
ruch(biale[0], 1, 0)
pokaz_plansze(plansza)



