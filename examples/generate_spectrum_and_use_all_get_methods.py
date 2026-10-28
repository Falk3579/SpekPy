# For compatibility with Python2

import spekpy as sp

print("\n**Script to generate a filtered spectrum and print summary statistics to screen **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0)
# Mutli-filter the spectrum
added_filtration=[ ['Al',4.0], ['Air',1000] ]
s.multi_filter(added_filtration)
# Using all the get methods
print('Energy bins:', s.get_k(), 'keV')
print()
print('Fluences:', s.get_spk(), '# per keV')
print()
print('Energy bins and fluences:',s.get_spectrum())
print()
print('Air kerma:', s.get_kerma(), 'uGy')
print()
print('1st Hvl:', s.get_hvl1(), 'mmAl')
print()
print('2nd Hvl:', s.get_hvl2(), 'mmAl')
print()
print('Homogeneity coefficient (Al):', s.get_hc())
print()
print('Thickness of Al that gives a 75% drop in air kerma:', s.get_matl(frac=0.25))
print()
print('1st Hvl:', s.get_hvl1(matl='Cu'), 'mmCu')
print()
print('2nd Hvl:', s.get_hvl2(matl='Cu'), 'mmCu')
print()
print('Homogeneity coefficient (Cu):', s.get_hc(matl='Cu'))
print()
print('Thickness of Cu that gives a 75% drop in air kerma:', s.get_matl(frac=0.25,matl='Cu'))
print()
print('Mean energy of spectrum:', s.get_emean(), 'keV')
print()
print('Effective energy of spectrum (Al):', s.get_eeff(), 'keV')
print()
print('Effective energy of spectrum (Cu):', s.get_eeff(matl='Cu'), 'keV')
print()
print('Integrated fluence:', s.get_flu(), '#')
print()
print('Integrated energy fluence:', s.get_eflu(), 'keV')
print()
print('Kerma normalized fluence:', s.get_norm_flu(), '# per uGy')
print()
print('All standard results in one call:')
std_results=s.get_std_results() # Returns a class instance
for name in dir(std_results):
    if name[0:2] != '__':
        print(name,':', getattr(std_results,name))

