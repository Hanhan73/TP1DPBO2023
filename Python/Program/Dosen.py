from Human import Human

# deklarasi class

# deklarasi class menjadi anak dari Human


class Dosen(Human):

    # deklarasi private atribut
    __nip = ""
    __whiteboardMarker = ""
    __laptop = ""
    __mahasiswa = []
    __asistenDosen = []
    # constructor dengan parameter nip, nama

    def __init__(self, nik="", nama="", jenis_kelamin="", nip="",  whiteboardMarker="", laptop="", mahasiswa=[], asistenDosen=[]):
        Human.__init__(self, nik, nama, jenis_kelamin)
        self.__nip = nip
        self.__nama = nama
        self.__whiteboardMarker = whiteboardMarker
        self.__laptop = laptop
        self.__mahasiswa = mahasiswa
        self.__asistenDosen = asistenDosen

    # setter dan getter untuk masing masing attribut nip, nama

    def get_nip(self):
        return self.__nip

    def set_nip(self, nip):
        self.__nip = nip

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_whiteboardMarker(self):
        return self.__whiteboardMarker

    def set_whiteboardMarker(self, whiteboardMarker):
        self.__whiteboardMarker = whiteboardMarker

    def get_laptop(self):
        return self.__laptop

    def set_laptop(self, laptop):
        self.__laptop = laptop

    def get_mahasiswa(self):
        return self.__mahasiswa

    def set_mahasiswa(self, mahasiswa):
        self.__mahasiswa = mahasiswa

    def get_asistenDosen(self):
        return self.__asistenDosen

    def set_asistenDosen(self, asistenDosen):
        self.__asistenDosen = asistenDosen

    def teaching(self):
        print(f"{super().get_nama()} sedang mengajar")

    def give_assignment(self):
        print(f"{super().get_nama()} sedang memberikan tugas")

    def give_score(self):
        print(f"{super().get_nama()} sedang memberikan nilai")
