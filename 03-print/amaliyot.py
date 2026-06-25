
'''AMALIYOT
Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:

1. 5 ning 4-darajasini toping

2. 22 ni 4 ga bo'lganda qancha qoldiq qoladi?

3. Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping

4. Diametri 12 ga teng bo'lgan doiraning yuzini toping  (π=3.14 deb oling)

5. Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
Javoblarni savol va yechim ko'rinishida chiqaring: 5 ning 4-darajasi 625

6. Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:
"Nexia", "Tico", 'Damas' ko'rganlar qilar havas'''


# 1-savol. 5 ning 4-darajasini toping
print("5 ning 4-darajasi ", 5**4)

# 2-savol. 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print("22 ni 4 ga bo'lgandagi qoldiq", 22%4)

# 3-savol. Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
print(f"Tomonlari 125 ga teng kvadratning yuzi {125 ** 2}ga teng va perimetrini {125 * 4}ga teng.")

# 4-savol. Diametri 12 ga teng bo'lgan doiraning yuzini toping  (π=3.14 deb oling)
d = 12
PI = 3.14
formula = PI * (d / 2) ** 2
print(f"Diametri {d} ga teng bo'lgan doiraning yuzini {formula}")

# 5-savol. Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
a = 6
b = 7
c = (a ** 2 + b ** 2) ** 0.5
print(f"Katetlari {a} va {b} bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi {c}ga teng.")
