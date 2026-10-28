# For compatibility with Python2

import numpy as np

import spekpy as sp

print("\n** Script to generate the NIST M150 spectrum filtered to match the NIST reference HVL **\n")

print("Reference hvl:", 10.3, "mmAl")

# Generate unfiltered spectrum
s=sp.Spek(kvp=150,th=20)
# Apply base filtering
s.filter('Be',3.0).filter('Al',5.25).filter('Air',966.8)
# Find thickness of copper to add to give specified HVL
tCu=s.get_matl(matl='Cu',hvl_matl='Al',hvl=10.3)

print("Estimated additional filtration:", tCu, "mmCu")

# Apply that thickness Cu filtration
s.filter('Cu',tCu)
# Get the first HVL in mm Al
hvl1=s.get_hvl1(matl='Al')
# Get the thickness of Al that halves air kerma
hvl1check=s.get_matl(matl='Al',frac=0.5)

assert np.isclose(hvl1,hvl1check), \
    "Inconsistancy in get_matll(): frac mode result disagrees with hvl mode"

print("Obtained hvl:", hvl1, "mmAl\n")
