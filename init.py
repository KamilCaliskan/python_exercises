class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def bilgileri_goster(self):
        print("Araba markası:", self.marka)
        print("Araba modeli:", self.model)
        print("Üretim yılı:", self.yil)

araba1 = Araba("Toyota", "Corolla", 2022)
araba1.bilgileri_goster()
