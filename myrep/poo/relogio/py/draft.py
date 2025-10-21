class Relogio:
    def __init__ (self, hora=0, minuto=0, segundo=0):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def set_hora(self, valor):
        if 0 <= valor <= 23:
            self.hora = valor
        else:
            print("Hora inválida. Deve estar entre 0 e 23.")

    def set_minuto(self, valor):
        if 0 <= valor <= 59:
            self.minuto = valor
        else:
            print("Minuto inválido. Deve estar entre 0 e 59.")

    def set_segundos(self, valor):
        if 0 <= valor <= 59:
            self.segundo = valor 
        else: 
            print("Segundo inválido. Deve estar entre 0 e 59.")

    def get_hora(self):
        return self.hora
    def get_minuto(self):
        return self.minuto
    def get_segundo(self):
        return self.segundo 
    def __str__ (self):
        return f"{self.hora:02}:{self.minuto:02}:{self.segundo:02}"
    def nextSecond(self):
        self.segundo += 1
        if self.segundo > 59:
            self.segundo = 0
            self.minuto += 1
            if self.minuto > 59:
                self.minuto = 0
                self.hora += 1
                if self.hora > 23:
                    self.hora = 0

    def main(): 
        relogio = Relogio()
        try:
            while True:
                raw = input()


    

    
    
