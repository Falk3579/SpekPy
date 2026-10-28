# For compatibility with Python2

import numpy as np

import spekpy as sp

try:
    from matplotlib import pyplot as plt
except:
    print("Cannot import matplotlib. Please check that it is installed")
print("\n**Script to generate a filtered spectrum and plot line profile of air kerma using matplotlib **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)

n=201
xarr=np.zeros([n])
darr=np.zeros([n])
for i in range(n):
  x=-10.0+0.1*float(i)
  xarr[i]=x
  darr[i]=s.get_kerma(x=x)

plt.plot(xarr, darr)
plt.xlabel('x [cm]')
plt.ylabel('Air kerma @ 1 m per mAs [uGy]')
plt.title('A line profile of air kerma')
plt.suptitle('Anode heel-effect, r-sq effect and path-length (in filter) included', y = 0.16, x= 0.53, fontsize=10)
plt.show()
