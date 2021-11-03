from generator import Generator
from enviroment import Enviroment
import sys

utilization = .4
processorsNumber = int(Enviroment.PROCESSORS_NUMBER)
generationNumber = int(Enviroment.GENERATION_INITIAL_NUMBER)
decimalPlaces = int(Enviroment.DECIMAL_PLACES)

print("Quantidade de processadores: ", processorsNumber)

try:
    while utilization <= 1:
        for i in range(Enviroment.ROUNDS):
            Generator(utilization, processorsNumber, generationNumber, decimalPlaces).generate()
        utilization = round(utilization + .1, 1)
        generationNumber = generationNumber + 1
    print("Tarefas geradas com sucesso")
except:
    print("Ocorreu um erro ao gerar as tarefas")