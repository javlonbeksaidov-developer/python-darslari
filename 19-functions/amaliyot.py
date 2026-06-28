
'''AMALIYOT
1. Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
2. Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
3. Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
4. Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
5. Foydalanuvchidan x va y sonlarini olib, x ** y ni konsolga chiqaruvchi funksiya yozing.
6. Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
7. Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
'''

# 1-amaliyot
def brithday(name, age):
    print(f"Salom {name.title()}, siz {2026 - age}-yilda to'g'ilgansiz.")

brithday("javlon", 21)

# 2-amaliyot
def kv(number):
    print(f"Berilgan {number} sonning kvadrati {number ** 2} soniga teng.")

def kub(number):
    print(f"Berilgan {number} sonning Kubi {number ** 3} soniga teng.")

kv(3)
kub(3)

# 3-amaliyot
def juft(number):
    if number % 2 == 0:
        return True
    return False

def main():
    number = int(input("Son kiritng: "))
    if juft(number):
        print(f"{number} - juft son.")
    else:
        print(f"{number} - toq son.")

main()

# 4-amaliyot
def max_or_min(num1, num2):
    if num1 == num2:
        return False
    elif num1 > num2:
        return True
    else:
        return False

def main():
    num1 = int(input("1-son: "))
    num2 = int(input("2-son: "))

    if num1 == num2:
        print("Sonlar teng")
    elif max_or_min(num1, num2):
        print(f"{num1} soni katta")
    else:
        print(f"{num2} soni katta")

main() 

# 5-amaliyot va 6-amaliyot
def darajaga_kutar(x, y = 2):
    return x ** y

def main():
    x = int(input("asos: "))
    y = int(input("daraja: "))

    result = darajaga_kutar(x, y)
    print(f"{x} ** {y} = {result:,}")

main()

# 7-amaliyot
def buluvchi(number):
    for i in range(2, 11):
        if number % i == 0:
            print(f"{number} soni {i} ga qoldiqsiz bo'linadi")

def main():
    number = int(input("Son: "))

    print(buluvchi(number))

main()