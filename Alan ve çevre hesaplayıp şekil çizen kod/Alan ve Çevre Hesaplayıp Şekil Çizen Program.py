class Dikdörtgen:

    def __init__(self, yükseklik, genişlik):
        self.yükseklik = yükseklik
        self.genişlik = genişlik

    def alan(self):
        return self.yükseklik * self.genişlik

    def çevre(self):
        return (self.yükseklik + self.genişlik) * 2

    def çizdir(self, sembol):
        for i in range(self.yükseklik):
            print(self.genişlik * sembol)

class Kare(Dikdörtgen):

    def __init__(self, kenar):
        self.yükseklik = kenar
        self.genişlik = kenar

class ParalelKenar(Dikdörtgen):
    "İç açılar 45 ve 135 derece olacak şekilde hesaplanacak"
    def __init__(self, yükseklik, taban):
        self.yükseklik = yükseklik
        self.genişlik = taban
        self.yankenar = yükseklik * 2**0.5

    def çevre(self):
        return (self.yankenar + self.genişlik) * 2

    def çizdir(self, sembol):
        for i in range(self.yükseklik):
            print(' ' * i, end='')
            print(self.genişlik * sembol)

class İkizKenarÜçgen(ParalelKenar):

    def alan(self):
        return self.yükseklik * self.genişlik / 2
        #return super().alan() / 2
    
    def çevre(self):
        return 2 * self.yankenar + self.genişlik
        #return super().çevre() - self.genişlik

    def çizdir(self, sembol): # Taban yüksekliğin 2 katı iken doğru çizer
        for i in range(self.yükseklik):
            print(' ' * ((self.genişlik//2 - i) - 1), end='')
            print(((i + 1) * 2 - 1) * sembol)
    
a = Dikdörtgen(10, 15)
b = Kare(10)
c = ParalelKenar(10, 15)
d = İkizKenarÜçgen(10, 20)

a.çizdir('D')
print("Alan :", a.alan(), ", Çevre :", a.çevre(), "\n")
b.çizdir('K')
print("Alan :", b.alan(), ", Çevre :", b.çevre(), "\n")
c.çizdir('P')
print("Alan :", c.alan(), ", Çevre :", c.çevre(), "\n")
d.çizdir('Ü')
print("Alan :", d.alan(), ", Çevre :", d.çevre(), "\n")

input()
