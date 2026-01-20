def tahta_hazirla():
    return [[' ' for _ in range(3)] for _ in range(3)]

def sahayi_goster(tahta):
    for satir in tahta:
        print(f" {satir[0]} | {satir[1]} | {satir[2]} ")
        print("---|---|---")

def hamle_yap(tahta, oyuncu):
    while True:
        try:
            satir = int(input(f"Sıra {oyuncu}'de. Satır (1-3): ")) - 1
            sutun = int(input(f"Sıra {oyuncu}'de. Sütun (1-3): ")) - 1
            
            if 0 <= satir <= 2 and 0 <= sutun <= 2:
                if tahta[satir][sutun] == " ":
                    tahta[satir][sutun] = oyuncu
                    break
                else:
                    print("Orası dolu, lütfen başka bir yer seçin.")
            else:
                print("Lütfen 1 ile 3 arasında bir değer giriniz.")
        except ValueError:
            print("Hatalı giriş! Lütfen sadece sayı giriniz.")
        except IndexError:
            print("Lütfen 1-3 aralığında seçim yapınız.")

def kazanani_kontrol_et(tahta, oyuncu):
    for i in range(3):
        if all(tahta[i][j] == oyuncu for j in range(3)): return True
        if all(tahta[j][i] == oyuncu for j in range(3)): return True
    
    if all(tahta[i][i] == oyuncu for i in range(3)): return True
    if all(tahta[i][2-i] == oyuncu for i in range(3)): return True
    
    return False

def beraberlik_kontrol(tahta):
    for satir in tahta:
        if " " in satir: return False
    return True

def oyunu_baslat():
    while True:
        oyun_alani = tahta_hazirla()
        aktif_oyuncu = "X"
        
        while True:
            sahayi_goster(oyun_alani)
            
            hamle_yap(oyun_alani, aktif_oyuncu)
            
            if kazanani_kontrol_et(oyun_alani, aktif_oyuncu):
                print(f"Tebrikler! Kazanan: {aktif_oyuncu}")
                sahayi_goster(oyun_alani)
                break
            
            if beraberlik_kontrol(oyun_alani):
                print("Oyun bitti! Sonuç: Berabere")
                sahayi_goster(oyun_alani)
                break
            
            aktif_oyuncu = "O" if aktif_oyuncu == "X" else "X"
            
        cevap = input("Tekrar oynamak ister misiniz? (e/h): ")
        if cevap.lower() != 'e':
            print("Oyun kapatılıyor, iyi günler!")
            break
oyunu_baslat()