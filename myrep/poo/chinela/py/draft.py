class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50 or valor % 2 != 0:
            print("fail: tamanho inválido, insira um número par entre 20 e 50")
        else:
            self.__tamanho = valor

    def __str__(self):
        return f"tamanho: {self.__tamanho}"

chinela = Chinela()

while True:
    try:
        linha = input().strip()
    except EOFError:
        break

    if not linha:
        continue

    print("$" + linha)
    partes = linha.split()
    cmd = partes[0]

    if cmd == "end":
        break
    elif cmd == "show":
        print(chinela)
    elif cmd == "set":
        tamanho = int(partes[1])
        chinela.setTamanho(tamanho)