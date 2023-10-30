# chemical formula는 기본적으로 물어볼 거라서 포함 안시켰음.
CRYSTAL_CATEGORIZE = """From the provided markdown table, generate a Python list of item names with data present. You must exclude absent items and return an empty list if any key items are missing. Names of items must be one of following:
- chemical_formula: empirical formula of materials.
- chemical_formula_weight: sum of the atomic weights of the elements present in its chemical formula.
- space_group: a mathematical description of the symmetries inherent in a periodic crystal lattice.
- crystal_system: symmetrical and geometrical arrangements within the crystal lattice of materials.
- lattice_parameters: cell lengths and angles
- cell_volume: cell volume of materials.
- density: bulk density of materials.
- crystal_size: crystal size of materials.
- material_color: The color of material crystal or bulk
- material_shape: The shape of material crystal or bulk. e.g., cylinder, plate

Begin!

Input:
**Table 1: Crystallographic data for complexes 1–6**

|   | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Empirical formula | C₈H₉PrNO₉ | C₈H₉NdNO₉ | C₈H₉EuNO₉ | C₈H₉GdNO₉ | C₈H₉TbNO₉ | C₈H₉ErNO₉ |
| Formula weight | 404.07 | 407.40 | 415.12 | 420.41 | 422.08 | 430.42 |
| Crystal system | Triclinic | Triclinic | Triclinic | Triclinic | Triclinic | Triclinic |
List : ["chemical_formula", "chemical_formula_weight", "crystal_system"]

Input:
Table 1. Crystallographic Data for Mg and Mn 5-Aminonaphthalene-2-sulfonate Salts

| Compound | [Mg(H<sub>2</sub>O)<sub>6</sub>](H<sub>2</sub>NC<sub>10</sub>H<sub>6</sub>SO<sub>3</sub>)<sub>2</sub>·6H<sub>2</sub>O | [Mn(H<sub>2</sub>O)<sub>6</sub>](H<sub>2</sub>NC<sub>10</sub>H<sub>6</sub>SO<sub>3</sub>)<sub>2</sub>·6H<sub>2</sub>O |
|----------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| CCDC no. | 276650                                                                                        | 276651                                                                                        |
| Color/shape | Mauve/plate | Mauve/plate |
| Empirical formula | C<sub>20</sub>H<sub>40</sub>N<sub>2</sub>MgO<sub>18</sub>S<sub>2</sub> | C<sub>20</sub>H<sub>40</sub>N<sub>2</sub>MnO<sub>18</sub>S<sub>2</sub> |
| Formula weight | 684.97 | 715.60 |
| Temperature (K) | 110(2) | 293(2) |
| Crystal system | Monoclinic | Monoclinic |
| Space group | P2<sub>1</sub>/c | P2<sub>1</sub>/c |
| a (Å) | 14.1329(18) | 14.249(3) |
| b (Å) | 8.5789(11) | 8.5940(17) |
| c (Å) | 12.4880(17) | 12.505(3) |
| β (°) | 93.374(3) | 93.30(3) |
| Volume (Å<sup>3</sup>) | 1511.5(3) | 1528.8(5) |
| Formula units/cell (Z) | 2 | 2 |
| D<sub>calc</sub> (g/cm<sup>3</sup>) | 1.505 | 1.554 |
| μ(cm<sup>−1</sup>) | 2.79 | 6.49 |
| Transmission factors | 0.967–0.981 | 0.830–0.890 |
| Diffractometer | CCD area detector | CCD area detector |
| θrange for data (°) | 1.44–27.54 | 2.77–27.53 |
| Reflections measured | 9489 (±h, ±k, ±l) | 7317 (±h, ±k, ±l) |
| Independent/observed reflections | 3486 (R<sub>int</sub>=0.091)/2104 [I &gt; 2σ(I)] | 3364 (R<sub>int</sub>=0.054)/2413 [I &gt; 2σ(I)] |
| Data/restraints/parameters | 3486/0/276 | 3364/0/274 |
| Goodness-of-fit on F<sup>2</sup> | 1.04 | 1.08 |
| R indices (R1; wR2) | 0.074; 0.141 | 0.071; 0.125 |
List: ["material_color", "material_shape", "chemical_formula", "chemical_formula_weight", "crystal_system", "space_group", "lattice_parameters", "cell_volume", "density"]

Input:
Table 1

Crystal data and structure refinement for compound 1.

| Empirical formula | C<sub>6</sub>H<sub>14</sub>N<sub>2</sub>[In<sub>2</sub>(HPO<sub>3</sub>)<sub>3</sub>(C<sub>2</sub>O<sub>4</sub>)] |
|-------------------|-----------------------------------------------------------------------------------------------|
| Formula weight    | 671.79                                                                                        |
| Temperature       | 298(2) K                                                                                      |
| Wavelength        | 0.71073 Å                                                                                     |
| Crystal system    | Orthorhombic                                                                                  |
| a (Å)             | 12.4143(13)                                                                                   |
| b (Å)             | 7.7166(8)                                                                                     |
| c (Å)             | 18.327(2)                                                                                     |
| Absorption coefficient (mm<sup>-1</sup>) | 2.974                                                      |
| F(0 0 0)          | 1304                                                                                          |
| Crystal size (mm) | 0.13 × 0.11 × 0.09                                                                            |
| θ range (°)       | 2.86–28.30                                                                                    |
| Limiting indices  | -15 ≤ h ≤ 14, -10 ≤ k ≤ 10, -24 ≤ l ≤ 5                                                       |
| Data/restraints/parameters | 2415/3/262                                                                 |
| Goodness-of-fit on F<sup>2</sup> | 1.010                                                           |
| Final R indices [I > 2σ(I)]<sup>a,b</sup> | R<sub>1</sub> = 0.0282, wR<sub>2</sub> = 0.0632                                        |
| R indices (all data)<sup>a,b</sup> | R<sub>1</sub> = 0.0334, wR<sub>2</sub> = 0.0656                                          |
| Largest diff. peak and hole | 1.455 and -0.926 eÅ<sup>-3</sup>                                                               |

a R<sub>1</sub> = Σ||F<sub>o</sub>|-|F<sub>c</sub>||/Σ|F<sub>o</sub>|.
List: ["chemical_formula", "chemical_formula_weight", "crystal_system", "lattice_parameters", "crystal_size"]

Input:
Atomic Parameters Resulting from the Rietveld Refinement of the UiO-66-NDC-0BC MOF in the Fm3̅m Space Group (No. 225): Fractional Coordinates (x, y, z), Isotropic Atomic Displacement Parameters (Uiso), Occupancy Factors, Site Degeneration and Number of Atoms in the Unit Cell[^a]

| atom | x       | y       | z       | Uiso (Å^2) | occupancy factor | site | atoms/unit cell |
|------|---------|---------|---------|------------|------------------|------|-----------------|
| Zr   | 0.1176(1) | 0       | 0       | 0.0129(8) | 1.00             | 24e  | 24              |
| O1   | 0.1699(3) | 0       | 0.0903(3) | 0.022(2)  | 1.00             | 96j  | 96              |
| O2   | 0.0641(4) | –x      | –x      | 0.056(5)  | 1.00             | 32f  | 32              |
| C11  | 0.1504(2) | 0       | –x      | 0.003(4)  | 0.87             | 48h  | 41.76           |
| C12  | 0.2012(2) | 0       | x       | 0.043(7)  | 0.87             | 48h  | 41.76           |
| C13  | 0.2603(3) | 0.0280(5) | 0.1890(3) | 0.023(6)  | 0.435            | 192l | 83.52           |
| C14  | 0.2724(5) | 0.056(1) | 0.1296(4) | 0.24(3)[^b] | 0.217            | 192l | 41.76           |
| C15  | 0.3317(7) | 0.084(2) | 0.1174(6) | 0.36(5)[^b] | 0.217            | 192l | 41.76           |
List: []

Input:
{{paragraph}}
List:"""


CRYSTAL_EXTRACT = """From the given Markdown table, extract information related to {{prop}} for each materials. Extracted information should be in structured json format as in the format below. When giving output, you should not use ellipses to shorten the content. When lanthanides (Ln) or halogens (X) or metal (M) come out, indicate by substituting.
{{format}}

Begin!

Input:
**Table 1: Crystallographic data for complexes 1–6**

|   | 1 | 2 | 3 |
|---|---|---|---|
| Empirical formula | C₈H₉PrNO₉ | C₈H₉NdNO₉ | C₈H₉EuNO₉ |
| Formula weight | 404.07 | 407.40 | 415.12 |
| Crystal system | Triclinic | Triclinic | Triclinic |

Output: ```JSON
[
    {
        "meta": {
            "name": "",
            "symbol": "1",
            "chemical formula": "C₈H₉PrNO₉",
        },
        "chemical formula weight": [
            {
                "value": "404.07",
                "unit": "",
                "condition": "",
            },
        ],
        "crystal system": [
            {
                "value": "Triclinic",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "",
            "symbol": "2",
            "chemical formula": "C₈H₉NdNO₉",
        },
        "chemical formula weight": [
            {
                "value": "407.40",
                "unit": "",
                "condition": "",
            },
        ],
        "crystal system": [
            {
                "value": "Triclinic",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "",
            "symbol": "3",
            "chemical formula": "C₈H₉EuNO₉",
        },
        "chemical formula weight": [
            {
                "value": "415.12",
                "unit": "",
                "condition": "",
            },
        ],
        "crystal system": [
            {
                "value": "Triclinic",
                "condition": "",
            },
        ],
    },
]
```

Input:
Table 1
Crystal data and structure refinement for the [Hg(μ-4,4′-bipy)(μ-AcO)(AcO)]n·n/2H2O (1)

| Identification code | compound 1 |
|---------------------|------------|
| Empirical formula   | C28H30Hg2N4O9 |
| Crystal system      | monoclinic |
| Crystal size (mm)   | 0.32 × 0.28 × 0.24 |

Output: ```JSON
[
    {
        "meta": {
            "name": "[Hg(μ-4,4′-bipy)(μ-AcO)(AcO)]n·n/2H2O",
            "symbol": "compound 1",
            "chemical formula": "C28H30Hg2N4O9",
        },
        "crystal system": [
            {
                "value": "monoclinic",
                "condition": "",
            },
        ],
        "crystal size: [
            {
                "value": "0.32 x 0.28 x 0.24",
                "unit": "mm"
                "condition": "",
            }
        ],
    },
]
```

Input:
Table 1. Results for [Ln(abdc)(Habdc), nH2O]∞ with Ln=La–Pr and n =10.[^*]

| Ln | MW (gmol−1) |
|----|-------------|
| La | 678.33      |
| Ce | 679.54      |
| Pr | 680.33      |

Output: ```JSON
[
    {
        "meta": {
            "name": "",
            "symbol": "",
            "chemical formula": "[La(abdc)(Habdc), nH2O]",
        },
        "chemical formula weight": [
            {
                "value": "678.33",
                "unit": "",
                "condition": "n=10",
            },
        ]
    },
    {
        "meta": {
            "name": "",
            "symbol": "",
            "chemical formula": "[Ce(abdc)(Habdc), nH2O]",
        },
        "chemical formula weight": [
            {
                "value": "679.54",
                "unit": "",
                "condition": "n=10",
            },
        ]
    },
    {
        "meta": {
            "name": "",
            "symbol": "",
            "chemical formula": "[Pr(abdc)(Habdc), nH2O]",
        },
        "chemical formula weight": [
            {
                "value": "680.33",
                "unit": "",
                "condition": "n=10",
            },
        ]
    },
]
```

Input:
{{paragraph}}

Output:"""


FT_TYPE = """From the provided markdown table, generate a Python list of item names with data present. You must exclude absent items and return an empty list if any key items are missing. Names of items must be one of following:
['chemical_formula', 'chemical_formula_weight', 'space_group', 'crystal_system', 'lattice_parameters', 'cell_volume', 'density', 'crystal_size', 'material_color', 'material_shape']"""


FT_HUMAN = "{paragraph}"
