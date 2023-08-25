example_1 = {
    "contain": ["surface area", "porosity", "pore volume", "gas adsorption", "etc"],
    "content": """
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
| Total H2 adsorption in wt% (1 bar/20 bar/total) | 0.79/1.33/1.45 | 0.29/0.78/0.83 |
| ΔH_ads (kJ/mol) | 7.81–5.87 | 5.88–4.94 |

[^a]: Calculated from single crystal structures with PLATON [36].
[^b]: Calculated from N2 isotherms.

Output:
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
                "probe": "",
                "value": "0.183",
                "unit": "cm^3/g",
            },
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
        "etc": [
            {
                "property name": "ΔH_ads",
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
                "probe": "",
                "value": "0.135",
                "unit": "cm^3/g",
            },
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
        "etc": [
            {
                "property name": "ΔH_ads",
                "value": "5.88–4.94"
                "unit": "kJ/mol",
                "condition": "",
            },
        ]
    }
]
<END>
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
| 4     |             | 4        | 58 (50)           |

[^a]: Conditions: Cyclohexene (1 mmol), H2O2 (1 mmol), CH3COOH (0.5 mmol) and C1 (0.1 mol%) in 2 mL CH3CN at 0°C.

Output:
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
    {
        "meta": {
            "name": "",
            "symbol": "4",
            "chemical formula": "",
        },
        "conversion": [
            {
                "value": "58",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "0°C" ,
                "solvent": "CH3CN",
                "time": "4h",
            },
        ],
        "yield": [
            {
                "value": "50",
                "unit": "%",
                "substrate": "Cyclohexene, H2O2, CH3COOH, C1",
                "catalyst": "",
                "pressure": "",
                "temperature": "0°C" ,
                "solvent": "CH3CN",
                "time": "4h",
            },
        ]
    },
]
<END>
""",
}


example_3 = {
    "contain": ["etc"],
    "content": """
Input:
Table 3

13C NMR spectral data (in ppm) of 1 and K4edta.

| Compounds | –CH2N | –NCH2CO2 | –CO2 |
| --- | --- | --- | --- |
| 1 | 57.3(3.6) | 64.4(4.3) | 183.0 (4.5) |
| [edta]4- | 53.7 | 60.1 | 178.5 |
|  |  |  |  |
| Solid |
| 1 | 57.5, 53.6 | 62.5 | 184.9, 179.8 |

Output:
[
    {
        "meta": {
            "name": "",
            "symbol": "1",
            "chemical formula": ""
        },
        "etc": [
            {
                "property name": "13C NMR spectral data",
                "value": "-CH2N: 57.3(3.6), -NCH2CO2: 64.4(4.3), -CO2: 183.0 (4.5)",
                "unit": "ppm",
                "condition": ""
            },
            {
                "property name": "13C NMR spectral data",
                "value": "-CH2N: 57.5, 53.6, -NCH2CO2: 62.5, -CO2: 184.9, 179.8",
                "unit": "ppm",
                "condition": "Solid"
            },
        ],
    },
    {
        "meta": {
            "name": "[edta]4-",
            "symbol": "",
            "chemical formula": ""
        },
        "etc": [
            {
                "property name": "13C NMR spectral data",
                "value": "-CH2N: 53.7, -NCH2CO2: 60.1, -CO2: 178.5",
                "unit": "ppm",
                "condition": ""
            }
        ],
    },
]
<END>
""",
}
