# TP1DPBO2023
## Janji
Saya Farhan Muzhaffar Tiras Putra NIM 2105879 mengerjakan soal Tugas Praktikum 1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Soal
Rapi (M) is a student as well as the President of BEM in his department. He has some friends with specific positions, such as Alga (M) who became a DPM member, or Najmi (F) and Bulan (M) who are the assistants of Mrs. Rose (F), a programming lecturer. However, there are some regular students, like Afri (M) and Anin (F).
As a happy human being, everyone could do what a human usually does, like eat, drink, and sleep. Meanwhile, Rapi as well as his friends have stuff a student usually has, such as NIM, a few textbooks, and a laptop. Besides, they could do what a student usually does, such as studying, attending classes, and working on assignments.
Fortunately enough, Rapi as a president of BEM, who has an enormous amount of programs and innovations on his mind, can do specific things such as doing a program, planning an innovation, and working on innovation. Meanwhile, Alga whose job is to monitor Rapi's activities will provide appreciation as well as recommendations. He always says “I appreciate your work” to every completed development from Rapi and his team. On the other hand, Najmi and Bulan may help Mrs. Rose in teaching and giving homework. Mrs. Rose herself, as a lecturer, has some stuff for teaching, such as NIP, some whiteboard markers, and a laptop. She also has to fulfill his duties by teaching, giving assignments, and giving scores. 
Based on the story above, choose keywords that may be important, then make their design, objects, as well as their relations in OOP!

## Desain Program
![TP1DPBO drawio](https://user-images.githubusercontent.com/96176429/225837406-1d612095-d7c1-4f3b-b050-518a33219eb1.png)
1. Human
   - Attribut:
     - nik
     - nama
     - jenis_kelamin 
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
     - eat() = untuk menampilkan sedang makan
     - sleep() = untuk menampilkan sedang tidur
     - drink() = untuk menampilkan sedang minum
   - Relasi: - 
2. Dosen
   - Attribut:
     - nip
     - whiteboardsMarker = jumlah spidol yang dimiliki oleh dosen tersebut
     - laptop
     - mahasiswa = para mahasiswa yang diajar oleh dosen tersebut
     - asistenDosen = para mahasiswa yang juga membantu dosen tersebut menjadi asisten dosen
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
     - teaching() = untuk menampilkan dosen sedang mengajar
     - give_assignment() = untuk menampilkan dosen sedang memberikan tugas
     - give_score() = untuk menampilkan dosen sedang memberikan nilai
   - Relasi:
     - Dosen is a Human
       Karena Dosen dan Human adalah objek yang sama dan attibut dalam Human dapat masuk ke dalam attribut Dosen
     - Dosen has a Laptop
       Setiap Dosen pasti memiliki sebuah Laptop yang digunakan untuk mengajar para Mahasiswa
3. Mahasiswa
   - Attribut:
     - nim
     - textbooks = sekumpulan buku catatan milik Mahasiswa
     - laptop
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
     - attend_class() = untuk menampilkan Mahasiswa sedang menghadiri kelas
     - study() = untuk menampilkan Mahasiswa sedang belajar
     - work_on_assignment() = untuk menampilkan Mahasiswa sedang mengerjakan tugas
   - Relasi:
     - Mahasiswa is a Human
       Karena Mahasiswa dan Human adalah objek yang sama dan attibut dalam Human dapat masuk ke dalam attribut Mahasiswa
     - Dosen has a Laptop
       Hampir Setiap Mahasiswa pasti memiliki sebuah Laptop yang digunakan untuk belajar
4. BEM
   - Attribut:
     - jabaran
     - innovations = sekumpulan inovasi yang dimiliki oleh anggota BEM ini
     - programs = sekumpulan program yang akan atau sedang berjalan yang dilakukan oleh anggota BEM ini
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
     - do_program() = untuk menampilkan program yang akan dilakukan
     - plan_innovation() = untuk menampilkan rencana inovasi
     - work_on_innovation() = untuk menampilkan inovasi yang sedang dilakukan
   - Relasi:
     - BEM is a Mahasiswa
       Karena yang dimaksud disini adalah anggota BEM, jadi pastinya anggota BEM adalah seorang mahasiswa, attribut yang dimiliki oleh Mahasiswa diperlukan dalam BEM
5. DPM
   - Attribut:
     - jabatan
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
     - give_appreciation() = untuk menampilakn apresiasi
     - give_recommendation() = untuk menampikan rekomendasi
   - Relasi:
     - DPM is a Mahasiswa
       Karena yang dimaksud disini adalah anggota DPM, jadi pastinya anggota DPM adalah seorang mahasiswa, attribut yang dimiliki oleh Mahasiswa diperlukan dalam DPM
6. AsistenDosen
   - Attribut:
     - jadwal = jadwal dimana asisten dosen ini membantu dosen
     - tugas = tugas yang asisten dosen lakukan
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
     - teaching() = menampilkan asisten dosen sedang mengajar
     - give_homework() = menampilkan asisten dosen memberikan pr
   - Relasi:
     - AsistenDosen is a Mahasiswa
       Karena pasti Asisten Dosen adalah seorang mahasiswa, attribut yang dimiliki oleh Mahasiswa diperlukan dalam AsistenDosen
7. Laptop
   - Attribut:
     - brand
     - model
     - year = tahun rilis dari laptop
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
   - Relasi:
     - asdasd 
8. Matkul
   - Attribut:
     - kode
     - nama_matkul
     - dosen = kumpulan dosen yang mengajar mata kuliah tersebut
   - Methods:
     - get_...() = mengambil value dari attribut
     - set_...() = menetapkan value untuk attribut
   - Relasi:
     - Matkul has a dosen
       Karena setiap matkul memiliki dosen yang mengajar mata kuliah tersebut
       
## Alur Program
1. Masukkan class yang akan digunakan
2. Deklarasikan array
3. instansiasi-kan class di dalam array
4. Menampilkan semua isi dari array dan aktivitas masing-masing class
5. DONE

## Dokumentasi
![Read](https://user-images.githubusercontent.com/96176429/225839893-f1b8a3ec-f2d6-4922-8db2-6cc08d28581b.png)











