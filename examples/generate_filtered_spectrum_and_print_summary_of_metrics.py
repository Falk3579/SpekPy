# For compatibility with Python2

import spekpy as sp

print("\n**Script to generate a filtered spectrum and print summary statistics to screen **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)
# Print full summary of spectrum metrics
s.summarize(mode='full')

