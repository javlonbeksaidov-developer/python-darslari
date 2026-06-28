
'''AMALIYOT
1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
2. Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
3. Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
4. Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
5. Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
6. Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
'''

# 1-amaliyot va 2-amaliyot
def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
    mijoz = {
        "ism" : ism,
        "familiya" : familiya,
        "tyil" : tyil,
        "yoshi" : 2026 - tyil,
        "tjoy" : tjoy,
        "email" : email,
        "telefon" : tel,
    }
    return mijoz

def main():
    print("Mijoz haqida ma'lumotlarni kiriting.")
    mijozlar = []
    while True:                         # 2-amaliyot
        ism = input("Ismi: ")
        familiya = input("Familiyasi: ")
        tyil = int(input("Tug'ilgan yili: "))
        tjoy = input("Tug'ilgan joyi: ")
        email = input("Email: ")
        telefon = input("Telefon raqami: ")
        mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))

        javob = input("Davom etasizmi? (yes/no)")
        if javob != "yes":
            break

    print("Mijozlar:")
    for mijoz in mijozlar:
        print(
            f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
            f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
        )

main()

# 3-amaliyot
def find_max(x, y, z):
    if x > y >= z or x > z >= y:
        return f"{x} soni eng katta."
    elif y > x >= z or y > z >= x:
        return f"{y} soni eng katta."
    else:
        return f"{z} soni eng katta."

def main():
    x = int(input("1-son: "))
    y = int(input("2-son: "))
    z = int(input("3-son: "))

    result = find_max(x, y, z)
    print(result)

main()

# 4-amaliyot
def aylana_info(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana

def main():
    radius = float(input("Radius: "))
    result = aylana_info(radius)
    print(result)

main()

# 5-amaliyot
def tubmi(min, max):
    tublar = []
    for i in range(min, max + 1):
        tub = True
        if i == 1:
            tub = False
        elif i == 2:
            tub = True
        else:
            for x in range(2, i):
                if i % x == 0:
                    tub = False
        
        if tub:
            tublar.append(i)

    return tublar

def main():
    min = int(input("Boshlanish son: "))
    max = int(input("Oxirgi son: "))

    print(tubmi(min, max))

main()

# 6-amaliyot
def fibonacci(n):
    sonlar = []
    for son in range(n):
        if son == 0 or son == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[son - 1] + sonlar[son - 2])
    return sonlar

def main():
    n = int(input("Son: "))

    res = fibonacci(n)
    print(res)

main()
