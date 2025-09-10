"# footballshop" 
Langkah A. Dasar Git

1. Buat repo di GitHub.
2. Inisialisasi lokal dengan git init.
3. Tambah file → buat README.md.
4. Add & commit.
5. Hubungkan remote.
6. Push ke GitHub.
7. Clone repo lain.
8. Branching.
9. Merge di GitHub.

Langkah B. Buat Proyek Django
1. Siapkan folder baru.
2. Aktifkan virtualenv
3. Buat requirements.txt.
4. Install dependencies.
5. Start project Django.
6. Buat file .env dan isi PRODUCTION=False.
7. Buat file .env.prod dan isi kredensial PostgreSQL dari ITF UI.
8. Ubah settings.py. Load dotenv, set ALLOWED_HOSTS, konfigurasi DB sesuai PRODUCTION.
9. Migrasi DB.
10. Jalankan server, lalu cek di localhost:8000.
11. Matikan server.
12. Tambahkan 'main' ke INSTALLED_APPS di settings.py.
13. Buat folder main/templates/ dan file main.html.
14. Buat model Shop, lalu tambahkan atribut, kategori, dan fungsi yang sesuai.
15. Jalankan migrasi.
16. Edit main/views.py dengan data diri.
17. Edit template main.html dengan ganti isi hardcode dengan variable Django.
18. Edit berkas urls.py di direktori proyek (football-news).
19. Jalankan server dan buka di browser.

Langkah C. Push ke PWS
1. Langkah pertama adalah membuka situs https://pbp.cs.ui.ac.id, lalu login menggunakan akun SSO UI.
2. Selanjutnya buat proyek baru dengan menekan tombol Create New Project.
3. Simpan project Credentials dan Project Command.
4. Kemudian pilih proyek yang sudah dibuat di sidebar, lalu buka tab Environs dan klik Raw Editor. Salin isi file .env.prod ke editor, lalu tekan Update All Variables.
5. Selanjutnya buka file settings.py pada proyek Django, kemudian tambahkan URL deployment ke dalam ALLOWED_HOSTS. Format URL adalah <username-sso>-<nama-proyek>.pbp.cs.ui.ac.id, dengan titik pada username diganti menjadi strip dan tanpa _ karena saya salah disitu.
6. Simpan perubahan ini, lalu jalankan git add, git commit, dan git push origin master. Setelah itu jalankan perintah dari Project Command di PWS dan login menggunakan credentials PWS.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](image.png)

Jelaskan peran settings.py dalam proyek Django?
Migrasi database di Django adalah mekanisme untuk menyinkronkan perubahan model Python dengan struktur database. Setiap perubahan pada model dicatat dalam file migrasi yang berisi instruksi perubahan skema, lalu diterjemahkan Django menjadi query SQL sesuai jenis database yang digunakan. Dengan konsep ini, database dapat berkembang mengikuti kode secara bertahap tanpa kehilangan data yang sudah ada, karena proses pembuatan, pengubahan, atau penghapusan tabel dilakukan secara terkontrol.

Bagaimana cara kerja migrasi database di Django?
Migrasi di Django adalah proses untuk menyamakan definisi model dalam kode Python dengan struktur database yang digunakan. Pertama, developer mendefinisikan atau mengubah model pada file models.py. Kedua, perintah python manage.py makemigrations digunakan untuk membuat file migrasi yang berisi instruksi perubahan database dalam bentuk Python. Ketiga, perintah python manage.py migrate mengeksekusi file migrasi tersebut sehingga struktur database benar-benar diperbarui sesuai dengan definisi model. Dengan sistem ini, developer tidak perlu menulis query SQL secara manual.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dijadikan framework awal untuk pembelajaran karena sifatnya yang lengkap dan terstruktur. Django menggunakan pola MVT (Model-View-Template) yang memperkenalkan konsep penting dalam pengembangan perangkat lunak, seperti pemisahan logika bisnis, data, dan tampilan. Selain itu, Django memiliki banyak fitur bawaan seperti sistem autentikasi, ORM, dan template engine, sehingga pemula bisa langsung membangun aplikasi nyata tanpa harus menambahkan banyak library eksternal. Django juga menekankan best practices dalam penulisan kode, memiliki komunitas besar, serta dokumentasi yang sangat baik, sehingga cocok sebagai dasar sebelum mempelajari framework lain.

Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Asdos sudah menjelaskan tutorial dengan legkap dan mudah dimengerti.