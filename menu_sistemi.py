# Menü sistemi modülü

class Menu:
  def __init__(self,baslik):
    self.baslik = baslik
    self.menu_ogeleri = []

  def menu_ogesi_ekle(self,oge,fonksiyon):
    self.menu_ogeleri.append([oge,fonksiyon])

  def menu_goster(self):
    print("\n" + self.baslik)
    print("\n")

    for i, oge in enumerate(self.menu_ogeleri):
      print(f"{i + 1}. {oge[0]}")
      
    print(f"{len(self.menu_ogeleri) + 1}. Çıkış")
    print("\n")

  def calistir(self):

    while True:
      self.menu_goster()

      try:
        secim = int(input("Kitaplık uygulamasına hoşgeldiniz. Lütfen yapmak istediğiniz işlemi seçiniz: "))
        
      except ValueError:
        print("Lütfen sadece sayı giriniz.")
        continue

      cikis_numarasi = len(self.menu_ogeleri) + 1


      if 1 <= secim <= len(self.menu_ogeleri):
        self.menu_ogeleri[secim - 1][1]()

      elif secim == cikis_numarasi:
        print("Çıkış işlemi seçildi. Program sonlandırılıyor...")
        break 

      else:
        print("Geçersiz seçim yaptınız. Yapmak istediğiniz işleme göre 1 ile", cikis_numarasi, "arasında bir sayı seçiniz." )
        print("\n")