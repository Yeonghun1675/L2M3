PROMPT_TYPE = """Find all the processes used during synthesis. Each process unconditionally must belong to one of the elements in the following list:
{list_operation}

You must write processes in the above list.
If "Teflon-lined" or "seal" exists in the paragraph, it includes "solvothermal_synthesis".

Paragraph: A mixture of tris-(4-bromophenyl)amine (2.00 g, 4.15 mmol) and CuCN (1.70 g, 18.98 mmol) was heated at reflux in 25 mL of anhydrous dimethylformamide (DMF) for 6 h under a nitrogen atmosphere at 150 °C. Upon cooling to room temperature (RT), the FeCl3/H2O/ethanol (8.00 g/10 mL/8 mL) mixture solvent was added to the reaction mixture and then heated to 125 °C. Then, dilute hydrochloric acid (100 mL, 2 M) was added into the solution. The resulting mixture was extracted with CH2Cl2 (5 × 50 mL), washed with ethylenediaminetetraacetic acid-2Na aqueous solution (5 × 100 mL), evaporated under a rotary evaporator, and dried over anhydrous MgSO4. The crude product was purified by flash chromatography on silica gel using CH2Cl2 as an eluent to afford 0.90 g (67.8%) of tris-(4-cyanophenyl)amine as a primrose yellow powder.
List: ```JSON
["chemical_synthesis", "washing"]
```

Paragraph: A solution comprising compound X (0.025 g, 0.12 mmol), Cu(NO3)2·3H2O (0.045 g, 0.12 mmol), KOH (0.005 g, 0.12 mmol), and distilled water (15 mL) was placed in a 20 mL Teflon-lined autoclave and maintained at 90°C for a duration of 48 hours. Upon cooling the mixture to room temperature, well-formed blue prismatic crystals of compound Y were obtained, yielding 42% of the desired product.
List: ```JSON
["solvothermal_synthesis"]
```

Paragraph: The pH level was modified to 7.0 using ammonium hydroxide.
List: ```JSON
["pH_adjustment"]
```

Paragraph:{paragraph}
List: """


PROMPT_STRUCT = """Extract the relevant information about the synthesis of MOFs mentioned in the paragraph.

There are guidelines for output format:
- Output must be in the format {{"meta":{{"name":"", "symbol":"", "chemical formula":""}}, "processes": list, "yield": str,and "other properties": [str, str, ...]}}.
- The "process" list consists of several dictionaries. Each dictionary consists of {{"synthesis method": str, information(different according to synthesis method)}}.

For each process, you must follow these formats:
{format}


You must follow rules below:
- According to the synthesis type, information you must write is different.
- If there are several "meta"s in the text, you must write several dictionaries for each "meta".
- If the synthesis procedure for a particular material remains consistent (including "similar", "substitute", "instead of", etc.), import the same synthesis method for that material, but must change only the precursor or condition specified in the article.
- In each dictionary, you must include yield, chemical formula and other properties if such information is available.
- Based on the synthesis method, ensure to include any additional details related to {synthesis_type}.
- If there are more than two instances of a precursor, additive, surfactant, solution, solvent, or reducing agent, list all of them in a single dictionary.
- Remember, a precursor is measured in units of mass, while a solution is measured in units of volume.
- Never fabricate or add information that isn't present in the paragraph. Do not write the information in the example.
- If a range symbol like "4-6" is provided, produce separate results for each number in the range.
- When "Ln" or "M" appears in the paragraph, you should substitute them with the specified metals. ex) ChemLn (Ln=Pr(1), Gd(2), Dy(3), Er(4)), There are four chemicals; ChemPr, ChemGd, ChemDy, ChemEr
- If the terms "Teflon-lined" or "seal" appear in the paragraph, consider them indicative of "solvothermal_synthesis".

If you are uncertain, please reply with "I do not know".

Begin!

Paragraph: [Ag3(Z[6])2(TDA)3(Cl)2(H2O)10][Ag(TDA)(H2O)5]·6Cl·nH2O (2)

Z[6] (20 mg, 2.0 mmol) was dissolved in 4.0 mL of deionized (DI) water. Silver chloride (536.1 mg; 3.0 mmol) and tetradecanoic acid (576.3 mg, 2.0 mmol) were dissolved in 4.0 mL of DI water and added to the above Z[6] solution. Diluted sodium hydroxide was used to adjust the solution to pH 7 (±0.1). After a period of one week, octahedral crystals of compound 2 were formed. The resulting product was achieved in a yield of 68% based on Z[6], which was collected and dried under vacuum. Elemental analysis (calc., found) for C104H142Ag3N71O95Cl7·12H2O: C (25.87, 26.01), H (3.38, 3.50), and N (20.12, 20.25).
JSON:```JSON
[{{"meta":{{"name":"[Ag3(Z[6])2(TDA)3(Cl)2(H2O)10][Ag(TDA)(H2O)5]·6Cl·nH2O", "symbol":"2", "chemical formula": "C104H142Ag3N71O95Cl7·12H2O"}}, "processes": [{{"synthesis method": "chemical synthesis", "precursor":[{{"name":"Z[6]", "amount":"20", "unit":"mg"}}, {{"name":"Silver chloride", "amount":"536.1", "unit":"mg"}}, {{"name":"tetradecanoic acid", "amount":"576.3", "unit":"mg"}}], "solution":[{{"name":"DI water", "amount":"4.0", "unit":"mL"}}], "pressure": "", "temperature": "", "time": "1 week"}}, {{"synthesis method": "pH adjustment", "pH": "7", "modulator": "diluted sodium hydroxide"}}, {{"synthesis method": "drying", "pressure": "", "temperature": "", "atmosphere": "vacuum", "time": ""}}], "yield": "68%"}}]
```

Paragraph: Synthesis of ([Ni(bdpx)2(OH2)2]·2ClO4·2H2O)n (3)
A solution of Ni(ClO4)2·6H2O (139.6 mg, 0.4 mmol) in 4 mL of H2O was added slowly into a MeOH/H2O solution (6:1 v/v) of bdpx (100.2 mg, 0.4 mmol) without stirring. The mixture was left to stand at room temperature (RT) for crystallization. After several days, green plate-shaped crystals were filtered off and washed with water. Yield 78%. Anal. Calcd C24H32NiN14O12: C, 37.89; H, 4.24; N, 25.76%. Found: C, 37.82; H, 4.27; N, 25.49%.
Synthesis of ([Cu(bdpx)2(OH2)2]·2ClO4·2H2O)n (4)
4 was synthesized in a procedure analogous to that of 3 except that Cu(ClO4)2·6H2O (134.5 mg, 0.4 mmol) was used instead of Ni(ClO4)2·6H2O. Blue rod-shaped crystals were filtered off and washed with water. Yield 71%. Anal. Calcd C24H32CuN14O12: C, 37.55; H, 4.20; N, 25.55%. Found: C, 37.50; H, 4.22; N, 25.33%.
JSON:```JSON
[{{"meta":{{"name":"([Ni(bdpx)2(OH2)2]·2ClO4·2H2O)n", "symbol":"3", "chemical formula":"C24H32NiN14O12"}}, "processes":[{{"synthesis method": "chemical synthesis", "precursor":[{{"name":"Ni(ClO4)2·6H2O", "amount":"139.6", "unit":"mg"}}, {{"name":"bdpx", "amount":"100.2", "unit":"mg"}}], "solution": [{{"name":"H2O", "amount":"4", "unit":"mL"}}, {{"name":"MeOH/H2O solution", "amount":"6:1 v/v", "unit":""}}], "pressure": "", "temperature":"room temperature", "time":"several days"}}, {{"synthesis method":"washing", "washing solution":"water", "amount":""}}]}} ,{{"meta":{{"name":"([Cu(bdpx)2(OH2)2]·2ClO4·2H2O)n", "symbol":"4", "chemical formula":"C24H32CuN14O12"}}, "processes":[{{"synthesis method":"chemical synthesis", "precursor":[{{"name":"Cu(ClO4)2·6H2O", "amount":"134.5", "unit":"mg"}}, {{"name":"bdpx", "amount":"100.2", "unit":"mg"}}], "solution": [{{"name":"H2O", "amount":"4", "unit":"mL"}}, {{"name":"MeOH/H2O solution", "amount":"6:1 v/v", "unit":""}}], "pressure": "", "temperature":"room temperature", "time":"several days"}}, {{"synthesis method":"washing", "washing solution":"water", "amount":""}}]}}]
```

Paragraph: The synthesis of [(Ca(H2O)6)(CaLn(oda)3)2]·4H2O (Ln = Er (10), Ho (11), Yb (12)) was carried out as follows: A mixture of Ln2O3 (0.12 mmol), CaCl2·2H2O (50 mg, 0.35 mmol), and 2,2-oxydiacetic acid (90 mg, 0.65 mmol) was dissolved in 20 mL of water. The solution was placed in a Teflon-lined 50 mL stainless steel acid digestion vessel and heated at 130°C for 3 days. Subsequently, the clear solution was left to evaporate at room temperature, resulting in the formation of well-defined cubic crystals after several weeks. The yield ranged from 35% to 50%. Elemental analysis yielded the following results: Calculated for C28H52O40Ca3Ln2: C, 21.2; H, 3.3 (10); C, 21.0; H, 3.2 (11); C, 20.8; H, 3.1 (12). Found: C, 21.1; H, 3.5 (10); C, 21.0; H, 3.3 (11); C, 20.7; H, 3.0 (12)%.
JSON:```JSON
[{{"meta":{{"name":"(Ca(H2O)6)(CaEr(oda)3)2]·4H2O", "symbol":"10", "chemical formula":"C28H52O40Ca3Er2"}}, "processes":[{{"synthesis method": "solvothermal synthesis", "precursor":[{{"name":"Er2O3", "amount":"0.12", "unit":"mmol"}}, {{"name":"CaCl2·2H2O", "amount":"50", "unit":"mg"}}, {{"name":"2,2-oxydiacetic acid", "amount":"90", "unit":"mg"}}], "solvent":[{{"name":"water", "amount":"20", "unit":"mL"}}], "reducing agent":[{{"name":"", "amount":"", "unit":""}}], "surfactant":[{{"name":"", "amount":"", "unit":""}}], "pressure":"", "temperature":"130°C", "time":"3 days", "heating rate":"", "cooling rate":""}}], "yield":"35% to 50%"}}, {{"meta":{{"name":"(Ca(H2O)6)(CaHo(oda)3)2]·4H2O", "symbol":"11", "chemical formula":"C28H52O40Ca3Ho2"}}, "processes":[{{"synthesis method": "solveothermal synthesis", "precursor":[{{"name":"Ho2O3", "amount":"0.12", "unit":"mmol"}}, {{"name":"CaCl2·2H2O", "amount":"50", "unit":"mg"}}, {{"name":"2,2-oxydiacetic acid", "amount":"90", "unit":"mg"}}], "solvent":[{{"name":"water", "amount":"20", "unit":"mL"}}], "reducing agent":[{{"name":"", "amount":"", "unit":""}}], "surfactant":[{{"name":"", "amount":"", "unit":""}}], "pressure":"", "temperature":"130°C", "time":"3 days", "heating rate":"", "cooling rate":""}}], "yield":"35% to 50%"}}, {{"meta":{{"name":"(Ca(H2O)6)(CaYb(oda)3)2]·4H2O", "symbol":"12", "chemical formula":"C28H52O40Ca3Yb2"}}, "processes":[{{"synthesis method": "solveothermal synthesis", "precursor":[{{"name":"Yb2O3", "amount":"0.12", "unit":"mmol"}}, {{"name":"CaCl2·2H2O", "amount":"50", "unit":"mg"}}, {{"name":"2,2-oxydiacetic acid", "amount":"90", "unit":"mg"}}], "solvent":[{{"name":"water", "amount":"20", "unit":"mL"}}], "reducing agent":[{{"name":"", "amount":"", "unit":""}}], "surfactant":[{{"name":"", "amount":"", "unit":""}}], "pressure":"", "temperature":"130°C", "time":"3 days", "heating rate":"", "cooling rate":""}}], "yield":"35% to 50%"}}]
```

Paragraph: {paragraph}
JSON: """


FT_TYPE = """Find all the processes used during synthesis. Each process unconditionally must belongs to one of the elements in the following list:
['pH_adjustment', 'filtration', 'ball_milling', 'centrifugation', 'chemical_mechanical_polishing', 'chemical_synthesis', 'chemical_vapor_deposition', 'drying', 'electrochemical_deposition', 'heat_treatment', 'microwave_assisted_synthesis', 'mixing', 'rinsing', 'solvothermal_synthesis', 'sol_gel_synthesis', 'sonication', 'sonochemical_synthesis', 'thermal_evaporation', 'wet_etching', 'washing', 'cooling']"""


FT_HUMAN = "{paragraph}"
