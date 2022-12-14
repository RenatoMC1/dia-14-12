class Carro:
    def __init__(self, modelo, ano, velocidade, ligado, cambio):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = bool
        self.cambio = cambio

    def ligar(self):
        self.ligado = True
        print('o carro esta ligado')

    def desligar(self):
        self.ligado = False
        print('Você desligou o carro')

    def Ligado(self, chave):
        if chave == 1:
            print('o carro está ligado')
            self.ligado = True
        else:
            print('O carro está desligado')
            self.Ligado = False

    def acelerar(self, velociade, ligado):
        ligado = self.ligado
        if ligado == True:
            self.velocidade = self.velocidade + velociade
            print('VRUUUUUM')
            print(f'sua velocidade atual é: {self.velocidade}Km/H')
        else:
            print('O carro está desligado você não pode acelerar')
            self.velocidade = 0

    def frear(self, velocidade):
        velocidade = self.velocidade
        if velocidade > 0:
            self.velocidade = self.velocidade - velocidade
            print('freando...')
            print(f'sua velocidade atual é: {self.velocidade}Km/H')
        else:
            print('O carro já esta parado')

    def verificarmarcha(self, velocidade):
        velocidade = self.velocidade
        if velocidade == 0:
            self.velocidade = velocidade
            return print('voce esta em ponto neutro')
        elif velocidade <= 20:
            self.velocidade = velocidade
            return print('você esta de 1ª marcha')
        elif velocidade > 20 and velocidade <= 30:
            self.velocidade = velocidade
            return print('você esta de 2ª marcha')
        elif 30 < velocidade <= 35:
            self.velocidade = velocidade
            return print('você esta de 3ª marcha')
        elif velocidade > 35 and velocidade <= 45:
            self.velocidade = velocidade
            return print('você esta de 4ª marcha')
        else:
            self.velocidade = velocidade
            return print('você esta de 5ª marcha')

    def velocimetro(self):
        print(f'{self.velocidade}Km/H')

