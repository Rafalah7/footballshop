<details>
<Summary><b>Tugas 2</b></Summary>
"footballshop" 
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
18. Edit berkas urls.py di direktori proyek (footballshop).
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
</details>

<details>
<Summary><b>Tugas 3</b></Summary>
Langkah-Langkah Tugas 3: 
A. Form dan Data Delivery

1. Buat direktori templates di root project.
2. Buat file `base.html` dengan isi template dasar:
3. Atur `settings.py` → tambahkan `DIRS: [BASE_DIR / 'templates']` di bagian `TEMPLATES`.
4. Ubah `main/templates/main.html` agar extend `base.html`.
---

B. Membuat Form Input Data (Product)
1. Buat file `forms.py` di direktori `main`:
2. Update `views.py`:

   * Tambahkan fungsi `show_main`, `create_product`, dan `show_products`.
3. Update `urls.py` di `main`:
4. Update `main/templates/main.html` untuk menampilkan daftar berita + tombol tambah.
5. Buat `create_product.html` (form tambah product).
6. Buat `product_detail.html` (halaman detail product).
---

C. Atur CSRF Trusted Origins
Di `settings.py`, tambahkan:
```
CSRF_TRUSTED_ORIGINS = [
    "https://rafalah-izak-footballshop.pbp.cs.ui.ac.id"
]
```
---

D. Mengembalikan Data dalam Bentuk XML
1. Tambahkan fungsi di `views.py`:

   ```
   from django.http import HttpResponse
   from django.core import serializers

   def show_xml(request):
       product_list = product.objects.all()
       xml_data = serializers.serialize("xml", product_list)
       return HttpResponse(xml_data, content_type="application/xml")
   ```
2. Tambahkan URL di `urls.py`:

   ```
   path('xml/', show_xml, name='show_xml'),
   ```
3. Coba buka `http://localhost:8000/xml/`.

---

6. Mengembalikan Data dalam Bentuk JSON

1. Tambahkan fungsi di `views.py`:

   ```
   def show_json(request):
       product_list = Product.objects.all()
       json_data = serializers.serialize("json", product_list)
       return HttpResponse(json_data, content_type="application/json")
   ```
2. Tambahkan URL di `urls.py`:

   ```
   path('json/', show_json, name='show_json'),
   ```
3. Coba buka `http://localhost:8000/json/`.

---

7. Mengembalikan Data Berdasarkan ID

1. Tambahkan fungsi di `views.py`:

   ```
   def show_xml_by_id(request, id):
       try:
           product_item = Product.objects.filter(pk=id)
           xml_data = serializers.serialize("xml", product_item)
           return HttpResponse(xml_data, content_type="application/xml")
       except product.DoesNotExist:
           return HttpResponse(status=404)

   def show_json_by_id(request, id):
       try:
           product_item = Product.objects.get(pk=id)
           json_data = serializers.serialize("json", [product_item])
           return HttpResponse(json_data, content_type="application/json")
       except product.DoesNotExist:
           return HttpResponse(status=404)
   ```
2. Tambahkan URL di `urls.py`:

   ```
   path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
   path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
   ```
3. Coba akses `http://localhost:8000/xml/1/` atau `http://localhost:8000/json/1/`.

---

8. Gunakan Postman untuk Mengecek

1. Buka Postman → buat request `GET` ke:

   * `http://localhost:8000/xml/`
   * `http://localhost:8000/json/`
2. Klik Send, lihat response dalam format XML atau JSON.
3. Bisa juga coba dengan `/xml/<id>` atau `/json/<id>`.

---

9. Push ke GitHub & PWS

```
git add .
git commit -m
git push origin master
git push pws master
```

---

Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

* Platform modern (misalnya e-commerce, media sosial, atau sistem kampus) biasanya punya banyak komponen: frontend (UI), backend (server), database, bahkan aplikasi mobile.
* Data delivery = cara mengirim dan menerima data antar komponen tersebut.
* Tanpa mekanisme ini, frontend tidak bisa menampilkan data dari database, dan aplikasi mobile tidak bisa sinkron dengan server.

Jadi, data delivery itu penting supaya sistem bisa komunikasi dan sinkron antar bagian.

Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer?

* XML:
  ✔️ Bagus untuk data yang **kompleks & terstruktur hierarkis**, mendukung atribut, namespace.
  ❌ Lebih berat, verbose (tag panjang), parsing lebih lambat.

* JSON:
  ✔️ Ringkas, mudah dibaca manusia, parsing cepat.
  ✔️ Native support di JavaScript (jadi gampang dipakai di web).
  ✔️ Lebih hemat bandwidth karena formatnya lebih ringan.
  ❌ Kurang bagus untuk data dengan metadata/atribut yang kompleks (dibanding XML).

Karena web modern butuh cepat, ringan, efisien, maka JSON lebih populer. Hampir semua REST API default-nya pakai JSON.

Fungsi dari method `is_valid()` pada form Django

Django punya sistem form untuk validasi input user.
Method `is_valid()`:
* Mengecek apakah semua field sudah diisi sesuai aturan (misalnya email valid, angka tidak negatif, field wajib tidak kosong).
* Jika valid → form bersih (cleaned data) bisa dipakai untuk disimpan ke database.
* Jika tidak valid → akan mengisi `form.errors` dengan pesan error.

Tanpa `is_valid()`, aplikasi bisa menyimpan data yang salah/berbahaya ke database (misalnya string di field umur).

Mengapa kita membutuhkan `csrf_token` pada form di Django?

* CSRF (Cross-Site Request Forgery) adalah serangan di mana penyerang membuat user tanpa sadar mengirim request berbahaya ke server yang sudah dipercaya.
* Django menambahkan `csrf_token` (random unik untuk tiap session) ke dalam setiap form.
* Server hanya menerima request yang punya token valid → mencegah request palsu.

Apa yang terjadi jika tidak ada `csrf_token`?

* Penyerang bisa bikin halaman palsu yang otomatis mengirim form ke server kamu (misalnya transfer uang, ubah password).
* Karena user sudah login, request itu bisa berhasil tanpa sepengetahuan user.

Dengan `csrf_token`, request palsu itu akan ditolak server.

![alt text](<Screenshot (9).png>) 
![alt text](<Screenshot (10).png>) 
![alt text](<Screenshot (11).png>) 
![alt text](<Screenshot (12).png>)


</details>