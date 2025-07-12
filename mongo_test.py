from pymongo import MongoClient

# Koneksi ke MongoDB lokal
client = MongoClient("mongodb://localhost:27017")
db = client['ecommerce']

# Contoh data pengguna
user = {
    "_id": "user123",
    "nama": "Ami",
    "riwayat_pembelian": ["produk1", "produk2"],
    "produk_dilihat": ["produk3", "produk4"],
    "preferensi": ["skincare", "lipstik"]
}

# Contoh data produk
produk1 = {
    "_id": "produk1",
    "nama": "Lipstik Matte",
    "kategori": "makeup",
    "deskripsi": "Lipstik tahan lama dengan warna matte.",
    "harga": 75000,
    "tags": ["matte", "tahanlama", "populer"]
}

produk2 = {
    "_id": "produk2",
    "nama": "Serum Wajah",
    "kategori": "skincare",
    "deskripsi": "Serum wajah untuk kulit cerah dan sehat.",
    "harga": 95000,
    "tags": ["serum", "whitening"]
}

# Masukkan data ke MongoDB
db.users.replace_one({"_id": user["_id"]}, user, upsert=True)
db.produk.replace_one({"_id": produk1["_id"]}, produk1, upsert=True)
db.produk.replace_one({"_id": produk2["_id"]}, produk2, upsert=True)

# Query produk serupa berdasarkan tag
tags = ["matte"]
produk_serupa = db.produk.find({"tags": {"$in": tags}})
print("Produk dengan tag serupa:")
for p in produk_serupa:
    print(p["nama"])