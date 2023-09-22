surface_area="""
Paragraph: A boasts exceptional features such as a pore volume of 1.2 cm3/g, a BET surface area of 1500 m2/g, and an adsorption capacity of 35.6 wt% for CO2 at 25°C and 1 atm. B showcases its versatility with a pore volume of 0.9 cm3/g, a Langmuir surface area of 1200 m2/g, and an adsorption capacity of 27.8 wt% for N2 at 77 K and 1 atm. Furthermore, C exhibits notable properties, including a pore volume of 1.5 cm3/g, a surface area of 2500 m2/g, and an adsorption capacity of 20.3 wt% for water at 298 K and 0.1 MPa.
JSON: ```JSON
[{{"probe":"", "type":"BET", "value":"1500", "unit":"m2/g"}}, {{"probe":"", "type": "Langmuir", "value":"1200", "unit":"m2/g"}}, {{"probe":"", "type": "", "value":"2500", "unit":"m2/g"}}]
```
"""

pore_volume="""
Paragraph: MOF-A demonstrates exceptional thermal stability, withstanding temperatures above 400°C as determined by thermogravimetric analysis (TGA). It also possesses a pore volume of 0.9 cm3/g, providing ample space for gas adsorption. In contrast, MOF-B exhibits an impressive surface area of 2500 m2/g, enabling high adsorption capacities.
JSON: ```JSON
[{{"probe":"", "value":"0.9", "unit":"cm3/g"}}]
```
"""

crystal_size="""
Paragraph: MOF-B stands out for its remarkable uniformity in crystal size. The crystal size of MOF-B typically falls in the range of 1 to 5 micrometers. This consistent crystal size is a significant advantage in applications such as gas adsorption, where precise control of crystal size can enhance performance and efficiency.
JSON: ```JSON
[{{"value":"1 to 5", "unit":"micrometers"}}]
```

Paragraph: Among the MOFs designed for various applications, MOF-A has attracted attention due to its impressive crystal size and structural versatility. The crystal size of MOF-A, which is formally known as Chromium(III) Terephthalate, spans a wide range from 500 nanometers to several micrometers. This extensive crystal size variation makes MOF-A adaptable to a multitude of applications, including gas storage and heterogeneous catalysis.
JSON: ```JSON
[{{"value":"500 nanometers to several micrometers", "unit":""}}]
```
"""

gas_adsorption="""
Paragraph: Metal-Organic Frameworks (MOFs) offer a rich landscape of properties, enabling diverse applications across numerous fields. One prominent MOF, MOF-A boasts exceptional features such as an adsorption capacity of 35.6 wt% for CO2 at 25°C and 1 atm. Another remarkable MOF, MOF-B showcases its versatility with an adsorption capacity of 27.8 wt% for N2 at 77 K and 1 atm. Furthermore, MOF-C exhibits a notable adsorption capacity of 20.3 wt% for water at 298 K and 0.1 MPa.
JSON: ```JSON
[{{"adsorbate":"CO2", "adsorbed amount":"35.6", "unit":"wt%", "temperature":"25°C", "pressure":"1 atm"}}, {{"adsorbate":"N2", "adsorbed amount":"27.8", "unit":"wt%", "temperature":"77 K", "pressure":"1 atm"}}, {{"adsorbate":"water", "adsorbed amount":"20.3", "unit":"wt%", "temperature":"298 K", "pressure":"0.1 MPa"}}]
```
"""

porosity ="""
Paragraph: MOF-A is a MOF renowned for its high porosity fraction. MOF-A possesses a remarkable porosity fraction of approximately 0.87, indicating that nearly 87% of its structure is composed of voids and pores. This substantial porosity fraction arises from the unique arrangement of its zinc and imidazole-based organic linkers. The high porosity fraction of MOF-A makes it an excellent candidate for gas adsorption and separation, as it can accommodate a significant volume of gas molecules within its pore network, allowing for efficient storage and separation processes.
JSON: ```JSON
[{{"value":"0.87", "unit":""}}]
```

Paragraph: The calculated solvent-accessible void space within the framework measures 852.8 Å3, representing approximately 38.2% of the unit cell volume of 2230.6 Å3.
JSON: ```JSON
[{{"value":"38.2", "unit":"%"}}, {{"value":"852.8", "unit":"Å3"}}]
```
"""


pore_diameter = """
Paragraph: MOF-A is a well-known MOF that possesses a remarkable pore size. The pores in MOF-A have a diameter of approximately 1.2 nm, which allows for efficient gas adsorption and storage within its porous structure. The well-defined and uniform pore size of MOF-A makes it an ideal candidate for various gas separation applications, where it can selectively adsorb and separate different gas molecules based on their size and affinity to the pores.
JSON:```JSON
[{{"value":"1.2", "unit":"nm"}}]
```
"""

crystal_system = """
Paragraph: MOF-A crystallizes in a tetragonal crystal system, which means its unit cell has three edges of equal length and right angles between them.
JSON:```JSON
[{{"value":"tetragonal"}}]
```
"""

topology = """
Paragraph :MOF-A exhibits the "primitive cubic net" (PCN) topology, characterized by corner-sharing metal clusters and organic linkers forming a 3D cubic framework. The PCN topology provides numerous open metal sites and accessible pores, making it ideal for gas storage and separation. Its regular structure enables efficient packing of molecules and guests. MOF-A is extensively studied for H2 and CH4 storage. PCN topology represents one of many fascinating frameworks in the diverse landscape of MOFs.
JSON:```JSON
[{{"value":"PCN"}}]
```
"""

space_group = """
Paragraph: In the field of crystallography, MOF-A is notable for its well-defined structure and crystallographic properties. MOF-A belongs to the Fm-3m space group, indicating a face-centered cubic crystal lattice. The space group value for MOF-A, Fm-3m, signifies its cubic symmetry and high degree of order within its crystalline framework. This well-characterized space group is instrumental in understanding and predicting the structural properties of MOF-A, which is essential for its various applications, such as gas storage, catalysis, and host-guest chemistry.
JSON:```JSON
[{{"value":"Fm-3m"}}]
```
"""

chemical_formula_weight = """
Paragraph: MOF-A is a well-known MOF composed of Zn4O clusters connected by terephthalate (TPA) ligands. The chemical formula weight of the repeating unit in MOF-A is approximately 756.9 g/mol. The calculated chemical formula weight of MOF-A facilitates its precise synthesis and characterization and contributes to its widespread use in various fields, including gas storage, catalysis, and drug delivery.
JSON:```JSON
[{{"value":"756.9", "unit":"g/mol"}}]
```
"""

decomposition_temperature = """
Paragraph: The MOF-A began to thermally decompose at 400 °C, suggesting its stability up to this temperature.
JSON:```JSON
[{{"value":"400", "unit":"°C", "type":"decomposition point"}}]
```

Paragraph: Complex 4 exhibits remarkable thermal stability, remaining stable up to a temperature of 155°C. A modest weight loss of 4.8% (calculated 4.6%) between 155 and 250°C can be attributed to the removal of coordinated solvent molecules. Beyond this point, the compound undergoes a consecutive weight loss process that persists until heating to 680°C.
JSON:```JSON
[{{"value":"150", "unit":"°C", "type":"stable"}}, {{"value":"150 and 250", "unit":"°C", "type":"removal of coordinated solvent molecules"}}, {{"value":"680", "unit":"°C", "type":"consecutive weight loss"}}]
```

Paragraph: In the case of MOF-XYZ, it was observed that there was an initial weight loss of 7.82% before reaching 120°C, corresponding closely to the departure of guest molecules. Subsequently, a temperature range spanning from 110°C to 280°C was attributed to the gradual removal of coordinated water molecules (experimental: 8.15%; calculated: 7.28%), after which the structure underwent decomposition. 
JSON: ```JSON
[{{"value":"120", "unit":"°C", "type":"an initial weight loss"}}, {{"value":"110 to 280", "unit":"°C", "type":"gradual removal of coordinated water molecules"}}]
```
"""

heat_capacity = """
Paragraph: The specific heat capacity of the MOF-A was measured to be 0.9 J/g·K, reflecting the energy required to change its temperature.
JSON:```JSON
[{{"value":"0.9", "unit":"J/g·K"}}]
```
"""

thermal_expansion_coefficient = """
Paragraph: With a thermal expansion coefficient of 12 x 10-6 K-1, the MOF-A exhibits minimal dimensional change with temperature variations.
JSON:```JSON
[{{"value":"0.000012", "unit":"K-1"}}]
```
"""

thermal_conductivity = """
Paragraph: The MOF-A demonstrated a thermal conductivity of 0.2 W/m·K, indicating its potential as a thermal insulator.
JSON:```JSON
[{{"value":"0.2", "unit":"W/m·K"}}]
```
"""
youngs_modulus = """
Paragraph: The Young's modulus of the MOF-A was found to be 10 GPa, indicating its relative stiffness.
JSON:```JSON
[{{"value":"10", "unit":"GPa"}}]
```
"""

bulk_modulus = """
Paragraph: The MOF-A's high bulk modulus of 15 GPa suggests it's resistant to uniform compression.
JSON:```JSON
[{{"value":"15", "unit":"GPa"}}]
```
"""

shear_modulus = """
Paragraph: A shear modulus of 5 GPa for the MOF-A indicates its ability to resist shearing forces.
JSON:```JSON
[{{"value":"5", "unit":"GPa"}}]
```
"""

poissons_ratio = """
Paragraph: With a Poisson's ratio of 0.3, the MOF-A displayed typical volumetric deformation under axial strain.
JSON:```JSON
[{{"value":"0.3"}}]
```
"""

selectivity= """
Paragraph: Metal-Organic Frameworks (MOFs) are well-known for their remarkable selectivity in gas separation and adsorption processes. Among various MOFs, MOF-A stands out with its exceptional CO2 selectivity over other gases, displaying a selectivity value of 20 at room temperature and 1 atm. This high CO2 selectivity makes MOF-A a promising candidate for carbon capture and storage applications. On the other hand, MOF-B exhibits impressive selectivity towards hydrogen, selectively adsorbing H2 over other gases with a selectivity value of 50 at 77 K and 1 bar. This makes MOF-B highly suitable for hydrogen purification and storage.
JSON: ```JSON
[{{"value": "20", "unit": "", "substrate": "CO2", "catalyst": "", "pressure":"1 atm", "temperature":"", "solvent": "", "time": ""}}, {{B", "value": "50", "unit": "", "substrate": "H2", "catalyst": "", "pressure":"1 bar", "temperature":"77 K", "solvent": "", "time": ""}}]
```
"""

catalytic_activity = """
Paragraph: Metal-Organic Frameworks (MOFs) exhibit a diverse range of properties, making them highly promising for various applications. For instance, MOF-A demonstrates exceptional thermal stability, withstanding temperatures above 400°C as determined by thermogravimetric analysis (TGA). It also possesses a pore volume of 0.9 cm3/g, providing ample space for gas adsorption. In contrast, MOF-B exhibits an impressive surface area of 2500 m2/g, enabling high adsorption capacities. Its pore volume of 1.5 cm3/g further enhances its gas storage capabilities. Another notable MOF, MOF-C, showcases outstanding catalytic activity, achieving a conversion rate of 95% in the conversion of organic compounds. Additionally, MOF-D displays strong fluorescence, emitting intense blue light with a maximum emission wavelength at 450 nm.
JSON: ```JSON
[{{"value":"95","unit":"%", "time":""}}]
```

Paragraph: MOF-A afforded 20%, 40%, and 60% conversions after 1, 2, and 3 h, respectively, and 99% conversion could be obtained if the reaction was continued for 8 h.
JSON: ```JSON
[{{"value":"20","unit":"%","time":"1 h"}}, {{"value":"40","unit":"%","time":"2 h"}}, {{"value":"60","unit":"%","time":"3 h"}}, {{"value":"99","unit":"%","etc":"8 h"}}]
```
"""

density = """
Paragraph: MOF-A stands out for its impressive density and structural stability. The density of MOF-A is approximately 1.12 g/cm3. This relatively high density, coupled with its robust framework, makes MOF-A suitable for applications where mechanical strength and stability are essential, such as in adsorption-based separation processes.
JSON: ```JSON
[{{"value": "1.12", "unit":"g/cm3"}}]
```
"""

magnetic_moment = """
Paragraph: The synthesized MOF-A exhibited a magnetic moment of 2.5 µ_B per formula unit, hinting at its strong magnetic character.
JSON: ```JSON
[{{"value":"2.5", "unit":"µ_B", "temperature":""}}]
```
"""

magnetic_susceptibility = """
Paragraph:Solid-state DC magnetic susceptibility measurements were carried out on desiccated sample 2 under a constant magnetic field of 0.15 T over a temperature range of 5.0–350 K. The χM*T product at room temperature was determined to be 0.98 cm3 mol-1 K per hexanuclear unit, closely approximating the anticipated value of 1.05 cm3 mol-1 K for six interacting Fe(III) ions with a calculated g value of 2.0.
JSON: ```JSON
[{{"value":"0.98", "unit":"cm3 mol-1 K", "temperature":"room temperature"}}]
```
"""

refractive_index = """
Paragraph: The refractive index of the MOF-A was found to be 1.42, indicating its ability to significantly bend light.
JSON: ```JSON
[{{"value":"1.42"}}]
```
"""

spectrum = """
Paragraph: The analysis of the MOF-A using infrared spectroscopy revealed a unique spectrum, with peaks at 1650 cm-1 and 3400 cm-1, suggesting the presence of carbonyl and hydroxyl groups, respectively.
JSON: ```JSON
[{{"value":"1650, 3400", "unit":"cm-1"}}]
```
"""

etc = """
Paragraph: MOF-A displays a dielectric constant of approximately 4.5 at 1 kHz, making it suitable for applications in electronics and capacitive devices. Its dielectric properties make it valuable in energy storage and electronic components.
JSON: ```JSON
[{{"property name": "dielectric constant", "value":"4.5", "unit":"", "condition":""}}]
```

Paragraph: MOF-B exhibits impressive electrical conductivity, with a measured value of approximately 10^-2 S/cm at room temperature.
JSON: ```JSON
[{{"property name": "electrical conductivity", "value":"0.02", "unit":"S/cm", "condition": ""}}]
```

Paragraph: NOTT-202 displays an electrical resistance of approximately 10^7 ohm·cm, positioning it as a potential insulating material in electronic applications. Its low electrical conductivity makes it useful for reducing electromagnetic interference in electronic circuits.
JSON: ```JSON
[{{"property name": "electrical resistance", "value": "10000000", "unit": "ohm·cm", "condition": ""}}]
```
"""

lattice_parameters = """
Paragraph: Crystallographic data for Compound 2: C36H42N6O4, M = 622.75, monoclinic, P21/c, a = 10.812(4) Å, b = 15.261(6) Å, c = 13.973(5) Å, V = 2293.0(14) cm^3, Z = 4, Dc = 1.292 g cm^−3, μ (X-ray) = 1.012 mm^−1, T = 298(2) K, 14056 reflections collected, 3668 unique (Rint = 0.0573), R1 on F(wR2 on F2) = 0.0397 (0.0884) for 3447 observed (I > 2σ(I)) reflections.
JSON: ```JSON
[{{"value": {{"a": "10.812", "b": "15.261", "c": "13.973", "alpha": "", "beta": "", "gamma": ""}}]
```
"""

cell_volume = """
Paragraph: Crystallographic data for Compound 2: C36H42N6O4, M = 622.75, monoclinic, P21/c, a = 10.812(4) Å, b = 15.261(6) Å, c = 13.973(5) Å, V = 2293.0(14) cm^3, Z = 4, Dc = 1.292 g cm^−3, μ (X-ray) = 1.012 mm^−1, T = 298(2) K, 14056 reflections collected, 3668 unique (Rint = 0.0573), R1 on F(wR2 on F2) = 0.0397 (0.0884) for 3447 observed (I > 2σ(I)) reflections.
JSON: ```JSON
[{{"value":"2293.0", "unit":"cm^3"}}]
```
"""

equation = """
Paragraph: The adsorption capacity of MOF-123 for methane (CH4) can be accurately predicted using the Langmuir equation, which is expressed as: Q = (Qmax * K * P) / (1 + (K * P))
JSON: ```JSON
[{{"value":"Q = (Qmax * K * P) / (1 + (K * P))", "parameters":"", "name":"Langmuir equation"}}]
```
"""

charge_related = """
Paragraph:  In the MOF known as 'MOF-456,' the charge distribution is characterized by a net charge of -0.15 on the metal center and a partial positive charge of +0.08 on the organic ligands, indicating a strong interaction between the metal clusters and ligands
JSON: ```JSON
[{{"value":"-0.15", "unit":"", "type":"on the metal center"}}, {{"value":"+0.8", "unit":"", "type":"on the organic ligands"}}]
```
"""

material_color = """
Paragraph: The material color of the MOF 'MOF-789' is a deep ruby red, imparting a distinctive and attractive appearance to the crystal lattice.
JSON: ```JSON
[{{"value":"deep ruby red", "type":"material color"}}]
```
"""

parameters = """
Paragraph: The experimental data conforms to the Van der Waals equation of state with a value of 'a' equal to 3.42 L^2 atm/mol^2 and 'b' equal to 0.0342 L/mol.
JSON: ```JSON
[{{"symbol":a", "value":"3.42", "unit":"L^2 atm/mol^2", "type":"Van der Waals equation"}}, {{"symbol":b", "value":"0.0342", "unit":"L/mol", "type":"Van der Waals equation"}}]
```
"""

energy_related = """
Paragraph: The isosteric heat of adsorption (Q\nst) of 1 was also calculated. At zero coverage, the Q\nst is 3.33kJ/mol.
JSON: ```JSON
[{{"value":"3.33", "unit":"kJ/mol", "type":"isoteric heat of adsorption"}}]
```
"""