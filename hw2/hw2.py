#==========================================
# Purpose: gets contracted distance according to the theory of special relativity 
# Input Parameter(s): distance and speed, distance is the original
# distance of the two objects, speed is the m/s in which we are travelling
# relative to two objects
# Return Value(s): the contracted distance between the two object
#==========================================

def length_contract(dist, speed):
    contr_dist = dist * (1 - (speed**2 / (3 * 10**8)**2))**.5
    return contr_dist

#==========================================
# Purpose: returns and prints the time necessary to finish 12 parsecs 
# Input Parameter(s): speed as in average speed
# Return Value(s): bessels time as seen by bessel
#==========================================

def bessel_run(speed):
    
    run = (3.086 * (10**16)) * 12
    print((run / speed)/31557600)
    return(((length_contract(run, speed)) / speed) / 31557600)


#==========================================
# Purpose: print "Who needs loops?" 100 times
# Input Parameter(s): none
# Return Value(s): none
#==========================================

def print_100():
    printx()
    printx()
    printx()
    printx()
    
def printx():
    printa()
    printa()
    printa()
    printa()
    printa()

def printa():
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
    print("Who needs loops?")
