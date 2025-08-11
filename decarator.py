# 1
is_logged_in = False

def login_required(func):
    def wrapper():
        if is_logged_in:
            return func()
        else:
            print("Iltimos, avval login qiling.")
    return wrapper

@login_required
def profile():
    print("Bu sizning profilingiz.")

# Test qilish:
profile()  # is_logged_in = False bo'lgani uchun xabar chiqadi

is_logged_in = True
profile()  # Endi profil chiqadi

# 2
import time

def time_tracker(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Funksiya bajarilishi {end - start:.2f} soniya oldi.")
        return result
    return wrapper

@time_tracker
def long_process():
    for _ in range(1000000):
        pass
    print("Tugadi.")

long_process()



# 3
user_role = "user"  # yoki "admin"

def admin_required(func):
    def wrapper():
        if user_role == "admin":
            return func()
        else:
            print("Ushbu funksiya faqat adminlar uchun.")
    return wrapper

@admin_required
def delete_user():
    print("Foydalanuvchi o‘chirildi.")

delete_user()  # user bo‘lgani uchun ruxsat berilmaydi

user_role = "admin"
delete_user()  # Endi o‘chirish

#4
def call_counter(func):
    count = 0
    def warapper():
        nonlocal count
        count += 1
        print(f"funksiya {count}-marta chaqirildi")
        return func()
    return warapper

@call_counter
def gr():
    print("salom")

gr()
gr()
gr()
gr()
gr()


#5
son = int(input("sonni kiriting: "))
def decorator(func):
    def warraper():
        global son
        if son % 2 == 0:
            return func()
        else:
            print("funksiya ishlamaydi")
    return warraper

@decorator
def juft():
    print("funksiya ishga tushdi")

juft()

#6
parol = int(input("parolni kiriting: "))

def decorator(func):
    def wrapper():
        global parol
        if parol == 1234:
            return func()
        else:
            print("parol notogri ❌")
    return wrapper

@decorator
def togri():
    print("parol togri ✅")
    
togri()

#variant-2
parol = int(input("parolni kiriting: "))

def decorator(func,func2):
    def wrapper():
        global parol
        if parol == 1234:
            return func()
        else:
            func2()
    return wrapper

def togri():
    print("parol togri ✅")
    
def notogri():
    print("parol hato ❌")

funksiya = decorator(togri, notogri)
funksiya()

#7
son1 = int(input("1-son: "))
son2 = int(input("2-son: "))

def decorator(func):
    def bolish():
        if son2 == 0:
            return func()
        else:
            print(f"{son1} / {son2} = {son1 / son2}")
    return bolish

@decorator
def son():
    print("0 ga bolish mumkin emas")

son()

#8
ism = input("ismingizni kiriting: ").lower()
def decorator(func):
    def tekshir():
        global ism
        if len(ism) < 3:
            return func()
        else:
            print("ism qabul qilindi")
    return tekshir

@decorator
def chiqish():
    print("ism qabul qilinmadi")

chiqish()

#9
def decorator(func):
    def katta():
        h = func()
        print(str(h).upper())
    return katta

@decorator
def kichik():
    return input("text: ")

kichik()

#10
existing_users = ["ali", "vali", "dilshod","new_login"]
def decorator(func):
    def login():
        global existing_users
        if "new_login" in existing_users:
            return func()
        else:
            print("funksiya ishga tushdi")

    return login

@decorator
def xato():
    print("funksiya ishlamaydi")

xato()