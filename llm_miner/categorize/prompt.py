PROMPT_CATEGORIZE = """First, you must decide type of paragraph that it should be one or more listed in ['synthesis condition', 'property', 'else'].

You must following rules below:
- If the paragraph includes `yield` information, return 'synthesis condition'.
- If the paragraph includes `specific name`, `value` and `unit` of the property, return 'property'. 
- When the paragraph does not include both synthesis condition and property, it means that there is no information. In this case, you must return a list with 'else'.

Begin!

Paragraph: MOF-5, a well-known Zn-based MOF, boasts a high surface area, with a value reaching up to 2,900 m2/g. This remarkable property makes MOF-5 a potential candidate for various applications, such as gas storage and separation. Furthermore, the pores in MOF-5 are uniform with diameters around 14 Å, ensuring selective adsorption of specific molecules based on their size.
List: ["property"]

Paragraph: A mixture of picolinaldehyde (0.0321 g, 0.3 mmol), ammonium acetate (0.0077 g, 0.1 mmol), FeCl3 (0.0161 g, 0.1 mmol), and EtOH (3 mL) was sealed in a 8 mL Pyrex tube. The tube was heated for 3 days at 125 °C under autogenous pressure. Slow cooling of the resultant solution to room temperature over 24 h gave brown crystals of the product. The crystals were collected by filtration, washed with Et2O (2 × 3 mL), and dried in air. Yield: 40% (based on FeCl3). Elem anal. Calcd for C18H12Cl2FeN4O: C, 66.66; H, 4.48; N, 15.55. Found: C, 65.98; H, 4.34; N, 15.48.
List: ["synthesis condition"]

Paragraph: Metal-organic frameworks (MOFs) are renowned for their exceptional properties. They offer high surface areas, tunable structures, and unique adaptability. These qualities make MOFs versatile materials, with applications ranging from efficient gas storage to tailored catalysis and drug delivery. MOFs continue to be a focus of research and development due to their diverse and promising properties.
List: ["else"]

Paragraph: The combination of terbium nitrate and 1,4-benzenedicarboxylic acid (H2BDC) in the presence of triethylamine yields the compound Tb2(BDC)3·(H2O)4, which has an extended nonporous structure constructed from copolymerized BDC and Tb(III) units. The multidentate functionality of BDC and the tendency of Tb to have a high coordination number has allowed water to act as a terminal ligand to Tb in the structure. Upon thermally liberating the water ligands, a microporous material, Tb2(BDC)3, is achieved, which has extended 1-D channels and the same framework structure as that of the as-synthesized solid as evidenced by XRPD. Water sorption isotherm data proves that Tb2(BDC)3 has permanent microporosity, and points to the presence of accessible metal sites within the pores, which also allows the sorption of ammonia to give Tb2(BDC)3·(NH3)4. Luminescence lifetime measurements confirm that resorbed water and sorbed ammonia are bound to Tb and that they give distinctly different decay constants.
List: ["else"]

Paragraph: {paragraph}
List:
"""