class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        self.__idade = idade

    def __str__(self):
        return f"{self.__nome}:{self.__idade}"


class Moto:
    def __init__(self, potencia=1):
        self.__potencia = potencia
        self.__tempo = 0
        self.__pessoa = None

    # getters e setters
    def get_potencia(self):
        return self.__potencia

    def set_potencia(self, valor):
        self.__potencia = valor

    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, valor):
        self.__tempo = valor

    def get_pessoa(self):
        return self.__pessoa

    def set_pessoa(self, pessoa):
        self.__pessoa = pessoa

    def enter(self, pessoa):
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
        else:
            self.__pessoa = pessoa

    def leave(self):
        if self.__pessoa is None:
            print("fail: empty motorcycle")
        else:
            print(self.__pessoa)
            self.__pessoa = None

    def buy(self, minutos):
        self.__tempo += minutos

    def drive(self, minutos):
        if self.__tempo == 0:
            print("fail: buy time first")
        elif self.__pessoa is None:
            print("fail: empty motorcycle")
        elif self.__pessoa.get_idade() > 10:
            print("fail: too old to drive")
        elif minutos > self.__tempo:
            print(f"fail: time finished after {self.__tempo} minutes")
            self.__tempo = 0
        else:
            self.__tempo -= minutos

    def honk(self):
        print("P" + "e" * self.__potencia + "m")

    def __str__(self):
        if self.__pessoa is None:
            pessoa_info = "(empty)"
        else:
            pessoa_info = f"({self.__pessoa})"
        return f"power:{self.__potencia}, time:{self.__tempo}, person:{pessoa_info}"


moto = Moto()

while True:
    linha = input().strip()
    if not linha:
        continue

    print("$" + linha)  
    partes = linha.split()
    cmd = partes[0]

    if cmd == "end":
        break
    elif cmd == "init":
        pot = int(partes[1])
        moto = Moto(pot)
    elif cmd == "show":
        print(moto)
    elif cmd == "enter":
        nome = partes[1]
        idade = int(partes[2])
        pessoa = Pessoa(nome, idade)
        moto.enter(pessoa)
    elif cmd == "leave":
        moto.leave()
    elif cmd == "buy":
        minutos = int(partes[1])
        moto.buy(minutos)
    elif cmd == "drive":
        minutos = int(partes[1])
        moto.drive(minutos)
    elif cmd == "honk":
        moto.honk()