# For compatibility with Python2

import spekpy as sp

try:
    from matplotlib import pyplot as plt
except:
    print("Cannot import matplotlib. Please check that it is installed")
print("\n** Script to generate a filtered spectrum and plot using matplotlib **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)
# Get energy values array and fluence arrays (return values at bin-edges)
karr, spkarr = s.get_spectrum(edges=True)
# Plot spectrum
plt.plot(karr, spkarr)
plt.xlabel('Energy [keV]')
plt.ylabel('Fluence per mAs per unit energy [photons/cm2/mAs/keV]')
plt.title('An example x-ray spectrum')
plt.show()
