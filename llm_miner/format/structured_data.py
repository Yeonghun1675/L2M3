meta = '''
'meta': {
    'name': "",
    'symbol': "",  # ex) 1a
    'chemical formula': "",
}
'''


surface_area = '''
'surface area': [
    {
        'type': "",  # BET or Langmuir
        'value': "",
        'unit': "",
    }, ...
]
'''


pore_volume = '''
'total pore volume': [
    {
        'value': "",
        'unit': "",
    }, ...
]
'''


crystal_size = '''
'crystal size': [
    {
        'value': "",
        'unit': "",  # ex) mm
    }, ...
]
'''


gas_adsorption = '''
'gas adsorption': [
    {
        'adsorbate': "",
        'adsorbed amount': "",
        'unit': "",
        'temperature': "",
        'pressure': "",
    }, ...
]
'''


porosity = '''
'porosity(void fraction)': [
    {
        'value': "",
        'unit': "",
    }, ...
]
'''


pore_diameter = '''
'pore diameter': [
    {
        'value': "",
        'unit': "",
    }, ...
]
'''


crystal_system = '''
'crystal system': [
    {
        'value': "",  # ex) Triclinic
    }, ...
]
'''


space_group = '''
'space group': [
    {
        'value': "",  # ex) P1
    }, ...
]
'''


chemical_formula_weight = '''
'chemical formula weight': [
    {
        'value': "",
    }, ...
]
'''


thermal_property = '''
'thermal property': [
    {
        'type': "",
        'value':"",
        'unit':""
    }, ...
]
'''


mechanical_property = '''
'mechanical property': [
    {
        'type': "",  # ex) Young's modulus, Poisson's ratio
        'value':"",
        'unit':""
    }, ...
]
'''


selectivity = '''
'selectivity': [
    {
        'value':"",
        'adsorbate':"",
        'pressure':"",
        'temperature':""
    }, ...
]
'''


catalytic_activity = '''
'catalytic activity': [
    {
        'value':"",
        'unit':""
    }, ...
]
'''


density = '''
'density': [
    {
        'value':"",
        'unit':""  # ex) g/cm^3
    }, ...
]
'''


magnetic_property = '''
'magnetic property': [
    {
        'type': "",
        'value':"",
        'unit':""
    }, ...
]
'''


optical_property = '''
'optical property': [
    {
        'type': "",  # ex) absorption spectrum
        'value':"",
        'unit':""
    }, ...
]
'''


cell_volume = '''
'cell volume': [
    {
        'value':"",
        'unit':""  # ex) Å^3
    }, ...
]
'''


lattice_parameters = '''
'lattice parameters': [
    {
        'value': {
            'a': "",
            'b': "",
            'c': "",
            'alpha': "",
            'beta': "",
            'gamma': "",
        }
    }, ...
]
'''


etc = '''
'etc': [
    {
        "property name": "",
        'value':"",
        'unit':"",
        'conditon': "",
    }, ...
]
'''
