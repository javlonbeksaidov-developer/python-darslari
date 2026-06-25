
'''AMALIYOT
1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
2. Ro'yxatning uzunligini konsolga chiqaring
3. sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
4. sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
5. Asl ro'yxatni qaytadan konsolga chiqaring
6. reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
7. sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
9. Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
10. Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
11. Ro'yxatdagi elementlar sonini hisoblang
12. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
13. taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
14. nonushta degan yangi ro'yxatga taomlardan nusxa oling
15. Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
16. Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
17. Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
'''

# 1-amaliyot
davlatlar = ["Uzbekistan", "USA", "Russian", "UK", "Japan", "Korea", "China", "Spain"]
print(davlatlar)

# 2-amaliyot
print(len(davlatlar))

# 3-amaliyot
print(sorted(davlatlar))

# 4-amaliyot
print(sorted(davlatlar, reverse=True))

# 5-amaliyot
print(davlatlar)

# 6-amaliyot
davlatlar.reverse()
print(davlatlar)

# 7-amaliyot
davlatlar = ["Uzbekistan", "USA", "Russian", "UK", "Japan", "Korea", "China", "Spain"]
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 8-amaliyot
juft_sonlar = list(range(120, 1201, 2))
print(juft_sonlar)

# 9-amaliyot
print(sum(juft_sonlar))

# 10-amaliyot
katta = max(juft_sonlar)
kichik = min(juft_sonlar)
print(katta - kichik)

# 11-amaliyot
uzunlik = len(juft_sonlar)
print(uzunlik)

# 12-amaliyot
print(juft_sonlar[:20])
print(juft_sonlar[-20:])
print(juft_sonlar[len(juft_sonlar) - 10 : len(juft_sonlar) + 10])

# 13-amaliyot
taomlar = ["osh", "manti", "somsa", "chuchvara", "kabob"]

# 14-amaliyot
nonushta = taomlar[:]

# 15-amaliyot
nonushta.append("tuxum")
nonushta.append("sut")

# 16-amaliyot
print(taomlar)
print(nonushta)

# 16-amaliyot
nonushta = tuple(nonushta)
print(nonushta)