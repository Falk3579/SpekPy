# For compatibility with Python2

import spekpy as sp

print("\n**Script to generate a filtered spectrum normalized to a reference air kerma **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)
print('* Unnormalized air kerma values *')
print('Air Kerma at (x,y,z)=(0 cm, 0 cm, 100 cm):',s.get_kerma(),'uGy')
print('Air Kerma at (x,y,z)=(10 cm, 0 cm, 100 cm):',s.get_kerma(x=10),'uGy')
print()
# See air kerma at reference point and at 10 cm displaced in anode-cathode direction
print('* Air kerma values after normalization to reference point *')
s.set(ref_kerma=100)
print('Air Kerma at (x,y,z)=(0 cm, 0 cm, 100 cm):',s.get_kerma(),'uGy')
print('Air Kerma at (x,y,z)=(10 cm, 0 cm, 100 cm):',s.get_kerma(x=10),'uGy')
print()
print('* Air kerma values after setting new reference point (defaults to unnormalized) *')
s.set(x=10)
print('Air Kerma at (x,y,z)=(0 cm, 0 cm, 100 cm):',s.get_kerma(x=0),'uGy')
print('Air Kerma at (x,y,z)=(10 cm, 0 cm, 100 cm):',s.get_kerma(),'uGy')
print()
print('* Air kerma values after normalization to new reference point *')
s.set(ref_kerma=100)
print('Air Kerma at (x,y,z)=(0 cm, 0 cm, 100 cm):',s.get_kerma(x=0),'uGy')
print('Air Kerma at (x,y,z)=(10 cm, 0 cm, 100 cm):',s.get_kerma(),'uGy')
print()
