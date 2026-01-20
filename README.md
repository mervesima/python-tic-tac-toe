# python-tic-tac-toe
Python ile geliştirilmiş, iki kişilik, hata yönetimi ve matris mantığına dayalı terminal tabanlı strateji oyunu
# 🎮 Python Tic-Tac-Toe (X-O-X) Oyunu

Bu proje, Python programlama dilinin temel mantığını, döngüleri ve karar yapılarını pekiştirmek amacıyla geliştirilmiş klasik bir X-O-X oyunudur.

## 🕹️ Oyun Özellikleri
- **İki Kişilik Mod:** Arkadaşınızla aynı terminal üzerinden karşılıklı oynama imkanı.
- **Hata Yönetimi (Error Handling):** Dolu hücreye hamle yapma veya geçersiz karakter girme gibi durumlarda kullanıcıyı uyaran kontrol mekanizması.
- **Dinamik Tahta:** Her hamleden sonra güncellenen ve terminalde temiz bir şekilde görüntülenen oyun alanı.

## 🧠 Algoritma Mantığı
- Oyun tahtası 3x3'lük bir liste (matris) yapısı üzerinde tutulur.
- Her hamleden sonra satır, sütun ve çapraz kontrol yapılarak kazanan olup olmadığı kontrol edilir.
- Beraberlik durumu için hamle sayısı takibi yapılır.

## 🚀 Nasıl Çalıştırılır?
```python
python main.py
