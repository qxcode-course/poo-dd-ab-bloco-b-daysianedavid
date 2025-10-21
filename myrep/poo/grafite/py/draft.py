class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre     # espessura (0.3, 0.5, 0.7, 0.9)
        self.dureza = dureza       # HB, 2B, 4B, 6B
        self.tamanho = tamanho     # mm

    def gasto_por_folha(self) -> int:
        # HB=1, 2B=2, 4B=4, 6B=6
        if self.dureza == "HB":
            return 1
        if self.dureza == "2B":
            return 2
        if self.dureza == "4B":
            return 4
        if self.dureza == "6B":
            return 6
        return 0

    def __str__(self) -> str:
        # formato: [calibre:dureza:tamanho]
        return f"[{self.calibre}:{self.dureza}:{self.tamanho}]"


# --------- Modelo de Lapiseira ---------
class Lapiseira:
    def __init__(self, calibre: float = 0.5):
        self.calibre = calibre
        self.grafite: Grafite | None = None  # só 1 grafite

    def tem_grafite(self) -> bool:
        return self.grafite is not None

    def inserir(self, g: Grafite):
        if self.tem_grafite():
            print("fail: ja existe grafite")
            return
        if g.calibre != self.calibre:
            print("fail: calibre incompativel")
            return
        self.grafite = g

    def remover(self):
        if not self.tem_grafite():
            print("fail: nao existe grafite")
            return
        self.grafite = None

    def escrever(self):
        if not self.tem_grafite():
            print("fail: nao existe grafite")
            return

        g = self.grafite
        uso = g.gasto_por_folha()

        # precisa ter mais que 10mm para começar
        if g.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return

        # se ao escrever a folha toda passaria de 10 para abaixo de 10,
        # gasta só até 10 e avisa "folha incompleta"
        if g.tamanho - uso < 10:
            g.tamanho = 10
            print("fail: folha incompleta")
            return

        # caso normal: dá para escrever a folha inteira
        g.tamanho -= uso

    def __str__(self) -> str:
        if self.grafite is None:
            return f"calibre: {self.calibre}, grafite: null"
        else:
            return f"calibre: {self.calibre}, grafite: {self.grafite}"


# --------- Shell (ecoando comandos com $) ---------
def main():
    lap = Lapiseira()  # valor inicial não importa; será trocado com init
    try:
        while True:
            raw = input()
            print("$" + raw)  # eco exato

            line = raw.strip()
            if not line:
                continue
            p = line.split()
            cmd = p[0]

            if cmd == "end":
                break

            elif cmd == "init":
                calib = float(p[1])
                lap = Lapiseira(calib)

            elif cmd == "show":
                print(lap)

            elif cmd == "insert":
                calib = float(p[1])
                dureza = p[2]
                tam = int(p[3])
                g = Grafite(calib, dureza, tam)
                lap.inserir(g)

            elif cmd == "remove":
                lap.remover()

            elif cmd == "write":
                lap.escrever()

    except EOFError:
        pass


if __name__ == "__main__":
    main()
        



    