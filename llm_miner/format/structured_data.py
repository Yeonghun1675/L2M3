meta = """
"meta": {
    "name": "",
    "symbol": "",  # ex) 1a
    "chemical formula": "",
}
"""


surface_area = """
"surface area": [
    {
        "type": "",  # ex) BET, Langmuir
        "probe": "",
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""


pore_volume = """
"pore volume": [
    {
        "probe": "", ex) N2, H2
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""


crystal_size = """
"crystal size": [
    {
        "value": "",
        "unit": "",  # ex) mm
        "condition": "",
    }, ...
]
"""


gas_adsorption = """
"gas adsorption": [
    {
        "adsorbate": "",
        "adsorbed amount": "",
        "unit": "",
        "temperature": "",
        "pressure": "",
        "condition": "",
    }, ...
]
"""


porosity = """
"porosity": [
    {
        "proboe": "",
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""


pore_diameter = """
"pore diameter": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""


crystal_system = """
"crystal system": [
    {
        "value": "",  # ex) Triclinic
        "condition": "",
    }, ...
]
"""


space_group = """
"space group": [
    {
        "value": "",  # ex) P1
        "condition": "",
    }, ...
]
"""


chemical_formula_weight = """
"chemical formula weight": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

decomposition_temperature = """
"decomposition temperature": [
    {
        "value": "",
        "unit": "",
        "type": "",  # ex) lattice collapse, weight loss, departure of water molecules, etc.
        "condition": "",
    }, ...
]
"""

heat_capacity = """
"heat capacity": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

thermal_expansion_coefficient = """
"thermal expansion coefficient": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

thermal_conductivity_coefficient = """
"thermal conductivity_coefficient": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

youngs_modulus = """
"Young's modulus": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

bulk_modulus = """
"bulk modulus": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

shear_modulus = """
"shear modulus": [
    {
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

poissons_ratio = """
"Poisson's ratio": [
    {
        "value": "",
        "condition": "",
    }, ...
]
"""

selectivity = """
"selectivity": [
    {
        "value": "",
        "unit": "",
        "substrate": "",
        "catalyst": "",
        "pressure":"",
        "temperature":""
        "solvent": "",
        "time": "",
    }, ...
]
"""

conversion = """
"conversion": [
    {
        "value": "",
        "unit": "",
        "substrate": "",
        "catalyst": "",
        "pressure":"",
        "temperature":""
        "solvent": "",
        "time": "",
    }, ...
]
"""

reaction_yield = """
"yield": [
    {
        "value": "",
        "unit": "",
        "substrate": "",
        "catalyst": "",
        "pressure": "",
        "temperature": "",
        "solvent": "",
        "time": "",
    }, ...
]
"""


catalytic_activity = """
"catalytic activity": [
    {
        "value": "",
        "unit": "",
        "time": "",
        "condition": "",
    }, ...
]
"""


density = """
"density": [
    {
        "value": "",
        "unit": "",  # ex) g/cm^3
        "condition": "",
    }, ...
]
"""

magnetic_moment = """
"magnetic moment": [
    {
        "value":"",
        "unit":"",
        "temperature":"",
        "condition": "",
    }, ...
]
"""

magnetic_susceptibility = """
"magnetic susceptibility": [
    {
        "value": "",
        "unit": "",
        "temperature": "",
        "condition": "",
    }, ...
]
"""


peak_spectrum = """
"peak spectrum": [
    {
        "value": "",
        "unit": "",
        "type": "",
    }, ...
]
"""

cell_volume = """
"cell volume": [
    {
        "value": "",
        "unit": "",  # ex) Å^3
        "condition": "",
    }, ...
]
"""


lattice_parameters = """
"lattice parameters": [
    {
        "value": {
            "a": "",
            "b": "",
            "c": "",
            "alpha": "",
            "beta": "",
            "gamma": "",
        "condition": "",
        }
    }, ...
]
"""

topology = """
"topology" : [
    {
        "value": "", # ex) pcu
        "condition": "",
    }, ...
]
"""


material_color = """
"material color": [
    {
        "value": "",
        "condition": "",
    }, ...
]
"""


material_shape = """
"material shape": [
    {
        "value": "",
        "condition": "",
    }, ...
]
"""

simulation_parameters = """
"simulation parameters": [
    {
        "symbol": "",  # ex) σ
        "value": "",
        "unit": "",
        "type": "",  # lennard-jones potential
    }, ...

]
"""

etc = """
"etc": [
    {
        "property name": "",
        "value": "",
        "unit": "",
        "condition": "",
    }, ...
]
"""

proton_conductivity = """
"proton_conductivity": [
    {
        "value": "",
        "value unit": "",
        "temperature": "",
        "temperature unit": "",
        "RH": "",
        "name": "",
        "Ea": "",
        "guest": "",
    }, ...
]
"""