# Flask SQLite User Management

Aplikasi web sederhana berbasis Flask yang menggunakan SQLite sebagai database. Aplikasi ini memiliki fitur registrasi pengguna, menampilkan daftar pengguna, dan menggunakan Bootstrap untuk tampilan yang lebih menarik.

## 📂 Struktur Folder

```
flask/
│── templates/             # Folder untuk halaman HTML
│   │── index.html         # Halaman utama
│   │── register.html      # Halaman pendaftaran
│   │── users.html         # Halaman daftar pengguna
│── app.py                 # File utama aplikasi Flask
│── config.py              # Konfigurasi aplikasi
│── models.py              # Model database (ORM SQLAlchemy)
│── database.db            # File database SQLite (terbentuk setelah migrasi)
│── README.md              # Dokumentasi proyek ini
```

## ⚙️ Instalasi

### 1. Clone Repository

```sh
git clone https://github.com/edisuherlan/website-python-flask.git 
cd repo-name
```

### 2. Buat Virtual Environment & Aktifkan

```sh
python -m venv env
source env/bin/activate   # Untuk Mac/Linux
env\Scripts\activate      # Untuk Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

```sh
flask run
```

Akses aplikasi di **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

## 🛠 Konfigurasi

Buka **config.py** untuk mengatur konfigurasi aplikasi:

```python
import os

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 🗃️ Database Migration (Opsional)

Jika ingin menggunakan Flask-Migrate:

```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## 🖥️ Fitur Aplikasi

1. **Registrasi Pengguna** → Halaman untuk mendaftarkan user baru.
2. **Menampilkan Data Pengguna** → Menampilkan daftar user yang telah terdaftar.
3. **Tampilan Bootstrap** → UI lebih menarik dan responsif.

## 📄 Lisensi

Proyek ini bersifat open-source dan bebas digunakan untuk keperluan pribadi maupun edukasi. 😊minta link unduhannya donk

## 📄 Penjelesan Aplikasi ada diwebsite : 

[https://audhighasu.com/2025/03/16/cara-mudah-install-flask-di-laragon-untuk-pemula/](https://audhighasu.com/2025/03/16/seri-2-web-dengan-flask-aplikasi-flask-dengan-sqlite-dan-bootstrap/)




