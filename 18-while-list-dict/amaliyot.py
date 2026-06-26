
'''AMALIYOT
1. Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
2. e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
3. Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
'''

# 1-amaliyot
buyurtmalar = []
n = 0
while True:
    n += 1
    buyurtma = input(f"{n}-mashsulot: ")
    buyurtmalar.append(buyurtma)

    yana = input("Yana buyurtma berasizmi? (yes/no) ")
    if yana == "no":
        break
    else:
        continue

print(buyurtmalar)

# 2-amaliyot
bozorlik = {}
n = 0
while True:
    n += 1
    mahsulot = input(f"{n}-mahsulot: ")
    narx = int(input(f"{mahsulot.title()}ning narxi: "))
    bozorlik[mahsulot] = narx

    yana = input("Yana buyurtma berasizmi? (yes/no) ")
    if yana == "no":
        break

print(bozorlik)

# 3-amaliyot
buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        print(f"{buyurtma.title()} e-bozorda mavjud. Narxi: {mahsulotlar[buyurtma]}")
    else:
        print(f"{buyurtma.title()} e-bozorda mavjud emas.")