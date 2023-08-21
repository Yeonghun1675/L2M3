PROMPT_CATEGORIZE = """First, you must decide whether properties exist or not. Except for topology, property must have a float value. If the properties have no float value, never extract that properties. If there is no property in the paragraph, please return an empty list.
If properties exist, you must find all the intensive properties in paragraphs. Names of properties must be one of following:
- synthesis condition: synthesis condition of mateirals
- surface area: surface area of materials. ex) SA, BET surface area, Langmuir surface area
- total pore volume: pore volume of materials ex) PV.
- crystal size: crystal size of materials.
- pore diameter: pore diameter of materials ex) LCD, PLD.
- gas adsorption: amount of gas uptake, gas storage, gas adsorption, selective gas uptake of materials.
- thermal property: decomposition temperature, thermal conductivity, glass transition temperature of materials ex) Tg, TDT.
- mechanical property: modulus, stress.
- selectivity: selectivity of materials. 'Selective' is not equal to 'selectivity'
- catalytic activity: turnover frequency of materials ex) TOF.
- density: bulk density.
- chemical formula weight
- porosity(void fraction): accessible volume fraction.
- crystal system: topology, structure of materials.
- space group
- magentic property
- optical property
- etc

You must not include the same property several times. If there are surface area and BET surface area in the paragraph at the same time, you must include 'surface area' once. Only properties must be included and the name of materials must not be included. If same property of different materials appears, you must include the property only once. If certain property you find does not have a value, please do not include that property. For example, even if selectivity is stated in the paragraph, do not write selectivity when specific value is not written. Do not be confused between gas adsorption and selectivity. Gas adsorption is a property that has a unit and selectivity is unitless. Even though there is a word 'selectivity', it is not always selectivity. If there is a value with unit, it is gas adsorption.
If you're uncertain, please replay with `I do not know`.

Begin!

Paragraph: Metal Organic Frameworks (MOFs) are known for their exceptional properties, including high surface area, large pore volume, and remarkable gas uptake capacities. One such MOF, MOF-A, exhibits a surface area of 1500 m2/g and a pore volume of 0.9 cm3/g. Additionally, MOF-B demonstrates impressive gas adsorption properties, with an uptake capacity of 200 cm3/g for methane and 180 cm3/g for carbon dioxide. These properties make MOF-B a promising material for applications in gas storage and separation. Another notable MOF, MOF-C, possesses a surface area of 4000 m2/g and a pore volume of 1.5 cm3/g. MOF-C shows exceptional hydrogen storage capacity, with an uptake of 7.5 wt% at 77 K and 1 bar.
List: ["surface area", "total pore volume", "gas adsorption"]

Paragraph: The MOF-C exhibited strong fluorescence, emitting intense blue light with a maximum emission wavelength at 450 nm. The MOF-D exhibits intriguing magnetic properties, displaying a high magnetic moment of 4.8 μB per Fe atom at room temperature.
List: ["optical property","magnetic property"]

Paragraph: The Metal-Organic Framework (MOF) material named MOF-G exhibited a remarkable pore volume of 1.2 cm3/g, enabling high gas adsorption capacities. MOF-G showed a Thermal Decomposition Temperature (TDT) of 450°C and a TDT of 350°C. The MOF material MOF-H demonstrated exceptional guest molecule selectivity, exhibiting a high adsorption preference for CO2 over N2. Moreover, MOF-I achieved a high turnover frequency (TOF) of 1000 h-1. Characterization results revealed significant flexibility in the MOF structure, allowing for the accommodation of guest molecules of different sizes.
List: ["total pore volume", "thermal property", "catalytic activity"]

Paragraph: Metal-Organic Frameworks (MOFs) are a class of porous materials known for their diverse properties. For instance, MOF-J exhibits a notable pore volume of 0.8 cm3/g, facilitating high gas adsorption capacities. The MOF-K demonstrates remarkable guest molecule selectivity, showcasing a strong adsorption preference for methane (CH4) over other gases like nitrogen (N2). Additionally, MOF-L achieves a high turnover frequency (TOF) in catalytic reactions. Comprehensive characterization results unveiled significant structural flexibility in MOF-L, allowing for the accommodation of guest molecules with varying sizes and shapes. These properties make MOFs promising candidates for various applications, including gas storage, gas separation, and catalysis.
List: ["total pore volume"]

Paragraph: Metal-Organic Frameworks (MOFs) are a class of porous materials with a diverse range of properties that make them attractive for numerous applications. MOFs possess high surface areas, allowing for efficient gas adsorption and storage. The tunable pore sizes in MOFs enable selective adsorption of specific gas molecules over others, making them promising for gas separation processes. Additionally, MOFs exhibit excellent thermal stability, withstanding high temperatures without structural degradation, making them suitable for catalytic reactions at elevated temperatures. Their inherent flexibility allows for guest molecule inclusion, facilitating various host-guest interactions for applications in molecular recognition and sensing. Moreover, MOFs can be engineered with tailored functionalities, such as catalytic sites, to enhance their reactivity for chemical transformations. Their vast structural diversity and modularity offer exciting possibilities for designing MOFs with unique properties for specific tasks.
List: []

Paragraph: <title> Synthesis of [La<sub>4</sub>(Q[5])<sub>3</sub>(DGC)<sub>2</sub>(NO<sub>3</sub>)<sub>2</sub>(H<sub>2</sub>O)<sub>12</sub>][La(DGC)(H<sub>2</sub>O)<sub>6</sub>]·7NO<sub>3</sub>·<italic>n</italic>H<sub>2</sub>O (<bold>1</bold>)</title>
===============================================
<p>Q[5] (10 mg, 1.0 mmol) was dissolved in 3.0 mL of deionized (DI) water. Lanthanum nitrate hexahydrate (433.1 mg; 1.0 mmol) and diglycolic acid (134.1 mg, 1.0 mmol) were dissolved in 3.0 mL of DI water and added to the above Q[5] solution.
Diluted triethylamine was used to neutralize the solution to pH 6 (±0.1). Fine needle crystalline product of compound <bold>1</bold> was formed in a week, with 74% yield based on Q[5], which was collected and dried in air. Elemental analysis (calc., found) for C<sub>102</sub>H<sub>138</sub>N<sub>69</sub>O<sub>90</sub>La<sub>5</sub>·11H<sub>2</sub>O: C (26.27, 26.56), H (3.46, 3.28), and N (20.73, 21.05).</p>
List: ["synthesis condition"]

Paragraph: {paragraph}
List:
"""


