import random
import itertools
import threading
import time
import sys

from decimal import Decimal,getcontext
getcontext().prec = 64

from os import system,name,path
if name == 'nt':
    _ = system('cls')
else:
    _ = system('clear')

prisonerCount = 0
currentPrisoner = -1
currentSim = -1

def prisoners(count):
    global currentSim, currentPrisoner, prisonerCount
    prisonerCount = count

    drawers = []
    for i in range(prisonerCount):
        drawers.append(i)
    
    results = 0
    for sim in range(simCount):
        currentSim = sim

        #shuffle drawers
        random.shuffle(drawers)

        #check all prisoners
        successes = 0
        for prisoner in range(prisonerCount):
            currentPrisoner = prisoner
            #for half the drawers...
            d = prisoner
            for i in range(round(prisonerCount/2)):
                if drawers[d] == prisoner:
                    successes += 1
                    break
                else:
                    d = drawers[d]
        
        if successes == prisonerCount:
            results += 1
    
    global done
    done = True

    with open(path.join(sys.path[0], 'result.txt'), 'a') as f:
        f.write("Prisoner Count: {}\n".format(prisonerCount))
        f.write("Simulation Count: {}\n".format(simCount))
        f.write("Success Rate: {}/{} ({}%)\n".format(results, simCount, Decimal(Decimal(results)/Decimal(simCount))*Decimal(100)))
        f.write("-------------\n")

def animate():
    for c in itertools.cycle(['\\', '|', '/', '-']):
        if done:
            print("\rSimulations for {} prisoners complete!       ".format(prisonerCount))
            break
        sys.stdout.write("\rWorking ({3} Prisoners) (Sim: {1}/{2}) {0}".format(c, currentSim, simCount, prisonerCount))
        sys.stdout.flush()
        time.sleep(0.15)

def StartAnimator():
    t = threading.Thread(target=animate)
    t.daemon = True
    
    global done
    done = False
    t.start()

simCount = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000

StartAnimator()
prisoners(10)

StartAnimator()
prisoners(100)

StartAnimator()
prisoners(1000)