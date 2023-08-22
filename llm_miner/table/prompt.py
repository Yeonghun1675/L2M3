# XML table이 너무 길어서 여기서는 예제 안넣음.
CONVERT2MD = """Your goal is to convert the provided XML/HTML table into a clear and concise Markdown format, ensuring that essential information, such as title label, captions and footnotes, is not omitted. Do not add any additional explanatory details. You must conclude with "<END>".

Begin!

Input:
<ce:table colsep="0" frame="topbot" id="TBL3" rowsep="0">
<ce:label>Table 3</ce:label>
<ce:caption>
<ce:simple-para view="all">Selected geometric parameters for <ce:bold>2</ce:bold> (Å, °)<ce:hsp sp="0.25"></ce:hsp>
<ce:cross-ref refid="TBLFN1">
<ce:sup loc="post">a</ce:sup>
</ce:cross-ref>
</ce:simple-para>
</ce:caption>
<tgroup cols="4">
<colspec colname="col1" colsep="0"></colspec>
<colspec colname="col2" colsep="0"></colspec>
<colspec colname="col3" colsep="0"></colspec>
<colspec colname="col4" colsep="0"></colspec>
<tbody>
<row>
<entry>Ta(1)Cl(1) (2<italic>x</italic>)</entry>
<entry>2.3442(8)</entry>
<entry>Li(1)Cl(4)</entry>
<entry>2.274(6)</entry>
</row>
<row>
<entry>Ta(1)Cl(2)</entry>
<entry>2.292(7)</entry>
<entry>Li(1)O(1)#2</entry>
<entry>1.930(6)</entry>
</row>
<row>
<entry>Ta(1)Cl(3)</entry>
<entry>2.303(4)</entry>
<entry>Li(1)O(2)</entry>
<entry>1.943(6)</entry>
</row>
<row>
<entry>Ta(1)Cl(2A)</entry>
<entry>2.355(6)</entry>
<entry>Li(1)O(3)</entry>
<entry>1.947(7)</entry>
</row>
<row>
<entry>Ta(1)Cl(3A)</entry>
<entry>2.407(4)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>
<vsp sp="0.5"></vsp>
</entry>
<entry align="char" char="."></entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(2)Ta(1)Cl(1)</entry>
<entry align="char" char=".">89.9(2)</entry>
<entry>O(1)#2Li(1)O(2)</entry>
<entry align="char" char=".">101.9(3)</entry>
</row>
<row>
<entry>Cl(3)Ta(1)Cl(1)</entry>
<entry align="char" char=".">90.65(9)</entry>
<entry>O(1)#2Li(1)O(3)</entry>
<entry align="char" char=".">107.0(3)</entry>
</row>
<row>
<entry>Cl(1)#1Ta(1)Cl(1)</entry>
<entry align="char" char=".">179.31(4)</entry>
<entry>O(2)Li(1)O(3)</entry>
<entry align="char" char=".">106.1(3)</entry>
</row>
<row>
<entry>Cl(1)Ta(1)Cl(2A)#1</entry>
<entry align="char" char=".">87.80(18)</entry>
<entry>O(1)#2Li(1)Cl(4)</entry>
<entry align="char" char=".">119.0(3)</entry>
</row>
<row>
<entry>Cl(1)Ta(1)Cl(3A)#1</entry>
<entry align="char" char=".">92.44(11)</entry>
<entry>O(2)Li(1)Cl(4)</entry>
<entry align="char" char=".">111.0(3)</entry>
</row>
<row>
<entry>Cl(2)Ta(1)Cl(3)</entry>
<entry align="char" char=".">94.1(2)</entry>
<entry>O(3)Li(1)Cl(4)</entry>
<entry align="char" char=".">110.9(3)</entry>
</row>
<row>
<entry>Cl(2)Ta(1)Cl(1)#1</entry>
<entry align="char" char=".">89.7(2)</entry>
<entry>Li(1)#2Cl(4)Li(1)</entry>
<entry align="char" char=".">172.3(3)</entry>
</row>
<row>
<entry>Cl(2)Ta(1)Cl(2A)#1</entry>
<entry align="char" char=".">91.42(17)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(2)Ta(1)Cl(3A)#1</entry>
<entry align="char" char=".">176.7(2)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(3)Ta(1)Cl(1)#1</entry>
<entry align="char" char=".">89.92(10)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(3)Ta(1)Cl(2A)#1</entry>
<entry align="char" char=".">174.3(2)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(3)Ta(1)Cl(3A)#1</entry>
<entry align="char" char=".">88.25(19)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(1)#1Ta(1)Cl(2A)#1</entry>
<entry align="char" char=".">91.67(18)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(1)#1Ta(1)Cl(3A)#1</entry>
<entry align="char" char=".">87.96(11)</entry>
<entry></entry>
<entry></entry>
</row>
<row>
<entry>Cl(2A)#1Ta(1)Cl(3A)#1</entry>
<entry align="char" char=".">86.33(18)</entry>
<entry></entry>
<entry></entry>
</row>
</tbody>
</tgroup>
<ce:table-footnote id="TBLFN1">
<ce:label>a</ce:label>
<ce:note-para>Symmetry operations: #<ce:bold>1</ce:bold>: 1−<ce:italic>x</ce:italic>, <ce:italic>y</ce:italic>, 1.5−<ce:italic>z</ce:italic>; #<ce:bold>2</ce:bold>: <ce:italic>x</ce:italic>, −<ce:italic>y</ce:italic>, <ce:italic>z</ce:italic>+0.5.</ce:note-para>
</ce:table-footnote>
</ce:table>
MD table:
Table 3

Selected geometric parameters for 2 (Å, °)[^a]

|                    |                    |                    |                    |
|--------------------|--------------------|--------------------|--------------------|
| Ta(1)Cl(1) (2*x) | 2.3442(8)          | Li(1)Cl(4)        | 2.274(6)           |
| Ta(1)Cl(2)       | 2.292(7)           | Li(1)O(1)#2       | 1.930(6)           |
| Ta(1)Cl(3)       | 2.303(4)           | Li(1)O(2)         | 1.943(6)           |
| Ta(1)Cl(2A)      | 2.355(6)           | Li(1)O(3)         | 1.947(7)           |
| Ta(1)Cl(3A)      | 2.407(4)           |                    |                    |
|                    |                    |                    |                    |
| Cl(2)Ta(1)Cl(1) | 89.9(2)            | O(1)#2Li(1)O(2) | 101.9(3)           |
| Cl(3)Ta(1)Cl(1) | 90.65(9)           | O(1)#2Li(1)O(3) | 107.0(3)           |
| Cl(1)#1Ta(1)Cl(1) | 179.31(4)         | O(2)Li(1)O(3)   | 106.1(3)           |
| Cl(1)Ta(1)Cl(2A)#1 | 87.80(18)        | O(1)#2Li(1)Cl(4) | 119.0(3)           |
| Cl(1)Ta(1)Cl(3A)#1 | 92.44(11)         | O(2)Li(1)Cl(4)  | 111.0(3)           |
| Cl(2)Ta(1)Cl(3) | 94.1(2)            | O(3)Li(1)Cl(4)  | 110.9(3)           |
| Cl(2)Ta(1)Cl(1)#1 | 89.7(2)            | Li(1)#2Cl(4)Li(1) | 172.3(3)           |
| Cl(2)Ta(1)Cl(2A)#1 | 91.42(17)         |                    |                    |
| Cl(2)Ta(1)Cl(3A)#1 | 176.7(2)          |                    |                    |
| Cl(3)Ta(1)Cl(1)#1 | 89.92(10)          |                    |                    |
| Cl(3)Ta(1)Cl(2A)#1 | 174.3(2)           |                    |                    |
| Cl(3)Ta(1)Cl(3A)#1 | 88.25(19)          |                    |                    |
| Cl(1)#1Ta(1)Cl(2A)#1 | 91.67(18)        |                    |                    |
| Cl(1)#1Ta(1)Cl(3A)#1 | 87.96(11)         |                    |                    |
| Cl(2A)#1Ta(1)Cl(3A)#1 | 86.33(18)        |                    |                    |

[^a]: Symmetry operations: #1: 1−x, y, 1.5−z; #2: x, −y, z+0.5.
<END>

Input:
{paragraph}
MD table:"""


# chemical formula는 기본적으로 물어볼 거라서 포함 안시켰음.
CRYSTAL_CATEGORIZE = """From the provided markdown table, generate a Python list of item names with data present. You must exclude absent items and return an empty list if any key items are missing. Names of items must be one of following:
- chemical formula: empirical formula of materials.
- chemical formula weight: sum of the atomic weights of the elements present in its chemical formula.
- space group: a mathematical description of the symmetries inherent in a periodic crystal lattice.
- crystal system: symmetrical and geometrical arrangements within the crystal lattice of materials.
- lattice parameters: cell lengths and angles
- cell volume: cell volume of materials.
- density: bulk density of materials.
- crystal size: crystal size of materials.

Begin!

Input:
**Table 1: Crystallographic data for complexes 1–6**

|   | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Empirical formula | C₈H₉PrNO₉ | C₈H₉NdNO₉ | C₈H₉EuNO₉ | C₈H₉GdNO₉ | C₈H₉TbNO₉ | C₈H₉ErNO₉ |
| Formula weight | 404.07 | 407.40 | 415.12 | 420.41 | 422.08 | 430.42 |
| Crystal system | Triclinic | Triclinic | Triclinic | Triclinic | Triclinic | Triclinic |
List : ['chemical formula', 'chemical formula weight', 'crystal system']

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
List: ['space group', 'lattice parameters', 'cell volume', 'density']

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
List: ['chemical formula', 'chemical formula weight', 'crystal system', 'lattice parameters', 'crystal size']

Input:
{paragraph}
List:"""


CRYSTAL_EXTRACT="""From the given Markdown table, extract information related to {{prop}} for each materials. Extracted information should be in structured json format as in the example below. You must conclude with "<END>".
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
