plik=open('liczby_przyklad.txt','r').readlines()

liczby=[]
for wiersz in plik:
    wiersz=int(wiersz)
    liczby.append(wiersz)

print(liczby)
#Zad 3.1
kwadraty=[]

licznik=0
n=100
for liczba in liczby:
    for i in range(1,n):
        if i*i==liczba:
            licznik+=1
            kwadraty.append(liczba)
print('Zad.3.1 ',licznik, kwadraty[0])

#Zad 3.2
pierwsze = []
n1 = 100
pierwsze.append(2)

for i in range(3, n1, 2):  # Skaczemy co 2, bo liczby parzyste (poza 2) nie są pierwsze
    for j in range(2, i):  # Sprawdzamy dzielniki od 2 do i-1
        if i % j != 0:
            if i not in pierwsze:
                pierwsze.append(i)

print(pierwsze)

for liczba in liczby:
    for pierwsza in pierwsze:
        if liczba % pierwsza == 0:
            print(liczba,j)
