import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'ro:') #pierwszy [] to x, drugi [] to y, a trzeci '' odpowiada za zmiane koloru itp.
# plt.ylabel('liczby z wektora')
# plt.show()
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'r:')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'bo:')
#
# plt.axis([0, 6, 0, 20]) #ustala minimum i maximum dla x i y gdzie pierwsze dwa są dla x a drugie dwa dlay

# x = np.arange(0, 5.2, 0.2)

# plt.plot(x, x, "r-", x, x**2, "b^",x, x**3, 'gs')
# plt.legend(labels=["liniowa", 'kwadratowa', 'szesciena'],loc="center left") #do każdej lini przypisuje legende loc przypisuje pozycje legendzie ale coś się wykrzaczyło u mnie
# plt.show()
# plt.plot(x, x, label='liniowa')
# plt.plot(x, x**2, label='kwadratowa')
# plt.plot(x, x**3, label='szescienna')
# plt.legend()
# plt.savefig('plot.png')
# plt.show()
# im1 = Image.open("plot.png")
# im1 = im1.convert('RGB')
# im1.save('plot.jpg')
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, "g-",label="hiperbola")
# plt.legend(loc='upper right')
# plt.show()
# x1 = np.arange(0, 10, 0.1)
# y = np.sin(x1)
# plt.plot(x1,y,"r-",label='sinus')
# plt.legend(loc='upper center')
# plt.show()
# x1 = np.arange(0, 2.02, 0.02)
# x2 = np.arange(0, 2.02, 0.02)
#
# y1 = np.sin(2*np.pi*x1)
# y2 = np.cos(2*np.pi*x2)

# plt.subplot(2,1,1) # indeksowanie w siatkach zaczynasie od 1
# plt.plot(x1, y1, 'r--')
# plt.ylabel('sin(y)')
# plt.title('wykres sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'go')
# plt.xlabel("x")
# plt.ylabel("cos(y)")
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5) #wykresy się
# plt.show()
##komentujemy siatke wektory zostają

# fig, axs = plt.subplots(3,2)
# print(type(fig))
# print(type(axs))
#
# axs[0, 0].plot(x1, y1,"r-")
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('Wykres sin(x)')
#
# axs[1, 1].plot(x1, y1,"b-")
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('sin(x)')
# axs[1, 1].set_title('Wykres sin(x)')
#
# axs[2,0].plot(x2, y2, 'g-')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('cos(x)')
# axs[2,0].set_title('wykres cos(x)')
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()
# dane = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
#
# dane['b'] = dane['a'] + 10 * np.random.randn(50)
# dane['d'] = np.abs(dane['d']) * 100
#
# plt.scatter(data = dane, x='a', y='b',color="red", s='d')
# plt.xlabel("wartosci a")
# plt.ylabel('wartsci b')
# plt.show()
# print(dane["c"])
##Wykres kolumnowy

dane = {"Kraj": ['Belgia','Indie','Brazylia', 'Polska'],
         "Stolica":['Bruksela','New Delhi', 'Brasilia','Warszawa'],
        'Populacja':[11190846, 1303171035, 207847528, 38675467],
        'Kontynent':['Europa','Azja','Ameryka Południowa','Europa']}
df = pd.DataFrame(dane)
print(df)
grupa = df.groupby('Kontynent')
etykiety = list(grupa.groups.keys())
wartosc = list(grupa.agg("Populacja").sum())

plt.bar(x=etykiety, height=wartosc, color=['red', 'green', 'blue'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja na kontynentach')
plt.show()