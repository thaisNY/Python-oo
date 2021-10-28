#classe fração com o metodos inverter, multiplicar, dividir
class Fracao():
    def __init__(self, num, den):
        self.numerador = num
        self.denominador = den
        if den == 0:
            return None
        else:
            self.denominador = den
    def __str__(self):
        if self.denominador == 0:
            return f'Não pode dividir por zero'
        return f'{self.numerador}/{self.denominador}'  #retorna o obj na forma de string
    def inverter (self):
        return Fracao(self.denominador, self.numerador)
    def negar(self):
        return Fracao(-self.numerador, self.denominador)
    def multiplicar(self, segundafracao):
        numer = self.numerador * segundafracao.numerador
        denom = self.denominador * segundafracao.denominador
        return Fracao(numer,denom)
    def dividir (self, segundafracao):
        return self.multiplicar(segundafracao.inverter())

#a = Fracao(4,0)
#b = a.inverter()
#c = a.negar()
#print(a)
#print(b)
#print(c)
a = Fracao(2,5)
b = Fracao(1,3)
multiplicar = a.multiplicar(b)
print(multiplicar)
print(multiplicar.numerador)
print(multiplicar.denominador)
divisao = a.dividir(b)
print(divisao)