def yazdirilanlar(isim, diller):
    print("Aranan:", isim)
    print("Dil:", diller)
    print("Aranıyor...")


def indirildi(isim, dil, uzanti):
    uzanti = uzanti.replace("--", "-")
    dosya_adi = isim.replace(" ", "-")
    dosya_adi = dosya_adi.lower()
    dosya_adi = dosya_adi + uzanti + ".zip"
    print(isim, "için", dil, "altyazı indirildi:", dosya_adi)
