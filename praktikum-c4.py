nim = ('2','3','1','0','3','1','0','7','1')

print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1])

print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua) {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'item indeks (pertama) {nim[len(nim)-1]}')

data = ['Shalza Naya Dwi Fortuna',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:2023', data[1])
print('status:aktif '+data[2])

print(f'{data[0]} status kuliah: {data[2]}')
print(f'data terbesar nilai adalah: {max(nilai)}')
print(f'data terkecil nilai adalah: {min(nilai)}')
print(f'rata-rata nilai adalah: {sum(nilai)/len(nilai)}')

print(data[0][0])
print(data[-1][0])
print(data[2][0])
print()
print(f'angkatan: {data[0][1]} {data[-1][1]}')
print(f'jumlah nilai {data[0][0]} adalah: {len(data[1])}')
print(f'data terbesar {data[0][0]} adalah: {max(data[1])}')
print(f'data terkecil {data[0][0]} adalah: {min(data[1])}')
print(f'rata-rata niali {data[0][0]} adalah: {sum(nilai)/len(nilai)}')









