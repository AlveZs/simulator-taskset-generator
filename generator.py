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
    
    def isInvalidSum(self, processorsNumber, tasksNumber, tasksWcet, tasksPeriod):
        totalUtilzation = 0.0
        precision = 10**-1
        targetUtilization = self.utilization * processorsNumber
        for i in range(tasksNumber):
            taskUtilization = float(tasksWcet[i])/tasksPeriod[i]
            totalUtilzation = totalUtilzation + taskUtilization
        difference = (totalUtilzation - targetUtilization)
        return difference > 0.0 or difference < -precision

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
                tasksUtilizations[i] = Decimal(random.random())
                tasksPeriod[i] = random.randrange(1, 100)

            sumTasksUtilizations = sum(tasksUtilizations)

            # proportionate utilization to total utilization of system
            for i in range(tasksNumber):
                tasksUtilizations[i] = (Decimal(tasksUtilizations[i])/Decimal(sumTasksUtilizations))*Decimal(totalUtilization)                
                # prevent WCET > Period
                if tasksUtilizations[i] > 1:
                    invalidTaskUtilization = True
                    break
                tasksWcet[i] = Decimal(Decimal(tasksUtilizations[i])*Decimal(tasksPeriod[i]))
            # checks if total usage exceeds system capacity
            if (not invalidTaskUtilization):
                invalidTaskUtilization = self.isInvalidSum(
                    self.processorsNumber,
                    tasksNumber,
                    tasksWcet,
                    tasksPeriod
                )
            validTaskSet = not invalidTaskUtilization

        # generate folders
        Path("./build/{:02d}-processors".format(self.processorsNumber)).mkdir(parents=True, exist_ok=True)

        f = open("./build/{:02d}-processors/{:04d}-{}n-{}U.txt"
            .format(
                self.processorsNumber,
                self.generationNumber,
                tasksNumber,
                self.utilization,
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