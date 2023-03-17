from Mahasiswa import Mahasiswa

# deklarasi class


class AsistenDosen(Mahasiswa):

    # deklarasi private atribut
    __jadwal = []
    __tugas = []

    # constructor dengan parameter

    def __init__(self, nik="", nama="", jenis_kelamin="", nim="", textbooks=[], laptop="", jadwal=[], tugas=[]):
        Mahasiswa.__init__(self, nik, nama, jenis_kelamin,
                           nim, textbooks, laptop)
        self.__jadwal = jadwal
        self.__tugas = tugas

    # setter dan getter untuk masing masing attribut
    def get_jadwal(self):
        return self.__jadwal

    def set_jadwal(self, jadwal):
        self.__jadwal = jadwal

    def get_tugas(self):
        return self.__tugas

    def set_tugas(self, tugas):
        self.__tugas = tugas

    def teaching(self, index):
        print(
            f"{super().get_nama()} sedang mengajar di kelas pada hari {self.__jadwal[index]}")

    def give_homework(self):
        print(f"{super().get_nama()} sedang memberikan PR")
