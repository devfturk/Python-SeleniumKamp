#video1
krediler = ["Hizli kredi","yasli kredi","a","b","x"]
print(krediler)
print(krediler[3])
print(krediler[0])
print(krediler[1])
print(krediler[2])#index değeri
print(len(krediler))#eleman sayısı

krediler[0] = "Cabuk kredi"
print(krediler)
#print(krediler[10]) index olmadığı için hata fırlatır.

#video2

#alias
for kredi in krediler:
    print(kredi)

for i in range(len(krediler)):
    print(krediler[i])
for i in range(0,10,2):#0 dan 10 a kadar 2 arttır(10 dahil değil)
    print(i)
