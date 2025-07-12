
# Judul : PERANCANGAN DAN IMPLEMENTASI SISTEM REKOMENDASI PRODUK KECANTIKAN BERBASIS NOSQL PADA PLATFORM E-COMMERCE MENGGUNAKAN MONGODB DAN REDIS
# Deskripsi
Proyek ini merupakan implementasi sistem rekomendasi produk kecantikan pada platform e-commerce menggunakan **MongoDB** dan **Redis**. Sistem ini menampilkan rekomendasi berdasarkan interaksi pengguna, tag produk, dan produk yang sering dibeli bersamaan.
# Teknologi yang Digunakan
* Python 3
* MongoDB (lokal, dengan MongoDB Compass)
* Redis (Redis Cloud)
* RedisInsight (opsional, untuk GUI Redis)
* Library Python: `pymongo`, `redis`
# Struktur Folder
```
TugasKlp_NoSQL_3/
├── mongo_test.py            # Simpan data dan jalankan 5 query utama ke MongoDB
├── redis_query.py           # Simpan dan ambil data rekomendasi dari Redis
├── src/
│   └── rekomendasi.py       # Analisis produk yang sering dibeli bersama
├── requirements.txt         # Library Python yang dibutuhkan
├── README.md                # Dokumentasi proyek
└── screenshots/             # Hasil output dan dokumentasi visual
```
# Setup Lingkungan
## 1. Install Python dan pip
Unduh Python dari: [https://www.python.org/downloads/](https://www.python.org/downloads/)
Pastikan pip sudah otomatis terinstall.
## 2. Install Library Python
```bash
pip install -r requirements.txt
```
## 3. Install MongoDB
* Unduh MongoDB dan MongoDB Compass:
  [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
* Jalankan MongoDB di background atau gunakan Compass GUI.
## 4. Buat Redis Cloud Gratis
* Daftar di Redis Cloud: [https://redis.com/try-free/](https://redis.com/try-free/)
* Setelah buat database, salin **host**, **port**, dan **password**
* Tambahkan di `redis_query.py`:

```python
r = redis.Redis(
    host='your-host',
    port=your-port,
    password='your-password',
    decode_responses=True
)
```
## 5. (Opsional) Install RedisInsight
Untuk melihat isi database Redis dengan antarmuka GUI:
[https://redis.com/redis-enterprise/redis-insight/](https://redis.com/redis-enterprise/redis-insight/)

# Cara Menjalankan Kode
## 1. Pastikan MongoDB dan Redis aktif

* MongoDB: berjalan di `localhost:27017`
* Redis: gunakan koneksi Redis Cloud

## 2. Jalankan script dari terminal:

```bash
python mongo_test.py         # Simpan data dan jalankan query MongoDB
python redis_query.py        # Simpan dan ambil cache dari Redis
python src/rekomendasi.py    # Analisis produk yang sering dibeli bersama
```

# Fitur Sistem

* Menyimpan data pengguna, produk, dan interaksi
* Menampilkan produk berdasarkan kategori dan tag
* Menampilkan riwayat pembelian dan yang sering dilihat pengguna
* Menampilkan produk populer (Redis Sorted Set)
* Menampilkan rekomendasi per user (Redis List)
* Menampilkan produk yang sering dibeli bersamaan (kombinasi)

# Contoh Output

```
Produk dengan tag serupa:
Lipstik Matte

Produk populer:
('produk1', 25.0)
('produk2', 15.0)

Rekomendasi untuk user123:
['produk2', 'produk1']

Produk yang sering dibeli bersamaan:
produk1 & produk2 → dibeli bersama oleh 1 user
```

# Anggota Kelompok

* Gusti Ayu Km. Anggriani
* Komang Rosmiani
* Gracia Anasthasia
* Riski Amanda
* Azwina Azzahra
* Asma Abidin
* Muhammad Asrul
* Wahyu Ramadan

# Referensi

* MongoDB Documentation: [https://www.mongodb.com/docs/manual](https://www.mongodb.com/docs/manual)
* Redis Documentation: [https://redis.io/docs](https://redis.io/docs)
* Sadalage, P., & Fowler, M. (2012). *NoSQL Distilled*. Addison-Wesley
* Chodorow, K. (2013). *MongoDB: The Definitive Guide*. O'Reilly Media

