#1
total = 0  

for angka in range(1, 11):
    total += angka 
    print(angka)

print("Total jumlah angka:", total)  
#2
total = 0

for angka in range(2, 21, 2):
    total += angka
    print(angka)

print("Total jumlah angka genap:", total)  
#3
i = 1
total = 0  

while i <= 50:
    total += i 
    print(i)
    i += 1

print("Total jumlah angka:", total)  
#4
i = 1
total = 0  

while i <= 15:
    total += i 
    print(i)
    i += 2

print("Total jumlah angka ganjil:", total) 
#5
kumpulan_makanan = ["nasi goreng", 'mie goreng', 'nasi bakar', 'mie bakar']

for makanan in kumpulan_makanan:
  print(makanan)
