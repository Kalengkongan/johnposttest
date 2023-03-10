list1 = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
def linearsearch(list1,x):
    for l in range(len(list1)):
        if type(list1[l]) == list:
            hasil_x = linearsearch(list1[l],x)
            if hasil_x == -1:
                return -1
            else:
                print(f"{x} ditemukan pada indeks {l} kolom {hasil_x}")
                exit()
        elif list1[l] == x:
            return l
    return -1
print(list1)
x = input("Masukan nama yang ingin kamu cari : ")
hasil_y = linearsearch(list1,x)
if hasil_y == -1:
    print(f'{x} ditemukan pada indeks {hasil_y}')
else:
    print(f'{x} ditemukan pada indeks {hasil_y}')