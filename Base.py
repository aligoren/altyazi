import requests as rq
from sys import *
from wget import *
from html.parser import *
from diller import *
from func import *

isim = []
dil = len(argv) - 1


def dilleri_yazdir():
    diller = ["Türkçe", "İngilizce", "Fransızca",
              "Almanca", "İtalyanca", "Rusça", "Arapça", "Kürtçe", "Çince",
              "Japonca", "Yunanca", "Bulgarca", "Vietnamca"]
    diller = sorted(diller)
    for dil in diller:
        print("\t"+dil)

if not len(argv) > 1:
    print()
    print("main.py Film Adı --dil")
    print()
    dilleri_yazdir()
    print()
    print("Desteklenen Dil Kodları:\ntr, en, fr, de, it,"
          " ru, ar, kr, ch, jp, gr, bg, vi")
    print()
    exit(0)

if not argv[dil].startswith("--"):
    print("Dil Belirlemelisiniz")
    exit(0)


class DownloadParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, print it.
                if name == "href":
                    if value.startswith("/download/"):
                        self.data = value

parser = DownloadParser()

harfler = {'İ': 'i', 'Ö': 'o', 'I': 'i', 'ı': 'i',
           'Ç': 'c', 'Ğ': 'g', 'Ş': 's', 'Ü': 'u',
           'ü': 'u', 'ö': 'o', 'ş': 's', 'ç': 'c',
           'ğ': 'g'
           }


def karakter(metin, sozluk):
    for i, j in sozluk.items():
        metin = metin.replace(i, j)
    return metin

for i in range(1, len(argv) - 1):
    isim.append(argv[i])

arananIsim = ' '.join(isim)


def isim_getir():
    isimGetir = '-'.join(isim)

    isimGetir = karakter(isimGetir, harfler)

    isimGetir = isimGetir.replace(" ", "-")

    isimGetir = isimGetir.lower()

    return isimGetir

arama_adres = "https://mvsubtitles.com/" + isim_getir() + "-subtitles"

getir = rq.get(arama_adres)


def adres_getir():
    getir = rq.get(arama_adres)
    return getir


def dilSec(dilGetir, dilTip):
    try:
        indirme_getir = rq.get("https://mvsubtitles.com/" +
                               isim_getir() + "/" + dilGetir + "-subtitles/")
        parser.feed(indirme_getir.text)
        indirmeGetir = parser.data
        download("https://mvsubtitles.com" + indirmeGetir,
                 out=isim_getir() + "-" + dilTip + ".zip", bar=None)
        indirildi(arananIsim, diller(argv[dil]), argv[dil])
    except TypeError as e:
        print("Aradığınız altyazı seçeneği bu film için mevcut değil!")


def altyazi_indir():
    if "Release" in adres_getir().text:
        if diller(argv[dil]) is not None:
            yazdirilanlar(arananIsim, diller(argv[dil]))

        if argv[dil] == "--tr":
            dilSec("turkish", "tr")
        elif argv[dil] == "--en":
            dilSec("english", "en")
        elif argv[dil] == "--fr":
            dilSec("french", "fr")
        elif argv[dil] == "--de":
            dilSec("german", "de")
        elif argv[dil] == "--it":
            dilSec("italian", "it")
        elif argv[dil] == "--ru":
            dilSec("russian", "ru")
        elif argv[dil] == "--ar":
            dilSec("arabic", "ar")
        elif argv[dil] == "--kr":
            dilSec("kurdish", "kr")
        elif argv[dil] == "--ch":
            dilSec("chinese-bg-code", "ch")
        elif argv[dil] == "--jp":
            dilSec("japanese", "jp")
        elif argv[dil] == "--gr":
            dilSec("greek", "gr")
        elif argv[dil] == "--bg":
            dilSec("bulgarian", "bg")
        elif argv[dil] == "--vi":
            dilSec("vietnamese", "vi")
        else:
            print("Bu film için çeviri dosyası yok :(")
    else:
        print("Böyle Bir Film ya da Çeviri Dosyası Yok :(")
