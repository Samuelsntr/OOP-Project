class Ayam:

    def __init__(self,nama,darah,tenaga,pertahanan):
        self.nama = nama
        self.darah = darah
        self.tenaga = tenaga
        self.pertahanan = pertahanan

    def serang(self,musuh):
        print(self.nama + ' menyerang ' + musuh.nama)
        musuh.diserang(self,self.tenaga)

    def diserang(self,musuh,serangan_musuh):
        print(self.nama + ' diserang oleh ' + musuh.nama)
        serangan_diterima = serangan_musuh/self.pertahanan
        print('Serangan diterima: ' + str(serangan_diterima))
        self.darah -= serangan_diterima
        print('Sisa darah '+ str(self.darah))

bangkok = Ayam('Bangkok',100,50,50)
kampung = Ayam('Kampung',100,50,50)

print('#'*50)
bangkok.serang(kampung)
print('#'*50)
kampung.serang(bangkok)