
'''AMALIYOT
Quyidagi mashqlarni bajaring:
1. Quyidagi o'zgaruvchilarni yarating: 
    kocha="Bog'bon"
    mahalla="Sog'bon"
    tuman="Bodomzor" 
    viloyat="Samarqand"

2. Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
    Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

3. Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

4. Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing

5. Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang

6. manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
'''

# 1-amaliyot mashq
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor" 
viloyat = "Samarqand"

# 2-amaliyot mashq
print(kocha, "ko'chasi,", mahalla, "mahallasi,", tuman, "tumani,", viloyat, "viloyati")

# 3-amaliyot mashq
kocha = input("Ko'cha: ")
mahalla = input("Mahalla: ")
tuman = input("Tuman: ") 
viloyat = input("Viloyat: ")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# 4-amaliyot mashq
print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")

# 5-amaliyot mashq
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

# 6-amaliyot mashq
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())