print("Nama          :Shalza Naya Dwi Fortuna")
print("Nim           :231031071")
print("prodi         :Sistem Informasi C")
print("Tanggal Lahir :14-10-2005")
#operator penugasan
print()
a =71
a +=1
print ('Nilai a +=1 akan menjadi',a)
a =71
a -=1
print ('Nilai a -=1 akan menjadi',a)
a =71
a *=2
print ('Nilai a *=2 akan menjadi',a)
a =71
a /=2
print ('Nilai a /=2 akan menjadi',a)
a =71
a %=2
print ('Nilai a %=2 akan menjadi',a)
a =71
a //=2
print ('Nilai a //=2 akan menjadi',a)
a =71
a **=2
print ('Nilai a **=2 akan menjadi',a )
#OR
b = True
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b |= False
print ('Nilai b|= False akan menjadi',b )
# AND
b = True
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b &= False
print ('Nilai b&= False akan menjadi',b )
# XOR
b = True
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )
b = False
print ('Nilai b =',b )
b ^= False
print ('Nilai b^= False akan menjadi',b )
# Shifting
c =0b0100
print ('Nilai c =',format (c , '04b') )
c >>=1
print ('Nilai c > >=1 akan menjadi ',format (c , '04b') )
c =0b0100
c <<=1
print ('Nilai c < <=1 akan menjadi ',format (c , '04b') )
#operator Komparasi/Perbandingan
a =1 # isi dengan ujung NIM
b =6 # Ubah dengan hasil jumlah ujung NIM dengan 5
print (' ================== Besar dari 6 ')
hasil = a>6
print (a ,'> 6 adalah ', hasil )
hasil = b>6
print (b ,'> 6 adalah ', hasil )

print (' ================== Kecil dari 6 ')
hasil = a<6
print (a ,'< 6 adalah ', hasil )
hasil = b<6
print (b ,'< 6 adalah ', hasil )

print (' ================== Besar atau sama dari 6 ')
hasil = a>=6
print (a ,' >= 6 adalah ', hasil )
hasil = b>=6
print (b ,' >= 6 adalah ', hasil )

print (' ================== Besar atau sama dari 6 ')
hasil = a<=6
print (a ,' <= 6 adalah ', hasil )
hasil = b<=6
print (b ,' <= 6 adalah ', hasil )

print (' ================== Sama dengan 6 ')
hasil = a==6
print (a ,'== 6 adalah ', hasil )
hasil = b==6
print (b ,'== 6 adalah ', hasil )

print (' ================== Tidak sama dengan 6 ')
hasil = a!=6
print (a ,'!= 6 adalah ', hasil )
hasil = b!=6
print (b ,'!= 6 adalah ', hasil )
#operator Logika
print (' ============= NOT ============= ')
a = True
c = not a
print ('a adalah ',a )
print (' ------c = not a- - - -- - - NOT ')
print ('c adalah ',c )

print (' ============= OR ============= ')
a = True
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = True
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = False
b = True
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

a = False
b = False
c = a or b
print (a ,'OR ',b ,'menjadi ',c )

print (' ============= AND ============= ')
a = True
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = True
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = False
b = True
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

a = False
b = False
c = a and b
print (a ,'AND ',b ,'menjadi ',c )

print (' ============= XOR ============= ')
a = True
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = True
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = False
b = True
c = a ^ b
print (a ,'^',b ,'menjadi ',c )

a = False
b = False
c = a ^ b
print (a ,'^',b ,'menjadi ',c )
# TUGAS
# Buat kode untuk masing masing operator berikut
print (' ============= NAND ============= ')
print (' ============= NOR ============== ')
print (' ============= NXOR ============= ')
#jawaban
print("jawaban")
print("=============NAND=============")
a=True
b=True
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

a=True
b=False
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

a=False
b=True
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

a=False
b=False
c=not (a and b)
print(a, "NOT AND",b,"menjadi",c)

print("=============NOR==============")
a=True
b=True
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

a=True
b=False
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

a=False
b=True
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

a=False
b=False
c=not (a or b)
print(a, "NOT OR",b,"menjadi",c)

print("=============NXOR=============")
a=True
b=True
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)

a=True
b=False
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)

a=False
b=True
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)

a=False
b=False
c=not (a ^ b)
print(a, "NOT ^",b,"menjadi",c)
print()
#operator Identitas
print (' ============== IS ')
a =5
b =5
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is b
print ('a is b = ', hasil )

a =5
b =6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is b
print ('a is b = ', hasil )

print (' ============== IS NOT ')
a =5
b =5
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )

a =5
b =6
print ('Nilai a =',a ,'Identitas =',hex (id( a ) ) )
print ('Nilai b =',b ,'Identitas =',hex (id( b ) ) )
hasil = a is not b
print ('a is not b = ', hasil )

#operator Membership
print (' ======================= IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

test = 'rud'
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

test = 'bac'
cek = test in nama_lengkap
print ( test +' terdapat di '+ nama_lengkap +' adalah '+ str( cek ) )

print (' ======================= NOT IN ')
nama_lengkap = ' Bacharuddin Jusuf Habibie '
test = 'a'
cek = test not in nama_lengkap
print ( test +' tidak terdapat di'+ nama_lengkap +'adalah '+str (cek
) )

test = 'rud '
cek = test not in nama_lengkap
print ( test +'tidak terdapat di'+ nama_lengkap +'adalah '+str (cek
) )

test = 'bac '
cek = test not in nama_lengkap
print ( test +'tidak terdapat di'+ nama_lengkap +'adalah '+str (cek
) )

# TUGAS
# Dengan cara yang sama buat operator in dan not in , ubah nama
#lengkap menjadi nama masing - masing dengan uji test
#test1 = 'AS' # pilih dua huruf berurut yang ada pada nama anda
#test2 = 'SA' # balik dua huruf tersebut
#test3 = 'a'
#test4 = 'i'
#test5 = 'u'
#test6 = 'e'
#test7 = 'o'

#jawaban
print("jawaban")
print("======================= IN")
nama_lengkap = "SHALZA NAYA DWI FORTUNA"
test1 = "AS"
cek = test1 in nama_lengkap
print(test1," terdapat di ",nama_lengkap," adalah ",str(cek))

test2 = "SA"
cek = test2 in nama_lengkap
print(test2," terdapat di ",nama_lengkap," adalah ",str(cek))

test3 = "a"
cek = test3 in nama_lengkap
print(test3," terdapat di ",nama_lengkap," adalah ",str(cek))

test4 = "i"
cek = test4 in nama_lengkap
print(test4," terdapat di ",nama_lengkap," adalah ",str(cek))

test5 = "u"
cek = test5 in nama_lengkap
print(test5," terdapat di ",nama_lengkap," adalah ",str(cek))

test6 = "e"
cek = test6 in nama_lengkap
print(test6," terdapat di ",nama_lengkap," adalah ",str(cek))

test7 = "o"
cek = test7 in nama_lengkap
print(test7," terdapat di ",nama_lengkap," adalah ",str(cek))

print()
print("======================= NOT IN")
nama_lengkap = "SHALZA NAYA DWI FORTUNA"
test1 = "SH"
cek = test1 not in nama_lengkap
print(test1," terdapat di ",nama_lengkap," adalah ",str(cek))

test2 = "HS"
cek = test2 not in nama_lengkap
print(test2," terdapat di ",nama_lengkap," adalah ",str(cek))

test3 = "a"
cek = test3 not in nama_lengkap
print(test3," terdapat di ",nama_lengkap," adalah ",str(cek))

test4 = "i"
cek = test4 not in nama_lengkap
print(test4," terdapat di ",nama_lengkap," adalah ",str(cek))

test5 = "u"
cek = test5 not in nama_lengkap
print(test5," terdapat di ",nama_lengkap," adalah ",str(cek))

test6 = "e"
cek = test6 not in nama_lengkap
print(test6," terdapat di ",nama_lengkap," adalah ",str(cek))

test7 = "o"
cek = test7 not in nama_lengkap
print(test7," terdapat di ",nama_lengkap," adalah ",str(cek))
print()
# Penggunaan pengecekan pada suatu data
data = ['Institut ',
' Teknologi ',
' Bacharuddin ',
' Jusuf ',
' Habibie ']
print ('data = ', data )
print (' ======================= IN ')
test1 = 'Habibie '
test2 = 'Parepare '
cek = test1 in data
print ('Apakah '+ test1 +' Terdapat di dalam data ? '+str ( cek ) )
cek = test2 in data
print ('Apakah '+ test2 +' Terdapat di dalam data ? '+str ( cek ) )

print (' ======================= NOT IN ')
test1 = 'institut '
test2 = 'Institut '
cek = test1 not in data
print ('Apakah '+ test1 + ' Tidak terdapat di dalam data ? '+ str ( cek
) )
cek = test2 not in data
print ('Apakah '+ test2 + ' Tidak terdapat di dalam data ? '+ str ( cek
) )
a =14 # ubah menjadi tanggal lahir anda
a +=60
b =10  # ubah menjadi bulan lahir anda
b += 90
print (' ============================= OR ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'10b') )
print ('Nilai ',b ,'dalam biner = ', format (b ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - - - -(|)')
hasil = a | b
print ('Nilai ',a ,'|',b ,'dalam biner = ', format ( hasil ,'10b') )

print (' ============================= AND ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'10b') )
print ('Nilai ',b ,'dalam biner = ', format (b ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - - - -(&)')
hasil = a & b
print ('Nilai ',a ,'&',b ,'dalam biner = ', format ( hasil ,'10b') )

print (' ============================= XOR ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'10b') )
print ('Nilai ',b ,'dalam biner = ', format (b ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - - - -(^)')
hasil = a ^ b
print ('Nilai ',a ,'^',b ,'dalam biner = ', format ( hasil ,'10b') )

print (' ============================= NOT ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - -(~a)')
hasil = ~a
print ('Nilai ~',a ,'dalam biner = ', format ( hasil ,'10b') )

print ('Nilai ',b ,'dalam biner = ', format (b ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - -(~b)')
hasil = ~b
print ('Nilai ~',b ,'dalam biner = ', format ( hasil ,'10b') )

print ('============================= > > ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)')
hasil = a >> 2
print ('Nilai ',a ,' > >2 dalam biner = ', format ( hasil ,'10b') )

print ('Nilai ',b ,'dalam biner = ', format (b ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -( > >2)')
hasil = b >> 2
print ('Nilai ',b ,' > >2 dalam biner = ', format ( hasil ,'10b') )

print ('============================= < < ')
print ('Nilai ',a ,'dalam biner = ', format (a ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -(<<2)')
hasil = a << 2
print ('Nilai ',a ,' < <2 dalam biner = ', format ( hasil ,'10b') )

print ('Nilai ',b ,'dalam biner = ', format (b ,'10b') )
print (' - - - - - - - - - - - - - - - - - - - - - - - - - -( < <2)')
hasil = b << 2
print ('Nilai ',b ,' < <2 dalam biner = ', format ( hasil ,'10b') )

# TUGAS
print (' ============================= NOT AND ')
print (' ============================= NOT OR ')
print (' ============================= NOT XOR ')
print (' ============================= NOT (>>2) ')
print (' ============================= NOT (<<2) ')
#jawaban
print("jawaban")
a=14 # ubah menjadi tanggal lahir 
a +=60
b=10  # ubah menjadi bulan lahir
b+= 90

print("=============================NOT AND")
print("Nilai",a,"dalam biner    =", format(a,"10b"))
print("Nilai",b,"dalam biner    =", format(b,"10b"))
print( "----------------------------(~&)")
hasil=~(a&b)
print("Nilai",a,"~&",b,"dalam biner =", format(hasil,"10b"))

print()
print("=============================NOT OR")
print("Nilai",a,"dalam biner    =", format(a,"10b"))
print("Nilai",b,"dalam biner    =", format(b,"10b"))
print( "----------------------------(~|)")
hasil=~(a|b)
print("Nilai",a,"~|",b,"dalam biner =", format(hasil,"10b"))

print()
print("=============================NOT XOR")
print("Nilai",a,"dalam biner    =", format(a,"10b"))
print("Nilai",b,"dalam biner    =", format(b,"10b"))
print( "----------------------------(~^)")
hasil=~(a^b)
print("Nilai",a,"~^",b,"dalam biner =", format(hasil,"10b"))

print()
print( "----------------------------NOT (>>2)")
hasil= ~(a >> 2)
print("Nilai",a,"~>>2 dalam biner =", format(hasil,"10b"))

print("Nilai",b,"dalam biner     =", format(b,"10b"))
print( "----------------------------NOT (>>2)")
hasil= ~(b >> 2)
print("Nilai",b,"~>>2 dalam biner =", format(hasil,"10b"))

print()
print( "----------------------------NOT (<<2)")
hasil= ~(a << 2)
print("Nilai",a,"~<<2 dalam biner =", format(hasil,"10b"))

print("Nilai",b,"dalam biner     =", format(b,"10b"))
print( "----------------------------NOT (<<2)")
hasil= ~(b << 2)
print("Nilai",b,"~<<2 dalam biner =", format(hasil,"10b"))
