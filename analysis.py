import numpy as np
import matplotlib.pyplot as plt


def rdfile(filename):
    data = np.loadtxt(filename)
    return data


def retrievedata(data, darray, param):
    for x in darray:
        data.append(x[param])
    return data


def sumall(darray, param):
    return sum([x[param] for x in darray])


#  files with parameter indnum=100 cycles=10000
f1 = rdfile("inout/rezs0.txt")
f2 = rdfile("inout/rezs1.txt")
f3 = rdfile("inout/rezs2.txt")
f4 = rdfile("inout/rezsn.txt")
#  files with parameter indnum=200 cycles=5000
f11 = rdfile("inout/rezs01.txt")
f21 = rdfile("inout/rezs11.txt")
f31 = rdfile("inout/rezs21.txt")
f41 = rdfile("inout/rezsn1.txt")
#  files with parameter indnum=400 cycles=5000 and a stop on 2000 cycles no change of max
ft1 = rdfile("inout/rezst0.txt")
ft2 = rdfile("inout/rezst1.txt")
ft3 = rdfile("inout/rezst2.txt")
ft4 = rdfile("inout/rezstn.txt")

alltimes = []
alltimes = retrievedata(alltimes, f1, 0)
alltimes = retrievedata(alltimes, f2, 0)
alltimes = retrievedata(alltimes, f3, 0)
alltimes = retrievedata(alltimes, f4, 0)
alltimes = retrievedata(alltimes, f11, 0)
alltimes = retrievedata(alltimes, f21, 0)
alltimes = retrievedata(alltimes, f31, 0)
alltimes = retrievedata(alltimes, f41, 0)
alltimes = retrievedata(alltimes, ft1, 0)
alltimes = retrievedata(alltimes, ft2, 0)
alltimes = retrievedata(alltimes, ft3, 0)
alltimes = retrievedata(alltimes, ft4, 0)

allacc = []
allacc = retrievedata(allacc, f1, 1)
allacc = retrievedata(allacc, f2, 1)
allacc = retrievedata(allacc, f3, 1)
allacc = retrievedata(allacc, f4, 1)
allacc = retrievedata(allacc, f11, 1)
allacc = retrievedata(allacc, f21, 1)
allacc = retrievedata(allacc, f31, 1)
allacc = retrievedata(allacc, f41, 1)
allacc = retrievedata(allacc, ft1, 1)
allacc = retrievedata(allacc, ft2, 1)
allacc = retrievedata(allacc, ft3, 1)
allacc = retrievedata(allacc, ft4, 1)


fff0=rdfile("inout/bandomieji0.txt")
onetime0 = []
oneacc0 = []
onetime0=retrievedata(onetime0,fff0,0)
oneacc0 = retrievedata(oneacc0,fff0,1)

print(sum(onetime0)/len(onetime0),sum(oneacc0)/len(oneacc0))


fff1=rdfile("inout/bandomieji1.txt")
onetime1 = []
oneacc1 = []
onetime1=retrievedata(onetime1,fff1,0)
oneacc1 = retrievedata(oneacc1,fff1,1)
tavg1 = sum(onetime1)/len(onetime1)
acavg1 = sum(oneacc1)/len(oneacc1)
print(tavg1,acavg1)

fff2=rdfile("inout/bandomieji2.txt")
onetime2 = []
oneacc2 = []
onetime2=retrievedata(onetime2,fff2,0)
oneacc2 = retrievedata(oneacc2,fff2,1)

print(sum(onetime2)/len(onetime2),sum(oneacc2)/len(oneacc2))

ffft=rdfile("inout/testinis2")
onetimet = []
oneacct = []
onetimet=retrievedata(onetimet,ffft,0)
oneacct = retrievedata(oneacct,ffft,1)

print(sum(onetimet)/len(onetimet),sum(oneacct)/len(oneacct))

fff3=rdfile("inout/bandomieji3.txt")
onetime3 = []
oneacc3 = []
onetime3=retrievedata(onetime3,fff3,0)
oneacc3 = retrievedata(oneacc3,fff3,1)

print(sum(onetime3)/len(onetime3),sum(oneacc3)/len(oneacc3))


fff4=rdfile("inout/bandomieji4.txt")
onetime4 = []
oneacc4 = []
onetime4=retrievedata(onetime4,fff4,0)
oneacc4 = retrievedata(oneacc4,fff4,1)

print(sum(onetime4)/len(onetime4),sum(oneacc4)/len(oneacc4))

fff5=rdfile("inout/bandomieji5.txt")
onetime5 = []
oneacc5 = []
onetime5=retrievedata(onetime5,fff5,0)
oneacc5 = retrievedata(oneacc5,fff5,1)

print(sum(onetime5)/len(onetime5),sum(oneacc5)/len(oneacc5))


fff6=rdfile("inout/bandomieji6.txt")
onetime6 = []
oneacc6 = []
onetime6=retrievedata(onetime6,fff6,0)
oneacc6 = retrievedata(oneacc6,fff6,1)

print(sum(onetime6)/len(onetime6),sum(oneacc6)/len(oneacc6))



fff7=rdfile("inout/bandomieji7.txt")#2000 200 0.01
onetime7 = []
oneacc7 = []
onetime7=retrievedata(onetime7,fff7,0)
oneacc7 = retrievedata(oneacc7,fff7,1)

print(sum(onetime7)/len(onetime7),sum(oneacc7)/len(oneacc7))


fff8=rdfile("inout/bandomieji8.txt")#2500 200 0.01
onetime8 = []
oneacc8 = []
onetime8=retrievedata(onetime8,fff8,0)
oneacc8 = retrievedata(oneacc8,fff8,1)

print(sum(onetime8)/len(onetime8),sum(oneacc8)/len(oneacc8))

fff9=rdfile("inout/bandomieji9.txt")#2500 200 0.1
onetime9 = []
oneacc9 = []
onetime9=retrievedata(onetime9,fff9,0)
oneacc9 = retrievedata(oneacc9,fff9,1)

print(sum(onetime9)/len(onetime9),sum(oneacc9)/len(oneacc9))


fff10=rdfile("inout/bandomieji10.txt")#2500 200 0.1
onetime10 = []
oneacc10 = []
onetime10=retrievedata(onetime10,fff10,0)
oneacc10 = retrievedata(oneacc10,fff10,1)

print(sum(onetime10)/len(onetime10),sum(oneacc10)/len(oneacc10))
'''
evo01=rdfile("tyrimas/results/evo01.txt")
full01=rdfile("tyrimas/results/full01.txt")
evo02=rdfile("tyrimas/results/evo02.txt")
full02=rdfile("tyrimas/results/full02.txt")
evo03=rdfile("tyrimas/results/evo03.txt")
full03=rdfile("tyrimas/results/full03.txt")
evo04=rdfile("tyrimas/results/evo04.txt")
full04=rdfile("tyrimas/results/full04.txt")
evo05=rdfile("tyrimas/results/evo05.txt")
full05=rdfile("tyrimas/results/full05.txt")
evo06=rdfile("tyrimas/results/evo06.txt")
full06=rdfile("tyrimas/results/full06.txt")
evo07=rdfile("tyrimas/results/evo07.txt")
full07=rdfile("tyrimas/results/full07.txt")
evo08=rdfile("tyrimas/results/evo08.txt")
full08=rdfile("tyrimas/results/full08.txt")
evo09=rdfile("tyrimas/results/evo09.txt")
full09=rdfile("tyrimas/results/full09.txt")
'''
tyrimas=[]
evotikslumaihistograma = []
evolaiko=[]
intervalaitikslumo = []
intervalailaiko = []
fulllaikas = []
for i in range(1,10):
    a=rdfile(f'tyrimas/results/evo0{i}.txt')
    b=rdfile(f'tyrimas/results/full0{i}.txt')
    for j in range(100):
        fulllaikas.append(b)
        c= a[j][0]/b[j][0]*100
        d = a[j][1] / b[j][1] * 100
        evotikslumaihistograma.append(c)
        evolaiko.append(d)
    if i%3==0:

        intervalaitikslumo.append(evotikslumaihistograma[(i-3)*100:i*100])
        intervalailaiko.append(evolaiko[(i-3)*100:i*100])

        skaicius = sum(intervalaitikslumo[int(i/3-1)])
        skaicius2 = sum(intervalailaiko[int(i / 3 - 1)])
        print(f'i {i} tikslumas {skaicius/300} laikas {skaicius2/300}')
    tyrimas.append([a, b])
print(sum(evotikslumaihistograma)/900)
print('laikutis')
print(sum(evolaiko)/900)
print(f'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa{len(intervalailaiko[0])}')
print(f'ababa{sum(intervalaitikslumo[2])/300}')

#plt.subplot(331)
plt.hist(evotikslumaihistograma, 25, alpha=0.90 )
plt.xticks(np.arange(0, 101, step=10))
plt.xlabel('Tikslumas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Biogeografiniu metodu visų apskaičiuotų tikslumų histograma')
plt.show()

plt.hist(evolaiko, 25, alpha=0.90)
plt.xticks(np.arange(0, 91, step=5))
plt.xlabel('Laikas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Biogeografiniu metodu skaičiavimų trukmės histograma')
plt.show()


plt.hist(intervalaitikslumo[0], 10, alpha=0.90)
plt.xlabel('Tikslumas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Pirmojo intervalo tikslumų histograma')
plt.xticks(np.arange(0, 101, step=10))
plt.show()


plt.hist(intervalaitikslumo[1], 10, alpha=0.90)
plt.xlabel('Tikslumas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Antrojo intervalo tikslumų histograma')
plt.xticks(np.arange(0, 101, step=10))
plt.show()


plt.hist(intervalaitikslumo[2], 10, alpha=0.90)
plt.xlabel('Tikslumas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Trečiojo intervalo tikslumų histograma')
plt.xticks(np.arange(0, 101, step=10))
plt.show()


plt.hist(intervalailaiko[0], 10, alpha=0.90)
plt.xlabel('Laikas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Pirmojo intervalo laikų histograma')
plt.xticks(np.arange(4, 8, step=1))
plt.show()



plt.hist(intervalailaiko[1], 20, alpha=0.90)
plt.xlabel('Laikas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Antrojo intervalo laikų histograma')
plt.xticks(np.arange(0, 61, step=10))
plt.show()



plt.hist(intervalailaiko[2], 50, alpha=0.90)
plt.xlabel('Laikas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Trečiojo intervalo laikų histograma')
plt.xticks(np.arange(30, 91, step=10))
plt.show()




'''
#kursinio darbo analize


timeavg = sum(alltimes) / len(alltimes)
accavg = sum(allacc) / len(allacc)
t1 = [sumall(f1, 0) / len(f1), sumall(f11, 0) / len(f11), sumall(ft1, 0) / len(ft1)]
t2 = [sumall(f2, 0) / len(f2), sumall(f21, 0) / len(f21), sumall(ft2, 0) / len(ft2)]
t3 = [sumall(f3, 0) / len(f3), sumall(f31, 0) / len(f31), sumall(ft3, 0) / len(ft3)]
t4 = [sumall(f4, 0) / len(f4), sumall(f41, 0) / len(f41), sumall(ft4, 0) / len(ft4)]
a1 = [sumall(f1, 1) / len(f1), sumall(f11, 1) / len(f11), sumall(ft1, 1) / len(ft1)]
a2 = [sumall(f2, 1) / len(f2), sumall(f21, 1) / len(f21), sumall(ft2, 1) / len(ft2)]
a3 = [sumall(f3, 1) / len(f3), sumall(f31, 1) / len(f31), sumall(ft3, 1) / len(ft3)]
a4 = [sumall(f4, 1) / len(f4), sumall(f41, 1) / len(f41), sumall(ft4, 1) / len(ft4)]

arrx = [148, 170, 157, 227]
arry = [100, 100, 100, 100]
# the histogram of the data
plt.figure(figsize=(20, 15))

plt.subplot(221)

plt.grid(True, alpha=0.5, ls='--')

plt.hist(alltimes, 100, alpha=0.90)
plt.xlabel('Laikas(s)')
plt.ylabel('Pasikartojimai')
plt.title('Skaičiavimams užimamo laiko histograma')
plt.annotate('Raudonos brūkšninės linijos žymi pilnuojo perrinkimo būdu gautų rezultatų poziciją', (0, 0), (40, -40),
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.annotate('sqr0', xy=(148, 225), xytext=(50, 225),
             arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('sqr1', xy=(170, 250), xytext=(250, 250),
             arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('sqr2', xy=(157, 275), xytext=(100, 275),
             arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('sqrn', xy=(227, 150), xytext=(300, 150),
             arrowprops=dict(facecolor='black', shrink=0.05),)
#  plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#  plt.xlim(40, 160)
#  plt.ylim(0, 0.03)
plt.xticks(np.arange(0, 700, 50))
plt.yticks(np.arange(0, 300, 25))
plt.axvline(148, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.axvline(170, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.axvline(157, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.axvline(227, color='r', linestyle='dashed', linewidth=1, zorder=0)

plt.subplot(222)

plt.grid(True, alpha=0.5, ls='--')

plt.hist(allacc, 100, alpha=0.90)
plt.axvline(100, color='r', linestyle='dashed', linewidth=1, zorder=0)
plt.xlabel('Tikslumas(%)')
plt.ylabel('Pasikartojimai')
plt.title('Tikslumo histograma')
plt.annotate('Raudona brūkšninė linija žymi pilnojo perrinkimo būdu gautų rezultatų poziciją', (0, 0), (40, -40),
             xycoords='axes fraction', textcoords='offset points', va='top')

plt.subplot(223)

plt.grid(True, alpha=0.5, ls='--')

plt.plot(arrx, arry, 'bo')
plt.plot(timeavg, accavg, 'ro')
plt.xlabel('Laikas(s)')
plt.ylabel('Tikslumas(%)')
plt.title('Pilno perrinkimo tikslumai, lyginant su vidutiniu visų skaičiavimų tikslumu')
plt.yticks(np.arange(40, 110, 10))
plt.xticks(np.arange(140, 260, 10))

plt.subplot(224)

plt.grid(True, alpha=0.5, ls='--')

plt.plot(arrx[0], arry[0], 'b^')
plt.plot(t1, a1, 'bo')
plt.plot(arrx[1], arry[1], 'g^')
plt.plot(t2, a2, 'go')
plt.plot(arrx[2], arry[2], 'r^')
plt.plot(t3, a3, 'ro')
plt.plot(arrx[3], arry[3], 'k^')
plt.plot(t4, a4, 'ko')
plt.plot(t1, a1, label='sqr0', color='b')
plt.plot(t2, a2, label='sqr1', color='g')
plt.plot(t3, a3, label='sqr2', color='r')
plt.plot(t4, a4, label='sqrn', color='k')
plt.yticks(np.arange(30, 110, 10))

plt.xlabel('Laikas(s)')
plt.ylabel('Tikslumas(%)')
plt.title('Pilno perrinkimo tikslumai, lyginant su vidutiniais failų skaičiavimų tikslumais.')
plt.legend(loc=4)
plt.annotate('Apskritimais pažymėti biogeoografiniai skaičiavimai, trikampiais - pilnojo perrinkimo.\nTaip pat matomas'
             ' ir bandymų nuoseklumas. Pirmas bandymas yra kairiausias,\npaskutinis - dešiniausias atitinkamose spalvos'
             'e.', (0, 0), (40, -40),
             xycoords='axes fraction', textcoords='offset points', va='top')
plt.savefig('inout/grafikas.png', bbox_inches='tight')
print("old test")
aa1 = rdfile("inout/rezsn.txt")
print(f"time: {sumall(aa1, 0)/len(aa1)}")
print(f"accuracy: {sumall(aa1, 1)/len(aa1)}")
print("new test")
aa1 = rdfile("inout/rezstnttttt.txt")
print(f"time: {sumall(aa1, 0)/len(aa1)}")
print(f"accuracy: {sumall(aa1, 1)/len(aa1)}")
'''
