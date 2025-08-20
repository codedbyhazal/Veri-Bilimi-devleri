matematik = int(input("Matematik notunu giriniz: "))
fizik = int(input("Fizik notunu giriniz: "))
kimya = int(input("Kimya notunu giriniz: "))
ortalama = (matematik + fizik + kimya) / 3

if ortalama > 50:
    print("Geçti")
else:
    print("Kaldı")
