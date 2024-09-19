# Pembuatan matriks sederhana
import numpy as np

# Membuat 2D array (matriks) berukuran 3x3
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

# Mengakses elemen di baris ke-2, kolom ke-3 (ingat indeks dimulai dari 0)
elemen = matrix[2, 2] 

# Melakukan penjumlahan pada semua elemen dalam array
jumlah_total = np.sum(matrix) 

# Mengambil kolom pertama dari matrix
kolom_pertama = matrix[:, 0]  

print("Matrix:\n", matrix)
print("Elemen di baris ke-2, kolom ke-3:", elemen)
print("Jumlah total elemen dalam matrix:", jumlah_total)
print("Kolom pertama:", kolom_pertama)



# Menghitung nilai rata - rata
import numpy as np

# Membuat array 2D dengan ukuran 2x4
array_2d = np.array([[5, 10, 15, 20], 
                     [25, 30, 35, 40]])

# Menampilkan array
print("Array 2D:")
print(array_2d)

# Menghitung rata-rata dari seluruh elemen di dalam array
average = np.mean(array_2d)
print("Rata-rata elemen:", average)

# Menjumlahkan seluruh elemen di tiap kolom
sum_per_column = np.sum(array_2d, axis=0)
print("Jumlah tiap kolom:", sum_per_column)



# Perkalian matrix 2x2
import numpy as np

# Membuat dua matriks 2x2
matrix_a = np.array([[1, 2], 
                     [3, 4]])

matrix_b = np.array([[5, 6], 
                     [7, 8]])

# Melakukan perkalian matriks (dot product)
result = np.dot(matrix_a, matrix_b)

# Menampilkan hasil
print("Hasil perkalian matriks:")
print(result)
