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
"total pore volume": [
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
    }, ...
]
"""


thermal_property = """
"thermal property": [
    {
        "type": "", # ex) Tg, TDT
        "value":"",
        "unit":""
    }, ...
]
"""


mechanical_property = """
"mechanical property": [
    {
        "type": "",  # ex) Young's modulus, Poisson's ratio
        "value":"",
        "unit":""
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
        "unit":""
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


magnetic_property = """
"magnetic property": [
    {
        "type": "", # ex) magnetic susceptibility
        "value":"",
        "unit":""
    }, ...
]
"""


optical_property = """
"optical property": [
    {
        "type": "",  # ex) absorption spectrum
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

etc = """
"etc": [
    {
        "property name": "",
        "value":"",
        "unit":"",
        "conditon": "",
    }, ...
]
"""
