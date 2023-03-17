from Human import Human
from Laptop import Laptop

# deklarasi class

# deklarasi class menjadi anak dari Human


class Mahasiswa(Human):

    # deklarasi private atribut
    __nim = ""
    __textbooks = []
    __laptop = ""

    # constructor dengan parameter nim, nama, textbooks, dan laptop
    def __init__(self, nik="", nama="", jenis_kelamin="", nim="", textbooks=[], laptop=""):
        Human.__init__(self, nik, nama, jenis_kelamin)
        self.__nim = nim
        self.__textbooks = textbooks
        self.__laptop = laptop

    # setter dan getter untuk masing masing attribut nim, textbooks dan laptop

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_textbooks(self):
        return self.__textbooks

    def set_textbooks(self, textbooks):
        self.__textbooks = textbooks

    def get_laptop(self):
        return self.__laptop

    def set_laptop(self, laptop):
        self.__laptop = laptop

    def attend_class(self):
        print(f"{super().get_nama()} sedang menghadiri kelas")

    def study(self):
        print(f"{super().get_nama()} sedang belajar")

    def work_on_assignment(self):
        print(f"{super().get_nama()} sedang mengerjakan tugas menggunakan laptop merk {self.__laptop.get_brand()}")
