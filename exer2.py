class Carro:
    def __init__(self, modelo, ano, velocidade, ligar_desligar, automatico):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligar_desligar = ligar_desligar
        self.automatico = automatico

    def ligar(self):
        self.ligar_desligar = True
        return self.ligar_desligar

    # def desligar(self):
    #     self.ligar_desligar = False
    #     return self.ligar_desligar

    # def acelerar(self, velocidade):


    # def frear(self, velocidade):

    def auto(self):
        self.automatico = False
        return self.automatico

a = Carro("Fiat", "2022", 10, True,True)
print(f"Modelo: ", a.modelo)
print(f"ano: ", a.ano)
print(f"velocidade: ", a.velocidade)
print(f"ligado: ", a.ligar())
print(f"automatico: ", a. auto())









# md = input("Digite modelo: ")
# aa = input("Digite ano: ")
# vel = float(input("Digite velocidade: "))
# resp = int(input("Esse Carro é automático? \n[1] Verdadeiro\n[2] Falso\n"))

# if resp == 1:
#     carro01 = Carro(md, aa, vel)
#     print("-=" * 50)
#     print("Carro01")
#     print(f"modelo:  {carro01.modelo}")
#     print(f"ano: {carro01.ano}")
#     print(f"velocidade: {carro01.velocidade}Km")
#     print("Esse carro é automático")
#     print("-=" * 50)
# else:
#     carro01 = Carro(md, aa, vel)
#     print("-=" * 50)
#     print("Carro01")
#     print(f"modelo:  {carro01.modelo}")
#     print(f"ano: {carro01.ano}")
#     print(f"velocidade: {carro01.velocidade}Km")
#     print("Esse carro não é automático")



