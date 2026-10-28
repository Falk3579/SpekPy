# For compatibility with Python2

import spekpy as sp

print("\n** Script to generate a filtered spectrum and export to a file **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)
# Export (save) spectrum to file
spek_name = 'Demo_export_spectrum.spk'
s.export_spectrum(spek_name, comment='A demo spectrum export')
s.summarize(mode='full')


