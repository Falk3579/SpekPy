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
# Get energy values array and differential fluence arrays (return values at bin-edges)
karr1, spkarr1 = s.get_spectrum(edges=True)
# Get energy values array and differential energy fluence arrays (return values at bin-edges)
karr2, spkarr2 = s.get_spectrum(edges=True,flu=False)
# Get energy values array and fluence arrays (return values at bin-edges)
karr3, spkarr3 = s.get_spectrum(edges=True,diff=False)
# Plot spectra (different ways of plotting the same thing)
fig1, axs1 = plt.subplots()
fig2, axs2 = plt.subplots()
fig3, axs3 = plt.subplots()
axs1.set_title('Differential fluence spectrum (default)')
axs2.set_title('Differential energy fluence spectrum (flu=False)')
axs3.set_title('Fluence spectrum (diff=False)')
axs1.plot(karr1, spkarr1)
axs1.set(xlabel='Energy [keV]',ylabel='Fluence / mAs / unit energy [photons/cm2/mAs/keV]')
axs2.plot(karr2, spkarr2)
axs2.set(xlabel='Energy [keV]',ylabel='Energy fluence / mAs / unit energy [photons/cm2/mAs]')
axs3.plot(karr3, spkarr3)
axs3.set(xlabel='Energy [keV]',ylabel='Fluence / mAs [photons/cm2/mAs]')

plt.show()
