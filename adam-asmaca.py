import random

def adam_asmaca():
    kelimeler = ["python", "programlama", "yapayzeka", "bilgisayar", "oyun"]
    secilen_kelime = random.choice(kelimeler)
    gizli_kelime = ["_"] * len(secilen_kelime)
    tahmin_hakki = 6
    harfler = set(secilen_kelime)

    print("Adam Asmaca Oyununa Hoş Geldiniz!")
    print(" ".join(gizli_kelime))

    while tahmin_hakki > 0 and harfler:
        tahmin = input("Bir harf tahmin edin: ").lower()
        
        if tahmin in harfler:
            harfler.remove(tahmin)
            for i, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    gizli_kelime[i] = tahmin
            print("Doğru tahmin!")
        else:
            tahmin_hakki -= 1
            print(f"Yanlış tahmin! Kalan tahmin hakkı: {tahmin_hakki}")

        print(" ".join(gizli_kelime))

    if not harfler:
        print("Tebrikler, kazandınız! Kelime:", secilen_kelime)
    else:
        print("Üzgünüm, kaybettiniz. Doğru kelime:", secilen_kelime)

# Oyunu başlat
adam_asmaca()
