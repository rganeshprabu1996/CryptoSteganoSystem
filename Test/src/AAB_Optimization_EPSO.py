from numpy import *
from random import *
from math import *
import AAC_Embedding_QStegano as es
iter_max = 10000
pop_size = 500
dimensions = 2
c1 = 2
c2 = 2
err_crit = 0.00001
global compress
class Particle:
    pass       
def f6(param):
    es.compress = param*10
    para = param[0:2]
    num = (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) * \
        (sin(sqrt((para[0] * para[0]) + (para[1] * para[1])))) - 0.5
    denom = (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1]))) * \
            (1.0 + 0.001 * ((para[0] * para[0]) + (para[1] * para[1])))
    f6 =  0.5 - (num/denom)
    errorf6 = 1 - f6
    return f6, errorf6;
particles = []
for i in range(pop_size):
    p = Particle()
    p.params = array([random() for i in range(dimensions)])
    p.fitness = 0.0
    p.v = 0.0
    particles.append(p)
gbest = particles[0]
err = 999999999
while i < iter_max :
    for p in particles:
        fitness,err = f6(p.params)
        if fitness > p.fitness:
            p.fitness = fitness
            p.best = p.params
        if fitness > gbest.fitness:
            gbest = p
        v = p.v + c1 * random() * (p.best - p.params) \
                + c2 * random() * (gbest.params - p.params)
        p.params = p.params + v
    i  += 1
    if err < err_crit:
        break
    if i % (iter_max/10) == 0:
        print ('\n.')
print ('\nParticle Swarm Optimisation\n')
print ('PARAMETERS\n','-'*9)
print ('Population size : ', pop_size)
print ('Dimensions      : ', dimensions)
print ('Error Criterion : ', err_crit)
print ('c1              : ', c1)
print ('c2              : ', c2)
print ('function        :  f6')
print ('RESULTS\n', '-'*7)
print ('gbest fitness   : ', gbest.fitness)
print ('gbest params    : ', gbest.params)
print ('iterations      : ', i+1)