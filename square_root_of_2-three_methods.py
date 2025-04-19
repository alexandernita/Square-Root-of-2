print("\n\t\t\t       The Square Root of 2")
print("\n\t\t\tComparison of the Methods So Far")
print("\t\t----------------------------------------------")
print("\n \t    Bisection   \t  Babylonian    \t  Newton's")
print("\t------------------------------------------------------------------\n")
    
###########################
#  Bisection Method

n=0

a = 1
b = 2

e = 1e-10
N = 41
k = 0

BIS = []

for i in range(1,N):
    n = n+1
    c = (a+b)/2
    y1 = a**2-2
    y2 = b**2-2
    y = c**2-2
    BIS.append(c)
    
    if y == 0 or abs(y)<e:
        k = 1
        break
    elif y*y1<0:
        b = c
    else:
        a = c



###########################
#  Babylonian Method + Banach Fixed Point Theorem

p = 1           # Initial guess, p_0
e = 1e-10       # Tolerance: 10 decimals
n = 0           # Counter (for # steps)
m = 40          # Upper limit on 'for' loop

BAB = []

for i in range(1,m+1):
    n = n+1
    BAB.append(p)
    q = p
    p = (p+2/p)/2
    if abs(q-p)<e:
        BAB.append(p)
        break



###########################
#  Newton's Method

p=1     # initial guess
q=p     
n=0     # counter
e=1e-10 # tolerance / error
N = 41  # upper limit on number of iterations

NEWT = []

for i in range(1,N):
    NEWT.append(p)
    p = p - (p**2-2)/(2*p)
    if abs(p-q)<e:
        NEWT.append(p)
        break
    q = p
    n = n+1


###########################
r = [len(BIS),len(BAB),len(NEWT)]    
t = [BIS,BAB,NEWT]

m = max(r)

if len(BIS)<m:
    l = len(BIS)
    for j in range(i+1,m+1):
        BIS.append(0)
        
if len(BAB)<m:
    l = len(BAB)
    for j in range(l+1,m+1):
        BAB.append(0)
        
if len(NEWT)<m:
    l = len(NEWT)
    for j in range(len(NEWT)+1,m+1):
        NEWT.append(0)

for x, y, z in zip(BIS,BAB,NEWT):
    print("\t   %.10f\t" % x,"\t",format(y, ".10f") if y else "",\
          "\t\t",format(z, ".10f") if z else "")

