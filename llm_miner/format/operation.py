atomic_layer_deposition="""
atomic layer deposition: {
"energy type":"",
"precursor name":"",
"precursor amount":"",
"precursor temperature":"",
"precursor bubbler":"",
"reactant name":"",
"reactant amount":"",
"reactant temperature":"",
"reactant bubbler":"",
"carrier gas name":"",
"carrier gas flow rate":"",
"carrier gas purity":"",
"purge gas name":"",
"purge gas flow rate":"",
"purge gas purity":"",
"purge time":"",
"feeding time":"",
"cycle time":"",
"cycle number":"",
"substrate temperature":"",
"working pressure":"",
"base pressure":"",
"growth per cycle":""
}
"""
atomic_layer_etching="""
atomic layer etching: {
"energy type":"",
"precursor name":"",
"precursor amount":"",
"precursor temperature":"",
"precursor bubbler":"",
"reactant name":"",
"reactant amount":"",
"reactant temperature":"",
"reactant bubbler":"",
"carrier gas name":"",
"carrier gas flow rate":"",
"carrier gas purity":"",
"purge gas name":"",
"purge gas flow rate":"",
"purge gas purity":"",
"purge time":"",
"feeding time":"",
"cycle time":"",
"cycle number":"",
"substrate temperature":"",
"working pressure":"",
"base pressure":"",
"etch per cycle":""
}
"""
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
blade_coating="""
blade coating: {
"coating material":"",
"substrate":"",
"gap":"",
"substrate speed":""
}
"""
bulk_metal_forming="""
bulk metal forming: {
"metal forming type":"",
"heating rate":"",
"forming force":"",
"forming temperature":"",
"reduction ratio":"",
"pass number":"",
"cooling rate":"",
"cooling method":""
}
"""
centrifugation="""
centrifugation: {
"revolution per time":"",
"relative centrifugal force":"",
"time":"",
"temperature":"",
"additive name":"",
"additive amount":"",
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
"precursor name":"",
"precursor amount":"",
"pressure":"",
"temperature":"",
"atmosphere":"",
"rpm":""
}
"""
chemical_synthesis="""
chemical synthesis: {
"precursor name":"",
"precursor amount":"",
"solution":"",
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
"precursor":"",
}
"""
directed_energy_deposition="""
directed energy deposition: {
"DED type":"",
"laser power":"",
"travel speed":"",
"working distance":"",
"substrate temperature":""
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
e_beam_lithography="""
e-beam lithography: {
"acceleration voltage":"",
"e-beam resist name":"",
"baking temperature":"",
"baking time":"",
"thickness":"",
"working distance":"",
"beam current":"",
"dwell time":"",
"step size":"",
"line spacing":"",
"area dose":"",
"developer":"",
"develop time":""
}
"""
electrochemical_deposition="""
electrochemical deposition: {
"precursor name":"",
"precursor amount":"",
"solvent":"",
"concentration":"",
"pH":"",
"additive":"",
"working electrode":"",
"counter electrode":"",
"reference electrode":"",
"deposition condition mode":"",
"voltage":"",
"stirring":"",
"temperature":"",
"atmosphere":"",
"time":""
}
"""
electrospinning="""
electrospinning: {
"type":"",
"solute precursor name":"",
"solute precursor amount":"",
"solvent precursor name":"",
"solvent precursor amount":"",
"concentration":"",
"tip size[inner diameter]":"",
"tip size[outer diameter]":"",
"collector":"",
"rotating speed":"",
"collector diameter":"",
"tip to collector distance":"",
"applied voltage":"",
"injection rate":"",
"relative humidity":"",
"temperature":""
}
"""
electrical_polinge="""
electrical poling: {
"time":"",
"applied voltage":"",
"atmosphere":"",
"temperature":"",
"corona needle":"",
"needle to sample distance":"",
"direct current poling":""
}
"""
casting="""
casting: {
"type":"",
"pouring temperature":"",
"mold temperature":"",
"pouring speed":"",
"cooling rate":"",
"solidification time":""
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
"precursor name":"",
"precursor amount":"",
"solution name":"",
"solution amount":"",
"temperature":"",
"atmosphere":"",
"time":""
}
"""
mixing="""
mixing: {
"type":"",
"material mix":"",
"solvent name":"",
"solvent amount":"",
"rotation speed":"",
"temperature":"",
"time":""
}
"""
molecular_beam_epitaxy="""
molecular beam epitaxy: {
"source name":"",
"source amount":"",
"substrate temperature":"",
"substrate orientation":"",
"substrate rotation rate":"",
"growth chamber pressure":"",
"source flux":"",
"growth rate":"",
"growth time":"",
"growth interruption time":""
}
"""
polishing="""
polishing: {
"method":"",
"medium":"",
"load":"",
"material removal rate":"",
"contact stress":"",
"relative velocity":"",
"Preston"s coefficient":"",
"temperature":"",
"atmosphere":"",
"rpm":""
}
"""
powder_bed_fusion="""
powder bed fusion: {
"PBF heat source":"",
"laser power":"",
"layer thickness":"",
"scan speed":"",
"hatch spacing":""
}
"""
pulsed_laser_deposition="""
pulsed laser deposition: {
"laser source":"",
"wavelength":"",
"frequency":"",
"fluence":"",
"angle":"",
"rotation speed":"",
"axis":"",
"substrate temperature":"",
"working pressure":"",
"base pressure":"",
"atmosphere":"",
"time":"",
"atmosphere name":"",
"atmosphere pressure":"",
"target-substrate distance":"",
"lens-target distance":""
}
"""
rinsing="""
rinsing: {
"temperature":"",
"time":"",
"additive name":"",
"additive amount":""
}
"""
pressing="""
pressing: {
"type":"",
"temperature":"",
"pressure":"",
"time":""
}
"""
sintering="""
sintering: {
"atmosphere":"",
"time":"",
"heating rate":"",
"cooling rate":"",
"pressure applied":""
}
"""

slurry_casting = """ {
"type":"",
"material mix":"",
"solvent name":"",
"solvent amount":"",
"rotation speed":"",
"temperature":"",
"humidity":"",
"time":""
}
"""
slot_coating = """
slot coating: {
"pump revolution":"",
"gap":"",
"substrate speed":""
}
"""
solvothermal_synthesis="""
solvothermal synthesis: {
"precursor name":"",
"precursor amount":"",
"solvent name":"",
"solvent amount":"",
"reducing agent name":"",
"reducing agent amount":"",
"surfactant name":"",
"surfactant amount":"",
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
"precursor name":"",
"precursor amount":"",
"solvent name":"",
"solvent amount":"",
"temperature":"",
"ultrasonic frequency":"",
"power":"",
"time":""
}
"""
spin_coating="""
spin coating: {
"precursor name":"",
"precursor amount":"",
"temperature":"",
"atmosphere":"",
"time":"",
"rpm":""
}
"""
spray_pyrolysis="""
spray pyrolysis: {
"precursor name":"",
"precursor amount":"",
"solvent name":"",
"solvent amount":"",
"droplet size":"",
"spray speed":"",
"flame temperature":"",
"heat treatment time":""
}
"""
sputter_deposition="""
sputter deposition: {
"base pressure":"",
"working pressure":"",
"sputtering gas":"",
"substrate distance":"",
"target":"",
"sputter power":"",
"power source type":"",
"time":"",
"substrate temperature":"",
"substrate rotation":""
}
"""
thermal_evaporation="""
thermal evaporation: {
"precursor name":"",
"precursor amount":"",
"working pressure":"",
"substrate temperature":"",
"deposition rate":"",
"time":""
}
"""
thermomechanical_process="""
thermomechanical process: {
"atmosphere":"",
"initial temperature":"",
"heating rate":"",
"holding temperature":"",
"deformation holding":"",
"holding time":"",
"cooling rate":"",
"deformation cooling":"",
"cooling method":"",
"final temperature":""
}
"""
transporting="""
transporting: {
"pump revolution":"",
"pipe material":"",
"pipe diamter":"",
"temperature":"",
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