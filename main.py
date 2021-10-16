from generator import Generator
import sys

utilization = .4
generationNumber = 1
processorsNumber = int(input("Digite o numero de processadores:\n"))

try:
    while utilization <= 1:
        Generator(utilization, processorsNumber, generationNumber).generate()
        utilization = round(utilization + .1, 1)
        generationNumber = generationNumber + 1
    print("Tarefas geradas com sucesso")
except:
    print("Ocorreu um erro ao gerar as tarefas")