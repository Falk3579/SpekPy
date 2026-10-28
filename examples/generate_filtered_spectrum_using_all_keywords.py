# For compatibility with Python2

import spekpy as sp

print("\n**Script to generate a filtered spectrum specifying all keywords and print summary of metrics **\n")

kvp = 90 # Tube potential in kV (default: 100)
th = 14 # Anode angle in degrees (default: 12)
dk = 1.0 # Spectrum bin width in keV (default: 0.5)
physics = "legacy" # Legacy physics mode rather than default (default: "default")
mu_data_source = "pene" # Penelope mu/mu_en data rather than NIST/XCOM (default: "nist")
z = 75 # Point-of-interest is at a focus-to-detector-distance of 75 cm (default: 100)
x = 5 # Point-of-interest displaced 5 cm towards cathode in anode-cathode direction (default: 0)
y = -5 # Point-of-interest displaced -5 cm in orthogonal direction (right-hand-rule is applicable) (default: 0)

mas = 2 # Exposure set to 2 mAs (default: 1)
brem = True # Whether the bremsstrahlung portion of spectrum is retained (default: True)
char = False # Whether the characteristic portion of spectrum is retained (default: True)
obli = False # Whether path-length through extrinsic filtration varies with x, y (default: True)

# Generate unfiltered spectrum
s = sp.Spek(kvp=kvp, th=th, dk=dk, physics=physics, mu_data_source=mu_data_source,
    x=x, y=y, z=z, mas=mas, brem=brem, char=char, obli=obli)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)
# Print full summary of spectrum metrics
s.summarize(mode='full')
