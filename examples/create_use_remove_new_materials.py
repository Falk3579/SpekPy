# For compatibility with Python2

import spekpy as sp

print("\n** Script to create use and remove new materials **\n")

# Generate filtered spectrum
s=sp.Spek(kvp=120,th=12).filter('Al',2.5)

# List all materials
sp.Spek.show_matls()
print()
# List only ICRU materials
sp.Spek.show_matls(matl_group='ICRU')

# Create a new material using weights
material_name = 'Wood, White Oak'
comment = 'PIET-43741-TM-963 PNNL-15870 Rev. 1 (http://www.pnnl.gov/main/publications/external/technical_reports/pnnl-15870rev1.pdf)'
material_density = 0.77
material_composition = [(1, 0.059642), (6, 0.497018), (7, 0.004970), (8, 0.427435), (12, 0.001988), (16, 0.004970), (19, 0.001988), (20, 0.001988)]
sp.Spek.make_matl(matl_name=material_name, matl_density=material_density, wt_matl_comp=material_composition, matl_comment=comment)
print()
# See new material composition
sp.Spek.show_matls(material_name)
print()
# Get HVL of the new material
print(material_name,'; HVL:',s.get_hvl1(matl=material_name),'mm')
print()

# Create a new water material using a chemical formula
another_material = 'Water (body temperature)'
sp.Spek.make_matl(matl_name=another_material, matl_density=0.992, chemical_formula='H2O')
# See new water material composition
sp.Spek.show_matls(another_material)

# See default water material composition
sp.Spek.show_matls('Water, Liquid')
# Print HVL of the new water material
print(another_material, '; HVL:',s.get_hvl1(matl=another_material), 'mm')
# Print HVL of the default water material
print('Water, Liquid', '; HVL:',s.get_hvl1(matl='Water, Liquid'), 'mm')
print()

# List all materials in user directory
sp.Spek.show_matls(matl_dir="usr")
# Delete the new water material
sp.Spek.remove_matl(matl_name=another_material)
# List all materials in user directory
sp.Spek.show_matls(matl_dir="usr")
