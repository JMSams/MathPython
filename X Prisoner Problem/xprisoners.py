import random
import itertools
import threading
import time
import sys

simCount = 1000000

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
    print("Success Rate: {}".format(results / simCount))

done = False
def animate():
    for c in itertools.cycle(['.', '..', '...']):
        if done:
            break
        sys.stdout.write('\working' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

prisoners(20)
done = True