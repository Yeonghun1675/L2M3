surface_area="""
Paragraph: MOF-A boasts exceptional features such as a pore volume of 1.2 cm3/g, a BET surface area of 1500 m2/g, and an adsorption capacity of 35.6 wt% for CO2 at 25°C and 1 atm. MOF-B showcases its versatility with a pore volume of 0.9 cm3/g, a Langmuir surface area of 1200 m2/g, and an adsorption capacity of 27.8 wt% for N2 at 77 K and 1 atm.
JSON: ```JSON
[{{"probe": "", "type": "BET", "value": "1500", "unit": "m2/g", "condition": ""}}, {{"probe": "", "type": "Langmuir", "value": "1200", "unit": "m2/g", "condition": ""}}]
```
"""

pore_volume="""
Paragraph: MOF-A possesses a pore volume of 0.9 cm3/g, providing ample space for gas adsorption.
JSON: ```JSON
[{{"probe":"", "value":"0.9", "unit":"cm3/g", "condition":""}}]
```
"""

crystal_size="""
Paragraph: MOF-B stands out for its remarkable uniformity in crystal size. The crystal size of MOF-B typically falls in the range of 1 to 5 micrometers.
JSON: ```JSON
[{{"value":"1 to 5", "unit":"micrometers", "condition":""}}]
```

Paragraph: Among the MOFs designed for various applications, MOF-A has attracted attention due to its impressive crystal size and structural versatility. The crystal size of MOF-A, which is formally known as Chromium(III) Terephthalate, spans a wide range from 500 nanometers to several micrometers.
JSON: ```JSON
[{{"value":"500 nanometers to several micrometers", "unit":"", "condition":""}}]
```
"""

gas_adsorption="""
Paragraph: One prominent MOF, MOF-A boasts exceptional features such as an adsorption capacity of 35.6 wt% for CO2 at 25°C and 1 atm. Another remarkable MOF, MOF-B showcases its versatility with an adsorption capacity of 27.8 wt% for N2 at 77 K and 1 atm.
JSON: ```JSON
[{{"adsorbate":"CO2", "adsorbed amount":"35.6", "unit":"wt%", "temperature":"25°C", "pressure":"1 atm", "condition":""}}, {{"adsorbate":"N2", "adsorbed amount":"27.8", "unit":"wt%", "temperature":"77 K", "pressure":"1 atm", "condition":""}}]
```
"""

porosity ="""
Paragraph: MOF-A is a MOF renowned for its high porosity fraction. MOF-A possesses a remarkable porosity fraction of approximately 0.87, indicating that nearly 87% of its structure is composed of voids and pores. This substantial porosity fraction arises from the unique arrangement of its zinc and imidazole-based organic linkers.
JSON: ```JSON
[{{"probe":"", "value":"0.87", "unit":"", "condition":""}}]
```

Paragraph: The calculated solvent-accessible void space within the framework measures 852.8 Å3, representing approximately 38.2% of the unit cell volume of 2230.6 Å3.
JSON: ```JSON
[{{"probe":"", "value":"38.2", "unit":"%", "conditioin":""}}, {{"probe":"", "value":"852.8", "unit":"Å3", "condition":""}}]
```
"""


pore_diameter = """
Paragraph: MOF-A is a well-known MOF that possesses a remarkable pore size. The pores in MOF-A have a diameter of approximately 1.2 nm, which allows for efficient gas adsorption and storage within its porous structure.
JSON:```JSON
[{{"value":"1.2", "unit":"nm", "condition":""}}]
```
"""

crystal_system = """
Paragraph: MOF-A crystallizes in a tetragonal crystal system, which means its unit cell has three edges of equal length and right angles between them.
JSON:```JSON
[{{"value":"tetragonal", "condition":""}}]
```
"""

topology = """
Paragraph :MOF-A exhibits the "primitive cubic net" (PCN) topology, characterized by corner-sharing metal clusters and organic linkers forming a 3D cubic framework. The PCN topology provides numerous open metal sites and accessible pores, making it ideal for gas storage and separation.
JSON:```JSON
[{{"value":"PCN", "condition":""}}]
```
"""

space_group = """
Paragraph: In the field of crystallography, MOF-A is notable for its well-defined structure and crystallographic properties. MOF-A belongs to the Fm-3m space group, indicating a face-centered cubic crystal lattice. The space group value for MOF-A, Fm-3m, signifies its cubic symmetry and high degree of order within its crystalline framework.
JSON:```JSON
[{{"value":"Fm-3m", "condition":""}}]
```
"""

chemical_formula_weight = """
Paragraph: MOF-A is a well-known MOF composed of Zn4O clusters connected by terephthalate (TPA) ligands. The chemical formula weight of the repeating unit in MOF-A is approximately 756.9 g/mol.
JSON:```JSON
[{{"value":"756.9", "unit":"g/mol", "condition":""}}]
```
"""

decomposition_temperature = """
Paragraph: The MOF-A began to thermally decompose at 400 °C, suggesting its stability up to this temperature.
JSON:```JSON
[{{"value":"400", "unit":"°C", "type":"decomposition point", "condition":""}}]
```

Paragraph: MOF-B exhibits remarkable thermal stability, remaining stable up to a temperature of 155°C. A modest weight loss of 4.8% (calculated 4.6%) between 155 and 250°C can be attributed to the removal of coordinated solvent molecules. Beyond this point, the compound undergoes a consecutive weight loss process that persists until heating to 680°C.
JSON:```JSON
[{{"value":"155", "unit":"°C", "type":"stable", "condition":""}}, {{"value":"155 and 250", "unit":"°C", "type":"removal of coordinated solvent molecules", "condition":""}}, {{"value":"680", "unit":"°C", "type":"consecutive weight loss", "condition":""}}]
```

Paragraph: In the case of MOF-A, it was observed that there was an initial weight loss of 7.82% before reaching 120°C, corresponding closely to the departure of guest molecules. Subsequently, a temperature range spanning from 140°C to 280°C was attributed to the gradual removal of coordinated water molecules (experimental: 8.15%; calculated: 7.28%), after which the structure underwent decomposition. 
JSON: ```JSON
[{{"value":"120", "unit":"°C", "type":"an initial weight loss"}}, {{"value":"140 to 280", "unit":"°C", "type":"gradual removal of coordinated water molecules"}}]
```
"""

heat_capacity = """
Paragraph: The specific heat capacity of the MOF-A was measured to be 0.9 J/g·K, reflecting the energy required to change its temperature.
JSON:```JSON
[{{"value":"0.9", "unit":"J/g·K", "condition":""}}]
```
"""

thermal_expansion_coefficient = """
Paragraph: With a thermal expansion coefficient of 12 x 10-6 K-1, the MOF-A exhibits minimal dimensional change with temperature variations.
JSON:```JSON
[{{"value":"0.000012", "unit":"K-1", "condition":""}}]
```
"""

thermal_conductivity_coefficient = """
Paragraph: The MOF-A demonstrated a thermal conductivity of 0.2 W/m·K, indicating its potential as a thermal insulator.
JSON:```JSON
[{{"value":"0.2", "unit":"W/m·K", "condition":""}}]
```
"""

elastic_constant = """
Paragraph: The Young's modulus of the MOF-A was found to be 10 GPa, indicating its relative stiffness.
JSON:```JSON
[{{"value":"10", "unit":"GPa", "condition":"", "type": "young's modulus"}}]
```

Paragraph: The MOF-A's high bulk modulus of 15 GPa suggests it's resistant to uniform compression.
JSON:```JSON
[{{"value":"15", "unit":"GPa", "condition":"", "type": "bulk modulus"}}]
```

Paragraph: A shear modulus of 5 GPa for the MOF-A indicates its ability to resist shearing forces.
JSON:```JSON
[{{"value":"5", "unit":"GPa", "condition":"", "type": "shear modulus"}}]
```
"""

formation_energy = """
Paragraph:The formation energy of the ZIF-8 was calculated to be -37.2 kcal/mol.
JSON:```JSON
[{{"value": "-37.2", "unit": "kcal/mol", "condition": ""}}]
```
"""

adsorption_energy = """
Paragraph: The adsorption energy of CO2 on the MOF-A was found to be -45.6 kJ/mol.
JSON:```JSON
[{{"value": "-45.6", "unit": "kJ/mol", "condition": ""}}]
```
"""

henry_coefficient = """
Paragraph: The Henry coefficient for hydrogen (H2) adsorption on the MOF-A material was determined to be 3.8 x 10^5 mol/(kg·Pa).
JSON:```JSON
[{{"value": "3.8 x 10^5", "unit": "mol/(kg·Pa)", "condition": "", "gas type": "H2"}}]
```
"""

selectivity= """
Paragraph: Among various MOFs, MOF-A stands out with its exceptional CO2 selectivity over other gases, displaying a selectivity value of 20 at room temperature and 1 atm. This high CO2 selectivity makes MOF-A a promising candidate for carbon capture and storage applications. On the other hand, MOF-B exhibits impressive selectivity towards hydrogen, selectively adsorbing H2 over other gases with a selectivity value of 50 at 77 K and 1 bar.
JSON: ```JSON
<<<<<<< HEAD
[{{"value": "20", "unit": "", "substrate": "CO2", "catalyst": "", "pressure":"1 atm", "temperature":"", "solvent": "", "time": "", "condition": ""}}, {{B", "value": "50", "unit": "", "substrate": "H2", "catalyst": "", "pressure":"1 bar", "temperature":"77 K", "solvent": "", "time": "", "condition": ""}}]
=======
[{{"value": "20", "unit": "", "substrate": "CO2", "catalyst": "", "pressure":"1 atm", "temperature":"", "solvent": "", "time": ""}}, {{"value": "50", "unit": "", "substrate": "H2", "catalyst": "", "pressure":"1 bar", "temperature":"77 K", "solvent": "", "time": ""}}]
>>>>>>> 80ceb36a5171296843926a1caeac1489c3bfa679
```
"""

catalytic_activity = """
Paragraph: Metal-Organic Frameworks (MOFs) exhibit a diverse range of properties, making them highly promising for various applications. One notable MOF, MOF-C, showcases outstanding catalytic activity, achieving a conversion rate of 95% in the conversion of organic compounds.
JSON: ```JSON
[{{"value":"95","unit":"%", "time":"", "condition":""}}]
```

Paragraph: MOF-A afforded 20%, 40%, and 60% conversions after 1, 2, and 3 h, respectively, and 99% conversion could be obtained if the reaction was continued for 8 h.
JSON: ```JSON
[{{"value":"20","unit":"%","time":"1 h", "condition":""}}, {{"value":"40","unit":"%","time":"2 h", "condition":""}}, {{"value":"60","unit":"%","time":"3 h", "condition":""}}, {{"value":"99","unit":"%","etc":"8 h", "condition":""}}]
```
"""

density = """
Paragraph: MOF-A stands out for its impressive density and structural stability. The density of MOF-A is approximately 1.12 g/cm3. This relatively high density, coupled with its robust framework, makes MOF-A suitable for applications where mechanical strength and stability are essential, such as in adsorption-based separation processes.
JSON: ```JSON
[{{"value": "1.12", "unit":"g/cm3", "condition":""}}]
```
"""

magnetic_moment = """
Paragraph: The synthesized MOF-A exhibited a magnetic moment of 2.5 µ_B per formula unit, hinting at its strong magnetic character.
JSON: ```JSON
[{{"value":"2.5", "unit":"µ_B", "temperature":"", "condition":""}}]
```
"""

magnetic_susceptibility = """
Paragraph:Solid-state DC magnetic susceptibility measurements were carried out on desiccated MOF-A under a constant magnetic field of 0.15 T over a temperature range of 5.0–350 K. The χM*T product at room temperature was determined to be 0.98 cm3 mol-1 K per hexanuclear unit.
JSON: ```JSON
[{{"value":"0.98", "unit":"cm3 mol-1 K", "temperature":"room temperature", "condition":""}}]
```
"""


peak_spectrum = """
Paragraph: The analysis of the MOF-A using infrared spectroscopy revealed a unique spectrum, with peaks at 1650 cm-1 and 3400 cm-1, suggesting the presence of carbonyl and hydroxyl groups, respectively.
JSON: ```JSON
[{{"value":"1650, 3400", "unit":"cm-1", "condition":"", "type":"infrared spectroscopy"}}]
```
"""

etc = """
Paragraph: MOF-A displays a dielectric constant of approximately 4.5 at 1 kHz, making it suitable for applications in electronics and capacitive devices. Its dielectric properties make it valuable in energy storage and electronic components.
JSON: ```JSON
[{{"property name": "dielectric constant", "value":"4.5", "unit":"", "condition":""}}]
```

Paragraph: MOF-B exhibits impressive electrical conductivity, with a measured value of approximately 10^-2 S/cm at room temperature.
JSON: ```JSON
[{{"property name": "electrical conductivity", "value":"0.02", "unit": "S/cm", "condition": ""}}]
```

Paragraph: MOF-C displays an electrical resistance of approximately 10^7 ohm·cm, positioning it as a potential insulating material in electronic applications. Its low electrical conductivity makes it useful for reducing electromagnetic interference in electronic circuits.
JSON: ```JSON
[{{"property name": "electrical resistance", "value": "10000000", "unit": "ohm·cm", "condition": ""}}]
```
"""

lattice_parameters = """
Paragraph: Crystallographic data for MOF-A: C36H42N6O4, M = 622.75, monoclinic, P21/c, a = 10.812(4) Å, b = 15.261(6) Å, c = 13.973(5) Å, V = 2293.0(14) cm^3, Z = 4, Dc = 1.292 g cm^−3, μ (X-ray) = 1.012 mm^−1, T = 298(2) K, 14056 reflections collected, 3668 unique (Rint = 0.0573), R1 on F(wR2 on F2) = 0.0397 (0.0884) for 3447 observed (I > 2σ(I)) reflections.
JSON: ```JSON
[{{"value": {{"a": "10.812", "b": "15.261", "c": "13.973", "alpha": "", "beta": "", "gamma": "", "condition": "T = 298(2) K"}}}}]
```
"""

cell_volume = """
Paragraph: Crystallographic data for MOF-A: C36H42N6O4, M = 622.75, monoclinic, P21/c, a = 10.812(4) Å, b = 15.261(6) Å, c = 13.973(5) Å, V = 2293.0(14) cm^3, Z = 4, Dc = 1.292 g cm^−3, μ (X-ray) = 1.012 mm^−1, T = 298(2) K, 14056 reflections collected, 3668 unique (Rint = 0.0573), R1 on F(wR2 on F2) = 0.0397 (0.0884) for 3447 observed (I > 2σ(I)) reflections.
JSON: ```JSON
[{{"value":"2293.0", "unit":"cm^3", "condition": "T = 298(2) K"}}]
```
"""

material_color = """
Paragraph: The material color of the MOF-A is a deep ruby red, imparting a distinctive and attractive appearance to the crystal lattice.
JSON: ```JSON
[{{"value":"deep ruby red", "type":"material color", "condition": ""}}]
```
"""

material_shape = """
Paragraph: MOF-A showcases a striking pyramid-shaped crystal structure, offering intriguing geometric properties for applications in materials science and catalysis.
JSON: ```JSON
[{{"value": "pyramid-shaped crystal", "condition": ""}}]
```
"""

simulation_parameters = """
Paragraph: In the mathematical model for population growth, the simulation parameters were fine-tuned to fit the observed data, with values set as follows: a = 0.05, b = -0.002, and c = 1.2, resulting in an accurate representation of population dynamics over time.
JSON: ```JSON
[{{"symbol": "a", "value": "0.05", "unit": "", "type": "mathematical model for population growth"}}, {{"symbol": "b", "value": "-0.002", "unit": "", "type": "mathematical model for population growth"}}, {{"symbol": "c", "value": "1.2", "unit": "", "type": "mathematical model for population growth"}}]
```
"""

proton_conductivity = """
Paragraph: Proton conductivities measured at 298 K are in the range from 1x10-6 to 1x10-5 S cm^(-1) over 40–95% RH for MOF-A.
JSON:```JSON
[{{"value":"1x10-6", "unit":"S/cm", "temperature": "298 K", "RH":"40", "Ea": "", "guest":""}}, {{"value":"1x10-5","unit":"S/cm","temperature": "298 K", "RH":"95", "Ea": "", "guest":""}}]
```

Paragraph: In summary, we have successfully achieved a high-performance MOF-based proton-conducting material via the facile encapsulation of the imidazole guests within the pores of robust MOF-808 and demonstrated that Im@MOF-808 possesses high proton conductivity with the value of 3.45 × 10−2 S cm−1 (338 K and 99% RH).The Arrhenius plot of Im@MOF-808 displayed in Figure 2b shows Ea = 0.25 eV,(<0.4 eV),
JSON:```JSON
[{{"value":"3.45 × 10−2","unit":"S/cm","temperature": "338 K", "RH":"99", "Ea": "0.25","guest":"imidazole"}}]
```

Paragraph: We report the proton conduction properties of a 2D flexible MOF and a 1D coordination polymer having the molecular formulas MOF-A and MOF-B, respectively. MOF-A and MOF-B show high conductivity values of 2.55 × 10−7 and 4.39 × 10−4 S cm−1 at 80 °C and 95% RH. As determined from least-squares fits of the slopes of Arrhenius plots, the activation energies of MOF-A and MOF-B were 0.96 and 0.84 eV.
JSON:```JSON
[{{"value":"2.55 × 10−7","unit":"S/cm","temperature": "80 °C", "RH":"95", "Ea": "0.96", "guest":""}}, {{"value":"4.39 × 10−4","unit":"S/cm","temperature": "80 °C", "RH":"95", "Ea": "0.84","guest":""}}]
```
"""
