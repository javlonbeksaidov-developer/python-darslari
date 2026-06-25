
'''AMALIYOT
1. Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
2. Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
3. Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
4. Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
5. Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
6. Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
'''

# 1-amaliyot
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())

# 2-amaliyot
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())

# 3-amaliyot
login = input("Login: ")
parol = input("Parol: ")
if login == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login}!")

# 4-amaliyot
a = int(input("1-son: "))
b = int(input("2-son: "))
if a == b:
    print("Sonlar teng")

# 5-amaliyot
son = int(input("Son: "))
if son >= 0:
    print("Musbat son")
else:
    print("Manfiy son")

# 6-amaliyot
son = int(input("Son: "))
if son >= 0:
    print(son ** 0.5)
else:
    print("Musbat son kiriting.")