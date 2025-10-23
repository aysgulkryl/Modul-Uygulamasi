from menu_sistemi import Menu

# Kitap arama fonksiyonu


def kitap_ara():
    arama = input("Aradığınız kitabın adını giriniz: ").strip().lower()
    print("\n")

    bulundu = False

    try:
        with open("kitaplar.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                kitap_adi_satir = satir.split("|")[0].strip().lower()
                if arama == kitap_adi_satir:
                    bulundu = True
                    print("Aradığınız kitap dosyada bulunmaktadır:\n")
                    print(satir.strip())
                    print("\n")
                    break

            if not bulundu:
                print("Aradığınız kitap dosyada bulunmamaktadır.\n")

    except FileNotFoundError:
        print("Henüz kitap eklenmemiş. Dosya bulunamadı.\n")

# Kitap ekleme fonksiyonu

def kitap_ekle():
  print("\n")
  kitap_adi = input("Eklemek istediğiniz kitabın adını giriniz: ").strip()
  print("\n")
  yazar = input("Eklemek istediğiniz kitabın yazarını giriniz: ").strip()
  print("\n")
  tur = input("Eklemek istediğiniz kitabın türünü giriniz: ").strip()
  print("\n")
  yayin_evi = input("Eklemek istediğiniz kitabın yayınevini giriniz: ").strip()
  print("\n")
  basim_yili =input("Eklemek istediğiniz kitabın basım yılını giriniz: ").strip()
  print("\n")

  yeni_kayit = f"{kitap_adi} | {yazar} | {tur} | {yayin_evi} | {basim_yili}"
  print("\n")

  with open ("kitaplar.txt", "a", encoding="utf-8") as dosya:
    dosya.write(yeni_kayit + "\n")

  print("Yeni kitap kaydı eklendi. \n")

# Kitap listeleme fonksiyonu

def kitap_listele():
  print("\n")
  print("Kitap Listesi")
  print("\n")

  try:
    with open("kitaplar.txt", "r", encoding="utf-8") as dosya:
      kitaplar = dosya.readlines()
      if not kitaplar:
        print("Henüz kitap eklenmemiş.\n")
      else:
       for satir in kitaplar:
        print(satir.strip())
        print("\n")

  except FileNotFoundError:
    print(" Kitaplar dosyasında kayıt bulunamadı. Lütfen önce kitap ekleyin.")
    print("\n")

# Menü Oluşturma

menu = Menu("Kitaplık Uygulaması")

menu.menu_ogesi_ekle("Kitap Ara", kitap_ara)
menu.menu_ogesi_ekle("Kitap Ekle", kitap_ekle)
menu.menu_ogesi_ekle("Kitapları Listele", kitap_listele)

menu.calistir()
