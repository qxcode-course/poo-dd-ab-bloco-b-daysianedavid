class Relogio:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def set_hora(self, valor):
        if 0 <= valor <= 23:
            self.__hora = valor
        else:
            print("fail: hora invalida")

    def set_minuto(self, valor):
        if 0 <= valor <= 59:
            self.__minuto = valor
        else:
            print("fail: minuto invalido")

    def set_segundo(self, valor):
        if 0 <= valor <= 59:
            self.__segundo = valor
        else:
            print("fail: segundo invalido")

    def get_hora(self):
        return self.__hora

    def get_minuto(self):
        return self.__minuto

    def get_segundo(self):
        return self.__segundo

    def __str__(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
            if self.__minuto > 59:
                self.__minuto = 0
                self.__hora += 1
                if self.__hora > 23:
                    self.__hora = 0


def main():
    relogio = Relogio()
    try:
        while True:
            raw = input()
            print("$" + raw)
            line = raw.strip()
            if line == "":
                continue

            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break

            elif cmd == "show":
                print(relogio)

            elif cmd == "set":
                h = int(parts[1])
                m = int(parts[2])
                s = int(parts[3])
                relogio.set_hora(h)
                relogio.set_minuto(m)
                relogio.set_segundo(s)

            elif cmd == "next":
                relogio.nextSecond()

            elif cmd == "init":
                h = int(parts[1])
                m = int(parts[2])
                s = int(parts[3])
                relogio = Relogio()
                relogio.set_hora(h)
                relogio.set_minuto(m)
                relogio.set_segundo(s)


    except EOFError:
        pass


if __name__ == "__main__":
    main()