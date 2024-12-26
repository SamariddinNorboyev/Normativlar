import random

#1.1 IF
harorat = int(input("Haroratni kiriting: "))
if harorat < 0:
    print("Sovuq kun, issiqroq kiying!")
elif harorat > 0 and harorat < 20:
    print("Ob-havo yaxshi, lekin sal sovuq.")
elif harorat > 20:
    print("Juda yaxshi ob-havo, zavqlaning!")

#b
age = int(input("Futbolchi yoshini kiriting!"))
gols = int(input("Futbolchi urgan gollarini kiriting!"))
if age < 18:
    if gols >= 1:
        print("Yosh ite'dod!")
    elif gols < 1:
        print("Mashq qilish kerak.")
if age > 18 and age < 35:
    if gols >= 3:
        print("Yulduz futbolchi!")
    elif gols < 3:
        print("Oddiy futbolchi.")
if age > 35:
    if gols >= 1:
        print("Mag‘lubiyatsiz veteran!")
    elif gols < 1:
        print("Tajribali murabbiy.")


#1.2
#a va #b
sonlar = [1,2,7,10,8]
engkatta = 0
engkichik = 10
for x in range(len(sonlar)):
    if engkatta < sonlar[x]:
        engkatta = sonlar[x]
    if engkichik > sonlar[x]:
        engkichik = sonlar[x]
print(engkichik)
print(engkatta)


summa = 0
for x in range(len(sonlar)):
    summa = summa+sonlar[x]
kopaytma = 1
for x in range(len(sonlar)):
    kopaytma = kopaytma*sonlar[x]

for x in range(len(sonlar)):
    for y in range(len(sonlar)):
        print(f"{sonlar[x]} * {sonlar[y]} == {sonlar[x] * sonlar[y]}")


x = random.randint(1, 20)
kiritilgan_son = int(input("Son kiriting - "))
while kiritilgan_son != x:
    if kiritilgan_son > x:
        print("Pastroq")
    elif kiritilgan_son < x:
        print("Yuqoriroq")
    kiritilgan_son = int(input("Son kiriting - "))
print(f"Son topildi - {x}")