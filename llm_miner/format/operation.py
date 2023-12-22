ball_milling="""
ball milling: {
    "material":"",
    "type":"",
    "rotation speed":"",
    "total time":"",
    "milling time":"",
    "rest time":"",
    "ball to material weight ratio":"",
    "material mass":"",
    "solvent":"",
    "ball material":"",
    "ball size":"",
    "jar shape":"",
    "jar volume":"",
    "jar material":"",
    "atmosphere":""
}
"""
centrifugation="""
centrifugation: {
    "revolution per time":"",
    "relative centrifugal force":"",
    "time":"",
    "temperature":"",
    "additive":[{"name":"", "amount":"", "unit":""}, ...],
    "tube material":"",
    "tube volume":""
}
"""
chemical_mechanical_polishing="""
chemical mechanical polishing: {
    "slurry concentration":"",
    "slurry density":"",
    "viscosity":"",
    "polishing rate":"",
    "surface roughness":"",
    "precursor":[{"name":"", "amount":"", "unit":""}, ...],
    "pressure":"",
    "temperature":"",
    "atmosphere":"",
    "rpm":""
}
"""
chemical_synthesis="""
chemical synthesis: {
    "precursor":[{"name":"", "amount":"", "unit":""}, ...],
    "solution":[{"name":"", "amount":"", "unit":""}, ...],
    "pressure":"",
    "temperature":"",
    "time":""
}
"""
chemical_vapor_deposition="""
chemical vapor deposition: {
    "working pressure":"",
    "carrier gas name":"",
    "carrier gas flow rate":"",
    "precursor":[{"name":"", "amount":"", "unit":""}, ...],
}
"""
drying="""
drying: {
    "pressure":"",
    "temperature":"",
    "atmosphere":"",
    "time":""
}
"""
electrochemical_deposition="""
electrochemical deposition: {
    "electrolyte precursor":[{"name":"", "amount":"", "unit":""}, ...],
    "electrolyte solvent":"",
    "electrolyte concentration":"",
    "electrolyte pH":"",
    "additive":"",
    "working electrode":"",
    "counter electrode":"",
    "reference electrode":"",
    "mode":"",
    "voltage":"",
    "current density":"",
    "stirring":"",
    "temperature":"",
    "atmosphere":"",
    "time":""
}
"""
heat_treatment="""
heat treatment: {
    "heat treatment method":"",
    "atmosphere":"",
    "heat treatment temperature":"",
    "heat treatment time":"",
    "heating rate":"",
    "cooling rate":""
}
"""
microwave_assisted_synthesis="""
microwave-assisted synthesis: {
    "precursor":[{"name":"", "amount":"", "unit":""}, ...],
    "solution":[{"name":"", "amount":"", "unit":""}, ...],
    "temperature":"",
    "atmosphere":"",
    "time":""
}
"""
mixing="""
mixing: {
    "type":"",
    "material mix":"",
    "solvent": {"name":"", "amount":"", "unit":""},
    "rotation speed":"",
    "temperature":"",
    "time":""
}
"""
rinsing="""
rinsing: {
    "temperature":"",
    "time":"",
    "additive":[{"name":"", "amount":"", "unit":""}, ...],
}
"""
solvothermal_synthesis="""
solvothermal synthesis: {
    "precursor":[{"name":"", "amount":"", "unit":""}, ...],
    "solvent":[{"name":"", "amount":"", "unit":""}, ...],
    "reducing agent":[{"name":"", "amount":"", "unit":""}, ...],
    "surfactant":[{"name":"", "amount":"", "unit":""}, ...],
    "pressure":"",
    "temperature":"",
    "time":"",
    "heating rate":"",
    "cooling rate":""
}
"""
sol_gel_syntehsis="""
sol-gel syntehsis: {
    "temperature":"",
    "precursor":"",
    "solvent":"",
    "time":""
}
"""
sonication="""
sonication: {
    "composition":"",
    "power":"",
    "solvent":"",
    "temperature":"",
    "time":"",
    "type":""
}
"""
sonochemical_synthesis="""
sonochemical synthesis: {
    "precursor":[{"name":"", "amount":"", "unit":""}, ...],
    "solvent":[{"name":"", "amount":"", "unit":""}, ...],
    "temperature":"",
    "ultrasonic frequency":"",
    "power":"",
    "time":""
}
"""
thermal_evaporation="""
thermal evaporation: {
    "precursor":[{"name":"", "amount":"", "unit":""}, ...],
    "working pressure":"",
    "substrate temperature":"",
    "deposition rate":"",
    "time":""
}
"""
wet_etching="""
wet etching: {
    "temperature":"",
    "etchant":"",
    "concentration":"",
    "solvent":"",
    "additive":"",
    "time":"",
    "stirring rate":""
}
"""
washing="""
washing: {
    "washing solution":"",
    "amount":""
}
"""
cooling="""
cooling: {
    "pressure":"",
    "temperature":"",
    "cooling rate":"",
    "time":""
}
"""
pH_adjustment="""
pH adjustment: {
    "pH":"",
    "modulator":""
}
"""
filtration="""
filtration: {
    "time":"",
    "atmosphere":"",
    "pressure":"",
}
"""
