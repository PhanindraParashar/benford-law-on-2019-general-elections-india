import numpy as np
import scipy
from scipy.stats import t
import pandas as pd
import matplotlib.pyplot as plt

cv = [287,128,127]
tn = [306,132,104]
zpd = [292,136,114]
rjb = [305,124,113]
abp = [267,127,140]
inp = [298,118,126]

ndt = [300,127,115]
nnx = [242,164,136]




A = [cv,tn,zpd,rjb,abp,inp,ndt,nnx]

nda = []
upa = []
oth = []
for i in A:
    nda.append(i[0])
    upa.append(i[1])
    oth.append(i[2])


#rv = t(df=5, loc=0, scale=1)
#x = np.linspace(rv.ppf(0.0001), rv.ppf(0.9999), 100)
#y = rv.pdf(x) 
#
#plt.xlim(-5,5)
#plt.plot(x,y)


#x = np.arange(-5,5,.01)
#td = t.pdf(x,7)
#
#plt.plot(x,td)

nc = nda.copy()
nc.sort()

uc = upa.copy()
uc.sort()

oc = oth.copy()
oc.sort()


x = np.array([0,1,2,3,4,5,6,7])
yn = np.array(nda)
yu = np.array(upa)
yo = np.array(oth)

plt.scatter(x,yu)

