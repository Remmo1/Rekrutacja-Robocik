import random
import datetime
import math
import time

n = int(input("Ile sygnałów: "))
deltaT = int(input("Co ile sekund: "))
i = 0
l = 0
xk = 0
yk = 0
zk = 0

while True:

    t = datetime.datetime.now().second

    if t % deltaT == 0:
        # sygnał
        time.sleep(1)               # żeby się nie tepnął z pętli od razu
        l = l + 1

        # losowe współrzędne
        x = random.randint(-10,10)
        print("x: " + str(x))
        y = random.randint(-10,10)
        print("y: " + str(y))
        z = random.randint(-10,10)
        print("z: " + str(z))

        # odległóści na osiach
        xk = x - xk
        print("xk: " + str(xk))
        yk = y - yk
        print("yk: " + str(yk))
        zk = z - zk
        print("zk: " + str(zk))

        # predkość
        v = math.sqrt(xk ** 2 + yk ** 2 + zk ** 2) / deltaT
        print("v: " + str(v))

        print("=======================")

    if l == n:                                      # wyjście z pętli po n liczbie sygnałów
        break

    i = i + 1
