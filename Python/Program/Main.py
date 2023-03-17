# import class dari file
from Human import Human
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from BEM import BEM
from DPM import DPM
from AsistenDosen import AsistenDosen
from Matkul import Matkul
from Laptop import Laptop

# deklarasi array
listMHS = []
listDosen = []
listBEM = []
listDPM = []
listAsistenDosen = []
listMatkul = []
listLaptop = []

# mengisi setiap list dengan instasisasi class seperti mahasiswa, bem, dpm, dosen, laptop, dan matkul
listMHS.extend([Mahasiswa("123456791230", "Afri", "M", "2100001", ["Catetan Programming", "Catetan RPL"],
                          Laptop("Apple", "MacBook Air", "2020")),
               Mahasiswa("123112791230", "Anin", "F", "2100002", ["Catetan Andal", "Catetan Promvis"],
                         Laptop("HP", "Envy 13", "2021"))])

listBEM.append(BEM("123552521230", "Rapi", "M", "2100003", ["Catetan Programming", "Catetan Andal"],
                   Laptop("Lenovo", "Yoga C940", "2020"), "President", ["Webinar", "Mentorship"], ["Hackatons", "Kompetisi Programming"]))

listDPM.append(DPM("123552522331", "Alga", "M", "2100004", ["Catetan Sistem Operasi"],
                   Laptop("Dell", "G3 15", "2021"), "Supervisor"))

listAsistenDosen.extend([AsistenDosen("1234412311", "Bulan", "M", "2100005", ["Catetan Programming"],
                                      Laptop("Acer", "Predator Helios 300", "2021"), ["Senin", "Selasa"], ["Memeriksa Tugas", "Mengajar"]),
                        AsistenDosen("12312411230", "Bulan", "M", "2100006", ["Catetan Programming"],
                                     Laptop("Acer", "Swift 5", "2021"), ["Kamis", "Jumat"], ["Memberikan Tugas", "Mengajar"])])

listDosen.append(Dosen("123456791230", "Mrs. Rose", "F", "12313451551", 2,
                       Laptop("ASUS", "ZenBook Pro Duo UX581", "2019"), [listMHS, listBEM, listDPM, listAsistenDosen], listAsistenDosen))

listMatkul.append(Matkul("IK21", "Ilmu Komputer", listDosen))

#  menampilkan isi dari list dengan looping for dan setiap attributnya ditampilkan dengan memanggil getter masing-masing attribut
n = 1
print("Data Lengkap Mata Kuliah: ")
for i in listMatkul:
    print(f"\t - {i.get_kode()} {i.get_nama_matkul()}")
    for j in listDosen:
        print(
            f"\t   List Dosen     :  {j.get_nip()} - {j.get_nama()}({j.get_jenis_kelamin()})")

print("")

print("Data Lengkap Mahasiswa: ")
print("A. Mahasiswa Biasa: ")
for i in listMHS:
    print(f"\t - {i.get_nim()} - {i.get_nama()}({i.get_jenis_kelamin()})")

print("")
print("B. Mahasiswa Anggota BEM: ")
for i in listBEM:
    print(
        f"\t - {i.get_nim()} - {i.get_nama()}({i.get_jenis_kelamin()}) - {i.get_jabatan()}")

print("")
print("C. Mahasiswa Anggota DPM: ")
for i in listDPM:
    print(
        f"\t - {i.get_nim()} - {i.get_nama()}({i.get_jenis_kelamin()}) - {i.get_jabatan()}")


# menampilkan aktivitas class dengan memanggil method masing" kelas
print("")
print("Aktivitas")
listMHS[1].work_on_assignment()
listDosen[0].teaching()
listDPM[0].give_appreciation()
listBEM[0].work_on_innovation(0)
listAsistenDosen[0].teaching(1)
