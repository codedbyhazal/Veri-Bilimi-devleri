dogum_yili = int(input("Doğum yılınızı giriniz: "))
guncel_yil = 2025

yas = guncel_yil - dogum_yili
print(f"Yaşınız: {yas}")

if 0 <= yas <= 12:
    print("Çocuksunuz")
elif 13 <= yas <= 17:
    print("Ergensiniz")
else:
    print("Yetişkinsiniz")

