# For compatibility with Python2

import spekpy as sp

print("\n** Script to import an external spectrum and print summary statistics **\n")

spek_name = 'Demo_export_spectrum.spk'

# Generate filtered spectrum
s=sp.Spek().filter('Al',2.5)
# Export spectrum
s.export_spectrum(spek_name)
# Import external spectrum
delim=';'
z_ext=100
mas_ext=1
e = sp.Spek.load_from_file(spek_name, delim, z=z_ext, mas=mas_ext)
# Summarize full statistics
e.summarize(mode='full')



