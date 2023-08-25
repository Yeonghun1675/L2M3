PROMPT_TYPE = """First, you must decide whether properties exist or not. Except for topology, property must have a float value. If the properties have no float value, never extract that properties. If there is no property in the paragraph, please return an empty list.
If properties exist, you must find all the intensive properties in paragraphs. Names of properties must be one of following:
- surface_area: surface area of materials. ex) SA, BET surface area, Langmuir surface area
- pore_volume: pore volume of materials ex) PV.
- crystal_size: crystal size of materials.
- pore_diameter: pore diameter of materials ex) LCD, PLD.
- gas_adsorption: amount of gas uptake, gas storage, gas adsorption, selective gas uptake of materials.
- thermal_property: decomposition temperature, thermal conductivity, glass transition temperature of materials ex) Tg, TDT.
- mechanical_property: properties related to application of forces. ex) Young"s modulus, Poisson"s ratio, stress.
- selectivity: selectivity of materials. "Selective" is not equal to "selectivity"
- catalytic_activity: turnover frequency of materials ex) TOF.
- density: bulk density of materials.
- chemical_formula_weight: sum of the atomic weights of the elements present in its chemical formula.
- porosity: fraction of total volume of material that is occupied by pores or voids ex) accessible volume fraction.
- crystal_system: symmetrical and geometrical arrangements within the crystal lattice of materials.
- topology: manner in which the metal nodes and organic linkers are connected in a three-dimensional arrangement.
- space_group: a mathematical description of the symmetries inherent in a periodic crystal lattice.
- magentic_property: properties of materials in the presence of a magnetic field.
- optical_property: properties of materials in response to electromagnetic radiation.
- etc: Other properties not included in the above.

You must not include the same property several times. If there are surface_area and BET surface_area in the paragraph at the same time, you must include "surface_area" once. Only properties must be included and the name of materials must not be included. If same property of different materials appears, you must include the property only once. If certain property you find does not have a value, please do not include that property. For example, even if selectivity is stated in the paragraph, do not write selectivity when specific value is not written. Do not be confused between gas adsorption and selectivity. Gas adsorption is a property that has a unit and selectivity is unitless. Even though there is a word "selectivity", it is not always selectivity. If there is a value with unit, it is gas adsorption.
If you"re uncertain, please replay with "I do not know".

Begin!

Paragraph: Metal Organic Frameworks (MOFs) are known for their exceptional properties, including high surface area, large pore volume, and remarkable gas uptake capacities. One such MOF, MOF-A, exhibits a surface area of 1500 m2/g and a pore volume of 0.9 cm3/g. Additionally, MOF-B demonstrates impressive gas adsorption properties, with an uptake capacity of 200 cm3/g for methane and 180 cm3/g for carbon dioxide. These properties make MOF-B a promising material for applications in gas storage and separation. Another notable MOF, MOF-C, possesses a surface_area of 4000 m2/g and a pore_volume of 1.5 cm3/g. MOF-C shows exceptional hydrogen storage capacity, with an uptake of 7.5 wt% at 77 K and 1 bar.
List: ["surface_area", "pore_volume", "gas_adsorption"]

Paragraph: The MOF-C exhibited strong fluorescence, emitting intense blue light with a maximum emission wavelength at 450 nm. The MOF-D exhibits intriguing magnetic properties, displaying a high magnetic moment of 4.8 μB per Fe atom at room temperature.
List: ["optical_property","magnetic_property"]

Paragraph: The Metal-Organic Framework (MOF) material named MOF-G exhibited a remarkable pore_volume of 1.2 cm3/g, enabling high gas adsorption capacities. MOF-G showed a Thermal Decomposition Temperature (TDT) of 450°C and a TDT of 350°C. The MOF material MOF-H demonstrated exceptional guest molecule selectivity, exhibiting a high adsorption preference for CO2 over N2. Moreover, MOF-I achieved a high turnover frequency (TOF) of 1000 h-1. Characterization results revealed significant flexibility in the MOF structure, allowing for the accommodation of guest molecules of different sizes.
List: ["pore_volume", "thermal_property", "catalytic_activity"]

Paragraph: Metal-Organic Frameworks (MOFs) are a class of porous materials known for their diverse properties. For instance, MOF-J exhibits a notable pore_volume of 0.8 cm3/g, facilitating high gas adsorption capacities. The MOF-K demonstrates remarkable guest molecule selectivity, showcasing a strong adsorption preference for methane (CH4) over other gases like nitrogen (N2). Additionally, MOF-L achieves a high turnover frequency (TOF) in catalytic reactions. Comprehensive characterization results unveiled significant structural flexibility in MOF-L, allowing for the accommodation of guest molecules with varying sizes and shapes. These properties make MOFs promising candidates for various applications, including gas storage, gas separation, and catalysis.
List: ["pore_volume"]

Paragraph: MOF-A displays a dielectric constant of approximately 4.5 at 1 kHz, making it suitable for applications in electronics and capacitive devices. Its dielectric properties make it valuable in energy storage and electronic components.
List: ["etc"]

Paragraph: Metal-Organic Frameworks (MOFs) are a class of porous materials with a diverse range of properties that make them attractive for numerous applications. MOFs possess high surface_areas, allowing for efficient gas adsorption and storage. The tunable pore sizes in MOFs enable selective adsorption of specific gas molecules over others, making them promising for gas separation processes. Additionally, MOFs exhibit excellent thermal stability, withstanding high temperatures without structural degradation, making them suitable for catalytic reactions at elevated temperatures. Their inherent flexibility allows for guest molecule inclusion, facilitating various host-guest interactions for applications in molecular recognition and sensing. Moreover, MOFs can be engineered with tailored functionalities, such as catalytic sites, to enhance their reactivity for chemical transformations. Their vast structural diversity and modularity offer exciting possibilities for designing MOFs with unique properties for specific tasks.
List: []

Paragraph: {paragraph}
List:"""


PROMPT_EXT = """Extract the relevant information about the {prop} of MOFs mentioned in the paragraph. Provide the MOF name, value, and any additional details such as units or conditions, if mentioned. You must output structured data in JSON format for {prop} for following template:
{structured_data}

You must follow below rules:
- You must fill all data in structured_data without "Optional".
- You must only write information about {prop}.
- You must not include information qualitative information. Only quantatitive information is necessary.
- You never forge information that is not in the paragraph.
- Do not write the information in the {example}.
- Room temperature means 298K.
- If the sentence includes more than one information, you must extract the information for each separately.

{information} 

If you"re uncertain, please reply with "I do not know".


Begin!

{example}

Paragraph: {paragraph}
JSON:
"""




