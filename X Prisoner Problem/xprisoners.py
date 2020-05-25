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

currentPrisoner = -1
currentSim = -1

def prisoners():
    global currentSim, currentPrisoner, prisonerCount

    drawers = []
    for i in range(prisonerCount):
        drawers.append(i)
    
    with open(path.join(sys.path[0], 'results for {} prisoners.csv'.format(prisonerCount)), 'w') as f:
        f.write('sim,win,')
        f.write(','.join(map(str, drawers)))
        f.write('\n')

        results = 0
        for sim in range(simCount):
            currentSim = sim

            f.write(str(sim) + ',')

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
                f.write('yes,')
                results += 1
            else:
                f.write('no,')
            f.write(','.join(map(str, drawers)))
    
    global done
    done = True

    #with open(path.join(sys.path[0], 'results for {} prisoners.csv'.format(prisonerCount)), 'w') as f:
    #    f.write("Prisoner Count: {}\n".format(prisonerCount))
    #    f.write("Simulation Count: {}\n".format(simCount))
    #    f.write("Success Rate: {}/{} ({}%)\n".format(results, simCount, Decimal(Decimal(results)/Decimal(simCount))*Decimal(100)))
    #    f.write("-------------\n")

def animate():
    for c in itertools.cycle(['\\', '|', '/', '-']):
        if done:
            print("\rSimulations for {} prisoners complete!       ".format(prisonerCount))
            break
        print("\rWorking ({3} Prisoners) (Sim: {1}/{2}) {0}".format(c, currentSim, simCount, prisonerCount), end="")
        sys.stdout.flush()
        time.sleep(0.2)

def StartAnimator():
    t = threading.Thread(target=animate)
    t.daemon = True
    
    global done
    done = False
    t.start()

prisonerCount = int(sys.argv[1]) if len(sys.argv) > 1 else 10
simCount = int(sys.argv[2]) if len(sys.argv) > 2 else 100000

StartAnimator()
prisoners()