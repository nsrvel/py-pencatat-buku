# py-pencatat-buku


<img src="https://github.com/nsrvel/py-pencatat-buku/blob/61bb6625528f13549340bc26cbbacac5fedd3c54/screen_capture.png?raw=true" width="1000"/>
<br></br>

## Description
#### UAS Pemrograman Dasar Lab
Aplikasi Pencatat Buku

Task: Anda diminta untuk menyiapkan aplikasi sederhana untuk mencatat
informasi buku (no_isbn, judul, pengarang, penerbit, kota, tahun) ke dalam
sebuah database (nama tabel: buku)

Task Feature:
-    Tambah data
-    Lihat data
-    Keluar Program

Adapun struktur tabel buku sebagai berikut: (field yang digunakan):
-    no_isbn : varchar(15)
-    judul : varchar(50)
-    pengarang : varchar(30)
-    penerbit : varchar(30)
-    kota : varchar(25)
-    tahun : varchar(4)

Kriteria Penilaian:

-    Program berjalan sesuai dengan spesifikasi yang diberikan
-    Gunakan teknik penulisan program yang sudah dipelajari selama
perkuliahan (penamaan variable, struktur kontrol, error handling, dll)

<br></br>
## 👨‍💻 Requirements
    pip install pyfiglet questionary python-dotenv rich

<br></br>
## 🚀 How to run?

#### Run:
  
    python ./main.py
      
#### Run and insert initial data books:
  
    python ./main.py --init
  
#### Run and reset database:
  
    python ./main.py --reset
