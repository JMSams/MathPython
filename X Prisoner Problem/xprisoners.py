import random
import itertools
import threading
import time
import sys

def prisoners(count):
    drawers = []
    for i in range(count):
        drawers.append(i)
    
    results = 0
    for sim in range(simCount):
        #shuffle drawers
        random.shuffle(drawers)

        #check all prisoners
        successes = 0
        for prisoner in range(count):
            if prisoner in random.sample(drawers, round(count/2)):
                successes += 1
        
        if successes == count:
            results += 1
    
    global done
    done = True
    print("\rPrisoner Count: {}".format(count))
    print("Simulation Count: {}".format(simCount))
    print("Success Rate: {}/{} ({}%)".format(results, simCount, (results/simCount)*100))

done = False
def animate():
    for c in itertools.cycle(['.  ', '.. ', '...']):
        if done:
            break
        sys.stdout.write('\rworking' + c)
        sys.stdout.flush()
        time.sleep(0.1)

prisonerCount = int(sys.argv[1]) if len(sys.argv) > 1 else 10

simCount = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

t = threading.Thread(target=animate)
t.start()

prisoners(prisonerCount)
done = True