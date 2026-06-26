
'''AMALIYOT
1. Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
2. Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
3. Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
4. Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
5. Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
'''

# 1-amaliyot
buxoriy = {"ism": "Abu Abdulloh Muhammad ibn Ismoil", "tyil": 810, "vyil": 870, "tjoy": "Buxoro",}
qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}
vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}
navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    print(f"{shaxs["ism"]} {shaxs["tyil"]}-yilda {shaxs["tjoy"]}da tavallud topgan. " f"{shaxs["vyil"] - shaxs["tyil"]} yil umr ko'rgan.")

# 2-amaliyot
buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
    "asarlar": ["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir",],
}

qodiriy = {
    "ism": "Abdulla Qodiriy",
    "tyil": 1894,
    "vyil": 1938,
    "tjoy": "Toshkent",
    "asarlar": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"],
}

vohidov = {
    "ism": "Erkin Vohidov",
    "tyil": 1936,
    "vyil": 2016,
    "tjoy": "Farg'ona",
    "asarlar": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"],
}

navoiy = {
    "ism": "Alisher Navoiy",
    "tyil": 1441,
    "vyil": 1501,
    "tjoy": "Xirot",
    "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"],
}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs["ism"]
    asarlar = shaxs["asarlar"]
    print(f"\n{ism}ning eng mashhur asarlari:")
    for asar in asarlar:
        print(asar) 

# 3-amaliyot
kinolar = {
    "ali": ["Terminator", "Rambo", "Titanic"],
    "vali": ["Tenet", "Inception", "Interstellar"],
    "hasan": ["Abdullajon", "Bomba", "Shaytanat"],
    "husan": ["Mahallada duv-duv gap", "John Wick"],
}

for key, values in kinolar.items():
    print(f"\n{key.title()}ning sevimli kinolari :")
    for value in values:
        print(value)

# 4-amaliyot
davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}

for davlat, info in davlatlar.items():
    if key.lower() == "aqsh":
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(
        f"\n{davlat}ning poytaxti {info["poytaxt"].title()}"
        f"\nHududi: {info["maydon"]:,.2f} kv.km"
        f"\nAholisi: {info["aholi"]:,}"
        f"\nPul birligi: {info["pul birligi"]}"
    )

# 5-amaliyot
davlatlar = {
    "o'zbekiston": {
        "poytaxt": "toshkent",
        "maydon": 448978,
        "aholi": 33_000_000,
        "pul birligi": "so'm",
    },
    "rossiya": {
        "poytaxt": "moskva",
        "maydon": 17_098_246,
        "aholi": 144_000_000,
        "pul birligi": "rubl",
    },
    "aqsh": {
        "poytaxt": "vashington",
        "maydon": 9_631_418,
        "aholi": 327_000_000,
        "pul birligi": "dollar",
    },
    "malayziya": {
        "poytaxt": "kuala-lumpur",
        "maydon": 329750,
        "aholi": 25_000_000,
        "pul birligi": "rinngit",
    },
}

davlat = input("Davlat nomini kiriting: ")
if davlat in davlatlar:
    info = davlatlar[davlat]
    if davlat.lower() == "aqsh":
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(
        f"\n{davlat}ning poytaxti {info["poytaxt"].title()}"
        f"\nHududi: {info["maydon"]:,.2f} kv.km"
        f"\nAholisi: {info["aholi"]:,}"
        f"\nPul birligi: {info["pul birligi"]}"
    )
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")