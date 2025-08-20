birinci_urun =int(input("Birinci ürünün fiyatı:"))
ikinci_urun =int(input("İkinci ürünün fiyatı:"))
ucuncu_urun = int(input("Üçüncü ürünün fiyatı:"))

toplam_fiyat = birinci_urun + ikinci_urun + ucuncu_urun

if toplam_fiyat > 200:
    indirimli_fiyat = toplam_fiyat - (toplam_fiyat * 0.10)
    print(f"Sepet Tutarı: {indirimli_fiyat} TL")

else:
    print(f"Sepet Tutarı: {toplam_fiyat} Tl.")