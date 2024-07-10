class Buah:
    def __init__(self,nama,warna,rasa):
        self.__nama = nama
        self.__warna = warna
        self.__rasa = rasa

    def getNama(self):
        return self.__nama
    def getWarna(self):
        return self.__warna
    def getRasa(self):
        return self.__rasa
    
    def Informasi(self):
        return f'Nama : {self.getNama()}, Warna : {self.getWarna()}, Rasa : {self.getRasa}'
    
class Mangga(Buah):
    def __init__(self,vitamin):
        Buah.__init__(self,vitamin)
        self.__vitamin = vitamin    

    def info(self):
        return f'{self.Informasi()}, Kandungan Vitamin : {self.__vitamin}'     