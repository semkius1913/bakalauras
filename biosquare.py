import numpy as np
import time
import random
import math
import sys
sys.setrecursionlimit(15000)
def binind(ftn, lns, lns1):
    b1 = createrandomnumber(ftn)
    b2 = createrandomnumber(ftn)
    b3 = createrandomnumber(ftn)
    b4 = createrandomnumber(ftn)
    d1 = binarytodecimal(b1)
    d2 = binarytodecimal(b2)
    d3 = binarytodecimal(b3)
    d4 = binarytodecimal(b4)
    pts = determine4points(d1, d2, d3, d4)
    rest = checkpts(pts, lns, lns1)

    if rest:
        return binind(ftn, lns, lns1)
    else:
        return [[b1, b2], [b3, b4]], [[d1, d2], [d3, d4]]


def checkpts(sq, lns, lns1):
    for point in sq:
        if point[0] < 0 or point[1] < 0 or point[0] > (lns - 1) or (point[1] > lns1 - 1):
            return 1
    return 0


def binarytodecimal(x):
    value = 0
    t = x.copy()
    for i in range(len(t)):
        digit = t.pop()
        if digit == 1:
            value = value + pow(2, i)
    return value


def roulettewheel(choices):
    maxi = sum(choices)
    decide = random.uniform(0, maxi)
    current = 0
    number = 0
    for choice in choices:
        current += choice
        if current > decide:
            return number
        number += 1


def createrandomnumber(x):
    tempr = []
    for j in range(x):
        temp2 = random.randint(0, 1)
        tempr.append(temp2)
    return tempr


def sign(x1, y1, x2, y2, x3, y3):
    return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)


def pointinsquare(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4):
    d1 = sign(x0, y0, x1, y1, x2, y2)
    d2 = sign(x0, y0, x2, y2, x3, y3)
    d3 = sign(x0, y0, x3, y3, x4, y4)
    d4 = sign(x0, y0, x4, y4, x1, y1)

    has_neg1 = (d1 < 0) or (d3 < 0) or (d2 < 0) or (d4 < 0)
    has_pos1 = (d1 > 0) or (d3 > 0) or (d2 > 0) or (d4 > 0)
    return not (has_neg1 and has_pos1)


def determine4points(ly1, lx1, ly3, lx3):
    xmidpoint = (lx1 + lx3) / 2
    ymidpoint = (ly1 + ly3) / 2
    dx = abs(xmidpoint - lx1)
    dy = abs(ymidpoint - ly1)
    if lx1 < xmidpoint:
        lx2 = xmidpoint - dy
        lx4 = xmidpoint + dy
    else:
        lx2 = xmidpoint + dy
        lx4 = xmidpoint - dy
    if ly1 < ymidpoint:
        ly2 = ymidpoint + dx
        ly4 = ymidpoint - dx
    else:
        ly2 = ymidpoint - dx
        ly4 = ymidpoint + dx
    return [ly1, lx1], [ly2, lx2], [ly3, lx3], [ly4, lx4]


def countdots(y, x, virtual, counter1, counter2, square):
    global lines
    if pointinsquare(x, y, square[0][1], square[0][0],
                     square[1][1], square[1][0], square[2][1], square[2][0], square[3][1], square[3][0]):
        if virtual[y, x] == 0:

            virtual[y, x] = 1
            if int(lines[y][x]) == 1:
                counter1 += 1
                if y<63:
                  virtual, counter1, counter2 = countdots(y + 1, x, virtual, counter1, counter2, square)
                if x<63:
                  virtual, counter1, counter2 = countdots(y, x + 1, virtual, counter1, counter2, square)
                if y>1:
                  virtual, counter1, counter2 = countdots(y - 1, x, virtual, counter1, counter2, square)
                if x>1:
                  virtual, counter1, counter2 = countdots(y, x - 1, virtual, counter1, counter2, square)
            else:
                counter2 += 1

    return virtual, counter1, counter2


def skaiciavimai(i):
    sqr = determine4points(i[0][0], i[0][1], i[1][0], i[1][1])
    midpoint = [int((i[0][0] + i[1][0]) / 2), int((i[0][1] + i[1][1]) / 2)]
    virtualus = np.zeros((64, 64), dtype=int)
    virtualus, dotsum, counter2 = countdots(midpoint[0], midpoint[1], virtualus, 0, 0, sqr)
    return [dotsum, counter2]

for seq in range(1,101):
    start_time = time.time()
        #  READ
    filename = f'/content/drive/MyDrive/Colab Notebooks/data/p01/sqr{seq}.txt'
    data = []
    with open(filename) as my_file:
        for line in my_file:
            data.append([list(map(float, x.split(', '))) for x in line.split(', ')])

    lines = np.array(data)


    maximum = [[0, [0, 0, 0, 0]]]
    #  CREATE INDIVIDUALS
    # try:
    #    indNum = int(input("Enter number of individuals: "))
    # except ValueError as err:
    #    print("error:")
    #    print(err)
    #    print("setting individuals number to default")
    indNum = 100
    # try:
    #    featNum = int(input("Enter number of features: "))
    # except ValueError as err:
    #    print("error:")
    #    print(err)
    #    print("setting features number to default")
    featNum = 6
    #  divider-1 = number of individuals/ (points of x's and y')
    divider = indNum / 4 + 1

    # print("Number of individuals:", indNum, "Number of features:", featNum)

    #  generate sequences of 0 and 1 for individuals
    individualsInBinary = []
    individualsInDecimal = []
    for i in range(int(indNum / 4)):
        bi1, di1 = binind(featNum, len(lines), len(lines[0]))
        individualsInBinary.append(bi1)
        individualsInDecimal.append(di1)
    #  print(individualsInBinary)

    statement = 0
    prev = maximum[0]
    repeats = 0
    # print('Dots, [[y1 x1], [y3, x3]], iteration')
    while statement < 2500:
        fieldsize = []
        #   print(len(individualsInDecimal))
        # for i in individualsInDecimal:
        # THREADS  THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS


        for i in individualsInDecimal:
            dotsum, counter2 = skaiciavimai(i)

            # THREADS  THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS THREADS
            if not counter2:
                fieldsize.append(dotsum)
            elif counter2 / (counter2 + dotsum) >= 0.95:
                fieldsize.append(dotsum * 0.9)
                dotsum = 0
            elif counter2 / (counter2 + dotsum) >= 0.90:
                fieldsize.append(dotsum * 0.8)
                dotsum = 0
            elif counter2 / (counter2 + dotsum) >= 0.85:
                fieldsize.append(dotsum * 0.7)
                dotsum = 0
            else:
                fieldsize.append(0)
                dotsum = 0
            if dotsum == 0:
                continue
            if dotsum > maximum[0][0]:
                maximum = [[dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]]]
                    # print(maximum, statement)
            elif dotsum == maximum[0][0]:
                maximum.append([dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]])
        #print(f'statement = {statement}')
        fieldssrt = sorted(fieldsize)
        lambd = []
        mu = []
        #    print(len(fieldssrt))
        masv = []
        for i in range(len(fieldsize)):
            z = 1
            for j in fieldssrt:
                if j == fieldsize[i]:
                    #key = z / divider
                    key = (1 / 2) * (1 - ((math.cos(math.pi * z / divider))))
                    #mu.append(key)  # or key
                    #lambd.append(1 - key)  # 1-key
                    masv.append([individualsInBinary[i],1-key,key])
                    break
                else:
                    z += 1
        masv =sorted(masv, key=lambda x: x[1], reverse=True)

        individualsInBinary = [i[0] for i in masv]
        lambd = [i[1] for i in masv]
        #print(lambd)
        mu = [i[2] for i in masv]
        tmpsqares = individualsInBinary.copy()
        #  keiciami 20% blogiausiu individu geriausiais, taciau islieka mu/lambda
        for i in range(int(len(tmpsqares)/5)):
            tmpsqares[(-i)-1]= tmpsqares[i].copy()
        for i in range(len(tmpsqares)):
            for j in range(len(tmpsqares[i])):
                for k in range(len(tmpsqares[i][j])):
                    for l in range(len(tmpsqares[i][j][k])):
                        probs = lambd[i]
                        # print(probs)
                        rand = random.random()
                        if rand < probs:
                            mu2 = mu.copy()
                            mu2.pop(i)
                            tmpsqares2 = individualsInBinary.copy()
                            tmpsqares2.pop(i)
                            selected = roulettewheel(mu2)

                            tmpsqares[i][j][k][l] = tmpsqares2[selected][j][k][l]
                            if random.random() < 0.01:
                                tmpsqares[i][j][k][l] = abs(tmpsqares[i][j][k][l] - 1)



        individualsInBinary = tmpsqares.copy()
        individualsInDecimal = []
        for x in individualsInBinary:
            x1 = binarytodecimal(x[0][0])
            x2 = binarytodecimal(x[0][1])
            x3 = binarytodecimal(x[1][0])
            x4 = binarytodecimal(x[1][1])
            sqr = determine4points(x1, x2, x3, x4)
            if not checkpts(sqr, len(lines), len(lines[0])):
                individualsInDecimal.append([[x1, x2], [x3, x4]])
            else:
                a, b = binind(featNum, len(lines), len(lines[0]))
                x = a
                individualsInDecimal.append(b)

        if prev == maximum[0]:
            repeats += 1
            if repeats == 200:
                repeats=0
                # break
                individualsInBinary = []
                individualsInDecimal = []
                for i in range(int(indNum / 4)):
                    bi1, di1 = binind(featNum, len(lines), len(lines[0]))
                    individualsInBinary.append(bi1)
                    individualsInDecimal.append(di1)
            # if repeats == 2000:
            # break
        else:
            repeats = 0
        # else:
        # prev = maximum[0]
        statement += 1

    for i in individualsInDecimal:
        dotsum, counter2 = skaiciavimai(i)
        if not counter2:
            if dotsum > maximum[0][0]:
                maximum = [[dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]]]
                # print(maximum)
            elif dotsum == maximum[0][0]:
                maximum.append([dotsum, [i[0][0], i[0][1], i[1][0], i[1][1]]])
        else:
            continue
    # print("Final:")
    # print('Length, dots, [[y1 x1], [y3, x3]]')
    '''
    print(len(maximum), " ", maximum[0])
    tm = int(time.time() - start_time)
    print("--- %s seconds ---" % tm)
    print("tikslumas: ", maximum[0][0] / 92 * 100)
    with open("inout/bandomieji10.txt", "a") as myfile2:  # 92
        myfile2.write(str(tm) + " " + str(int(maximum[0][0] / 92 * 100)) + "\n")
    '''
    tm = time.time() - start_time
    pth2 = '/content/drive/MyDrive/Colab Notebooks/data/results/evo01.txt'
    with open(pth2, "a+") as myfile2:
      myfile2.write(f'{maximum[0][0]} {tm}\n')
