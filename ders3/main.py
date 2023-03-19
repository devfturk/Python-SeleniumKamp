

from ders3.human import Human


human1 = Human("Ahmet")
human1.talk("Merhaba")
human1.name = "Enes"
human1.talk("Merhaba")
human1.walk()

human2 = Human("Mehmet")
print(human2.name)
human2.name = "Cem"
human2.talk("Selam")
human2.walk

print(human1)
print(human2)
