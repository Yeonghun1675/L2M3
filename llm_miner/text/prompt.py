PROMPT_TYPE = """First, determine whether properties exist or not. Except for topology, crystal system, and space group, properties must have a float value. If a property does not have float value, do not extract it. If there is no property in the paragraph, please return an empty list.
If properties exist, you must find all the properties in paragraphs. Names of properties must be one of following:
{explanation}

You must follow below rules:
- Avoid including the same property multiple times. If there are surface_area and BET surface_area in the paragraph at the same time, you must include "surface_area" once.
- You must include only the properties, excluding the names of materials.
- If a property you find lacks a value, please exclude it.
- Do not be confused between gas adsorption and selectivity. Gas adsorption is a property that has a unit and selectivity is unitless. Even though there is a word "selectivity", it is not always selectivity. If there is a value with unit, it is gas adsorption.
- In crystal system, there are triclinic, monoclinic, orthorhombic, tetragonal, trigonal, hexagonal, and cubic. If one of them exists in the paragraph, it means there is "crystal system" information.
- If "TGA" or "TG" exists in the paragraph, it includes "decomposition_temperature".
- When property does not exist in the list, write "etc".

If you are uncertain, please reply with "I do not know".

Begin!

Paragraph: MOF-A exhibits a surface area of 1500 m2/g and a pore volume of 0.9 cm3/g. Another notable MOF, MOF-C, possesses a surface_area of 4000 m2/g and a pore volume of 1.5 cm3/g.
List: ```JSON
["surface_area", "pore_volume"]
```

Paragraph: MOF-C shows exceptional hydrogen storage capacity, with an uptake of 7.5 wt% at 77 K and 1 bar.
List: ```JSON
["gas_adsorption"]
```

Paragraph: The MOF-D exhibits intriguing magnetic properties, displaying a high magnetic moment of 4.8 μB per Fe atom at room temperature.
List: ```JSON
["magnetic_moment"]
```

Paragraph: The MOF material MOF-H demonstrated exceptional guest molecule selectivity, exhibiting a high adsorption preference for CO2 over N2. Moreover, MOF-I achieved a high turnover frequency (TOF) of 1000 h-1.
List: ```JSON
["catalytic_activity"]
```

Paragraph: MOF-A displays a dielectric constant of approximately 4.5 at 1 kHz, making it suitable for applications in electronics and capacitive devices.
List: ```JSON
["etc"]
```

Paragraph: An intense emission occurs at 407nm with the excitation wavelength at 318nm.
List: ```JSON
["peak_spectrum"]
```

Paragraph: In the case of 2, during the entire decomposition process up to 550°C, the residual material observed at the end comprises approximately 22.3% of the original sample, possibly indicating a mixture of ZrO2 and ZrC (calculated 23.8%).
List: ```JSON
["decomposition_temperature"]
```

Paragraph: MOF-A exhibits (4,4)-connected 3D frameworks with a Schläfli symbol of 42638.
List: ```JSON
["topology"]
```

Paragraph: The Co(II) compound exhibits a χ_MT product of 3.87 cm^3 mol^−1 K at room temperature, which closely matches the expected value of 3.90 cm^3 mol^−1 K, affirming the suitability of the free-ion approximation to explain its magnetic behavior
List: ```JSON
["magnetic_susceptibility"]
```

Paragraph: Crystallographic data for Compound 2: C36H42N6O4, M = 622.75, monoclinic, P21/c, a = 10.812(4) Å, b = 15.261(6) Å, c = 13.973(5) Å, V = 2293.0(14) cm^3, Z = 4, Dc = 1.292 g cm^−3, μ (X-ray) = 1.012 mm^−1, T = 298(2) K, 14056 reflections collected, 3668 unique (Rint = 0.0573), R1 on F(wR2 on F2) = 0.0397 (0.0884) for 3447 observed (I > 2σ(I)) reflections.
List: ```JSON
["chemical_formula_weight", "crystal_system", "space_group", "lattice_parameters", "density"]
```

Paragraph: The calculated solvent-accessible void space within the framework measures 852.8 Å3, representing approximately 38.2% of the unit cell volume of 2230.6 Å3.
List: ```JSON
["porosity"]
```

Paragraph: In summary, we have successfully achieved a high-performance MOF-based proton-conducting material via the facile encapsulation of the imidazole guests within the pores of robust MOF-808 and demonstrated that Im@MOF-808 possesses high proton conductivity with the value of 3.45 × 10−2 S cm−1 (338 K and 99% RH).
List: ```JSON
["proton_conductivity"]
```

Paragraph: {paragraph}
List:"""


PROMPT_EXT = """Extract the information about {prop} mentioned in the paragraph. Follow the structured data in JSON format:
{structured_data}

You must follow below rules:
- You must write all the information about {prop} in the paragraph.
- Do not forge information that is not in the paragraph.
- Do not write the information in the examples.
- When property is "etc", do not extract {prop}.
- Make a list that shows properties of each material. The list consists of several dictionaries of all materials. Each dictionary must include "meta":{{"name":"", "symbol":"", "chemical formula":""}}. ex) [{{"meta":{{"name":"", "symbol":"", "chemical formula":""}}, {structured_data}]
- When material is expressed as a number, you must fill in "symbol" of "meta". ex) Paragraph: The corresponding BET surface area is 100 m2/g for 1. JSON: [{{"meta":{{"name":"", "symbol":"1", "chemical formula":""}}, "surface area": {{"type": "BET", "probe": "", "value": "100", "unit": "m2/g"}}}}]
- "condition" means not only pressure, temperature, but specific details of property like crystal form.

{information} 

If you are uncertain, please reply with "I do not know".

Begin!

{example}

Paragraph: {paragraph}
JSON:
"""

FT_TYPE = (
    "You must decide whether properties exist or not. "
    "Except for topology, crystal system, and space group, property must have a float value. "
    "If there is no property in the paragraph, please return an empty list. "
    "You must find all the properties in the paragraphs. "
    "Names of properties must be one of following:\n"
    "['adsorption_energy', 'catalytic_activity', 'chemical_formula_weight', 'crystal_size', 'crystal_system', 'decomposition_temperature', 'density', 'elastic_constant', 'formation_energy', 'gas_adsorption', 'heat_capacity', 'henry_coefficient', 'lattice_parameters', 'magnetic_moment', 'magnetic_susceptibility', 'material_color', 'material_shape', 'simulation_parameters', 'pore_diameter', 'pore_volume', 'porosity', 'selectivity', 'space_group', 'peak_spectrum', 'surface_area', 'thermal_conductivity_coefficient', 'thermal_expansion_coefficient', 'topology', 'etc', 'proton_conductivity']"
)

FT_HUMAN = "{paragraph}"
