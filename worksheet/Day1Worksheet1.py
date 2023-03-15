#Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
# Sayısal Veri Tipleri:
#     Integer (Tam sayılar): Bu veri tipi, pozitif ve negatif tamsayıları ifade eder. Örneğin: 2, 5, -10, 0 gibi.
#     Float (Ondalıklı Sayılar): Bu veri tipi, ondalık sayıları ifade eder. Örneğin: 3.14, 2.5, 1.0 gibi.
#     Complex (Karmaşık Sayılar): Bu veri tipi, karmaşık sayıları ifade eder. Örneğin: 3+4j, -1-2j gibi.

# Metinsel Veri Tipleri:
#     String (Karakter Dizisi): Bu veri tipi, metinleri ifade eder. 
#     Örneğin: "Merhaba Dünya", "Python Programlama Dili", "123" gibi.

# Mantıksal Veri Tipleri:
#     Boolean (Mantıksal Değerler): Bu veri tipi,
#     doğru ve yanlış değerlerini ifade eder. True ve False değerlerini alabilir.

# İteratif Veri Tipleri:
#     List (Liste): Bu veri tipi, birden fazla veriyi saklamak için kullanılır. 
#     Örneğin: [1, 2, 3, 4], ["Python", "Java", "C#"] gibi.

#     Tuple (Demet): Bu veri tipi, listeye benzer ancak değiştirilemezdir. 
#     Örneğin: (1, 2, 3), ("Ankara", "İstanbul", "İzmir") gibi.

#     Set (Küme): Bu veri tipi, tekrarlamayan elemanları saklamak için kullanılır. 
#     Örneğin: {1, 2, 3}, {"Python", "Java", "C#"} gibi.  

#     Dictionary (Sözlük): Bu veri tipi, anahtar-değer çiftleri şeklinde veri saklamak için kullanılır. 
#     Örneğin: {"ad": "Ali", "yaş": 25}, {"isim": "Ahmet", "meslek": "mühendis"} gibi.


# İlerleme bari sayisal veri tipi olan "İnteger", ve genel olarak sitenin cogunda string veri tipi kullanilmıştır.



# kodlama io sitesin de sart bloklarina örnek olarak giris yapmak olabilir
kullaniciAdi="turk"
sifre="12345"

inputKullaniciAdi=input("Lütfen Kullanici Adinizi giriniz: ")
inputSifre=input("Lütfen sifrenizi giriniz: ")

if(kullaniciAdi==inputKullaniciAdi and sifre==inputSifre):
    print("Giris Basarili!")
    #hide btn_giris
else:
    print("Hatali Giris")

#döngülere örnek olarak da gösterilecek alan eğitimler  ve eğitmenler olabilir. Bir listeden döngü ile çekildiğini düşünüyorum.