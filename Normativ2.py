#1.1 - list
#a
ismlar = []

#b
ismlar.append("Doston")
ismlar.append("Akbar")
ismlar.append("Ali")
ismlar.append("Ahmad")
ismlar.append("Baxodir")
ismlar.append("Baxtiyor")
ismlar.append("Zabixulloh")


#c
ismlar.pop(4)
#pop index yoziladi va yozilgan indexdagi elementn o'chirib tashlaydi
# del ismlar[1:3]
#del butun arrayni yoki indexni o'chirib tashlaydi
ismlar.remove("Ali")
#remove qiymat qabul qiladi va o'sha qiymatni o'chirib tashlaydi






#d
yaqinlar = ismlar.copy()


#e
yaqinlar.sort()
print(yaqinlar)

#f
sonlar = []
for x in range(1, 101):
    sonlar.append(x)
sonlar.reverse()
print(sonlar)

sonlar1 = sonlar[:10]
sonlar2 = sonlar[90:]
sonlar3 = sonlar[45:55]

#1.2 - tuple
sonlar = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sonlar[3:7])
sonlar = list(sonlar)
sonlar[4] = "Asqar"
sonlar = tuple(sonlar)
print(sonlar)




#1.3 - dict
#a
talabalar_baholari = {
    "Ali": {"Matematika": 5, "Ingilis-tili": 4},
    "Vali": {"Matematika": 4, "Ingilis-tili": 3},
    "Zuhra": {"Matematika": 5, "Ingilis-tili": 5},
    "Olim": {"Matematika": 3, "Ingilis-tili": 4}
}
#b
talabalar_baholari["Doston"] = {"Matematika": 5,
                                "Ingilis-tili": 4}
#c
talabalar_baholari.pop("Doston")
#pop va del deyarli bir xil ishlaydi ammo ularning farqi shundaki:
#pop o'chirib tashlagan parasini return qiladi
#dict o'chirib tashlagan juftligini return qilmaydi


#d
for key, value in talabalar_baholari.items():
    print(f"{key} - {value}")

#e
talabalar_baholari["Ali"]["Matematika"] = 4
talabalar_baholari["Olim"]["Matematika"] = 2
talabalar_baholari["Olim"]["Ingilis-tili"] = 3

#f
ortacha = {}
for key, value in talabalar_baholari.items():
    ort = ((talabalar_baholari[key]["Matematika"] + talabalar_baholari[key]["Ingilis-tili"])/2)
    ortacha[key] = ort
print(ortacha)

#g
uchdan_katta = {}
for key, value in ortacha.items():
    if ortacha[key]<3:
        print(f"{key} - yiqildingiz")
    else:
        uchdan_katta[key] = value

print(uchdan_katta)




#1.4
bosh_toplam = set()


bosh_toplam = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
bosh_toplam.remove(4)
bosh_toplam.discard(1)





toplam_1 = {1, 2, 3, 4, 5}
toplam_2 = {4, 5, 6, 7, 8}


birlashma = toplam_1.union(toplam_2)
kesishma = toplam_1.intersection(toplam_2)
farq = toplam_1.difference(toplam_2)



print(toplam_1 == toplam_2)