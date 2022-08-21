print("Sipariş Sepetine Hoşgeldiniz")
print("1. Adana kebap: 20TL\n2. Lahmacun: 12TL\n3. Günün çorbası: 10TL\n4. Pizza: 30TL")
yiyecekler = input("Şiparişlerinizi virgülle ayırarak girin. örnek (1,3) :")
print("1. Kola: 10TL\n2. Şalgam: 8TL\n3. Ayran: 5TL\n4. Su: 3TL")
icecekler = input("Şiparişlerinizi virgülle ayırarak girin. örnek (1,3) :")

yiyecek_listesi = yiyecekler.split(",")
icecek_listesi = icecekler.split(",")
yiyecek_siparisler = []
yiyecek_fiyatlar = []
for siparis in yiyecek_listesi:
    if siparis == "1":
        yiyecek = "Adana kebap"
        fiyat = 20
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)
    if siparis == "2":
        yiyecek = "Lahmacun"
        fiyat = 12
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)
    if siparis == "3":
        yiyecek = "Günün çorbası"
        fiyat = 10
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)
    if siparis == "4":
        yiyecek = "Pizza"
        fiyat = 30
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)

for siparis in icecek_listesi:
    if siparis == "1":
        yiyecek = "Kola"
        fiyat = 10
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)
    if siparis == "2":
        yiyecek = "Şalgam"
        fiyat = 8
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)
    if siparis == "3":
        yiyecek = "Ayran"
        fiyat = 5
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)
    if siparis == "4":
        yiyecek = "Su"
        fiyat = 3
        yiyecek_siparisler.append(yiyecek)
        yiyecek_fiyatlar.append(fiyat)

siparisler = ", ".join(yiyecek_siparisler)
toplam_fiyat = sum(yiyecek_fiyatlar)
print(f"Siparişleriniz : {siparisler}\nToplam tutar : {toplam_fiyat} TL")
