class Carro:
    def __init__(self, modelo, ano, velocidade, ligado, cambio):
        if modelo is str(modelo):
            self.modelo = modelo
        else:
            raise Exception('O modelo do carro precisa ser str')

        if ano is int(ano):
            if 1900 < ano <= 2022:
                self.ano = ano
            else:
                raise Exception('O ano do carro precisa estar entre 1900 e o ano atual.')
        else:
            raise Exception('O ano do carro precisa ser int')

        if velocidade is int(velocidade):
            if velocidade >= 0:
                self.velocidade = velocidade
            else:
                raise Exception('Velocidade não pode ser menor do que 0 (zero).')
        else:
            raise Exception('A velocidade do carro precisa ser int')

        onoff = ['ligado', 'desligado']
        if ligado in onoff:
            self.ligado = ligado
        else:
            raise Exception('Carro só aceita as condições \'ligado\' ou \'desligado\'')

        marcha = ['auto', 'manual']
        if cambio in marcha:
            self.cambio = cambio
        else:
            raise Exception('A marcha do carro só aceita as condições \'auto\' ou \'manual\'')

    def ligar(self):
        if self.ligado == 'desligado':
            self.ligado = 'ligado'
            print('O carro agora está ligado.')

        else:
            print('O carro já está ligado.')

    def desligar(self):
        if self.ligado == 'ligado':
            self.ligado = 'deslligado'
            print('O carro agora está desligado.')
        else:
            print('O carro já está desligado.')

    def acelerar(self, aceleracao):
        if self.ligado == 'desligado':
            print('É impossível acelerar um carro desligado.')
        else:
            self.velocidade += aceleracao
            print(f'A velocidade atual é {self.velocidade}Km/h')

    def frear(self):
        if self.velocidade > 0:
            self.velocidade = 0
            print('O carro parou.')
            return self.velocidade
        else:
            print('O carro já está parado')

    def check_marcha(self):
        if self.velocidade == 0 or self.ligado == 'desligado':
            print('Seu carro está parado ou desligado.')
        elif 0 < self.velocidade <= 20:
            print('O carro está na 1ª marcha.')
        elif 20 < self.velocidade <= 30:
            print('O carro está na 2ª marcha.')
        elif 30 < self.velocidade <= 35:
            print('O carro está na 3ª marcha.')
        elif 35 < self.velocidade <= 45:
            print('O carro está na 4ª marcha.')
        else:
            print('O carro está na 5ª marcha.')

    def check_velocidade(self):
        print(f'A velocidade atual do carro é {self.velocidade}Km/h')

