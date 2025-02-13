# Fotoğraf İşleme Uygulaması

Bu proje, kullanıcıların fotoğraflarını kolayca işleyebilmelerini sağlayan bir Python uygulamasıdır. Uygulama, kullanıcıya çeşitli seçenekler sunarak fotoğraflar üzerinde temel düzenlemeler yapmasına olanak tanır.

## Özellikler
- **Fotoğraf Boyutlandırma**: Kullanıcıdan yeni genişlik ve yükseklik değerleri alarak fotoğrafı yeniden boyutlandırır.
- **Fotoğrafı Dereceli Döndürme**: Kullanıcının belirttiği derece kadar fotoğrafı döndürür.
- **Fotoğraf Kırpma**: Kullanıcının belirttiği genişlik ve yükseklik değerlerine göre fotoğrafı kırpar.
- **Fotoğrafı Grileştirme**: Fotoğrafı gri tonlamaya çevirir.

## Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```bash
pip install pillow
```

## Kullanım
1. Projeyi bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/proje-adi.git
   ```
2. Terminal veya Komut İstemcisi'ni açarak proje klasörüne girin:
   ```bash
   cd proje-adi
   ```
3. Python dosyasını çalıştırın:
   ```bash
   python dosya_adi.py
   ```
4. Açılan menüden yapmak istediğiniz işlemi seçin ve gerekli girdileri girerek işlemi tamamlayın.

## Kullanım Adımları
1. Program çalıştırıldığında kullanıcıdan bir işlem seçmesi istenir.
2. Kullanıcı bir seçim yaptıktan sonra fotoğrafın dosya yolu sorulur.
3. Seçime bağlı olarak ilgili işlem gerçekleştirilir ve çıktı dosyası oluşturulur.
4. İşlem tamamlandığında, yeni oluşturulan fotoğraf dosyası kaydedilir ve kullanıcıya işlemin tamamlandığı bildirilir.

## Çıktılar
- **Boyutlandırılmış Fotoğraf**: `boyutlandırılmış_fotoğraf.jpg`
- **Döndürülmüş Fotoğraf**: `döndürülmüş_fotoğraf.jpg`
- **Kırpılmış Fotoğraf**: `kırpılmış_fotoğraf.jpg`
- **Grileştirilmiş Fotoğraf**: `grileştirilmiş_fotoğraf.jpg`

## Katkıda Bulunma
Eğer projeye katkıda bulunmak isterseniz, lütfen bir `fork` yapın ve geliştirmelerinizi içeren bir `pull request` gönderin.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.

---
**Not**: Lütfen kendi GitHub kullanıcı adınızı ve proje adınızı klonlama komutunda değiştirin.

