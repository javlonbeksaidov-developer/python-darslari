
'''AMALIYOT
Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
1. Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
2. Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
3. Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
4. mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
5. Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
6. foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
7. Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
'''

# 1-amaliyot
son = int(input("Juft son: "))
if son % 2 == 0:
    print("Rahmat")
else:
    print("Bu juft son emas")

# 2-amaliyot
yosh = int(input("Yosh: "))
if 0 <= yosh < 5:
    print("Chipta narxi bepul.")
elif 5 <= yosh < 18:
    print("Chipta narxi 10000.")
elif 18 <= yosh < 60:
    print("Chipta narxi 20000.")
else:
    print("Chipta narxi bepul.")

# 3-amaliyot
son_1 = int(input("1-son: "))
son_2 = int(input("2-son: "))
if son_1 == son_2:
    print("Sonlar teng.")
elif son_1 > son_2:
    print("1-son katta.")
else:
    print("2-son katta.")

# 4-amaliyot
mahsulotlar = ["olma", "anor", "uzum", "nok", "gosht", "non", "bodring", "pamidor", "tarvuz", "qovun"]
savat = []
for i in range(5):
    mahsulot = input(f"Savatga {i + 1}-mahsulotni qo'shing: ")
    savat.append(mahsulot)
    i += 1

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")

# 5-amaliyot
mahsulotlar = ["olma", "anor", "uzum", "nok", "gosht", "non", "bodring", "pamidor", "tarvuz", "qovun"]
savat = []
bor_mahsulotlar = []
mavjud_emas = []

for i in range(5):
    mahsulot = input(f"Savatga {i + 1}-mahsulotni qo'shing: ")
    savat.append(mahsulot)
    i += 1

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 6-amaliyot
foydalanuvchilar = ["Ali", "Vali", "Husan", "Hasan", "Anvar"]
login = input("Login: ")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang")
else:
    foydalanuvchilar.append(login)
    print("Xush kelibsiz!")

# 7-amaliyot
son = int(input("Butun son: "))
for i in range(2, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")