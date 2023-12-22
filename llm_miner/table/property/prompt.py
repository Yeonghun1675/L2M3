PROPERTY_CATEGORIZE = """From the provided markdown table, generate a Python list of item names with data present. You must exclude absent items and return an empty list if any key items are missing. Names of items must be one of following:

{{explanation}}

You must not include the same property several times. If there are surface_area and BET surface_area in the paragraph at the same time, you must include "surface_area" once. Only properties must be included and the name of materials must not be included. If certain property you found does not have a value, please do not include that property. For example, even if selectivity is stated in the paragraph, do not write selectivity when specific value is not written. Do not be confused between gas adsorption and selectivity. Gas adsorption is a property that has a unit and selectivity is unitless. Even though there is a word "selectivity", it is not always selectivity. If there is a value with unit, it is gas adsorption.

Begin!

Input:
Table 2

Structure and H2 absorption parameters for compounds I and II.

| Compound | I    | II   |
|----------|------|------|
| Calculated surface area | 480.4 | 462.7 |
| BET surface area[^b] (m^2/g) | 405.7 | 445.3 |
| Calcd. free space[^a] (%) | 24.7 | 16.8 |
| Pore volume[^a] (cm^3/g) | 0.183 | 0.135 |
| Pore volume[^b] (cm^3/g) | 0.104 | 0.108 |
| Pore volume[^c] (cm^3/g) | 0.141 | 0.114 |
| Total H2 adsorption in wt% (1 bar/20 bar/total) | 0.79/1.33/1.45 | 0.29/0.78/0.83 |
| ΔH_ads (kJ/mol) | 7.81–5.87 | 5.88–4.94 |
| K_H (mol/g·Pa) | 1.4312×10^-6 | 3.61863×10^-7 |
| A_0/ln (mol/g·Pa) | -13.457 | -14.832 |
| A_1 (g/mol) | -395.06 | -256.56 |
| W_0[^d] (wt%) | 1.342 | 0.791 |
| βE_0 (kJ/mol) | 5.4 | 4.4 |
| q_st,(I)=1/e[^e] (kJ/mol) | 6.3 | 5.3 |

[^a]: Calculated from single crystal structures with PLATON [36].
[^b]: Calculated from N2 isotherms.
[^c]: Calculated from H2 isotherms.
[^d]: Estimated value from Langmuir fitting.
[^e]: The ΔHv of gas at its bp was used (H2 0.92 kJ/mol at 20 K)
List : ["surface_area", "porosity", "pore_volume", "gas_adsorption", "adsorption_energy", "henry_coefficient", "etc"]

Input:
Table 4

Cyanosilylation of benzaldehyde in the presence of different Mg-MOF loadings.

| Entry | Cat. mol % | TMSCN | Temp.(°C) | Time (h) | Conv.% |
|-------|------------|-------|-----------|----------|--------|
| 1     | 1          | 2 eq  | r.t.      | 2        | >99    |
| 2     | 0.5        | 2 eq  | r.t.      | 2        | >99    |
| 3     | 0.1        | 2 eq  | r.t.      | 2        | >99    |

Determined by GC based on the carbonyl substrate.
List: ["conversion"]

Input:
Table 2

Adsorption properties of NENU-28, NENU-3, NENU-29, and Cu3(BTC)2.

|                  | SA<sub>BET</sub><sup>a</sup> | Methanol | Ethanol | 1-propanol<sup>d</sup> | 2-propanol | Cyclohexane | Benzene | Toluene |
|------------------|-----------------------------|----------|---------|------------------------|-------------|-------------|---------|---------|
|                  |                             | 298K     | 308K    | ΔH<sub>ads</sub><sup>c</sup> | 298K        | 308K        | ΔH<sub>ads</sub> |         |         |
| NENU-28          | 470                         | 6.70     | 5.92    | 43.66                  | 4.78        | 4.17        | 40.64   | 3.62    | 2.69    | 1.70    | 3.42    | 2.89    |
| NENU-29          | 466                         | 6.28     | 5.58    | 40.57                  | 4.25        | 3.87        | 38.52   | 2.98    | 1.91    | 1.64    | 3.38    | 2.78    |
| NENU-3           | 405                         | 5.89     | 4.74    | 37.55                  | 3.97        | 3.38        | 36.28   | 0.61    | 0.41    | 1.58    | 3.29    | 2.65    |
| Cu3(BTC)2        | 1507                        | 5.14     | 4.04    | 35.27                  | 3.54        | 2.92        | 34.51   | –       | –       | 1.48    | 3.21    | 2.54    |

a Obtained from the N2 isotherms at 77K, m2 g<sup>-1</sup>.
b mmol g<sup>-1</sup>.
c kJ mol<sup>-1</sup>.
d at 298K, mmol g<sup>-1</sup>.
List: ["surface_area", "gas_adsorption", "adsorption_energy"]

Input:
Table 7

Cyclohexene oxidation in varying reaction temperature and time.[^a]

| Entry | Temperature | Time (h) | Conv. (Yield[^b])% |
|-------|-------------|----------|-------------------|
| 1     | -30°C       | 1        | 33 (30)           |
| 2     |             | 2        | 45 (41)           |
| 3     |             | 3        | 55 (49)           |
| 4     |             | 4        | 58 (50)           |
| 5     | 0°C         | 1        | 55 (55)           |
| 6     |             | 2        | 70 (70)           |
| 7     |             | 3        | 75 (71)           |
| 8     |             | 4        | 77 (68)           |
| 9     | 30°C        | 1        | 25 (18)           |
| 10    |             | 4        | 33 (21)           |

[^a]: Conditions: Cyclohexene (1 mmol), H2O2 (1 mmol), CH3COOH (0.5 mmol) and C1 (0.1 mol%) in 2 mL CH3CN at 0°C within 2 h.
[^b]: Yields based on the epoxides formed.
List: ["conversion", "reaction_yield"]

Input:
{{paragraph}}
List:"""


PROPERTY_EXTRACT = """From the given Markdown table, extract information related to {{prop}} for each materials. Extracted information should be in structured json format as in the Format below but when presenting the output, strictly refrain from using ellipsis. When lanthanides (Ln) or halogens (X) or metal (M) come out, indicate by substituting.
{{format}}

Begin!

{{examples}}

Input:
{{prop}}\n
{{paragraph}}

Output:"""


FT_TYPE = """From the provided markdown table, generate a Python list of item names with data present. You must exclude absent items and return an empty list if any key items are missing. Names of items must be one of following:
['proton_conductivity', 'elastic_constant', 'conversion', 'crystal_size', 'decomposition_temperature', 'density', 'gas_adsorption', 'heat_capacity', 'magnetic_moment', 'magnetic_susceptibility', 'material_color', 'material_shape', 'simulation_parameters', 'pore_diameter', 'pore_volume', 'porosity', 'reaction_yield', 'selectivity', 'space_group', 'peak_spectrum', 'surface_area', 'thermal_conductivity_coefficient', 'thermal_expansion_coefficient', 'topology', 'formation_energy', 'henry_coefficient', 'adsorption_energy', 'etc']"""


FT_HUMAN = "{paragraph}"
