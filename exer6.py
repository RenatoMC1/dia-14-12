class Veiculo:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano
        self.cml = None
        self.modelo = None

veiculo = Veiculo("azul",2000)
print(veiculo.cor)
print(veiculo.ano)
print(veiculo.cml)

print("-="*50)

class Onibus(Veiculo):
    def Capmaxlug(self):
        cml = int(input("Digite a capaciade máxima do ônibus: "))
        self.cml = cml
        return self.cml
    def Mod(self):
        mod = input("Digite modelo do ônibus: ")
        self.modelo = mod
        return self.modelo

onibus1 = Onibus("verde", 1990)
print("Dados do ônibus ")
print("A cor é: ", onibus1.cor)
print("O ano é: ", onibus1.ano)
print("A capacidade máxima é: ", onibus1.Capmaxlug())
print("O modelo é: ", onibus1.Mod())

print("-="*50)

class Moto(Veiculo):
    def Capmaxlug(self):
        cml = int(input("Digite a capaciade máxima da Moto: "))
        self.cml = cml
        return self.cml
    def Mod(self):
        mod = input("Digite modelo da Moto: ")
        self.modelo = mod
        return self.modelo

moto1 = Moto("Vermelha", 2018)
print("Dados da Moto ")
print("A cor é: ", moto1.cor)
print("O ano é: ", moto1.ano)
print("A capacidade máxima é: ", moto1.Capmaxlug())
print("O modelo é: ", moto1.Mod())





