# For compatibility with Python2

import numpy as np

import spekpy as sp

print("\n**Script to clone a spectrum **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)
# Clone (creat a deep copy of) the spectrum
t=sp.Spek.clone(s)
t.filter('Al',4.0)
# Print full summary of spectrum metrics
print('Cloned (then filtered) hvl:',t.get_hvl1())
print()
print('Original spectrum hvl:',s.get_hvl1())
print()
if not np.isclose(s.get_hvl1(),t.get_hvl1()):
    print('As expected, filtering the cloned spectrum does not affect the original spectrum')
else:
    print('Something has gone wrong here ... the two HVLs should be different')
print()

