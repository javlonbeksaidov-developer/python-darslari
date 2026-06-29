
'''AMALIYOT
1. Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

2. Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing

3. get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin

4. Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.

5. update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

6. Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

7. Avtosalonga yangi avtomobillar qo'shish uchun metod yozing

8. Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing

9. Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring

10. dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini toping (dir(str), dir(int) va hokazo)
'''

# 1-amaliyot: Avto klassi
class Avto:
    def __init__(self, make, model, rang, karobka, narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.km = 0  # Standart qiymat

    # 2 va 3-topshiriqlar: Xususiyatlarni qaytaruvchi metodlar
    def get_info(self):
        return f"{self.make} {self.model}, Rangi: {self.rang}, Korobka: {self.karobka}, Narxi: {self.narh}$, Yurgan masofasi: {self.km} km."
    
    # 4 va 5-topshiriqlar: Xususiyatlarni yangilovchi metodlar
    def set_narh(self, yangi_narh):
        """Avtomobil narhini yangilovchi metod"""
        if yangi_narh > 0:
            self.narh = yangi_narh
        else:
            print("Narh noto'g'ri kiritildi!")

    def update_km(self, km):
        """Kilometrajni musbat songa ko'paytirib boruvchi metod"""
        if km > 0:
            self.km += km
        else:
            print("Kilometr musbat qiymat qabul qiladi.")


# 6-amaliyot: Avtosalon klassi
class Avtosalon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtos = []  # Sotuvdagi avtomobillar ro'yxati

    # 7-topshiriq: Avto qo'shish metodi
    def add_avto(self, avto):
        self.avtos.append(avto)

    # 8-topshiriq: Salon va undagi avtolar haqida ma'lumot
    def get_salon_info(self):
        info = f"{self.nomi} avtosaloni (Manzil: {self.manzil}).\nSotuvdagi avtomobillar:\n"
        if not self.avtos:
            info += "Hozircha mashina yo'q."
        else:
            for avto in self.avtos:
                info += f"- {avto.get_info()}\n"
        return info
    

# 1. Avtomobillar yaratamiz
avto1 = Avto("Chevrolet", "Gentra", "Qora", "Avtomat", 13000)
avto2 = Avto("BYD", "Song Plus", "Oq", "Avtomat", 30000)

# 2. Avto metodlarini tekshiramiz
avto1.update_km(1500)
avto1.set_narh(12800) 


salon = Avtosalon("Driver's Village", "Toshkent sh.")
salon.add_avto(avto1)
salon.add_avto(avto2)

print(salon.get_salon_info())


print("avto1 obyektining xususiyatlari (lug'at ko'rinishida):")
print(avto1.__dict__) 

print("\nAvto klassining barcha metodlari:")
print(dir(Avto))

print("\nString (matn) klassining metodlari:")
print(dir(str))
