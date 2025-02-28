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
    for i in range(1, n):
        if i*i==liczba:
            licznik+=1
            kwadraty.append(liczba)
print('Zad.3.1 ',licznik, kwadraty[0])

#Zad 3.2
pierwsze = [2]
n1 = 10000

for kandydat in range(3, n1):
    for dzielnik in range(2, kandydat):
        if kandydat % dzielnik == 0:  # nie jest liczbą pierwszą
            break
    else:  # jest liczbą pierwszą
        pierwsze.append(kandydat)
print(pierwsze)

liczby_z_dziel_pierwsz=[]

for liczba in liczby:
    licznik = 0
    for pierwsza in pierwsze:
         if liczba % pierwsza == 0:
            licznik+=1
            if licznik>=5:
                liczby_z_dziel_pierwsz.append(liczba)

print('Zad.3.2 ',liczby_z_dziel_pierwsz)

# Zad 3.3

licznik_mniej = 0
licznik_wieksz = 0
licznik_row = 0

for liczba1 in liczby:
    cyfry = []  # Lista cyfr
    temp = liczba1

    # Rozbijamy liczbę na cyfry
    while temp > 0:
        cyfry.append(temp % 10)
        temp //= 10

    # Jeśli liczba miała mniej niż 4 cyfry, uzupełniamy zerami
    while len(cyfry) < 4:
        cyfry.append(0)
    print(cyfry)
    cyfry.sort()
    min_liczba = cyfry[0] * 1000 + cyfry[1] * 100 + cyfry[2] * 10 + cyfry[3]

    cyfry.sort(reverse=True)
    max_liczba = cyfry[0] * 1000 + cyfry[1] * 100 + cyfry[2] * 10 + cyfry[3]

    print(min_liczba, max_liczba)  # Sprawdzamy wynik

    roznica = max_liczba - min_liczba
    print(roznica)

    if roznica < liczba1:
        licznik_mniej += 1
    elif roznica > liczba1:
        licznik_wieksz += 1
    else:
        licznik_row += 1

print("Mniejsze:", licznik_mniej, "Większe:", licznik_wieksz, "Równe:", licznik_row)
