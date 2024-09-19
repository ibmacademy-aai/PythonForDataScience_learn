import requests

# Endpoint API untuk permintaan HTTP GET
url = 'https://jsonplaceholder.typicode.com/posts/4'

# Mengirimkan request GET ke URL
response = requests.get(url)

# Menampilkan status kode respons
print("Status Kode:", response.status_code)

# Mengambil data respons dalam format JSON
data = response.json()

# Menampilkan data hasil respons
print("\nData JSON yang diterima: \n")
print("Judul:", data['title'])
print("Isi:", data['body'])
