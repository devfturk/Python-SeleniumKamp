faiz = 1.59
vade = "36"
krediAdi = "ihtiyac kredisi"

print(int(vade) + 12)

print(type(faiz))
print(type(vade))
print(type(krediAdi))

#vade1 = int(input("Lütfen istediğiniz vade sayısını giriniz : "))
vade1 = 10
print(type(vade1)) #default str

print(int(vade1) + 10)
vade1 = vade1 + 12

#string interpolation# 3 farklı kullanım 3. sü baya dinamik sevdim.
print("Seçtiğiniz vade sonucu ortaya çıkan vade : " + str(vade1))
print("Seçtiğiniz vade sonucu ortaya çıkan vade : {vadeSayisi}".format(vadeSayisi = vade1))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade : {vade1}")

isim = "Furkan"
metin = "Merhaba {name}".format(name = isim)
print(metin)


#f-string
metin1 = f"Hoşgeldiniz {1+1}"
print(metin1)


#Listeler
#döngüler
#fonksiyonlar

krediler = ["a","b","c","d"]
print(type(krediler))
print(krediler[0])

krediler.append("e")
print(krediler)
krediler.append("f")#ekledi
krediler.pop(krediler.index("d")) #çıkardı parametresiz son indexi atar
krediler.remove("a")# bulduğu ilk eşleşen değeri siler
print(krediler)
krediler.extend(["a","b"])# tek seferde birden fazla değer ekleme
print(krediler)

for i in range(10):
    print(i)
print("**************")
for i in range(5,10):
    print(i)
for i in range(0,51,10):
    print(i)

krediler = ["a","b","c","d"]
for kredi in krediler:
    print(kredi)
print("******************")
for i in range(len(krediler)):
    print(krediler[i])
i = 0
while i<10:
    print("x")
    i+=1
print("y")
while True:
    print("x")
    break
print("****döngü*******")
i = 0
krediler = ["a","b","c","d"]
while i < len(krediler):
    if krediler[i] == "c":
        break
    print(krediler[i])
    i+=1

# Fonksiyonlar

fiyat = 100
indirim = 20

#defination define
def calculate():
    print(100-20)

def calculateWithParams(a,b):
    print(a-b)
calculate()
calculateWithParams(fiyat,indirim)

def sayHello(name):
    print(f"Merhaba {name}")

sayHello("furkan")

def calculateAndReturn(price,discount):
    return price-discount
yepyeniFiyat = calculateAndReturn(fiyat,indirim)
print(yepyeniFiyat)
print("**************************")
fonk1 = calculateWithParams(100,50)
fonk2 = calculateAndReturn(200,100)
print(f"107.satır: {fonk1}")# return olmadığı için none döner
print(f"108.satır: {fonk2+ 500}")# return olduğu için yazılır işlem yapılabilir.
print("**************************")
