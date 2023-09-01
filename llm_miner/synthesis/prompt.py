PROMPT_TYPE = """Find all the processes used during synthesis. Each process unconditionally must belongs to one of the elements in the following list:
["atomic_layer_deposition", "atomic_layer_etching", "ball_milling", "blade_coating", "bulk_metal_forming", "centrifugation", "chemical_mechanical_polishing", "chemical_synthesis", "chemical_vapor_deposition", "directed_energy_deposition", "drying", "e_beam_lithography", "electrochemical_deposition", "electrospinning", "electrical_poling", "casting", "heat_treatment", "hydrothermal_reaction", "microwave_assisted_synthesis", "mixing", "molecular_beam_epitaxy", "polishing", "powder_bed_fusion", "pulsed_laser_deposition", "rinsing", "pressing", "sintering", "slurry_casting", "slot_coating", "solvothermal_synthesis", "sol_gel_syntehsis", "sonication", "sonochemical_syntehsis", "spin_coating", "spray_pyrolysis", "sputter_deposition", "thermal_evaporation", "thermomechanical_process", "transporting", "wet_etching", "washing", "cooling"]

You must write processes in the above list.

Paragraph: A mixture of tris-(4-bromophenyl)amine (2.00 g, 4.15 mmol) and CuCN (1.70 g, 18.98 mmol) was heated at reflux in 25 mL of anhydrous dimethylformamide (DMF) for 6 h under a nitrogen atmosphere at 150 °C. Upon cooling to room temperature (RT), the FeCl3/H2O/ethanol (8.00 g/10 mL/8 mL) mixture solvent was added to the reaction mixture and then heated to 125 °C. Then, dilute hydrochloric acid (100 mL, 2 M) was added into the solution. The resulting mixture was extracted with CH2Cl2 (5 × 50 mL), washed with ethylenediaminetetraacetic acid-2Na aqueous solution (5 × 100 mL), evaporated under a rotary evaporator, and dried over anhydrous MgSO4. The crude product was purified by flash chromatography on silica gel using CH2Cl2 as an eluent to afford 0.90 g (67.8%) of tris-(4-cyanophenyl)amine as a primrose yellow powder.
List: ["chemical_synthesis","washing"]

Paragraph:{paragraph}
List:
"""

PROMPT_STRUCT = """Extract the relevant information about the synthesis of MOFs mentioned in the paragraph.

There are guildlines for output format:
- You must write like {{"Mof name": str, "symbol":float, "processes": list, "yield": str, "chemial formula":str, and "other properties": [str, str, ...]}}.
- The "process" list consists of several dictionaries. Each dictionary consists of {{"synthesis method": str, information(different according to synthesis method)}}.

For each process, you must follow these formats:
{format}


You must follow rules belows:
- According to the synthesis type, information you must write is different. You must write one dictionary per one product.
- If there are several products in the text, you must write several dictionaries. Each product usually has an index, so you must check the index and write accurately which characteristics correspond to which product.
- In some cases, it is stated that the synthesis method is the same as before. In this case, check the product with the same synthesis method and fill in the information(precursor, temperature, pressure, time, etc) based on what you recorded earlier.
- For each dictionary, you must include yield, chemical formula and other properties if information exists.
- According to the synthesis method, you must include other information about {synthesis_type}.
- In case of precursor, reactant, additive, surfactant, source, solution, solvent and reducing agent, if these exist more than 2, you must write all the things. 
- Do not confuse precursor with solution. Precursor has a unit of mass and solution has a unit of volume.
- If there are more than two solutions, write down all solutions in the form of a list.
- You must focus on "time" and if there are more than two "time", this means there are several steps and there must be several dictionaries same number with "time".
- If certain information does not exist, you must write "Not mentioned".
- Temperature must consist of number and unit like "200K".
- You must fill all data in structured_data without "Optional".
- You must only write information about synthesis condition.
- You must not include information qualitative information. Only quantatitive information is necessary.
- You never forge information that is not in the paragraph. Do not write the information in the {example}.
- Room temperature means 298K.
- If the sentence includes more than one information, you must extract the information for each separately.
- If symbol is written altogether like "4-6", write three different results. There is at least one metal precursor and one organic precursor.
- If several symbols exist at the same paragraph, you must write separately all the things.
- You must include chemical formula if information exists. Chemical formula consists of combination of several elements and numbers like C2H5OH.
- When "Ln" exists in the paragraph, you must write other elements instead of "Ln". ex) ChemLn (Ln=Pr(1), Gd(2), Dy(3), Er(4)), There are four chemicals; ChemPr, ChemGd, ChemDy, ChemEr

If you"re uncertain, please reply with "I do not know".


Begin!

{example}

Paragraph: {paragraph}
JSON:
"""


EXAMPLE_STRUCT = """
Paragraph: [Ag3(Z[6])2(TDA)3(Cl)2(H2O)10][Ag(TDA)(H2O)5]·6Cl·nH2O (2)

Z[6] (20 mg, 2.0 mmol) was dissolved in 4.0 mL of deionized (DI) water. Silver chloride (536.1 mg; 3.0 mmol) and tetradecanoic acid (576.3 mg, 2.0 mmol) were dissolved in 4.0 mL of DI water and added to the above Z[6] solution. Diluted sodium hydroxide was used to adjust the solution to pH 7 (±0.1). After a period of one week, octahedral crystals of compound 2 were formed. The resulting product was achieved in a yield of 68% based on Z[6], which was collected and dried under vacuum. Elemental analysis (calc., found) for C104H142Ag3N71O95Cl7·12H2O: C (25.87, 26.01), H (3.38, 3.50), and N (20.12, 20.25).
JSON: [{"Mof name": "[Ag3(Z[6])2(TDA)3(Cl)2(H2O)10][Ag(TDA)(H2O)5]·6Cl·nH2O", "symbol":2, "processes": [{"synthesis method": "chemical synthesis", "precursor1 name": "Z[6]", "precursor1 amount": "20 mg", "precursor2 name": "Silver chloride", "precursor2 amount": "536.1 mg", "precursor3 name": "tetradecanoic acid", "precursor3 amount":"576.3 mg", "solution": "DI water", "pressure": "Not mentioned", "temperature": "Not mentioned", "time": "1 week"}, {"synthesis method": "drying", "pressure": "Not mentioned", "temperature": "Not mentioned", "atmosphere": "vacuum", "time": "Not mentioned"}], "yield": "68%", "chemical formula": "C104H142Ag3N71O95Cl7·12H2O"}]


Paragraph:Synthesis of {[Ni(bdpx)2(OH2)2]·2ClO4·2H2O}n (3)
A solution of Ni(ClO4)2·6H2O (139.6 mg, 0.4 mmol) in 4 mL of H2O was added slowly into a MeOH/H2O solution (6:1 v/v) of bdpx (100.2 mg, 0.4 mmol) without stirring. The mixture was left to stand at room temperature (RT) for crystallization. After several days, green plate-shaped crystals were filtered off and washed with water. Phase purity was established by XRPD. Yield 78%. Anal. Calcd C24H32NiN14O12 (761.56): C, 37.89; H, 4.24; N, 25.76%. Found: C, 37.82; H, 4.27; N, 25.49%.
Synthesis of {[Cu(bdpx)2(OH2)2]·2ClO4·2H2O}n (4)
4 was synthesized in a procedure analogous to that of 3 except that Cu(ClO4)2·6H2O (134.5 mg, 0.4 mmol) was used instead of Ni(ClO4)2·6H2O. Blue rod-shaped crystals were filtered off and washed with water. Yield 71%. Anal. Calcd C24H32CuN14O12 (767.08): C, 37.55; H, 4.20; N, 25.55%. Found: C, 37.50; H, 4.22; N, 25.33%.
JSON: [{"Mof name":"{[Ni(bdpx)2(OH2)2]·2ClO4·2H2O}n", "symbol":3, "processes":[{"synthesis method":"chemical synthesis", "precursor1": ("Ni(ClO4)2·6H2O", "139.6 mg", "0.4 mmol"), "precursor2": ("bdpx","100.2 mg", "0.4 mmol"), "solution": ["H2O", "MeOH/H2O solution (6:1 v/v)"], "pressure": "Not mentioned", "temperature":"room temperature", "time":"several days"}, {"synthesis method":"washing", "washing solution":"water", "amount":"Not mentioned"}]} ,{"Mof name":"{[Cu(bdpx)2(OH2)2]·2ClO4·2H2O}n", "symbol":4, "processes":[{"synthesis method":"chemical synthesis", "precursor": [["Cu(ClO4)2·6H2O", "134.5 mg", "0.4 mmol"],["bdpx","100.2 mg", "0.4 mmol"]], "solution": ["H2O", "MeOH/H2O solution (6:1 v/v)"], "pressure": "Not mentioned", "temperature":"room temperature", "time":"several days"}, {"synthesis method":"washing", "washing solution":"water", "amount":"Not mentioned"}]}]
"""