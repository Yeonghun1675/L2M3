# chemical formula는 기본적으로 물어볼 거라서 포함 안시켰음.
CRYSTAL_CATEGORIZE = """From the provided markdown table, generate a Python list of item names with data present. You must exclude absent items and return an empty list if any key items are missing. Names of items must be one of following:
- chemical_formula: empirical formula of materials.
- chemical_formula weight: sum of the atomic weights of the elements present in its chemical formula.
- space_group: a mathematical description of the symmetries inherent in a periodic crystal lattice.
- crystal_system: symmetrical and geometrical arrangements within the crystal lattice of materials.
- lattice_parameters: cell lengths and angles
- cell_volume: cell volume of materials.
- density: bulk density of materials.
- crystal_size: crystal size of materials.
- crystal_color: color of crystal.

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
Table 1

Crystal data and structure refinements for complexes 1–2.

| Compound | 1 | 2 |
| --- | --- | --- |
| Space group | P2<sub>1</sub>/c | R -3m |
| a (Å) | 13.990 (5) | 19.504 (3) |
| b (Å) | 13.749 (4) | 19.504 (3) |
| c (Å) | 14.073 (5) | 37.930 (5) |
| α (°) | 90.00 | 90.00 |
| β (°) | 110.538(13) | 90.00 |
| γ (°) | 90.00 | 120.00 |
| T (K) | 200 | 200 |
| V (Å<sup>3</sup>) | 2534.8 (15) | 12,496 (3) |
| Z | 4 | 18 |
| D<sub>c</sub> (g·cm<sup>-3</sup>) | 1.299 | 0.956 |
| μ (mm<sup>-1</sup>) | 1.011 | 0.911 |
| F(0 0 0) | 1024 | 3667 |
| R<sub>int</sub> | 0.1132 | 0.0830 |
| Parameters refined | 370 | 168 |
| Goodness-of-fit | 1.048 | 1.132 |

a R<sub>1</sub> = Σ|F<sub>o</sub> - F<sub>c</sub>| / Σ|F<sub>o</sub>|.
b wR<sub>2</sub> = |Σw(|F<sub>o</sub><sup>2</sup> - F<sub>c</sub><sup>2</sup>)| / Σw(F<sub>o</sub><sup>2</sup>)<sup>1/2</sup>, where w = 1/[σ<sup>2</sup>(F<sub>o</sub><sup>2</sup>) + (aP)<sup>2</sup> + bP]. P = (F<sub>o</sub><sup>2</sup> + 2F<sub>c</sub><sup>2</sup>)/3.
List: ["space_group", "lattice_parameters", "cell_volume", "density"]

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
{{paragraph}}
List:"""


CRYSTAL_EXTRACT = """From the given Markdown table, extract information related to {{prop}} for each materials. Extracted information should be in structured json format as in the example below. When giving output, you should not use ellipses to shorten the content. You must conclude with "<END>".
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
        "formula weight": [
            {
                "value": "404.07",
            },
        ]
        "crystal system": [
            {
                "value": "Triclinic",
            },
        ]
    },
    {
        "meta": {
            "name": "",
            "symbol": "2",
            "chemical formula": "C₈H₉NdNO₉",
        },
        "formula weight": [
            {
                "value": "407.40",
            },
        ]
        "crystal system": [
            {
                "value": "Triclinic",
            },
        ]
    },
    {
        "meta": {
            "name": "",
            "symbol": "3",
            "chemical formula": "C₈H₉EuNO₉",
        },
        "formula weight": [
            {
                "value": "415.12",
            },
        ]
        "crystal system": [
            {
                "value": "Triclinic",
            },
        ]
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
        "crystal system": [
            {
                "value": "monoclinic",
            },
        ]
        "crystal size: [
            {
                "value": "0.32 x 0.28 x 0.24",
                "unit": "mm"
            }
        ]
    },
]
<END>

Input:
{{paragraph}}

Output:"""
