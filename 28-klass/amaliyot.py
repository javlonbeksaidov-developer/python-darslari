
'''AMALIYOT
1. Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
2. Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
3. Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
'''

# 1-amaliyot va 2-amaliyot va 3-amaliyot
class User:
    def __init__(self, ism, familiya, email, tyil):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.tyil = tyil

    def get_first_name(self):
        return self.ism
    
    def get_last_name(self):
        return self.familiya
    
    def get_full_name(self):
        return f"{self.ism} {self.familiya}"
    
    def get_eamil(self):
        return self.email
    
    def get_age(self, year):
        return year - self.tyil
    
    def get_info(self):
        return f"Foydalanuvchi: {self.ism}{self.tyil}, ismi: {self.ism} {self.familiya}, email: {self.email}"
    

user1 = User("Javlon", "Saidov", "javlon@gmail.com", 2005)
user2 = User("Javlon", "Saidov", "javlon@gmail.com", 2005)
user3 = User("Javlon", "Saidov", "javlon@gmail.com", 2005)
print(user1.get_full_name())
print(user1.get_age(2026))
print(user1.get_info())
