# SHALOMMITA PRANATANTRI
# 71200640
# INFORMATIKA UKDW
# PERCABANGAN DAN PERULANGAN KOMPLEKS

# INPUT
# INPUT ANGKA DIWAJIBKAN GANJIL
angka=int(input("Masukkan Angka (Ganjil): "))

# PROSES
for i in range(angka):
    for j in range(angka):
        if i==0 or i==(angka-1) or i==(angka-1)//2:
            print("*",end=" ")
        elif j==0 or j==(angka-1) or j==(angka-1)//2:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

# OUTPUT