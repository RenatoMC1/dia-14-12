class Carro:
    def __init__(self, modelo, ano, velocidade, ligado, automatico):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico

    def ligar(self, ligado):
        while ligado == "n":
            opcao = input('Você deseja ligar seu carro?')
            if opcao == 's':
                print('carro ligado, ACELERA!')
                break
            elif opcao == 'n':
                print('carro desligado!')
                break

    def acelerar(self, velocidade):
        while velocidade >= 0:
            acelera = int(input('Aperta 1 para acelerar ou 2 para frear seu carro: '))
            if acelera == 2:
                break
            if acelera == 1:
                print('Acelerando!')
                velocidade += 10
                print(f"Sua velocidade atual é de {velocidade}km/h")
                if velocidade <= 20:
                    print('Você esta na marcha 1, continua ta dboa!')
                elif velocidade <= 30:
                    print('Você esta na marcha 2, continua ta dboa!')
                elif velocidade <= 35:
                    print('Você esta na marcha 3, continua ta dboa!')
                elif velocidade <= 45:
                    print('Você esta na marcha 4, melhor parar!')
                elif velocidade >= 45:
                    print('Você esta na marcha 5, pare agora!')

    def frear(self, velocidade):
        while velocidade >= 0:
            opcao2 = input('FREANDO! ,Voce deseja frear por completo? (s/n)')
            if opcao2 == "n":
                print('Tome cuidado!')
                acelera = int(input('Aperta 1 para acelerar ou 2 para frear seu carro: '))
                if acelera == 2:
                    continue
                if acelera == 1:
                    print('Acelerando!')
                    velocidade += 10
                    print(f"Sua velocidade atual é de {velocidade}km/h")
                    if velocidade <= 20:
                        print('Você esta na marcha 1, continua ta dboa!')
                    elif velocidade <= 30:
                        print('Você esta na marcha 2, continua ta dboa!')
                    elif velocidade <= 35:
                        print('Você esta na marcha 3, continua ta dboa!')
                    elif velocidade <= 45:
                        print('Você esta na marcha 4, melhor parar!')
                    elif velocidade >= 45:
                        print('Você esta na marcha 5, pare agora!')
                continue
            elif opcao2 == "s":
                print('Freando..., voce está parado!')
                velocidade -= velocidade
                if velocidade == 0:
                    break
                elif velocidade > 0:
                    continue

    def desligar(self, ligado):
        while ligado == "n":
            opcao = input('Você deseja desligar seu carro?')
            if opcao == 's':
                print('carro desligado!')
                break
            elif opcao == 'n':
                print('carro ligado!')
                continue


modelo = input('Qual modelo do seu carro? ')
ano = int(input('Qual ano do seu carro? '))
ligado = input('Seu carro está ligado?(s/n)').lower()
automatico = input('Seu carro é automático?(s/n) ').lower()
velocidade = int(input('Qual velocidade inicial do seu carro? '))
carro01 = Carro(modelo, ano, ligado, automatico, velocidade)

carro01.ligar(ligado)
carro01.acelerar(velocidade)
carro01.frear(velocidade)
carro01.desligar(ligado)