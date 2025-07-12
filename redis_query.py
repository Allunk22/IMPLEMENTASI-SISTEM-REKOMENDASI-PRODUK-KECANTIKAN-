import redis

# Koneksi ke Redis Cloud
r = redis.Redis(
    host='redis-10719.c265.us-east-1-2.ec2.redns.redis-cloud.com',  
    port=10719,                                     
    password='tugas3',                        
    decode_responses=True
)

r.zadd('produk_populer', {'produk1': 25, 'produk2': 15})

print("Top produk populer:")
for item in r.zrevrange('produk_populer', 0, 2, withscores=True):
    print(item)

r.lpush('rekomendasi:user123', 'produk2', 'produk1')

print("Rekomendasi untuk user123:")
print(r.lrange('rekomendasi:user123', 0, -1))
