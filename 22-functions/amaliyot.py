
'''AMALIYOT
1. Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
2. Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
'''

# 1-amaliyot
def kopaytir(*sonlar):
    i = 1
    for son in sonlar:
        i *= son
    return i

def main():
    sonlar = []
    i = 0
    while True:
        i += 1
        son = int(input(f"{i}-son:"))
        sonlar.append(son)

        yana = input("Davom (yes/no) ").lower().strip()
        if yana == "no":
            break
    
    print(sonlar)
    res = kopaytir(*sonlar)
    print(res)

main()

# 2-amaliyot
def talaba_haqida(ism, familiya, **malumotlar):
    talaba = {
        'ism': ism.title(),
        'familiya': familiya.title(),
        **malumotlar
    }
    return talaba

def main():
    ism = input("Ism: ")
    familiya = input("familiya: ")
    malumotlar = {}

    while True:
        yana = input("\nQo'shimcha ma'lumot qo'shasizmi? (yes/no): ").lower().strip()
        if yana == "no":
            break

        kalit = input("Qanday ma'lumot? (masalan: yoshi, kursi, yonalishi): ").lower().strip()
        qiymat = input(f"{kalit} qiymatini kiriting: ")

        malumotlar[kalit] = qiymat

    talaba = talaba_haqida(ism, familiya, **malumotlar)

    print(f"\nNatija: {talaba}")

main()