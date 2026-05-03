# Isla'Store Website Katalog Produk Django

## Informasi Mahasiswa

- **Nama:** Dian Islami
- **NIM:** 2308107010048

## Penjelasan Program

Website katalog produk sederhana menggunakan framework Django (Python). Menampilkan daftar produk beserta detail lengkapnya tanpa menggunakan database, data disimpan langsung di `views.py`.

### Halaman yang tersedia:
| URL | Keterangan |
|-----|-----------|
| `/` | Beranda dengan hero section dan fitur unggulan |
| `/produk/` | Daftar semua produk (11 produk) |
| `/produk/<id>/` | Detail satu produk berdasarkan ID |
| `/kontak/` | Informasi kontak dan jam operasional |

## Struktur File dan Route

### Direktori Utama
```
tugas_katalog/
├── katalog/                      # Main application
│   ├── models.py                # Model database (tidak digunakan)
│   ├── views.py                 # View logic dan data produk
│   ├── urls.py                  # Route aplikasi katalog
│   ├── admin.py                 # Admin panel
│   └── templates/
│       └── katalog/
│           ├── base.html        # Template dasar (header, nav, footer)
│           ├── index.html       # Halaman beranda
│           ├── produk.html      # Daftar produk
│           ├── detail.html      # Detail produk
│           └── kontak.html      # Halaman kontak
├── tugas_katalog/               # Project settings
│   ├── settings.py              # Konfigurasi Django
│   ├── urls.py                  # URL routing utama
│   └── wsgi.py                  # WSGI config
├── manage.py                    # Django CLI
└── db.sqlite3                   # Database
```

### Routes Detail
| Route | File | View Function | Template |
|-------|------|---------------|----------|
| `/` | `urls.py` → `views.py` | `index` | `index.html` |
| `/produk/` | `urls.py` → `views.py` | `produk` | `produk.html` |
| `/produk/<id>/` | `urls.py` → `views.py` | `detail` | `detail.html` |
| `/kontak/` | `urls.py` → `views.py` | `kontak` | `kontak.html` |

### File Penting

**katalog/views.py**
- Menyimpan data produk (11 produk dummy)
- Fungsi views: `index()`, `produk()`, `detail()`, `kontak()`
- Mengirim data ke template melalui context

**katalog/urls.py**
- Path routing: `/produk/<id>/` untuk detail produk
- Menghubungkan URL dengan view function

**templates/katalog/base.html**
- Template parent untuk semua halaman
- Berisi navbar, footer, dan styling dasar

### Cara Menjalankan:
1. Install Django: `pip install django`
2. Masuk ke folder: `cd tugas_katalog`
3. Jalankan server: `python manage.py runserver`
4. Buka browser: `http://127.0.0.1:8000`
