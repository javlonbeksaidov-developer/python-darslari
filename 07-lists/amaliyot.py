
'''AMALIYOT
Quyidagi mashqlarni bajaring:
1. ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
1.1. Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 

2. sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
2.1. Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 

3. t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
3.1. Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

4. friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
4.1. Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
4.2. Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
4.3. Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.'''

# 1-amaliyot
ismlar = ["Ali", "Vali", "Husan"]
# 1.1-amaliyot
print(f"{ismlar[0]} va {ismlar[1]} aka-uka.")
print(f"{ismlar[2]}ning akasi Hasan")


# 2-amaliyot
sonlar = [10, -5, 43.0, -63.8, 20, 6.7]
print(sonlar)
# 2.1-amaliyot
sonlar[1] = sonlar[1] + sonlar[4]
sonlar[-1] = 7.6
del sonlar[3]
print(sonlar)


# 3-amaliyot
t_shaxslar = ["Pele", "Maradonna", "Puskash", "Distifano"]
z_shaxslar = ["Ronaldo", "Messi", "Neymar"]
# 3.1-amaliyot
print(f"Tarixiy shaxslardan: {t_shaxslar.pop(1)} Argentenalik futbolchi. Zamonaviy shaxslardan {z_shaxslar.pop(-1)} Braziliyalik futbolchi.")


# 4-amaliyot
friends = []
friends.append("Ronaldo")
friends.append("Khusanov")
friends.append("Messi")
friends.append("Fayzullayev")
friends.append("Neymar")
friends.append("Shomuradov")
friends.append("Modric")
print(friends)

# 4.1-amaliyot
friends.remove("Neymar")
friends.remove("Fayzullayev")

# 4.2-amaliyot
friends.insert(0, "Pele")
friends.insert(-1, "Maradonna")
friends.insert(3, "Ermatov")

# 4.3-amaliyot
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop())
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(1))
print("\nKelgan mehmonlar: ", mehmonlar)