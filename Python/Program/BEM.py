from Mahasiswa import Mahasiswa

# deklarasi class


class BEM(Mahasiswa):

    # deklarasi private atribut
    __jabatan = ""
    __innovation = []
    __program = []

    # constructor dengan parameter

    def __init__(self, nik="", nama="", jenis_kelamin="", nim="", textbooks=[], laptop="", jabatan="", innovation=[], program=[]):
        Mahasiswa.__init__(self, nik, nama, jenis_kelamin,
                           nim, textbooks, laptop)
        self.__jabatan = jabatan
        self.__innovation = innovation
        self.__program = program

    # setter dan getter untuk masing masing attribut

    def get_jabatan(self):
        return self.__jabatan

    def set_jabatan(self, jabatan):
        self.__jabatan = jabatan

    def get_innovation(self):
        return self.__innovation

    def set_innovation(self, innovation):
        self.__innovation = innovation

    def get_program(self):
        return self.__program

    def set_program(self, program):
        self.__program = program

    def do_program(self, index):
        print(
            f"{super().get_nama()} sebagai {self.__jabatan} sedang melakukan program {self.__program[index]}")

    def plan_innovation(self, index):
        print(
            f"{super().get_nama()} sebagai {self.__jabatan} sedang merencanakan inovasi beruapa {self.__innovation[index]}")

    def work_on_innovation(self, index):
        print(
            f"{super().get_nama()} sebagai {self.__jabatan} sedang mengerjakan inovasi-nya, yaitu {self.__innovation[index]}")
