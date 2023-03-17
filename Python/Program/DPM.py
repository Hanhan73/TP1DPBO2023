from Mahasiswa import Mahasiswa

# deklarasi class


class DPM(Mahasiswa):

    # deklarasi private atribut
    __jabatan = ""

    # constructor dengan parameter

    def __init__(self, nik="", nama="", jenis_kelamin="", nim="", textbooks=[], laptop="", jabatan=""):
        Mahasiswa.__init__(self, nik, nama, jenis_kelamin, nim,
                           textbooks, laptop)
        self.__jabatan = jabatan

    # setter dan getter untuk masing masing attribut
    def get_jabatan(self):
        return self.__jabatan

    def set_jabatan(self, jabatan):
        self.__jabatan = jabatan

    def give_appreciation(self):
        print("I appreciate your work")

    def give_recommendation(self):
        print("I think you should do better!")
