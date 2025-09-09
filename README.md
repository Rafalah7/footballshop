"# football_shop" 
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

Langkah C. Upload Django ke GitHub
1. Inisialisasi Git di folder football-news → git init.
2. Buat .gitignore → isi daftar file yang diabaikan (env, db.sqlite3, dll).
3. Hubungkan remote GitHub.
Push

git add .

git commit -m "Tutorial 0"

git branch -M master

git push origin master.

Langkah E. Deployment ke PWS

Login ke PWS → pbp.cs.ui.ac.id
, pakai SSO.

Create Project → beri nama footballnews.

Simpan credentials → jangan hilang.

Set environment variables → copy isi .env.prod ke Environs → Raw Editor.

Tambahkan URL PWS ke ALLOWED_HOSTS di settings.py.

Commit & push perubahan ke GitHub.

Hubungkan ke PWS → jalankan perintah Project Command dari dashboard.

Push ke PWS → git push pws master.

Cek status di dashboard → kalau Running, buka URL <username>-footballnews.pbp.cs.ui.ac.id.