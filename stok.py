class Urun:
    def _init_(self, ad, stok_miktari, fiyat):
        self.ad = ad
        self.stok_miktari = stok_miktari
        self.fiyat = fiyat

    def stok_durumu_guncelle(self, miktar):
        self.stok_miktari += miktar

    def _str_(self):
        return f"{self.ad} - Stok: {self.stok_miktari}, Fiyat: {self.fiyat}"


class Depo:
    def _init_(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        self.urunler[urun.ad] = urun

    def urun_cikar(self, urun_adı):
        if urun_adı in self.urunler:
            del self.urunler[urun_adı]
            print(f"{urun_adı} depodan çıkarıldı.")
        else:
            print(f"{urun_adı} depoda bulunamadı.")

    def urun_stok_guncelle(self, urun_adı, miktar):
        if urun_adı in self.urunler:
            self.urunler[urun_adı].stok_durumu_guncelle(miktar)
            print(f"{urun_adı} stok güncellendi.")
        else:
            print(f"{urun_adı} depoda bulunamadı.")

    def urunleri_listele(self):
        print("Depodaki Ürünler:")
        for urun in self.urunler.values():
            print(urun)


# Örnek kullanım
if _name_ == "_main_":
    depo = Depo()

    # Ürünleri oluştur
    urun1 = Urun("Bilgisayar", 10, 3000)
    urun2 = Urun("Telefon", 20, 2000)
    urun3 = Urun("Tablet", 15, 1500)

    # Depoya ürünleri ekle
    depo.urun_ekle(urun1)
    depo.urun_ekle(urun2)
    depo.urun_ekle(urun3)

    # Depodaki ürünleri listele
    depo.urunleri_listele()

    # Stok güncelleme
    depo.urun_stok_guncelle("Bilgisayar", -5)
    depo.urun_stok_guncelle("Telefon", 10)

    # Depodaki ürünleri tekrar listele
    depo.urunleri_listele()

    # Ürün çıkarma
    depo.urun_cikar("Tablet")

    # Depodaki son durumu listele
    depo.urunleri_listele()
