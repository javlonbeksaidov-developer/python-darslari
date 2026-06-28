
'''AMALIYOT
1. Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)
Kutilgan natija: ['Ali', 'Vali', 'Hasan', 'Husan']

2. Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
Kutilgan natija: 

['ali', 'vali', 'hasan', 'husan'] 

['Ali', 'Vali', 'Hasan', 'Husan']

3. Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.
'''

# 1-amaliyot va 2-amaliyot
def first__upper(royhat):
    x = []
    for ism in royhat:
        x.append(ism.title())
    return x

def main():
    ismlar = []
    i = 0
    while True:
        i += 1
        ism = input(f"{i}-ism: ")
        ismlar.append(ism)

        yana = input("Davom: (yes/no) ")
        if yana == "no":
            break

    print(ismlar)
    res = first__upper(ismlar[:])   # 2-amaliyot
    print(res)

main()

# 3-amaliyot
def bahola(ismlar):
    print("O'quvchilarni baholash")
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism.title()}ga nechi baho: ")
        baholar[ism] = baho
    
    natija = "\n--- Baholash Natijalari ---\n"
    for k, v in baholar.items():
        natija += f"{k.title()}ning bahosi: {v}\n"
    
    return natija

def main():
    ismlar = []
    i = 0
    while True:
        i += 1
        ism = input(f"{i}-ism: ")
        ismlar.append(ism)

        yana = input("Davom: (yes/no) ")
        if yana == "no":
            break

    print(f"Talabalar ro'yxati : {ismlar}")
    res = bahola(ismlar) 
    print(res)

main()