letternums = {'A':1, 'J':1, 'S':1,'Ş':1, 'B':2, 'K':2, 'T':2, 'C':3, 'Ç':3, 'L':3, 'U':3, 'Ü':3, 'D':4, 'M':4, 'V':4, 'E':5,
              'N':5, 'W':5,'Ö':5, 'F':6, 'O':6,'Ö':6, 'X':6, 'G':7, 'Ğ':7, 'P':7, 'Y':7, 'H':8, 'Q':8, 'Z':8, 'I':9, 'İ':9, 'R':9}

def reduce(x, y):
    strx = str(x)
    total = x
    total_ex = x
    while len(strx) > 1:
        if y == 1 and total_ex == 11:
            break
        total = sum(int(i) for i in strx)
        strx = str(total)
        total_ex = total 
    return int(strx), total_ex



def genelisimenerji(name, surname):
    name_total = 0
    surname_total = 0
    name = name.upper()
    surname = surname.upper()
    for letter in name:
        if letter in letternums:
            name_total += letternums[letter]
    for letter in surname:
        if letter in letternums:
            surname_total += letternums[letter]
    name_total = reduce(name_total, 0)[0]
    surname_total = reduce(surname_total, 0)[0]
    generaltotal = reduce(name_total + surname_total, 1)[0]
    return name_total, surname_total, generaltotal

def ruhgudusu(isim, soyisim):
    isimsesli, isimsessiz = seslisessiz(isim)
    soyisimsesli, soyisimsessiz = seslisessiz(soyisim)
    ruh_gudusu = 0
    for i in isimsesli:
        if i == ' ':
            continue
        ruh_gudusu += letternums.get(i, 0)
    for i in soyisimsesli:
        if i == ' ':
            continue
        ruh_gudusu += letternums.get(i, 0)
    ruh_gudusu = reduce(ruh_gudusu, 1)[0]
    return ruh_gudusu

def gizlibenlik(isim, soyisim):
    isimsesli, isimsessiz = seslisessiz(isim)
    soyisimsesli, soyisimsessiz = seslisessiz(soyisim)
    gizlibenlik = 0
    for i in isimsessiz:
        if i == ' ':
            continue
        gizlibenlik += letternums.get(i, 0)
    for i in soyisimsessiz:
        if i == ' ':
            continue
        gizlibenlik += letternums.get(i, 0)
    gizlibenlik = reduce(gizlibenlik, 1)[0]
    return gizlibenlik

def ifadebicimi(isim, soyisim):
    a = ruhgudusu(isim, soyisim)
    b = gizlibenlik(isim, soyisim)
    ifadebicimi = reduce(a + b, 0)[0]
    return ifadebicimi

def erkenders(gun, ay, yil):
    a = int(gun) - int(ay)
    b = int(ay) - int(yil)
    
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    
    a = reduce(a, 0)[0]
    b = reduce(b, 0)[0]
    
    sonuc = a - b
    if sonuc < 0:
        sonuc *= -1 
    sonuc = reduce(sonuc, 0)[0]

    return sonuc


def seslisessiz(word):
    seslidata = ['A', 'E', 'I', 'İ', 'O', 'Ö', 'U', 'Ü']
    seslilog = []
    sessizlog = []
    word = word.upper()
    for i in word:
        if i in seslidata:
            seslilog.append(i)
        elif i.isalpha():  # Exclude non-alphabetic characters
            sessizlog.append(i)
    return seslilog, sessizlog

def karmikborc(gun, ay, yil):
    ay_red = reduce(int(ay), 0)[0]
    gun_red = reduce(int(gun), 0)[0]
    yil_red = reduce(int(yil), 0)[0]
    karmiktoplam = ay_red + gun_red + yil_red
    if karmiktoplam in [13, 14, 16, 19]:
        print("\nKarmik borç mevcut:", karmiktoplam, "/", reduce(karmiktoplam, 0)[0])
    else:
        print("\nKarmik borç mevcut değil.")
        print(f"Hayat yolu: ", karmiktoplam,"/", reduce(karmiktoplam, 0)[0])
    return karmiktoplam

def varlikkodu(gun, ay, yil):
    # Extract individual digits from the inputs
    digits = [int(d) for d in str(gun) + str(ay) + str(yil)]
    
    # Calculate the full sum of all digits
    varlikkodu = sum(digits)
    
    # Use the existing reduce function to get the reduced value
    varlikkodu_reduced = reduce(varlikkodu, 1)[0]
    
    return varlikkodu, varlikkodu_reduced



def isimcakra(isim, soyisim):
    cakralar = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    isim = isim.upper()
    soyisim = soyisim.upper()
    
    #Aktivasyon hesabı
    for i in isim:
        if i == ' ':
            continue
        chakra = letternums[i]
        cakralar[chakra - 1] += 1
    for i in soyisim:
        if i == ' ':
            continue
        chakra = letternums[i]
        cakralar[chakra - 1] += 1
    return cakralar
    
def zirveyillar(gun, ay, yil):
    gun_red = reduce(int(gun), 0)[0]
    ay_red = reduce(int(ay), 0)[0]
    yil_red = reduce(int(yil), 0)[0]
    
    varlikkodu1 = varlikkodu(gun, ay, yil)[1]
    yas_1 = 36 - varlikkodu1
    yas_2 = yas_1 + 9
    yas_3 = yas_2 + 9
    yas_4 = yas_3 + 9
    
    birincidonem = reduce(gun_red + ay_red, 1)[0]
    ikincidonem = reduce(gun_red + yil_red, 1)[0]
    ucuncudonem = reduce(birincidonem + ikincidonem, 1)[0]
    dorduncudonem = reduce(ay_red + yil_red,1 )[0]
    
    toplam = [
        f"Yaş: {yas_1}, Enerji: {birincidonem}",
        f"Yaş: {yas_2}, Enerji: {ikincidonem}",
        f"Yaş: {yas_3}, Enerji: {ucuncudonem}",
        f"Yaş: {yas_4}, Enerji: {dorduncudonem}"
    ]
    return toplam

def pinkodu(gun, ay, yil):
    pin = []
    
    pin.append(reduce(gun, 0)[0])
    pin.append(reduce(ay, 0)[0])
    pin.append(reduce(yil, 0)[0]) #3
    pin.append(reduce(pin[0] + pin[1] + pin[2], 0)[0])  #4
    pin.append(reduce(pin[0] + pin[3], 0)[0])  #5
    pin.append(reduce(pin[0] + pin[1], 0)[0]) #6
    pin.append(reduce(pin[1] + pin[2], 0)[0])  #7
    pin.append(reduce(pin[5] + pin[6], 0)[0])  #8
    pin.append(reduce(sum(pin), 0)[0]) #9

    return pin

def pindencakra(pin):
    cakralar = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in pin:
        cakralar[i-1] += 1
    return cakralar

def genelcakra(cakra, pindencakra):
    cakralar = []

    for i in range(len(cakra)):
        cakralar.append([pindencakra[i], f" {i+1}.ÇAKRA ", cakra[i]])

    for i in range(len(cakra)):
            if cakralar[i][0] != 0 and cakralar [i][2] == 0:
                cakralar[i][2] = 'BORÇ'

    return cakralar


print("\nLütfen isim, soyisim (ikisi de ayrı ayrı) ve gün, ay, yıl olacak şekilde (yine ayrı ayrı) doğum tarihi giriniz: \n")
isim = input("İsim: ")
soyisim = input("Soyisim: ")
gun = input("Gün: ")
ay = input("Ay: ")
yil = input("Yıl: ")

karmikborc(gun, ay, yil)
isimenerji = genelisimenerji(isim, soyisim)
ruh = ruhgudusu(isim, soyisim)
gizli = gizlibenlik(isim, soyisim)
ifade = ifadebicimi(isim, soyisim)
erkendrs = erkenders(gun, ay, yil)
varlikkodu1 = varlikkodu(gun, ay, yil)
zirveyaslar = zirveyillar(gun, ay, yil)
pinkod = pinkodu(gun, ay, yil)
cakralar = isimcakra(isim, soyisim)
cakralarpin = pindencakra(pinkod)
cakralargenel = genelcakra(cakralar, cakralarpin)
misyon = reduce(pinkod[5] + pinkod[6], 1)[0], reduce(pinkod[5] + pinkod[6], 0)[1]
vizyon = reduce(pinkod[1] + pinkod[5] + pinkod[1] + pinkod[6], 1)[0], reduce(pinkod[1] + pinkod[5] + pinkod[1] + pinkod[6], 0)[0]


print(f"İsim Enerjisi: {isimenerji[0]}, Soyisim Enerjisi: {isimenerji[1]}, Genel İsim Enerjisi: {isimenerji[2]}")
print(f"Ruhgüdüsü: {ruh}")
print(f"Gizli Benlik: {gizli}")
print(f"İfade Biçimi: {ifade}")
print(f"Olgunluk Sayısı: {reduce(ifade + varlikkodu1[1], 0)[0]}")
print(f"Erken Ders: {erkendrs}")
print("Varlık kodu:", varlikkodu1[0], "/", varlikkodu1[1], "\n")
print(f"Zirve Yaşlar ve Enerjiler: {zirveyaslar}", "\n")

if misyon[0] == 11:
    print(f"Misyon: {misyon[0]}/{misyon[1]}")
else:
    print(f"Misyon: {misyon[0]}")

if vizyon[0] == 11:
    print(f"Vizyon: {vizyon[0]}/{vizyon[1]}\n")
else:
    print(f"Vizyon: {vizyon[0]}\n")

for i in range (8, -1, -1):
    print(cakralargenel[i][0], cakralargenel[i][1], cakralargenel[i][2])

print("\n")
print(" ".join(map(str, pinkod[:5])))
print(" ".join(map(str, pinkod[5:7])))
print(pinkod[7])
print(f"\nPin kod toplam: {pinkod[8]}")


"""
file_name = f"{isim}{soyisim}_results.txt"
with open(file_name, "w", encoding="utf-8") as file:
    file.write(f"İsim: {isim}\n")
    file.write(f"Soyisim: {soyisim}\n")
    file.write(f"Doğum Tarihi: {gun}/{ay}/{yil}\n\n")

    file.write(f"İsim Enerjisi: {isimenerji[0]}, Soyisim Enerjisi: {isimenerji[1]}, Genel İsim Enerjisi: {isimenerji[2]}\n")
    file.write(f"Ruhgüdüsü: {ruh}\n")
    file.write(f"Gizli Benlik: {gizli}\n")
    file.write(f"İfade Biçimi: {ifade}\n")
    file.write(f"Olgunluk Sayısı: {reduce(ifade + varlikkodu1[1], 0)[0]}\n")
    file.write(f"Erken Ders: {erkendrs}\n")
    file.write(f"Varlık Kodu: {varlikkodu1[0]} / {varlikkodu1[1]}\n\n")
    
    file.write("Zirve Yaşlar ve Enerjiler:\n")
    for zirve in zirveyaslar:
        file.write(f"{zirve}\n")
    file.write("\n")
    
    if misyon[0] == 11:
        file.write(f"Misyon: {misyon[0]}/{misyon[1]}\n")
    else:
        file.write(f"Misyon: {misyon[0]}\n")
    
    if vizyon[0] == 11:
        file.write(f"Vizyon: {vizyon[0]}/{vizyon[1]}\n")
    else:
        file.write(f"Vizyon: {vizyon[0]}\n")
    file.write("\n")
    
    file.write("Çakra Durumları:\n")
    for i in range(8, -1, -1):
        file.write(f"{cakralargenel[i][0]} {cakralargenel[i][1]} {cakralargenel[i][2]}\n")
    file.write("\n")
    
    file.write("Pin Kod:\n")
    file.write(" ".join(map(str, pinkod[:5])) + "\n")
    file.write(" ".join(map(str, pinkod[5:7])) + "\n")
    file.write(str(pinkod[7]) + "\n")
    file.write(f"\nPin kod toplam: {pinkod[8]}\n")

# Confirmation message for the user
print(f"Sonuçlar '{file_name}' adlı dosyaya kaydedildi.")

"""