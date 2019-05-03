# membuat function pangkat
def pangkat(a,b):
    kali = int(a)
    i = 1
    while i < int(b):
        kali = kali * a
        i += 1
    return kali
    
print(pangkat(2,2))
print(pangkat(3,3))
print(pangkat(10,5))

# just in case menggunakan input untuk parameter a & b
# print(pangkat(input('Masukkan angka pertama: '), input('Masukkan angka kedua: ')))