example_1 = {
    "contain": ["surface area", "porosity", "pore volume", "gas adsorption", "adsorption energy"],
    "content": """
Input:
Table 2

Structure and H2 absorption parameters for compounds I and II.

| Compound | I    | II   |
|----------|------|------|
| Calculated surface area | 480.4 | 462.7 |
| BET surface area[^a] (m^2/g) | 405.7 | 445.3 |
| Calcd. free space (%) | 24.7 | 16.8 |
| Pore volume[^a] (cm^3/g) | 0.104 | 0.108 |
| Total H2 adsorption in wt% (1 bar/20 bar/total) | 0.79/1.33/1.45 | 0.29/0.78/0.83 |
| ΔH_ads (kJ/mol) | 7.81–5.87 | 5.88–4.94 |

[^a]: Calculated from N2 isotherms.

Output: ```JSON
[
    {
        "meta": {
            "name": "",
            "symbol": "I",
            "chemical formula": "",
        },
        "surface area": [
            {
                "type": "calculated",
                "probe": "",
                "value": "480.4",
                "unit": "",
            },
            {
                "type": "BET",
                "probe": "N2",
                "value": "405.7",
                "unit": "m^2/g",
            },
        ]
        "porosity": [
            {
                "probe": "",
                "value": "24.7",
                "unit": "%",
            },
        ]
        "pore volume": [
            {
                "probe": "N2",
                "value": "0.104",
                "unit": "cm^3/g",
            },
        ]
        "gas adsorption": [
            {
                "adsorbate": "H2",
                "adsorbed amount": "0.79",
                "unit": "wt%",
                "temperature": "",
                "pressure": "1 bar",
            },
            {
                "adsorbate": "H2",
                "adsorbed amount": "1.33",
                "unit": "wt%",
                "temperature": "",
                "pressure": "20 bar",
            },
            {
                "adsorbate": "H2",
                "adsorbed amount": "1.45",
                "unit": "wt%",
                "temperature": "",
                "pressure": "total",
            },
        ]
        "adsorption energy": [
            {
                "value": "7.81–5.87"
                "unit": "kJ/mol",
                "condition": "",
            },
        ]
    },
    {
        "meta": {
            "name": "",
            "symbol": "II",
            "chemical formula": "",
        },
        "surface area": [
            {
                "type": "calculated",
                "probe": "",
                "value": "462.7",
                "unit": "",
            },
            {
                "type": "BET",
                "probe": "N2",
                "value": "445.3",
                "unit": "m^2/g",
            },
        ]
        "porosity": [
            {
                "probe": "",
                "value": "16.8",
                "unit": "%",
            },
        ]
        "pore volume": [
            {
                "probe": "N2",
                "value": "0.108",
                "unit": "cm^3/g",
            },
        ]
        "gas adsorption": [
            {
                "adsorbate": "H2",
                "adsorbed amount": "0.29",
                "unit": "wt%",
                "temperature": "",
                "pressure": "1 bar",
            },
            {
                "adsorbate": "H2",
                "adsorbed amount": "0.78",
                "unit": "wt%",
                "temperature": "",
                "pressure": "20 bar",
            },
            {
                "adsorbate": "H2",
                "adsorbed amount": "0.83",
                "unit": "wt%",
                "temperature": "",
                "pressure": "total",
            },
        ]
        "adsorption energy": [
            {
                "value": "5.88–4.94"
                "unit": "kJ/mol",
                "condition": "",
            },
        ]
    }
]
```
""",
}


example_2 = {
    "contain": ["conversion", "reaction yield"],
    "content": """
Input:
Table 7

Cyclohexene oxidation in varying reaction temperature and time.[^a]

| Entry | Temperature | Time (h) | Conv. (Yield[^b])% |
|-------|-------------|----------|-------------------|
| 1     | -30°C       | 1        | 33 (30)           |
| 2     |             | 2        | 45 (41)           |
| 3     |   0°C       | 3        | 55 (49)           |

[^a]: Conditions: Cyclohexene (1 mmol), H2O2 (1 mmol), CH3COOH (0.5 mmol) and C1 (0.1 mol%) in 2 mL CH3CN at 0°C.

Output: ```JSON
[
    {
        "meta": {
            "name": "",
            "symbol": "1",
            "chemical formula": "",
        },
        "conversion": [
            {
                "value": "33",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "-30°C" ,
                "solvent": "CH3CN",
                "time": "1h",
            },
        ],
        "yield": [
            {
                "value": "30",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "-30°C" ,
                "solvent": "CH3CN",
                "time": "1h",
            },
        ]
    },
    {
        "meta": {
            "name": "",
            "symbol": "2",
            "chemical formula": "",
        },
        "conversion": [
            {
                "value": "45",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "-30°C" ,
                "solvent": "CH3CN",
                "time": "2h",
            },
        ],
        "yield": [
            {
                "value": "41",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "-30°C" ,
                "solvent": "CH3CN",
                "time": "2h",
            },
        ],
    },
    {
        "meta": {
            "name": "",
            "symbol": "3",
            "chemical formula": "",
        },
        "conversion": [
            {
                "value": "55",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "0°C" ,
                "solvent": "CH3CN",
                "time": "3h",
            },
        ],
        "yield": [
            {
                "value": "49",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "0°C" ,
                "solvent": "CH3CN",
                "time": "3h",
            },
        ],
    },
]
```
""",
}


example_3 = {
    "contain": ["peak spectrum"],
    "content": """
Input:
Table 3

13C NMR spectral data (in ppm) of 1 and K4edta.

| Compounds | –CH2N | –NCH2CO2 | –CO2 |
|-----------|-------|----------|------|
| 1         | 57.3(3.6) | 64.4(4.3) | 183.0 (4.5) |
| [edta]4-  | 53.7 | 60.1 | 178.5 |
|  |  |  |  |
| Solid |
| 1 | 57.5, 53.6 | 62.5 | 184.9, 179.8 |

Output: ```JSON
[
    {
        "meta": {
            "name": "",
            "symbol": "1",
            "chemical formula": "",
        },
        "peak spectrum": [
            {
                "value": "-CH2N: 57.3(3.6), -NCH2CO2: 64.4(4.3), -CO2: 183.0 (4.5)",
                "unit": "ppm",
                "type": "13C NMR",
                "condition": "",
            },
            {
                "value": "-CH2N: 57.5, 53.6, -NCH2CO2: 62.5, -CO2: 184.9, 179.8",
                "unit": "ppm",
                "type": "13C NMR",
                "condition": "Solid",
            },
        ],
    },
    {
        "meta": {
            "name": "[edta]4-",
            "symbol": "",
            "chemical formula": "",
        },
        "peak spectrum": [
            {
                "value": "-CH2N: 53.7, -NCH2CO2: 60.1, -CO2: 178.5",
                "unit": "ppm",
                "type": "13C NMR",
                "condition": "",
            },
        ],
    },
]
```
""",
}


example_4 = {
    "contain": ["gas adsorption", "selectivity"],
    "content": """
Input:
Table 1. Adsorption Capacity and Selectivity Calculated Based on the Dry and Humid C2H4/C2H6 Breakthrough Experiments at 293 K and 1 bar

|              | C2H4 (mmol/g) | C2H6 (mmol/g) | selectivity (C2H4/C2H6) |
|--------------|--------------|--------------|------------------------|
| CuBTC (dry)  | 4.22         | 1.80         | 2.3                    |
| Ni-MOF-74 (dry) | 3.00       | 1.08         | 2.8                    |
| CuBTC (humid) | 3.95        | 1.53         | 2.6                    |
| Ni-MOF-74 (humid) | 2.65    | 0.49         | 5.4                    |

Output: ```JSON
[
    {
        "meta": {
            "name": "CuBTC",
            "symbol": "",
            "chemical formula": "",
        },
        "gas adsorption": [
            {
                "adsorbate": "C2H4",
                "adsorbed amount": "4.22",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "dry",
            },
            {
                "adsorbate": "C2H6",
                "adsorbed amount": "1.80",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "dry",
            },
            {
                "adsorbate": "C2H4",
                "adsorbed amount": "3.95",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "humid",
            },
            {
                "adsorbate": "C2H6",
                "adsorbed amount": "1.53",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "humid",
            },
        ],
        "selectivity": [
            {
                "value": "2.3",
                "unit": "",
                "substrate": "C2H4/C2H6",
                "catalyst": "",
                "pressure": "1 bar",
                "temperature": "293 K",
                "solvent": "",
                "time": "",
                "condition": "dry",
            },
            {
                "value": "2.6",
                "unit": "",
                "substrate": "C2H4/C2H6",
                "catalyst": "",
                "pressure": "1 bar",
                "temperature": "293 K",
                "solvent": "",
                "time": "",
                "condition": "humid",
            },
        ],
    },
    {
        "meta": {
            "name": "Ni-MOF-74",
            "symbol": "",
            "chemical formula": "",
        },
        "gas adsorption": [
            {
                "adsorbate": "C2H4",
                "adsorbed amount": "3.00",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "dry",
            },
            {
                "adsorbate": "C2H6",
                "adsorbed amount": "1.08",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "dry",
            },
            {
                "adsorbate": "C2H4",
                "adsorbed amount": "2.65",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "humid",
            },
            {
                "adsorbate": "C2H6",
                "adsorbed amount": "0.49",
                "unit": "mmol/g",
                "temperature": "293 K",
                "pressure": "1 bar",
                "condition": "humid",
            },
        ],
        "selectivity": [
            {
                "value": "2.8",
                "unit": "",
                "substrate": "C2H4/C2H6",
                "catalyst": "",
                "pressure": "1 bar",
                "temperature": "293 K",
                "solvent": "",
                "time": "",
                "condition": "dry",
            },
            {
                "value": "5.4",
                "unit": "",
                "substrate": "C2H4/C2H6",
                "catalyst": "",
                "pressure": "1 bar",
                "temperature": "293 K",
                "solvent": "",
                "time": "",
                "condition": "humid",
            },
        ],
    },
]
```
"""
}


example_5 = {
    "contain": ["simulation parameters"],
    "content": """
Input:
Table 1. Lennard-Jones Parameters for the Adsorbates Used, Where ε is the LJ Well Depth, k<sub>B</sub> is the Boltzmann Constant, and σ is the Molecular Diameter

| adsorbate | σ (Å) | ε/k<sub>B</sub> (K) | ref |
|-----------|-------|--------------------|-----|
| H<sub>2</sub> | 2.958 | 36.7 | [^ref29] |
| CH<sub>4</sub> | 3.73 | 148.0 | [^ref30] |

Output: ```JSON
[
    {
        "meta": {
            "name": "H<sub>2</sub>",
            "symbol": "",
            "chemical formula": "H2",
        },
        "simulation parameters": [
            {
                "symbol": "σ",
                "value": "2.958",
                "unit": "Å",
                "type": "Lennard-Jones Parameter",
            },
            {
                "symbol": "ε/k<sub>B</sub>",
                "value": "36.7",
                "unit": "K",
                "type": "Lennard-Jones Parameter",
            },
        ],
    },
    {
        "meta": {
            "name": "CH<sub>4</sub>",
            "symbol": "",
            "chemical formula": "CH4",
        },
        "simulation parameters": [
            {
                "symbol": "σ",
                "value": "3.73",
                "unit": "Å",
                "type": "Lennard-Jones Parameter",
            },
            {
                "symbol": "ε/k<sub>B</sub>",
                "value": "148.0",
                "unit": "K",
                "type": "Lennard-Jones Parameter",
            },
        ],
    },
]
```
"""
}


example_6 = {
    "contain": ["simulation parameters"],
    "content": """
Input:
Table 2. Parameters for the Langmuir Isotherm Model of Two Different Dyes

| adsorbate | parameters | 298.15 K | 308.15 K | 318.15 K |
|-----------|------------|----------|----------|----------|
| R6G       | Q<sub>0</sub> (mmol·g<sup>–1</sup>) | 0.1679 | 0.1749 | 0.1850 |
|           | R<sup>2</sup> | 0.9930 | 0.9992 | 0.9989 |
| RB        | Q<sub>0</sub> (mmol·g<sup>–1</sup>) | 0.1434 | 0.1528 | 0.1601 |
|           | R<sup>2</sup> | 0.9979 | 0.9936 | 0.9987 |

Output: ```JSON
[
    {
        "meta": {
            "name": "R6G",
            "symbol": "",
            "chemical formula": "",
        },
        "simulation parameters": [
            {
                "symbol": "Q<sub>0</sub>",
                "value": "0.1679(298.15K), 0.1749(308.15K), 0.1850(318.15K)",
                "unit": "mmol·g<sup>–1</sup>",
                "type": "Langmuir Isotherm Model Parameter",
            },
            {
                "symbol": "R<sup>2</sup>",
                "value": "0.9930(298.15K), 0.9992(308.15K), 0.9989(318.15K)",
                "unit": "",
                "type": "Langmuir Isotherm Model Parameter",
            },
        ],
    },
    {
        "meta": {
            "name": "RB",
            "symbol": "",
            "chemical formula": "",
        },
        "simulation parameters": [
            {
                "symbol": "Q<sub>0</sub>",
                "value": "0.1434(298.15K), 0.1528(308.15K), 0.1601(318.15K)",
                "unit": "mmol·g<sup>–1</sup>",
                "type": "Langmuir Isotherm Model Parameter",
            },
            {
                "symbol": "R<sup>2</sup>",
                "value": "0.9979(298.15K), 0.9936(308.15K), 0.9987(318.15K)",
                "unit": "",
                "type": "Langmuir Isotherm Model Parameter",
            },
        ],
    },
]
```
"""
}


example_7 = {
    "contain": ["surface area"],
    "content": """
Input:
Table 1. Summary of Calculated Geometric Surface Areas for Ultrahigh Surface Area MOFs

| MOF    | geometric surface area (m²g⁻¹) | ref       |
|--------|--------------------------------|-----------|
| NU-110 | 6229                           | [6]       |
| NU-109 | 6175                           | [6]       |

Output: ```JSON
[
    {
        "meta": {
            "name": "NU-110",
            "symbol": "",
            "chemical formula": "",
        },
        "surface area": [
            {
                "type": "calculated geometric",
                "probe": "",
                "value": "6229",
                "unit": "m²g⁻¹",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "NU-109",
            "symbol": "",
            "chemical formula": "",
        },
        "surface area": [
            {
                "type": "calculated geometric",
                "probe": "",
                "value": "6175",
                "unit": "m²g⁻¹",
                "condition": "",
            },
        ],
    },
]
```
"""
}


example_8 = {
    "contain": ["henry coefficient"],
    "content": """
Input:
Table 5. Henry Coefficients (K<sub>H</sub>) × 10<sup>–3</sup> [mol/kg/Pa] of CO<sub>2</sub> in the M<sub>2</sub>(DHFUMA) vs M<sub>2</sub>(DOBDC) Series at 313 and 400 K

| metal | DHFUMA 313 K | DHFUMA 400 K | DOBDC 313 K | DOBDC 400 K |
|-------|--------------|--------------|------------|------------|
| Mg    | 10.7         | 0.22         | 1.56       | 0.064      |
| Fe    | 1.8          | 0.07         | 0.20       | 0.017      |

Output: ```JSON
[
    {
        "meta": {
            "name": "NU-110",
            "symbol": "",
            "chemical formula": "",
        },
        "henry coefficient": [
            {
                "value": "6229",
                "unit": "mol/kg/Pa",
                "condition": "313 K",
            },
        ],
    },
]
```
"""
}






# Table 1. BET Surface Areas, Pore Diameters, and Pore Volumes for NU-1000 and SALI-Derived Variants

# | MOF      | ligand       | ligand:Zr<sub>6</sub><xref rid="t1fn1"></xref> | BET surface area (m<sup>2</sup> g<sup>–1</sup>) | BJH pore diameter (Å) | pore vol. (cm<sup>3</sup> g<sup>–1</sup>)<xref rid="t1fn1"></xref> |
# |----------|--------------|----------------------------------------------|------------------------------------------------|-----------------------|-----------------------------------------------------------------------|
# | NU-1000  | –OH, −H<sub>2</sub>O |                                              | 2145                                           | 31                    | 1.46                                                                  |
# | SALI-BA  | PhCO<sub>2</sub>–   | 4.0                                          | 2005                                           | 28                    | 1.21                                                                  |
# | SALI-PPA@2 | PhPO<sub>2</sub>(OH)– | 2.4                                        | 1920                                           | 30                    | 1.27                                                                  |



# Table 4. Adsorption Uptakes of CH<sub>4</sub> and Working Capacities (Considering Desorption at 5 bar) at Room Temperature for 1 and 2[^a]

# |           | P = 35 bar |           | P = 65 bar |           |
# |-----------|------------|-----------|------------|-----------|
# |           | uptake     | working capacity | uptake     | working capacity |
# | UiO-67    | 102        | 72        | 127        | 104       |
# | UiO-67-Me | 113        | 75        | 135        | 104       |

# [^a]: Volumes are given in cm<sup>3</sup>(STP) cm<sup>–3</sup>.



# Table 5. Heats of Adsorption (kJ mol–1) Calculated by Extrapolation of the Low Pressure Data of the Virial Isotherms (n vs ln­(p/n)) for 1 and 3 at 25, 40, and 70 °C

# |         | CH<sub>4</sub> | CO<sub>2</sub> |
# |---------|----------------|----------------|
# | UiO-67  | 15.2           | 23.6           |
# | UiO-67-BN | 20.3           | 20.6           |




# "['selectivity', 'henry_coefficient', 'etc']"
# Table 1. Virial Graph Analysis of Compound 1A

# | temperature (K) | adsorbate | A₀ ln(mol g⁻¹ Pa⁻¹) | Henry's const Kₕ (mol g⁻¹ Pa⁻¹) | R²   | Sᵢⱼ |
# |-----------------|-----------|-------------------|-------------------------------|------|-----|
# | 273             | CO₂       | -17.45994         | 2.6 × 10⁻⁸                   | 0.988|     |
# | 273             | CH₄       | -20.79051         | 9.3497 × 10⁻¹⁰               | 0.846| 28  |
# | 273             | H₂        | -23.04742         | 9.7866 × 10⁻¹¹               | 0.972| 266 |

# a. The selectivity for CO₂ (i) over different gases (j) calculated as Sᵢⱼ = Kₕ (CO₂)/Kₕ(j).
