from generator import Generator
from enviroment import Enviroment
import sys

utilization = round(float(Enviroment.INITAL_UTILIZATION), 2)
finalUtilization = round(float(Enviroment.FINAL_UTILIZATION), 2)
processorsNumber = int(Enviroment.PROCESSORS_NUMBER)
generationNumber = int(Enviroment.GENERATION_INITIAL_NUMBER)
decimalPlaces = int(Enviroment.DECIMAL_PLACES)
step = round(float(Enviroment.STEP), 2)

print("Quantidade de processadores: ", processorsNumber)

while utilization <= finalUtilization:
    for i in range(Enviroment.ROUNDS):
        Generator(utilization, processorsNumber, generationNumber, decimalPlaces).generate()
        generationNumber = generationNumber + 1
    utilization = round(utilization + step, 2)
print("Tarefas geradas com sucesso")