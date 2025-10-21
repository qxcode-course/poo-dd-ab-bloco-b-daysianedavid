class Pessoa:
    def __init__(self, nome: str, dinheiro: int):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def get_nome(self):
        return self.__nome

    def get_dinheiro(self):
        return self.__dinheiro

    def set_dinheiro(self, valor: int):
        self.__dinheiro = valor

    def __str__(self):
        return f"{self.__nome}:{self.__dinheiro}"

class Moto:
    def __init__(self):
        self.__custo = 0                
        self.__motorista: Pessoa | None = None
        self.__passageiro: Pessoa | None = None

    def setDriver(self, nome: str, dinheiro: int):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self, nome: str, dinheiro: int):
        if self.__motorista is None:
            return 
        self.__passageiro = Pessoa(nome, dinheiro)


    def drive(self, km: int):
        if self.__passageiro is None:
            return
        self.__custo += km

    def leavePass(self):
        if self.__passageiro is None:
            return

        passageiro = self.__passageiro
        motorista = self.__motorista
        custo = self.__custo

        if passageiro.get_dinheiro() >= custo:
            passageiro.set_dinheiro(passageiro.get_dinheiro() - custo)
            motorista.set_dinheiro(motorista.get_dinheiro() + custo)
            print(f"{passageiro.get_nome()}:{passageiro.get_dinheiro()} left")
        else:
            print("fail: Passenger does not have enough money")
      
            motorista.set_dinheiro(motorista.get_dinheiro() + custo)  # Uber cobre a diferença
            passageiro.set_dinheiro(0)
            print(f"{passageiro.get_nome()}:0 left")

  
        self.__custo = 0
        self.__passageiro = None

    def __str__(self):
        cost = self.__custo
        drv = "None" if self.__motorista is None else str(self.__motorista)
        pas = "None" if self.__passageiro is None else str(self.__passageiro)
        return f"Cost: {cost}, Driver: {drv}, Passenger: {pas}"

def main():
    moto = Moto()
    try:
        while True:
            raw = input()
            print("$" + raw)         
            line = raw.strip()
            if not line:
                continue

            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break

            elif cmd == "show":
                print(moto)

            elif cmd == "setDriver":
                nome = parts[1]
                dinheiro = int(parts[2])
                moto.setDriver(nome, dinheiro)

            elif cmd == "setPass":
                nome = parts[1]
                dinheiro = int(parts[2])
                moto.setPass(nome, dinheiro)

            elif cmd == "drive":
                km = int(parts[1])
                moto.drive(km)

            elif cmd == "leavePass":
                moto.leavePass()


    except EOFError:
        pass


if __name__ == "__main__":
    main()

        