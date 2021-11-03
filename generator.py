from pathlib import Path
import random
from decimal import Decimal, getcontext

class Generator:
    def __init__(self, utilization, processorsNumber, generationNumber, decimalPlaces):      
        self.utilization = float(utilization)
        self.processorsNumber = int(processorsNumber)
        self.decimalPlaces = int(decimalPlaces)
        self.generationNumber = generationNumber
        getcontext().prec = decimalPlaces
    
    def generatedTasksetOutput(self, tasksNumber):
        print("Conjunto com utilizacao {} e {} tarefas gerado".format(self.utilization, tasksNumber))

    def generate(self):
        tasksNumber = random.randrange(self.processorsNumber + 1, 2*self.processorsNumber + 1)

        totalUtilization = float(self.utilization * self.processorsNumber)

        tasksUtilizations = []
        tasksPeriod = []
        tasksWcet = []

        validTaskSet = False

        while not validTaskSet:
            invalidTaskUtilization = False
            tasksUtilizations = [0.0] * tasksNumber
            tasksPeriod = [0] * tasksNumber
            tasksWcet = [0.0] * tasksNumber
            
            # generate a list with tasks utilizations
            for i in range(tasksNumber):
                tasksUtilizations[i] = random.random()
                tasksPeriod[i] = random.randrange(1, 100)

            sumTasksUtilizations = sum(tasksUtilizations)

            # proportionate utilization to total utilization of system
            for i in range(tasksNumber):
                tasksUtilizations[i] = Decimal(tasksUtilizations[i])/Decimal(sumTasksUtilizations)*Decimal(totalUtilization)                
                # prevent WCET > Period
                if tasksUtilizations[i] > 1:
                    invalidTaskUtilization = True
                    break
                tasksWcet[i] = Decimal(tasksUtilizations[i])*Decimal(tasksPeriod[i])
            # checks if total usage exceeds system capacity    
            sumTasksUtilizations = sum(tasksUtilizations)
            if (sumTasksUtilizations > (1 * self.processorsNumber)):
                invalidTaskUtilization = True
            validTaskSet = not invalidTaskUtilization

        # generate folders
        Path("./build/{:02d}-processors".format(self.processorsNumber)).mkdir(parents=True, exist_ok=True)

        f = open("./build/{:02d}-processors/tasks-{}n-{}U-{:04d}.txt"
            .format(
                self.processorsNumber,
                tasksNumber,
                self.utilization,
                self.generationNumber
            ), "w")

        # generate taskset file
        f.write("{} {} {}\n".format(1, self.processorsNumber, tasksNumber))
        for i in range(tasksNumber):
            f.write("1  ")
            for j in range(self.processorsNumber):
                f.write("{} ".format(tasksWcet[i]))    
            f.write("0  ")
            f.write("{} {}".format(tasksPeriod[i], tasksPeriod[i]))
            f.write("\n")
        f.close()

        # print success
        self.generatedTasksetOutput(tasksNumber)