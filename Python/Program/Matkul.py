# deklarasi class

class Matkul:

    # deklarasi private atribut
    __kode = ""
    __nama_matkul = ""
    __dosen = []

    # constructor dengan parameter

    def __init__(self, kode="", nama_matkul="", dosen=[]):
        self.__kode = kode
        self.__nama_matkul = nama_matkul
        self.__dosen = dosen

    # setter dan getter untuk masing masing attribut
    def get_kode(self):
        return self.__kode

    def set_kode(self, kode):
        self.__kode = kode

    def get_nama_matkul(self):
        return self.__nama_matkul

    def set_nama_matkul(self, nama_matkul):
        self.__nama_matkul = nama_matkul

    def get_dosen(self):
        return self.__dosen

    def set_dosen(self, dosen):
        self.__dosen = dosen
