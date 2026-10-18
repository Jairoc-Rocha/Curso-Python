class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco


fusca = Carro(4, 1.0, True, "VW", 40000)

print(fusca.portas)
print(fusca.motor)
print(fusca.teto_solar)
print(fusca.marca)
print(fusca.preco)
