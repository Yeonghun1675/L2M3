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
    }, ...
]
"""


pore_volume = """
"pore volume": [
    {
        "probe": "", ex) N2, H2
        "value": "",
        "unit": "",
    }, ...
]
"""


crystal_size = """
"crystal size": [
    {
        "value": "",
        "unit": "",  # ex) mm
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
    }, ...
]
"""


porosity = """
"porosity(void fraction)": [
    {
        "value": "",
        "unit": "",
    }, ...
]
"""


pore_diameter = """
"pore diameter": [
    {
        "value": "",
        "unit": "",
    }, ...
]
"""


crystal_system = """
"crystal system": [
    {
        "value": "",  # ex) Triclinic
    }, ...
]
"""


space_group = """
"space group": [
    {
        "value": "",  # ex) P1
    }, ...
]
"""


chemical_formula_weight = """
"chemical formula weight": [
    {
        "value": "",
        "unit": ""
    }, ...
]
"""

decomposition_temperature = """
"decomposition temperature": [
    {
        "value": "",
        "unit": "",
        "type": ""

    }, ...
]
"""

heat_capacity = """
"heat capacity": [
    {
        "value": "",
        "unit": ""
    }, ...
]
"""

thermal_expansion_coefficient = """
"thermal expansion coefficient": [
    {
        "value": "",
        "unit": ""
    }, ...
]
"""

thermal_conductivity = """
"thermal conductivity": [
    {
        "value": "",
        "unit": ""
    }, ...
]
"""

youngs_modulus = """
"Young's modulus": [
    {
        "value": "",
        "unit": ""
    }, ...
]
"""

bulk_modulus = """
"bulk modulus": [
    {
        "value": "",
        "unit": ""
    }, ...
]
"""

shear_modulus = """
"shear modulus": [
    {
        "value": "",
        "unit": ""
    }, ...
]
"""

poissons_ratio = """
"Poisson's ratio": [
    {
        "value": "",

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
        "value":"",
        "unit":"",
        "time":""
    }, ...
]
"""


density = """
"density": [
    {
        "value":"",
        "unit":""  # ex) g/cm^3
    }, ...
]
"""

magnetic_moment = """
"magnetic moment": [
    {
        "value":"",
        "unit":"",
        "temperature":""
    }, ...
]
"""

magnetic_susceptibility = """
"magnetic susceptibility": [
    {
        "value":"",
        "unit":"",
        "temperature":""
    }, ...
]
"""


refractive_index = """
"refractive index": [
    {
        "value":""
    }, ...
]
"""

spectrum = """
"spectrum": [
    {
        "value":"",
        "unit":""
    }, ...
]
"""

cell_volume = """
"cell volume": [
    {
        "value":"",
        "unit":""  # ex) Å^3
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
        }
    }, ...
]
"""

topology = """
"topology" : [
    {
        "value":"", # ex) pcu
    }, ...
]
"""


material_color = """
"material color": [
    {
        "value":"",
        "type":""
    }, ...
]
"""


etc = """
"etc": [
    {
        "property name":"",
        "value":"",
        "unit":"",
        "condition":"",
    }, ...
]
"""

equation = """
"equation": [
    {
        "value":"",
        "parameters":"",
        "name":""
    }
]
"""

charge_related = """
"charge_related": [
    {
        "value":"",
        "unit":"",
        "type":""
    }
]

"""

parameters = """
"parameters": [
    {
        "symbol":"",
        "value":"",
        "unit":"",
        "type":""
    }

]
"""

energy_related = """
"energy_related": [
    {
        "value":"",
        "unit":"",
        "type":""
    }
]
"""