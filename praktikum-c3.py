
nama="Shalza Naya Dwi Fortuna"
nim="231031071"
meet="Praktikum 3(string)"
prodi="Sistem Informasi C"
email="shalza.df3@gmail.com"
ttl="Banjarmasin, 14-Oktober-2005"
alamat="Jln Chalik"
asal="Parepare"
hobi="Menyanyi"
tinggi="160"
print("-"*110)
print(nama.upper().center(100))

str1= "231031071"
a= str1.center(100)
print(a)
print()
print()
str1= "Praktikum 3(String)"
a= str1.rjust(110)
print(a)
str1= "Sistem Informasi(c)"
a= str1.rjust(110)
print(a)
str1= "shalza.df3@gmail.com"
a= str1.rjust(110)
print(a)
print("-"*110)
print()
print()


print(f'''\tHalo, nama saya {nama} dengan NIM {nim} dari prodi {prodi}, ini adalah file {meet}. Terima Kasih''')
print(f''' Biodata Saya,
Nama\t: {nama}
Nim\t: {nim}
Prodi\t:{prodi}
TTL\t: {ttl}
Alamat\t:{alamat}
Asal\t:{asal}
Hobi\t:{hobi}
Tinggi\t:{tinggi} cm
''')
print()
#jawaban
stat1 = 'duFort Frankel Sir Issac'
# Issac duFort Frankel Sir
print(stat1[19:],stat1[0:19])

stat2 = 'duFort Frankel Sir Issac'
# d F S Issac
print(stat2[0],stat2[7],stat2[15],stat2[19:])

stat3 = 'duFort Frankel Sir Issac'
# duFort F S I
print(stat3[0:7],stat3[7],stat3[15],stat3[19])

stat4 = 'duFort Frankel Sir Issac'
# I duFort Frankel Sir
print(stat4[19],stat4[0:18])

stat5 = 'duFort Frankel Sir Issac'
# Issac d F S
print(stat5[19:],stat5[0],stat5[7],stat5[15])

stat6 = 'duFort Frankel Sir Issac'.upper()
# ISSAC D F S
print(stat6[19:],stat6[0],stat6[7],stat6[15])

stat7 = '#duFort Frankel Sir Issac$'
# duFort Frankel Sir Issac
stat7 = stat7.strip("#$")
print(stat7)

stat8 = '#duFort-Frankel-Sir-Issac$'
# duFort Frankel Sir Issac
stat8 = stat8.strip("#$").replace("-"," ")
print(stat8)

stat9 = '#duFort@ ^Frankel* (Sir( (Issac$'
# duFort Frankel Sir Issac
import re
stat9 = re.findall(r'\w+', stat9)
hasil = ' '.join(stat9)
print(hasil)

stat10 = '#duFort@-^Frankel*-(Sir(-(Issac$'
# DUFORT FRANKEL SIR ISSAC
import re
stat10 = re.findall(r'\w+', stat10)
hasil = ' '.join(stat10.upper() for stat10 in stat10)
print(hasil)


print()
