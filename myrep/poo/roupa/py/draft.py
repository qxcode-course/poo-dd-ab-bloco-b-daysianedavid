class Roupa:
    def __init__(self):
        self.__tamanho = "" 

    def get_tamanho(self):
        return self.__tamanho

    def set_tamanho(self, valor):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if valor in tamanhos_validos:
            self.__tamanho = valor
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")

    def __str__(self):
        return f"size: ({self.__tamanho})"

def main():
    roupa = Roupa()

    while True:
        linha = input()
        if not linha:
            continue

        print("$" + linha) 
        partes = linha.split()
        cmd = partes[0]

        if cmd == "end":
            break

        elif cmd == "show":
            print(roupa)

        elif cmd == "size":
            valor = partes[1]
            roupa.set_tamanho(valor)


if __name__ == "__main__":
    main()
