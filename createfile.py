import random
for i in range(1, 10):
    loc = f'tyrimas/p0{i}'
    randsize = i/10
    for x in range(1,101):
        lst = []
        for i in range(64):
            lst2 = []
            for j in range(64):
                if randsize > random.uniform(0, 1):
                    lst2.append(1)
                else:
                    lst2.append(0)
            lst.append(lst2)

        location = f'{loc}/sqr{x}.txt'
        with open(location, "w+") as myfile:
            for i in lst[:-1]:
                myfile.write(str(i)[1:-1] + "\n")
        #  not to have newline symbol in the end of file
            myfile.write(str(lst[-1])[1:-1])
