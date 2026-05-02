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

### Cara Menjalankan:
1. Install Django: `pip install django`
2. Masuk ke folder: `cd katalog_project`
3. Jalankan server: `python manage.py runserver`
4. Buka browser: `http://127.0.0.1:8000`
