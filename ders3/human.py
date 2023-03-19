class Human:
    name = "Furkan"
    def __init__(self,name) :
        self.name = name
        print("Bir Human instance'ı oluşturuldu.")
    def __str__(self) -> str:
        return f"Str fonksiyonundan dönen değer : {self.name}"
    def talk(self,sentence):
        name = "Beyza"
        print(f"{self.name} : {sentence}")
    def walk(self):
        print(f"{self.name} is walking.")