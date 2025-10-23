class Bateria:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def getCarga(self):
        return self.__carga

    def getCapacidade(self):
        return self.__capacidade

    def carregar(self, valor):
        self.__carga += valor
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def descarregar(self, valor):
        self.__carga -= valor
        if self.__carga < 0:
            self.__carga = 0

    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"

    def mostrar(self):
        print(self.__str__())


class Carregador:
    def __init__(self, potencia):
        self.__potencia = potencia

    def getPotencia(self):
        return self.__potencia

    def __str__(self):
        return f"(Potência {self.__potencia})"

    def mostrar(self):
        print(self.__str__())


class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__bateria = None
        self.__carregador = None

    def setBateria(self, bateria: Bateria):
        self.__bateria = bateria
        print("bateria conectada")

    def rmBateria(self):
        if self.__bateria is None:
            print("fail: nenhuma bateria para remover")
            return None
        print("bateria removida")
        temp = self.__bateria
        self.__bateria = None
        return temp

    def setCarregador(self, carregador: Carregador):
        self.__carregador = carregador
        print("carregador conectado")

    def rmCarregador(self):
        if self.__carregador is None:
            print("fail: nenhum carregador para remover")
            return None
        print("carregador removido")
        temp = self.__carregador
        self.__carregador = None
        return temp

    def ligar(self):
        if (self.__bateria and self.__bateria.getCarga() > 0) or self.__carregador:
            if not self.__ligado:
                self.__ligado = True
                print("notebook ligado")
            else:
                print("notebook já está ligado")
        else:
            print("não foi possível ligar")

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("notebook desligado")
        else:
            print("notebook já está desligado")

    def usar(self, tempo):
        if not self.__ligado:
            print("notebook desligado")
            return

        if self.__bateria is None and self.__carregador is None:
            print("erro: sem energia disponível")
            self.desligar()
            return

        if self.__bateria and self.__carregador:
            self.__bateria.carregar(self.__carregador.getPotencia() * tempo)
            print("Notebook utilizado com sucesso (carregando e usando)")
        elif self.__bateria and not self.__carregador:
            if self.__bateria.getCarga() > tempo:
                self.__bateria.descarregar(tempo)
                print(f"Usando por {tempo} minutos")
            else:
                usado = self.__bateria.getCarga()
                self.__bateria.descarregar(usado)
                print(f"Usando por {usado} minutos, notebook descarregou")
                self.desligar()
        elif self.__carregador and not self.__bateria:
            print("Notebook utilizado com sucesso")
        else:
            print("fail: impossível usar")

    def mostrar(self):
        estado = "Ligado" if self.__ligado else "Desligado"
        bat = str(self.__bateria) if self.__bateria else "Nenhuma"
        car = str(self.__carregador) if self.__carregador else "Desconectado"
        print(f"Status: {estado}, Bateria: {bat}, Carregador: {car}")