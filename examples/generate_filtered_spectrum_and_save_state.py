# For compatibility with Python2

import spekpy as sp

print("\n** Script to generate a filtered spectrum and save the state to disk **\n")

# Generate unfiltered spectrum
s=sp.Spek(kvp=120,th=12)
# Filter the spectrum
s.filter('Be',1.0).filter('Al',4.0).filter('Air',1000)

# Save the state to disk
save_name = 'demo_save_state'
s.save_state(file_name=save_name)

