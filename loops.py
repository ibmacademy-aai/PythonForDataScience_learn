print("Saya berjanji untuk tidak mengulangi perbuatan tersebut \n" * 10) # Bukan loops, tapi string multiplication

for i in range(5):
    print(i)

for j in range(10):
    print("Saya berjanji untuk tidak mengulangi perbuatan tersebut \n")

# Menambahkan perkataan yang berbeda pada iterasi print ke 5
for j in range(10):
    if j == 5:
        print("Ini peringatan ke-5!")
    print("Saya berjanji untuk tidak mengulangi perbuatan tersebut \n")



# Menggunakan while loop untuk mencetak angka 0 hingga 4
count = 0
while count < 5:
    print(count)
    count += 1
