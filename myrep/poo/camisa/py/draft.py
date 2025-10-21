class Roupa:

    def __init__(self): 
        self.__tamanho: str = "" 
    def getTamanho(self) -> str: 
        return self.__tamanho

    def setTamanho(self, valor: str):
        tamanhos_validos = {"PP", "P", "M", "G", "GG"}
        if valor in tamanhos_validos:
            self.__tamanho = valor
        else:
            print("Tamanho inválido. Tamanhos válidos são: PP, P, M, G, GG ou XG.")

     
    # while self.getTamanho() == "": 
    #     print("Digite seu tamanho de roupa")
    #     tamanho = input() 
    #     self.setTamanho(tamanho)
 
roupa = Roupa()
roupa.setTamanho("M")
print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())