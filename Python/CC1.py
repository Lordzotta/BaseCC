def checkCats(CatsTuti, CatsNining):
    # 1. Tuti mengetahui bahwa pemilik dari Kucing Pertama dan dua Kucing Terakhir sebenarnya memiliki anjing,
    # bukan kucing! Jadi, kita membuat salinan dari array CatsTuti dan hapus usia kucing dari array yang disalin
    correctedCatsTuti = CatsTuti.copy()
    if len(correctedCatsTuti) >= 1:
        correctedCatsTuti[0] = "Anjing"
    if len(correctedCatsTuti) >= 3:
        correctedCatsTuti[-3] = "Anjing"
    if len(correctedCatsTuti) >= 2:
        correctedCatsTuti[-2] = "Anjing"
    
    # 2. ini adalah sebuah array yang berisi data Tuti yang sudah dikoreksi dan data Nining
    combinedCats = correctedCatsTuti + CatsNining
    
    # 3. ini adalah Tampilan di konsol apakah itu Kucing Dewasa atau Kucing Kecil untuk setiap kucing yang tersisa
    for i, usia in enumerate(combinedCats):
        if usia == "Anjing":
            print(f'Kucing Nomor {i + 1} adalah Anjing!')
        else:
            usia = int(usia)
            if usia >= 3:
                print(f'Kucing Nomor {i + 1} adalah Kucing Dewasa, dan berusia {usia} tahun')
            else:
                print(f'Kucing Nomor {i + 1} masih anak-anak')

# penggunaan data uji 1:
CatsTuti = [3, 5, 2, 12, 7]
CatsNining = [4, 1, 15, 8, 3]

checkCats(CatsTuti, CatsNining)
