menu = {
    "Osh": 25000,
    "Manti": 15000,
    "Lag'mon": 20000,
    "Shashlik": 10000
}
def display_menu():
        print("\n1. Buyurtma berish.")
        print("2. Savatni taxrirlash.")
        print("3. Buyurtmani hisoblash.")
        print("4. Promokod qo'llash.")
        print("5. Programmni to'xtatish.\n")
        ans = int(input("O'zingizga kerakli sonni kiriting: "))
        if ans == 1:
            take_order()
        elif ans == 2:
            taxrirlash()
        elif ans == 3:
            calculate_total()
        elif ans == 4:
            promokod()
        elif ans == 5:
            return 0
        else:
            print("Invalid input. Please enter numbers!")
            display_menu()
order = {}
times = {}
total = 0
def take_order():
    global total
    x = 1
    for key, value in menu.items():
        print(f"{x}. {key} - {int(value/1000)} 000 so'm")
        x+=1
    ans = str(input("Qaysi ovqatni buyurtma qilasiz: "))
    if ans in menu:
        if ans in order:
            times[ans] += 1
        else:
            times[ans] = 1
        order[ans] = menu[ans]
        total += menu[ans]
    qaytar()
def qaytar():
    ans = str(input("Yana ovqat zakaz qilasizmi: (ha/yoq) - "))
    if ans == "ha":
        take_order()
    elif ans == "yoq":
        display_menu()
    else:
        print("ha yoki yoq ni kiriting!")
        qaytar()
def taxrirlash():
    ans = int(input("Qanday amal bajarmoqchisiz: (1 - qo'shish/2 - o'chirish) - "))
    if ans == 1:
        take_order()
    elif ans == 2: 
        x = 1
        for key, value in order.items():
            print(f"{x}. {key} - {int(value/1000)} 000 so'm - {times[key]}")
            x+=1
        q = str(input("Qaysi ovqatni o'chirasiz - "))
        order.pop(q)
        display_menu()
    else:
        print("1 yoki 2 ni kiriting!")
        taxrirlash()
def calculate_total():
    global total
    print("Buyurtmalaringiz: ")
    x = 1
    for key, value in order.items():
        print(f"{x}. {key} - {int(value/1000)} 000 so'm - {times[key]}")
        x+=1
    print(f"Umumiy summa: {total}")
def promokod():
    global total
    ans = str(input("Promokodni kiriting:"))
    if ans == "uz24":
        print("Chegirma qo'llanildi!")
        total = total * 0.7
        print(f"Umumiy summa: {int(total)}")
    else:
        print("Chegirma qo'llanilmadi!")
    print("Xizmatdan foydalanganingiz uchun rahmat")
    return 0
display_menu()