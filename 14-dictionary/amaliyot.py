
'''AMALIYOT
1. otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
3.1. Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
3.2. Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
'''

# 1-amaliyot
otam = {
    "name" : "Alijon",
    "year" : "1972",
    "city" : "Samarqand",
    "address" : "Kattaqo'rg'on"
}
print(f"Otamning ismi {otam["name"]}, {otam["year"]}-yilda, {otam['city']} viloyatida tug'ilgan")

# 2-amaliyot
taomlar = {
    "ota" : "osh",
    "ona" : "somsa",
    "akam" : "manti"
}

for k, v in taomlar.items():
    print(f"{k}ning sevimli taomi {v}.")

# 3-amaliyot
python = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
}

# 3.1-amaliyot
kalit = input("Kalit so'z kiriting: ").lower()
print(python.get(kalit, "Bunday so'z mavjud emas"))

# 3.2-amaliyot
kalit = input("Kalit so'z kiriting: ").lower()
tarjima = python.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")