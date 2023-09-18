PROMPT_CATEGORIZE = """First, you must decide type of paragraph that it should be one or more listed in ["synthesis condition", "property", "else"].

You must follow rules below:
- You must return ["synthesis condition"] only when the paragraph includes several processes such as chemical synthesis, washing, and drying. It also includes specific IR or NMR information often. ex) "IR: 3137(m), 2359(m), 1655(s), 1493(s), 1262(s), 1210(s), 1148(s), 805(m), 668(m), 589(m).
- You must return ["property"] only when the paragraph includes "property type", "specific value of property" and "unit of the property". ex) surface area of 2500 m2/g
- If there are both "synthesis condition" and "property", return ["property", "synthesis condition"].
- When the paragraph does not include both synthesis condition and property, it means that there is no information. In this case, you must return ["else"].
- Only possible answer is ["property"], ["synthesis condition"], ["property","synthesis condition"] or ["else"]
- If "TGA" is in the paragraph, it means that it contains only "property", not "synthesis condition".

Begin!

Paragraph: MOF-5, a well-known Zn-based MOF, boasts a high surface area, with a value reaching up to 2,900 m2/g. This remarkable property makes MOF-5 a potential candidate for various applications, such as gas storage and separation. Furthermore, the pores in MOF-5 are uniform with diameters around 14 Å, ensuring selective adsorption of specific molecules based on their size.
List: ["property"]

Paragraph: TGA was conducted on compounds 5 to 8 under a continuous nitrogen atmosphere. Interestingly, these compounds exhibit distinct thermal behaviors. TG profiles for compounds 5 and 6 reveal a single plateau extending from room temperature to 380°C, after which the ligand decomposition triggers a complete structural breakdown. In contrast, compounds 7 and 8 display two distinct plateaus in their TG curves. For compound 7, the initial weight loss of 22% between 270 and approximately 320°C corresponds to the complete liberation of diethyl ether molecules (calculated: 21.4%), with the residual framework [Mn(lig)]n exhibiting no weight loss up to approximately 400°C. Comparative powder X-ray diffraction analyses confirm that the framework [Mn(lig)]n remains unchanged at 300°C, transitioning to an unidentified phase only after the complete removal of diethyl ether ligands at 350°C (). The total solvent-accessible volume of 7 is estimated at 36.2% using the PLATON program. The TGA profile of compound 8 closely mirrors that of compound 7, although compound 8 demonstrates greater thermal stability. Supported by powder X-ray diffraction patterns, it is evident that the framework of compound 8 remains unaltered even at 350°C.
List: ["property"]

Paragraph: A mixture of H2L (0.0138 g, 0.05 mmol), Zn(NO3)2·6H2O (0.0149 g, 0.05 mmol), and NaOH (0.0040 g, 0.1 mmol) in 6 mL of mixed H2O–MeCN (1:1 v/v) was placed in a Teflon-lined stainless steel vessel, heated to 120 °C for 3 days, and then cooled to room temperature. Colorless block-like crystals of 1 were obtained in 80% yield based on zinc. Anal. Calcd for C13H9NO5SZn (356.64): C, 43.74; H, 2.53; N, 3.93. Found: C, 43.70 ; H, 2.57; N, 3.98. IR/cm–1 (KBr): 3423(s), 1604(s), 1424(s), 1375(s), 1356(s).
List: ["synthesis condition"]

Paragraph: Metal-organic frameworks (MOFs) are renowned for their exceptional properties. They offer high surface areas, tunable structures, and unique adaptability. These qualities make MOFs versatile materials, with applications ranging from efficient gas storage to tailored catalysis and drug delivery. MOFs continue to be a focus of research and development due to their diverse and promising properties.
List: ["else"]

Paragraph: The combination of terbium nitrate and 1,4-benzenedicarboxylic acid (H2BDC) in the presence of triethylamine yields the compound Tb2(BDC)3·(H2O)4, which has an extended nonporous structure constructed from copolymerized BDC and Tb(III) units. The multidentate functionality of BDC and the tendency of Tb to have a high coordination number has allowed water to act as a terminal ligand to Tb in the structure. Upon thermally liberating the water ligands, a microporous material, Tb2(BDC)3, is achieved, which has extended 1-D channels and the same framework structure as that of the as-synthesized solid as evidenced by XRPD. Water sorption isotherm data proves that Tb2(BDC)3 has permanent microporosity, and points to the presence of accessible metal sites within the pores, which also allows the sorption of ammonia to give Tb2(BDC)3·(NH3)4. Luminescence lifetime measurements confirm that resorbed water and sorbed ammonia are bound to Tb and that they give distinctly different decay constants.
List: ["else"]

Paragraph: Cyclic triimidazole (C9H6N6, L), with C3h molecular symmetry and three nitrogen atoms available for coordination, is here successfully employed for the first time in the synthesis of coordination compounds. In particular, by varying the reaction conditions (e.g., solvent, temperature, template), seven Cu(I)-halide coordination polymers of different dimensionality are obtained: two 1D polymers, [CuIL]n (1) and {{[CuIL]·(I2)0.5}}n (2), three 2D nets, [CuXL]n (X = I, Br) (3–5), and two 3D networks, [CuClL]n (6) and {{[Cu3L4]I3}}n (7). Single crystal X-ray diffraction analysis reveals that the structural versatility of both the ligand and the CuX moiety allows isolating 1D double-stranded stairs in which L is monodentate, 2D layers containing either Cu2(μ-X)2 or Cu2(μ-X) moieties and bidentate L ligands, 3D frameworks built up by tridentate L linkers and either monodentate or noncoordinating halogen atoms. The 3D frameworks show nets of srs and bor topologies. The SHG efficiency of powders of 7 (the only noncentrosymmetric derivative of the series) is 10 times higher than that of sucrose. Phosphorescent emission of XLCT character is observed for 1 and 6.
List: ["else"]

Paragraph: {paragraph}
List:
"""


FT_CATEGORIZE = (
    "Categorize the paragraph given. "
    "Select one or more categories from \"synthesis condition\" and \"property\". "
    "If the paragraph does not fit into either of these categories, choose \"else\". "
    "\"property\" paragraph must include specific numerical value of the property. "
    "ex) surface area of 2500 m2/g"
)

FT_HUMAN = "{paragraph}"