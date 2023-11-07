from tabulate import tabulate
import math as m

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

studKP = 0.95
studKs = {
   0.95:[12.7,4.3,3.2,2.8,2.6,2.4,2.4,2.3,2.3],
   }

def getEpsilon():
   return "NO DATA"

def calcDeltas(data:list,studKP:float):
    experiments = len(data)
    ret = []
    dA = []
    dAsq = []
    dataMean = sum(data)/len(data)
 
    for a in data:
       dA.append(abs(a - dataMean))
       dAsq.append(abs(a - dataMean)**2)
 
    for i, a in enumerate(data):
       dAi = dA[i]
       sigma = ((sum(dAsq))/(experiments*(experiments-1)))**0.5
       studKPN = studKs[studKP][experiments-1]
       epsilon = getEpsilon()
       ret.append([a,dataMean,dAi,dAi**2,sigma,studKP,studKPN,epsilon])
    return ret

table = [["N опыта","Знач. опыта"]]



print("Вводите найденные значения")

while True:
  n = len(table)
  inp = input(f"{n}>".ljust(3))
  try:
    table.append([n,float(inp)])
  except ValueError:
    break


studKN = studKs[studKP][len(table)-1]


print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
print(f"Количество опытов: {bcolors.BOLD+str(len(table)-1)+bcolors.ENDC}, коэф. Стьюдента: {bcolors.BOLD+str(studKN)+bcolors.ENDC}")

deltaTable = calcDeltas([float(x[1]) for x in table[1:]],studKP=studKP)



print(tabulate(deltaTable, headers=["ai","a ср.","d ai","d ai^2","sigma","P","t PN","d a сл"], tablefmt='fancy_grid'))