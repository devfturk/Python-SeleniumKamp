#Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.
ogrenciList = ["a","b","c","d","e"]
#Aldığı isim soy isim ile listeye öğrenci ekleyen
def ogrenciEkle(isimSoyisim):
    print(ogrenciList)
    ogrenciList.append(isimSoyisim)
    print(ogrenciList)
#Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
def ogrenciSil(isimSoyisim):
    print(ogrenciList)
    ogrenciList.remove(isimSoyisim)
    print(ogrenciList)
#Listeye birden fazla öğrenci eklemeyi mümkün kılan
def ogrenciListesiEkle(isimSoyisimList):
    print(ogrenciList)
    ogrenciList.extend(isimSoyisimList)
    print(ogrenciList)
#Listedeki tüm öğrencileri tek tek ekrana yazdıran
def ogrenciYazdir():
    for ogrenci in ogrenciList:
        print(ogrenci)
#Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
def ogrenciYazdirIndex():
    print(ogrenciList)
    for i in range(len(ogrenciList)):
        print(f"Index: {i} İsim: {ogrenciList[i]}")
    print(ogrenciList)
#Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
def ogrenciListSil(ogrenciSilinecek): # a b c
    i = 0
    print(ogrenciList)
    while(i < len(ogrenciSilinecek) ):#3
        ogrenciList.remove(ogrenciSilinecek[i])
        i+=1
    print("İşlem tamam.")
    print(ogrenciList)
    
ogrenciYazdirIndex()

ogrenciYazdir()

ogrenciEkle("Furkan Türk")

ogrenciListesiEkle(["f","x","y"])

ogrenciSil("a")

ogrenciListSil(["f","x","y"])