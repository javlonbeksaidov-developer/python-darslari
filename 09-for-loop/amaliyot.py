
'''AMALIYOT
1. Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
2. Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
3. 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
4. Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
5. Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
'''

# 1-amaliyot
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Anvar"]
for ism in ismlar:
    print(f"Salom {ism}")

# 2-amaliyot
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Anvar"]
marta = 0
for ism in ismlar:
    print(f"Salom {ism}")
    marta += 1

print(f"Dastur {marta} marta takrorlandi.")

# 3-amaliyot
toqlar = list(range(11, 100, 2))
kublar = []
for toq in toqlar:
    kub = toq ** 3
    kublar.append(kub)

print(kublar)

# 4-amaliyot
kinolar = []
for i in range(5):
    kino = input(f"{i+1}-kino:")
    kinolar.append(kino)
    i+=1

print(kinolar)

# 5-amaliyot
odamlar_soni = int(input("Odamlar soni: "))
odamlar = []
for i in range(odamlar_soni):
    odam = input(f"{i + 1}-odam: ")
    odamlar.append(odam)
    i+=1

print(odamlar)