example_1 = {
    "contain": ["surface area", "porosity", "pore volume", "gas adsorption", "adsorption energy"],
    "content": """
Input:
["surface area", "porosity", "pore volume", "gas adsorption", "adsorption energy"],
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
["conversion", "reaction yield"],
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
["peak spectrum"],
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
["gas adsorption", "selectivity"],
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
["simulation parameters"],
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
["simulation parameters"],
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
["surface area"],
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
["henry coefficient"],
Table 5. Henry Coefficients (K<sub>H</sub>) × 10<sup>–3</sup> [mol/kg/Pa] of CO<sub>2</sub> in the M<sub>2</sub>(DHFUMA) vs M<sub>2</sub>(DOBDC) Series at 313 and 400 K

| metal | DHFUMA 313 K | DHFUMA 400 K | DOBDC 313 K | DOBDC 400 K |
|-------|--------------|--------------|------------|------------|
| Mg    | 10.7         | 0.22         | 1.56       | 0.064      |
| Fe    | 1.8          | 0.07         | 0.20       | 0.017      |

Output: ```JSON
[
    {
        "meta": {
            "name": "Mg<sub>2</sub>(DHFUMA)",
            "symbol": "",
            "chemical formula": "",
        },
        "henry coefficient": [
            {
                "value": "10.7",
                "unit": "mol/kg/Pa",
                "condition": "313 K",
                "gas type": "CO<sub>2</sub>",
            },
            {
                "value": "0.22",
                "unit": "mol/kg/Pa",
                "condition": "400 K",
                "gas type": "CO<sub>2</sub>",
            },
        ],
    },
    {
        "meta": {
            "name": "Mg<sub>2</sub>(DOBDC)",
            "symbol": "",
            "chemical formula": "",
        },
        "henry coefficient": [
            {
                "value": "1.56",
                "unit": "mol/kg/Pa",
                "condition": "313 K",
                "gas type": "CO<sub>2</sub>",
            },
            {
                "value": "0.064",
                "unit": "mol/kg/Pa",
                "condition": "400 K",
                "gas type": "CO<sub>2</sub>",
            },
        ],
    },
    {
        "meta": {
            "name": "Fe<sub>2</sub>(DHFUMA)",
            "symbol": "",
            "chemical formula": "",
        },
        "henry coefficient": [
            {
                "value": "1.8",
                "unit": "mol/kg/Pa",
                "condition": "313 K",
                "gas type": "CO<sub>2</sub>",
            },
            {
                "value": "0.07",
                "unit": "mol/kg/Pa",
                "condition": "400 K",
                "gas type": "CO<sub>2</sub>",
            },
        ],
    },
    {
        "meta": {
            "name": "Fe<sub>2</sub>(DOBDC)",
            "symbol": "",
            "chemical formula": "",
        },
        "henry coefficient": [
            {
                "value": "0.20",
                "unit": "mol/kg/Pa",
                "condition": "313 K",
                "gas type": "CO<sub>2</sub>",
            },
            {
                "value": "0.017",
                "unit": "mol/kg/Pa",
                "condition": "400 K",
                "gas type": "CO<sub>2</sub>",
            },
        ],
    },
]
```
"""
}


example_9 = {
    "contain": ["pore diameter", "pore volume"],
    "content": """
Input:
["pore diameter", "pore volume"],
Table 1. Pore Diameters, and Pore Volumes for NU-1000 and SALI-Derived Variants

| MOF        | BJH pore diameter (Å) | pore vol. (cm<sup>3</sup> g<sup>–1</sup>) |
|------------|-----------------------|-------------------------------------------|
| NU-1000    | 31                    | 1.46                                      |
| SALI-BA    | 28                    | 1.21                                      |
| SALI-PPA@2 | 30                    | 1.27                                      |

Output: ```JSON
[
    {
        "meta": {
            "name": "NU-1000",
            "symbol": "",
            "chemical formula": "",
        },
        "pore diameter": [
            {
                "value": "31",
                "unit": "Å",
                "condition": "",
            },
        ],
        "pore volume": [
            {
                "probe": "",
                "value": "1.46",
                "unit": "cm<sup>3</sup> g<sup>–1</sup>",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "SALI-BA",
            "symbol": "",
            "chemical formula": "",
        },
        "pore diameter": [
            {
                "value": "28",
                "unit": "Å",
                "condition": "",
            },
        ],
        "pore volume": [
            {
                "probe": "",
                "value": "1.21",
                "unit": "cm<sup>3</sup> g<sup>–1</sup>",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "SALI-PPA@2",
            "symbol": "",
            "chemical formula": "",
        },
        "pore diameter": [
            {
                "value": "30",
                "unit": "Å",
                "condition": "",
            },
        ],
        "pore volume": [
            {
                "probe": "",
                "value": "1.27",
                "unit": "cm<sup>3</sup> g<sup>–1</sup>",
                "condition": "",
            },
        ],
    },
]
```
"""
}


example_10 = {
    "contain": ["gas adsorption", "etc"],
    "content": """
Input:
["gas adsorption", "etc"],
Table 4. Adsorption Uptakes of CH<sub>4</sub> and Working Capacities (Considering Desorption at 5 bar) at Room Temperature for 1 and 2

|           | P = 35 bar |           | P = 65 bar |           |
|-----------|------------|-----------|------------|-----------|
|           | uptake     | working capacity | uptake     | working capacity |
| UiO-67    | 102        | 72        | 127        | 104       |
| UiO-67-Me | 113        | 75        | 135        | 104       |

Output: ```JSON
[
    {
        "meta": {
            "name": "UiO-67",
            "symbol": "",
            "chemical formula": "",
        },
        "gas adsorption": [
            {
                "adsorbate": "CH<sub>4</sub>",
                "adsorbed amount": "102",
                "unit": "",
                "temperature": "room temperature",
                "pressure": "35 bar",
                "condition": "",
            },
            {
                "adsorbate": "CH<sub>4</sub>",
                "adsorbed amount": "127",
                "unit": "",
                "temperature": "room temperature",
                "pressure": "65 bar",
                "condition": "",
            },
        ],
        "etc": [
            {
                "property name": "CH4 working capacity",
                "value": "72",
                "unit": "",
                "condition": "35 bar, desorption at 5bar, room temperature",
            },
            {
                "property name": "CH4 working capacity",
                "value": "104",
                "unit": "",
                "condition": "65 bar, desorption at 5bar, room temperature",
            },
        ],
    },
    {
        "meta": {
            "name": "UiO-67-Me",
            "symbol": "",
            "chemical formula": "",
        },
        "gas adsorption": [
            {
                "adsorbate": "CH<sub>4</sub>",
                "adsorbed amount": "113",
                "unit": "",
                "temperature": "room temperature",
                "pressure": "35 bar",
                "condition": "",
            },
            {
                "adsorbate": "CH<sub>4</sub>",
                "adsorbed amount": "135",
                "unit": "",
                "temperature": "room temperature",
                "pressure": "65 bar",
                "condition": "",
            },
        ],
        "etc": [
            {
                "property name": "CH4 working capacity",
                "value": "75",
                "unit": "",
                "condition": "35 bar, desorption at 5bar, room temperature",
            },
            {
                "property name": "CH4 working capacity",
                "value": "104",
                "unit": "",
                "condition": "65 bar, desorption at 5bar, room temperature",
            },
        ],
    },
]
```
"""
}


example_11 = {
    "contain": ["adsorption energy", "etc"],
    "content": """
Input:
["adsorption energy", "etc"],
Table 5. Heats of Adsorption (kJ mol–1) Calculated by Extrapolation of the Low Pressure Data of the Virial Isotherms (n vs ln­(p/n)) for 1 and 3 at 25, 40, and 70 °C

|         | CH<sub>4</sub> | CO<sub>2</sub> |
|---------|----------------|----------------|
| UiO-67  | 15.2           | 23.6           |
| UiO-67-BN | 20.3           | 20.6           |

Output: ```JSON
[
    {
        "meta": {
            "name": "UiO-67",
            "symbol": "",
            "chemical formula": "",
        },
        "adsorption energy": [
            {
                "value": "15.2",
                "unit": "kJ mol-1",
                "condition": "",
                "gas type": "CH<sub>4</sub>",
            },
            {
                "value": "23.6",
                "unit": "kJ mol-1",
                "condition": "",
                "gas type": "CO<sub>2</sub>",
            },
        ],
    },
    {
        "meta": {
            "name": "UiO-67-BN",
            "symbol": "",
            "chemical formula": "",
        },
        "adsorption energy": [
            {
                "value": "20.3",
                "unit": "kJ mol-1",
                "condition": "",
                "gas type": "CH<sub>4</sub>",
            },
            {
                "value": "20.6",
                "unit": "kJ mol-1",
                "condition": "",
                "gas type": "CO<sub>2</sub>",
            },
        ],
    },
]
```
"""
}


example_12 = {
    "contain": ["density", "etc"],
    "content": """
Input:
["density", "etc"],
Table 2. Comparison of the results for HKUST-1 and IRMOF1

| property | HKUST-1 PB | HKUST-1 Zeo++ | IRMOF-1 PB | IRMOF-1 Zeo++ |
|----------|------------|--------------|------------|--------------|
| density [g/cm³] | 0.884 | 0.884 | 0.593 | 0.593 |
| CPU time [s] | 116.847 | 683.857 | 92.104 | 672.437 |

Output: ```JSON
[
    {
        "meta": {
            "name": "HKUST-1",
            "symbol": "",
            "chemical formula": "",
        },
        "density": [
            {
                "value": "0.884",
                "unit": "g/cm³",
                "condition": "PB",
            },
            {
                "value": "0.884",
                "unit": "g/cm³",
                "condition": "Zeo++",
            },
        ],
        "etc": [
            {
                "property name": "CPU time",
                "value": "116.847",
                "unit": "s",
                "condition": "PB",
            },
            {
                "property name": "CPU time",
                "value": "683.857",
                "unit": "s",
                "condition": "Zeo++",
            },
        ],
    },
    {
        "meta": {
            "name": "IRMOF1",
            "symbol": "",
            "chemical formula": "",
        },
        "density": [
            {
                "value": "0.593",
                "unit": "g/cm³",
                "condition": "PB",
            },
            {
                "value": "0.593",
                "unit": "g/cm³",
                "condition": "Zeo++",
            },
        ],
        "etc": [
            {
                "property name": "CPU time",
                "value": "92.104",
                "unit": "s",
                "condition": "PB",
            },
            {
                "property name": "CPU time",
                "value": "672.437",
                "unit": "s",
                "condition": "Zeo++",
            },
        ],
    },
]
```
"""
}


example_13 = {
    "contain": ["crystal size"],
    "content": """
Input:
["crystal size"],
Table 1
Crystal data and structure refinement for the [Hg(μ-4,4′-bipy)(μ-AcO)(AcO)]n·n/2H2O (1)

| Identification code | compound 1 |
|---------------------|------------|
| Empirical formula   | C28H30Hg2N4O9 |
| Crystal size (mm)   | 0.32 × 0.28 × 0.24 |

Output: ```JSON
[
    {
        "meta": {
            "name": "[Hg(μ-4,4′-bipy)(μ-AcO)(AcO)]n·n/2H2O",
            "symbol": "compound 1",
            "chemical formula": "C28H30Hg2N4O9",
        },
        "crystal size": [
            {
                "value": "0.32 x 0.28 x 0.24",
                "unit": "mm"
                "condition": "",
            }
        ],
    },
]
```
"""
}


example_14 = {
    "contain": ["material color", "material shape"],
    "content": """
Input:
["material color", "material shape"],
Table 1. Data for isolated copper(I) complexes of pyrazine carboxamide

| Complex | Colour |
|---------|--------|
| Cu(pyza)2Cl (1) | red fine needle-like crystals |
| Cu(pyza)2Br (2) | red needle-like crystals |
| Cu(pyza)2I (3) | red crystals |

Output: ```JSON
[
    {
        "meta": {
            "name": "Cu(pyza)2Cl",
            "symbol": "1",
            "chemical formula": "",
        },
        "material color": [
            {
                "value": "red",
                "condition": "",
            }
        ],
        "material shape": [
            {
                "value": "fine needle-like crystals",
                "condition": "",
            }
        ],
    },
    {
        "meta": {
            "name": "Cu(pyza)2Br",
            "symbol": "2",
            "chemical formula": "",
        },
        "material color": [
            {
                "value": "red",
                "condition": "",
            }
        ],
        "material shape": [
            {
                "value": "needle-like crystals",
                "condition": "",
            }
        ],
    },
    {
        "meta": {
            "name": "Cu(pyza)2I",
            "symbol": "3",
            "chemical formula": "",
        },
        "material color": [
            {
                "value": "red",
                "condition": "",
            }
        ],
        "material shape": [
            {
                "value": "crystals",
                "condition": "",
            }
        ],
    },
]
```
"""
}


example_15 = {
    "contain": ["space group", "etc"],
    "content": """
Input:
["space group", "etc"],
Table 5. Data for the Metal Shell of Metal Complexes of Uncharged Erythritol

| stoichiometry | space group | M−Cl distance (Å) |
|---------------|-------------|-------------------|
| 2CaCl<sub>2</sub>·C<sub>4</sub>H<sub>10</sub>O<sub>4</sub>·4H<sub>2</sub>O | P2<sub>1</sub>/c | 2.7171 |
| CaCl<sub>2</sub>·C<sub>4</sub>H<sub>10</sub>O<sub>4</sub>·4H<sub>2</sub>O | C2/c | 2.418 |
| CaCl<sub>2</sub>·2C<sub>4</sub>H<sub>10</sub>O<sub>4</sub>·4H<sub>2</sub>O | Fddd | 2.416 |

Output: ```JSON
[
    {
        "meta": {
            "name": "2CaCl<sub>2</sub>·C<sub>4</sub>H<sub>10</sub>O<sub>4</sub>·4H<sub>2</sub>O",
            "symbol": "",
            "chemical formula": "",
        },
        "space group": [
            {
                "value": "P2<sub>1</sub>/c",
                "condition": "",
            }
        ],
        "etc": [
            {
                "property name": "M-Cl distance",
                "value": "2.7171",
                "unit": "Å",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "CaCl<sub>2</sub>·C<sub>4</sub>H<sub>10</sub>O<sub>4</sub>·4H<sub>2</sub>O",
            "symbol": "",
            "chemical formula": "",
        },
        "space group": [
            {
                "value": "C2/c",
                "condition": "",
            }
        ],
        "etc": [
            {
                "property name": "M-Cl distance",
                "value": "2.418",
                "unit": "Å",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "CaCl<sub>2</sub>·2C<sub>4</sub>H<sub>10</sub>O<sub>4</sub>·4H<sub>2</sub>O",
            "symbol": "",
            "chemical formula": "",
        },
        "space group": [
            {
                "value": "Fddd",
                "condition": "",
            }
        ],
        "etc": [
            {
                "property name": "M-Cl distance",
                "value": "2.416",
                "unit": "Å",
                "condition": "",
            },
        ],
    },
]
```
"""
}


example_16 = {
    "contain": ["decomposition temperature", "elastic constant"],
    "content": """
Input:
["decomposition temperature", "elastic constant"],
Table 1. Decomposition Temperature and the Mechanical Properties of Hybrid Membranes

| sample name       | MNS content (in weight) | T<sub>d</sub> (°C) | Young’s modulus (GPa) | maximum elongation (%) |
|-------------------|-------------------------|---------------------|-----------------------|-------------------------|
| SNF-PAEK          | 0                       | 244.93              | 0.90 ± 0.14           | 118 ± 26                |
| MNS@SNF-PAEK-1%   | 1%                      | 247.72              | 0.91 ± 0.17           | 123 ± 19                |

Output: ```JSON
[
    {
        "meta": {
            "name": "SNF-PAEK",
            "symbol": "",
            "chemical formula": "",
        },
        "decomposition temperature": [
            {
                "value": "244.93",
                "unit": "°C",
                "type": "",
                "condition": "MNS content 0%",
            }
        ],
        "elastic constant": [
            {
                "value": "0.90 ± 0.14",
                "unit": "GPa",
                "condition": "MNS content 0%",
                "type": "Young's modulus",
            },
            {
                "value": "118 ± 26",
                "unit": "%",
                "condition": "MNS content 0%",
                "type": "maximum elongation",
            },
        ],
    },
    {
        "meta": {
            "name": "MNS@SNF-PAEK-1%",
            "symbol": "",
            "chemical formula": "",
        },
        "decomposition temperature": [
            {
                "value": "247.72",
                "unit": "°C",
                "type": "",
                "condition": "MNS content 1%",
            }
        ],
        "elastic constant": [
            {
                "value": "0.91 ± 0.17",
                "unit": "GPa",
                "condition": "MNS content 1%",
                "type": "Young's modulus",
            },
            {
                "value": "123 ± 19",
                "unit": "%",
                "condition": "MNS content 1%",
                "type": "maximum elongation",
            },
        ],
    },
]
```
"""
}


example_17 = {
    "contain": ["magnetic susceptibility", "magnetic moment"],
    "content": """
Input:
["magnetic susceptibility", "magnetic moment"],
Table 3. Main Magnetic Parameters for 1 and 2

|   | χT (300 K)/cm³ K mol⁻¹ | M (70 kOe, 1.8 K)/μB |
|---|------------------------|----------------------|
| 1 | 4.73                   |  6.02                |
| 2 | 5.99                   |  0.82                |

Output: ```JSON
[
    {
        "meta": {
            "name": "1",
            "symbol": "",
            "chemical formula": "",
        },
        "magnetic susceptibility": [
            {
                "value": "4.73",
                "unit": "cm³ K mol⁻¹",
                "temperature": "300 K",
                "condition": "",
            },
        ],
        "magnetic moment": [
            {
                "value": "6.02",
                "unit": "μB",
                "temperature": "1.8 K",
                "condition": "70 kOe",
            },
        ],
    },
    {
        "meta": {
            "name": "2",
            "symbol": "",
            "chemical formula": "",
        },
        "magnetic susceptibility": [
            {
                "value": "5.99",
                "unit": "cm³ K mol⁻¹",
                "temperature": "300 K",
                "condition": "",
            },
        ],
        "magnetic moment": [
            {
                "value": "0.82",
                "unit": "μB",
                "temperature": "1.8 K",
                "condition": "70 kOe",
            },
        ],
    },
]
```
"""
}


example_18 = {
    "contain": ["proton conductivity", "etc"],
    "content": """
Input:
["proton conductivity", "etc"],
Table 4. Proton Conductivity (σ) and Methanol Permeability (P) of Different Types of Hybrid PEMs Studied in Previous Works

| hybrid PEMs      | σ (S·cm–1) | P (10–7 cm2·s–1) | references |
|------------------|------------|------------------|------------|
| MNS@SNF-PAEK-3%  | 0.198      | 5.28             | this work  |
| SPEEK/SHGO       | 0.136      | 30.83            | [36]       |

Output: ```JSON
[
    {
        "meta": {
            "name": "MNS@SNF-PAEK-3%",
            "symbol": "",
            "chemical formula": "",
        },
        "proton conductivity": [
            {
                "value": "0.198",
                "unit": "S·cm–1",
                "temperature": "",
                "RH": "",
                "Ea": "",
                "guest": "",
            },
        ],
        "etc": [
            {
                "property name": "Methanol Permeability (P)",
                "value": "5.28",
                "unit": "10–7 cm2·s–1",
                "condition": "",
            },
        ],
    },
    {
        "meta": {
            "name": "SPEEK/SHGO",
            "symbol": "",
            "chemical formula": "",
        },
        "proton conductivity": [
            {
                "value": "0.136",
                "unit": "S·cm–1",
                "temperature": "",
                "RH": "",
                "Ea": "",
                "guest": "",
            },
        ],
        "etc": [
            {
                "property name": "Methanol Permeability (P)",
                "value": "30.83",
                "unit": "10–7 cm2·s–1",
                "condition": "",
            },
        ],
    },
]
```
"""
}


example_19 = {
    "contain": ["topology"],
    "content": """
Input:
["topology"],
Table 1. Nets Assigned to MOFs Described in the Text

| MOF     | unit  | all node |
|---------|-------|----------|
| MOF-505 | Figure b | fof   |
| JUC-62  | Figure b | fog   |

Output: ```JSON
[
    {
        "meta": {
            "name": "MOF-505",
            "symbol": "",
            "chemical formula": "",
        },
        "topology": [
            {
                "value": "fof",
                "condition": "all node",
            },
        ],
    },
    {
        "meta": {
            "name": "JUC-62",
            "symbol": "",
            "chemical formula": "",
        },
        "topology": [
            {
                "value": "fog",
                "condition": "all node",
            },
        ],
    },
]
```
"""
}


example_20 = {
    "contain": ["formation energy"],
    "content": """
Input:
["formation energy"],
Table 1. Formation Energies for Species As Calculated by DFT

| species | formation energy (kcal/mol) |
|---------|-----------------------------|
| (H<sub>4</sub>TTFTB)<sub>2</sub> | –1.62 |
| (H<sub>4</sub>TTFTB)<sub>2</sub><sup>•+</sup> | –5.52 |

Output: ```JSON
[
    {
        "meta": {
            "name": "(H<sub>4</sub>TTFTB)<sub>2</sub>",
            "symbol": "",
            "chemical formula": "",
        },
        "formation energy": [
            {
                "value": "-1.62",
                "unit": "kcal/mol",
                "condition": "calculate by DFT",
            },
        ],
    },
    {
        "meta": {
            "name": "(H<sub>4</sub>TTFTB)<sub>2</sub><sup>•+</sup>",
            "symbol": "",
            "chemical formula": "",
        },
        "formation energy": [
            {
                "value": "-5.52",
                "unit": "kcal/mol",
                "condition": "calculate by DFT",
            },
        ],
    },
]
```
"""
}


