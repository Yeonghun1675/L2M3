surface_area = '''
Paragraph: Metal-Organic Frameworks (MOFs) offer a rich landscape of properties, enabling diverse applications across numerous fields. A boasts exceptional features such as a pore volume of 1.2 cm3/g, a BET surface area of 1500 m2/g, and an adsorption capacity of 35.6 wt% for CO2 at 25°C and 1 atm. B showcases its versatility with a pore volume of 0.9 cm3/g, a Langmuir surface area of 1200 m2/g, and an adsorption capacity of 27.8 wt% for N2 at 77 K and 1 atm. Furthermore, C exhibits notable properties, including a pore volume of 1.5 cm3/g, a surface area of 2500 m2/g, and an adsorption capacity of 20.3 wt% for water at 298 K and 0.1 MPa.
JSON: [{{'material':'A', 'type':'BET', 'value':1500, 'unit':'m2/g'}, {'material':'B', 'type': 'Langmuir', 'value':1200, 'unit':'m2/g'}, {'material':'C', 'type': '', 'value':2500, 'unit':'m2/g'}}]
'''

pore_volume = '''
In this example, the selected property is pore volume.
Paragraph: Metal-Organic Frameworks (MOFs) exhibit a diverse range of properties, making them highly promising for various applications. For instance, MOF-A demonstrates exceptional thermal stability, withstanding temperatures above 400°C as determined by thermogravimetric analysis (TGA). It also possesses a pore volume of 0.9 cm3/g, providing ample space for gas adsorption. In contrast, MOF-B exhibits an impressive surface area of 2500 m2/g, enabling high adsorption capacities. Its pore volume of 1.5 cm3/g further enhances its gas storage capabilities.
JSON: [{{'material':'MOF-A','value':0.9,'unit':'cm3/g'}}]
'''

crystal_size = '''

'''

gas_adsorption = '''
In this example, the selected property is gas gas adsorption.
Paragraph: Metal-Organic Frameworks (MOFs) offer a rich landscape of properties, enabling diverse applications across numerous fields. One prominent MOF, MOF-A boasts exceptional features such as an adsorption capacity of 35.6 wt% for CO2 at 25°C and 1 atm. Another remarkable MOF, MOF-B showcases its versatility with an adsorption capacity of 27.8 wt% for N2 at 77 K and 1 atm. Furthermore, MOF-C exhibits a notable adsorption capacity of 20.3 wt% for water at 298 K and 0.1 MPa.
JSON: [{{'material':'MOF-A', 'adsorbate':'CO2', 'adsorbed amount':'35.6 wt%', 'temperature':'25°C', 'pressure':'1 atm'}}, {{'material':'MOF-B', 'adsorbate':'N2', 'adsorbed amount':'27.8 wt%' 'temperature':'77 K', 'pressure':'1 atm'}}, {{'material':'MOF-C', 'adsorbate':'water', 'adsorbed amount':'20.3 wt%', 'temperature':'298 K', 'pressure':'0.1 MPa'}}]
'''

porosity = '''

'''


pore_diameter = '''
In this example, the selected property is pore size.
Paragraph: MOF-A is a well-known MOF that possesses a remarkable pore size. The pores in MOF-A have a diameter of approximately 1.2 nm, which allows for efficient gas adsorption and storage within its porous structure. The well-defined and uniform pore size of MOF-A makes it an ideal candidate for various gas separation applications, where it can selectively adsorb and separate different gas molecules based on their size and affinity to the pores.
JSON:{{'material':'MOF-A', 'value':1.2, 'unit':'nm'}}
'''


crystal_system = '''
Paragraph :MOF-A exhibits the 'primitive cubic net' (PCN) topology, characterized by corner-sharing metal clusters and organic linkers forming a 3D cubic framework. The PCN topology provides numerous open metal sites and accessible pores, making it ideal for gas storage and separation. Its regular structure enables efficient packing of molecules and guests. MOF-5 is extensively studied for H2 and CH4 storage. PCN topology represents one of many fascinating frameworks in the diverse landscape of MOFs.
JSON:[{{'material':'MOF-A','crystal system':'PCN'}}]
'''

space_group = '''

'''

weight = '''
In this example, the selected property is molecular weight.
Paragraph: MOF-A is a well-known MOF composed of Zn4O clusters connected by terephthalate (TPA) ligands. The molecular weight of the repeating unit in MOF-A is approximately 756.9 g/mol. The crystal structure of MOF-A forms a three-dimensional network with high porosity and a large surface area of 3800 m2/g, allowing for efficient gas adsorption and storage. Its remarkable thermal stability up to 300°C makes it suitable for applications in gas separation and storage. The calculated molecular weight of MOF-A facilitates its precise synthesis and characterization and contributes to its widespread use in various fields, including gas storage, catalysis, and drug delivery.
JSON:[{{'material':'MOF-A','value':756.9,'unit':'g/mol'}}]
'''

thermal_property = '''
In this example, the selected property is thermal property.
Paragraph: Several Metal-Organic Frameworks (MOFs) were investigated for their thermal properties. MOF-A exhibited exceptional thermal stability, withstanding temperatures up to 800°C, making it suitable for high-temperature catalytic reactions. On the other hand, MOF-B displayed a relatively lower thermal stability, with a decomposition temperature of 300°C. MOF-C demonstrated excellent thermal conductivity, efficiently transferring heat in various applications. Furthermore, MOF-D showcased a high heat capacity of 150 J/g°C, indicating its ability to absorb and store substantial amounts of heat. Among these MOFs, MOF-E had a low coefficient of thermal expansion (CTE) of 0.00005 /°C, making it an ideal candidate for applications requiring dimensional stability over a wide temperature range. These diverse thermal properties highlight the versatility of MOFs and their potential in various thermal-related applications.
JSON: [{{'material':'MOF-A','value':800,'unit':'°C'}}, {{'material':'MOF-B','value':300,'unit':'°C'}}, {{'material':'MOF-D','value':150,'unit':'J/g°C'}}, {{'material':'MOF-E','value':0.00005,'unit':'/°C'}}]
'''

mechanical_property = '''
In this example, the selected property is mechanical property.
Paragraph: The mechanical properties of Metal-Organic Frameworks (MOFs) are crucial determinants of their structural stability and applicability. Among various MOFs, MOF-A stands out with its exceptional mechanical strength, boasting a Young's modulus of 20 GPa, a testament to its robust framework and resistance to deformation. Additionally, MOF-B showcases remarkable flexibility, allowing it to undergo structural transformations without loss of integrity, making it advantageous for gas separation applications. On the other hand, MOF-C exhibits outstanding rigidity, preserving its structural integrity under mechanical stress. In terms of porosity, MOF-D demonstrates a high surface area of 3000 m2/g, providing substantial adsorption capacity for gases. Moreover, MOF-E exhibits a remarkable pore volume of 1.2 cm3/g, making it suitable for gas storage applications.
JSON: [{{'material':'A','value':20,'unit':'GPa'}}]
'''

selectivity= '''
In this example, the selected property is selectivity.
Paragraph: Metal-Organic Frameworks (MOFs) are well-known for their remarkable selectivity in gas separation and adsorption processes. Among various MOFs, MOF-A stands out with its exceptional CO2 selectivity over other gases, displaying a selectivity value of 20 at room temperature and 1 atm. This high CO2 selectivity makes MOF-A a promising candidate for carbon capture and storage applications. On the other hand, MOF-B exhibits impressive selectivity towards hydrogen, selectively adsorbing H2 over other gases with a selectivity value of 50 at 77 K and 1 bar. This makes MOF-B highly suitable for hydrogen purification and storage.
JSON: [{{'material':'MOF-A','value':20,'gas molecule':'CO2','temp':298,'pressure':1}}, {{'material':'MOF-B','value':50,'gas molecule':'H2','temp':77,'pressure':1}}]
'''

catalytic_activity = '''
In this example, the selected property is catalytic activity.
Paragraph: Metal-Organic Frameworks (MOFs) exhibit a diverse range of properties, making them highly promising for various applications. For instance, MOF-A demonstrates exceptional thermal stability, withstanding temperatures above 400°C as determined by thermogravimetric analysis (TGA). It also possesses a pore volume of 0.9 cm3/g, providing ample space for gas adsorption. In contrast, MOF-B exhibits an impressive surface area of 2500 m2/g, enabling high adsorption capacities. Its pore volume of 1.5 cm3/g further enhances its gas storage capabilities. Another notable MOF, MOF-C, showcases outstanding catalytic activity, achieving a conversion rate of 95% in the conversion of organic compounds. Additionally, MOF-D displays strong fluorescence, emitting intense blue light with a maximum emission wavelength at 450 nm.
JSON: [{{'material':'MOF-C','value':95,'unit':'%'}}]

Paragraph: MOF-A afforded 20%, 40%, and 60% conversions after 1, 2, and 3 h, respectively, and 99% conversion could be obtained if the reaction was continued for 8 h.
JSON: [{{'material':'MOF-A','value':20,'unit':'%','etc':'1 h','material':'MOF-A','value':40,'unit':'%','etc':'2 h','material':'MOF-A','value':60,'unit':'%','etc':'3 h','material':'MOF-A','value':99,'unit':'%','etc':'8 h'}}]
'''

density = '''

'''
magnetic_property = '''
In this example, the selected property is magnetic property.
Paragraph: Metal-Organic Frameworks (MOFs) represent a diverse class of materials with unique properties, making them highly sought after for a wide range of applications. Among them, MOF-A exhibits exceptional thermal stability, with a decomposition temperature above 500°C, as determined by thermogravimetric analysis (TGA). This MOF also showcases a substantial pore volume of 1.2 cm3/g, allowing for efficient gas adsorption and storage. In contrast, MOF-B demonstrates outstanding catalytic activity, achieving a high conversion rate of 95% in the conversion of organic compounds. Additionally, MOF-C exhibits strong fluorescence, emitting intense blue light with a maximum emission wavelength at 450 nm, making it potentially valuable for optoelectronic applications. Furthermore, MOF-D displays intriguing magnetic properties, exhibiting a high magnetic moment of 4.8 μB per metal center at room temperature.
JSON: [{{'material':'MOF-D','value':4.8,'unit':'μB per metal center','temp':298}}]
'''

optical_property = '''
In this example, the selected property is optical property.
Paragraph: MOF-C is a well-known and extensively studied Metal-Organic Framework with fascinating optical properties. MOF-C exhibits strong light absorption in the visible region of the electromagnetic spectrum, with an absorption peak at around 500 nm. The material also displays excellent photoluminescence properties, emitting light in the blue-green region when excited by ultraviolet radiation at 365 nm. The photoluminescence quantum yield of ZIF-8 has been measured at 0.35, indicating a moderate efficiency of light emission.
JSON: [{{'material':'MOF-C','value':500,'unit':'nm','etc':'absorption peak'}}, {{'material':'MOF-C', 'value':365, 'unit':'nm', 'etc':'photoluminescence property'}}]
'''

etc = '''

'''
