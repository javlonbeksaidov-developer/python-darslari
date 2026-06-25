
'''AMALIYOT
1. Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
2.1. Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
3. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
'''

# 1-amaliyot
python = {
    "int": "Butun son",
    "float": "O'nlik son",
    "bool": "Mantiqiy qiymat",
    "for": "Biror amalni qayta-qayta bajarish tsikli",
    "if": "Shartlarni tekshirish operatori",
}

for k, v in sorted(python.items()):
    print(f"{k.title()} - {v}")

# 2-amaliyot
davlatlar = {
    "AQSH" : "Vashington",
    "Kanada" : "Ottava",
    "Meksika" : "Mexico",
    "Uzbekiston" : "Toshkent",
    "Rossiya" : "Moskva",
    "Koreya" : "Seul",
}

print("\nDunyo davlatlari:")
for davlat in sorted(davlatlar.keys()):
    print(davlat)

print("\nDunyo davlatlarining poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)

# 2.1-amaliyot
davlat_nomi = input("Qaysi davlatning poytaxtini bilishni istaysiz?: ")
if davlat_nomi in davlatlar:
    print(f"{davlat_nomi}ning poytaxti {davlatlar[davlat_nomi]} shahri.")
else:
    print("Kechirasiz, bizda bunday ma'lumot yo'q.")

# 3-amaliyot
menu = {
    "osh" : 25_000,
    "somsa" : 5_000,
    "manti" : 6_000,
    "shashlik" : 15_000,
    "non" : 4_000,
    "choy" : 2_000,
    "kofe" : 3_000,
    "kola" : 10_000,
    "pepsi" : 10_000,
    "fanta" : 10_000
}

buyurtmalar = []
for i in range(3):
    taom = input(f"{i + 1}-taom: ")
    buyurtmalar.append(taom)
    i += 1

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma} {menu[buyurtma]}")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q")