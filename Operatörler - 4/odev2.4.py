fiyat = float(input("Ürün fiyatını giriniz: "))
indirim_orani = float(input("İndirim oranını giriniz (%): "))
indirimli_fiyat = fiyat - (fiyat * indirim_orani / 100)

print(f"İndirimli fiyat:{indirimli_fiyat} TL")
