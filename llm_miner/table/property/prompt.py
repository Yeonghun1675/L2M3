PROPERTY_CATEGORIZE = """From the provided markdown table, generate a Python list of item names with data present. You must exclude absent items and return an empty list if any key items are missing. Names of items must be one of following:

- synthesis condition: synthesis condition of materials
- surface area: surface area of materials. ex) SA, BET surface area, Langmuir surface area
- total pore volume: pore volume of materials ex) PV.
- crystal size: crystal size of materials.
- pore diameter: pore diameter of materials ex) LCD, PLD.
- gas adsorption: amount of gas uptake, gas storage, gas adsorption, selective gas uptake of materials.
- thermal property: decomposition temperature, thermal conductivity, glass transition temperature of materials ex) Tg, TDT.
- mechanical property: properties related to application of forces. ex) Young's modulus, Poisson's ratio, stress.
- selectivity: selectivity of materials. 'Selective' is not equal to 'selectivity'
- catalytic activity: turnover frequency of materials ex) TOF.
- density: bulk density of materials.
- porosity: fraction of total volume of material that is occupied by pores or voids ex) accessible volume fraction, void fraction.
- topology: manner in which the metal nodes and organic linkers are connected in a three-dimensional arrangement.
- magentic property: properties of materials in the presence of a magnetic field.
- optical property: properties of materials in response to electromagnetic radiation.
- etc: Other properties not included in the live above but can be represented by numeric values.

You must not include the same property several times. If there are surface_area and BET surface_area in the paragraph at the same time, you must include 'surface_area' once. Only properties must be included and the name of materials must not be included. If same property of different materials appears, you must include the property only once. If certain property you find does not have a value, please do not include that property. For example, even if selectivity is stated in the paragraph, do not write selectivity when specific value is not written. Do not be confused between gas adsorption and selectivity. Gas adsorption is a property that has a unit and selectivity is unitless. Even though there is a word 'selectivity', it is not always selectivity. If there is a value with unit, it is gas adsorption.
If you're uncertain, please return empty list.

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
List : ['chemical formula', 'chemical formula weight', 'crystal system']

Input:
List: ['space group', 'lattice parameters', 'cell volume', 'density']

Input:
List: ['chemical formula', 'chemical formula weight', 'crystal system', 'lattice parameters', 'crystal size']

Input:
{{paragraph}}
List:"""


PROPERTY_EXTRACT="""From the given Markdown table, extract information related to {{prop}} for each materials. Extracted information should be in structured json format as in the example below. You must conclude with "<END>".
{{format}}

Begin!

Input:
**Table 1: Crystallographic data for complexes 1–6**

|   | 1 | 2 | 3 | 
|---|---|---|---|
| Empirical formula | C₈H₉PrNO₉ | C₈H₉NdNO₉ | C₈H₉EuNO₉ |
| Formula weight | 404.07 | 407.40 | 415.12 |
| Crystal system | Triclinic | Triclinic | Triclinic |

Output:
[
    {
        "meta": {
            "name": "",
            "symbol": "1",
            "chemical formula": "C₈H₉PrNO₉",
        },
        "formula weight": {
            "value": "404.07",
        },
        "crystal system": {
            "value": "Triclinic",
        },
    },
    {
        "meta": {
            "name": "",
            "symbol": "2",
            "chemical formula": "C₈H₉NdNO₉",
        },
        "formula weight": {
            "value": "407.40",
        },
        "crystal system": {
            "value": "Triclinic",
        },
    },
    {
        "meta": {
            "name": "",
            "symbol": "3",
            "chemical formula": "C₈H₉EuNO₉",
        },
        "formula weight": {
            "value": "415.12",
        },
        "crystal system": {
            "value": "Triclinic",
        },
    },
]
<END>

Input:
Table 1
Crystal data and structure refinement for the [Hg(μ-4,4′-bipy)(μ-AcO)(AcO)]n·n/2H2O (1)

| Identification code | compound 1 |
|---------------------|------------|
| Empirical formula   | C28H30Hg2N4O9 |
| Crystal system      | monoclinic |
| Crystal size (mm)   | 0.32 × 0.28 × 0.24 |

Output:
[
    {
        "meta": {
            "name": "[Hg(μ-4,4′-bipy)(μ-AcO)(AcO)]n·n/2H2O",
            "symbol": "compound 1",
            "chemical formula": "C28H30Hg2N4O9",
        },
        "crystal system": {
            "value": "monoclinic",
        },
        "crystal size: {
            "value": "0.32 x 0.28 x 0.24",
            "unit": "mm"
        }
    },
]
<END>

Input:
{{paragraph}}

Output:"""
