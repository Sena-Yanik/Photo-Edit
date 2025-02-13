def secenek(deger):
  if(deger==1):#fotoğrafı boyutlandırma

    from PIL import Image
    img = Image.open(fotograf)#fotoğrafı açar
    boyut=(img.size)
    print(f"yüklediğiniz fotoğrafın boyutu :{boyut}")
    width = int(input("Yeni genişliği girin: "))
    height = int(input("Yeni yüksekliği girin: "))
    new_boyut = img.resize((width, height))
    new_boyut.save("boyutlandırılmış_fotoğraf.jpg")
    print(f"fotoğraf {width}x{height} boyutuna başarıyla yeniden boyutlandırıldı.")

  elif(deger==2):#fotoğrafı dereceli döndür
    from PIL import Image
    img = Image.open(fotograf)
    derece=int(input("derece giriniz:"))
    img_rotated = img.rotate(derece)
    img_rotated.save("döndürülmüş_fotoğraf.jpg")
    print(f"fotoğraf {derece} derece saat tersinde başarılı şekilde döndürüldü.")

  elif(deger==3):#fotoğraf kırpma
    from PIL import Image
    img = Image.open(fotograf)
    width, height = img.size
    print(f"Orijinal görüntü boyutu: {width}x{height}")
    new_width = int(input("Yeni genişliği girin: "))
    new_height = int(input("Yeni yüksekliği girin: "))

    # Kırpma işlemi için merkezi hesapla
    left = (width - new_width) // 2
    top = (height - new_height) // 2
    right = left + new_width
    bottom = top + new_height

    # Görüntüyü kırp
    cropped_img = img.crop((left, top, right, bottom))

    cropped_img.save("kırpılmış_fotoğraf.jpg")

    cropped_width, cropped_height = cropped_img.size
    print(f"Kırpılmış görüntü boyutu: {cropped_width}x{cropped_height} olarak başarılı şekilde kaydedildi.")

  elif(deger==4):#fotoğrafı grileştirme

    from PIL import Image
    img = Image.open(fotograf)
    img_gray = img.convert("L")
    img_gray.save("grileştirilmiş_fotoğraf.jpg")
    print(f"fotoğrafı grileştirme işlemi başarılı şekilde kaydedildi.")
  
  else:
    print("hatalı seçim yaptınız veya fotoğrafın yolunu doğru yazmadınız tekrar deneyin")


def tamsayi_kontrolu(deger):
  try:
    deger = int(deger)
          
  except ValueError:
    print("Hata: Geçersiz giriş.Yeniden deneyin ve bir tam sayı girin.")

    
print("fotoğraf işleme uygulamasına hoşgeldiniz")
print("1-fotoğrafı boyutlandırma")
print("2-fotoğrafı dereceli döndürme")
print("3-fotoğrafı kırpma")
print("4-fotoğrafı grileştirme")
deger = input("seçim yapınız: ")
tamsayi_kontrolu(deger)
#deger = int(deger)
fotograf = input("fotoğrafın yolunu yaz: ")
secenek(int(deger))