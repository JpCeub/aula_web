class Retangulo:
    def __init__(self, x1, y1, x2, y2): #(x1, y1) (x2, y2) atributos construtores
        self.base = abs(x2 - x1) #atributos instanciais
        self.altura = abs(y2 - y1) #abs = função que pega o modulo

    def perimetro(self):
        perim = (self.base + self.altura)*2
        print(f'Perímetro: {perim}')
    
    def area(self):
        ar = self.base * self.altura
        print(f'Área: {ar}')
        
    def diagonal(self):
        D = (self.base**2 + self.altura**2)**0.5 
        print(f'Diagonal: {D}')

ret = Retangulo(2,8,5,3)
ret.perimetro()
ret.area()
ret.diagonal()