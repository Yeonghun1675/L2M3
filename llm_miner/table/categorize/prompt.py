PROMPT_CATEGORIZE = """Determine the category of the given markdown table from the following options: ["Crystal", "Bond & Angle", "Coordinate", "Elemental Composition", "Property"].

You must follow rules below:
- Typical "Crystal" markdown table includes lattice parameter, spacegroup and etc. "Crystal" table is mostly comprised of crystal information. In that case, return "Crystal".
- If the markdown table is mostly comprised of bond or angle information of specific materials, return "Bond & Angle".
- If the markdown table is mostly comprised of coorination information of specific materials, return "Coordinate".
- If the markdown table is mostly comprised of elemental composition information of specific materials, return "Elemental Composition".
- If the markdown table is not included in "Crystal", "Bond & Angle", "Coordinate", and "Elemental Composition", return "Property".

Begin!

Input:
Table 1

Selected crystallographic data for {MnII(4,4′-bpy)[AgI(CN)2]2}·2CHCl3.

| Empirical formula | C16H10Ag2Cl6MnN6 |
|-------------------|------------------|
| Formula weight    | 769.68           |
| T (K)             | 173              |
| Crystal system    | orthorhombic     |
| Space group       | Cmca             |
| a (Å)             | 11.7060(6)       |
| b (Å)             | 17.6369(9)       |
| c (Å)             | 12.2246(6)       |
| V (Å^3)           | 2523.9(2)        |
| Z                 | 4                |
| D calc (g cm^-3)  | 2.026            |
| μ (mm^-1)         | 2.681            |
| F (0 0 0)         | 1476             |
| Crystal size (mm^3) | 0.17 × 0.13 × 0.12 |
| Reflections collected | 9064          |
| Independent reflections (R int) | 1651 (0.0215) |
| Absorption correction | empirical    |
| Goodness-of-fit (GOF) on F^2 | 1.287   |
| R^1, wR^2 [I > 2σ(I)] | 0.0833, 0.2284 |
| R^1, wR^2 (all data) | 0.0851, 0.2290 |
| Δρ max, Δρ min (e Å^-3) | 2.065, −2.372 |

Output: "Crystal"

Input:
Table 1

Summary of the unit cell parameters for selected well-known oxalate-containing compounds

|                | Space group | a (Å)    | b (Å)    | c (Å)    | α (°)    | β (°)    | γ (°)    |
|----------------|-------------|----------|----------|----------|----------|----------|----------|
| Ln2(C2O4)3(H2O)6·4 H2O (Ln = La–Er) [7, 8] | P21/c       | 11.516(250) | 9.631(30)  | 10.081(400) |            | 118.82(25) |            |
| Ln2(C2O4)3(H2O)4·2 H2O (Ln = Er–Lu, Y, Sc) [9] | P1̄         | 9.597(150)  | 8.455(15)  | 9.758(300)  | 93.42(40) | 106.27(30) | 85.41(90) |
| K3Ln(C2O4)3·3 H2O (Ln = Nd–Tb) [10] | P1̄         | 9.383(50)   | 8.484(20)  | 9.751(50)   | 88.86(50) | 81.76(50)  | 96.55(30) |
| K8Ln2(C2O4)7·14 H2O (Ln = Tb, Er, Yb, Dy, Y) [11] | C2/c        | 16.079(50)  | 11.773(60) | 23.371(120) |            | 91.21(35)  |            |
| [LiLn(H2O)n](C2O4)·H2O (Ln = La–Gd, n = 1) [12] | P2/a        | 9.399(100)  | 7.666(80)  | 12.877(140) |            | 103.77(45) |            |
| [NaLn(H2O)n](C2O4)·H2O (Ln = Ce–Nd, n = 2) [12] | P2/a        | 10.033(35)  | 7.591(40)  | 13.093(70)  |            | 102.02(20) |            |
| YM(C2O4)2·4 H2O (M = K, Rb) [13] | I41/a       | 11.4612(8)  |            | 8.9040(8)  |            |            |            |
| Y(H2O)Na(C2O4)2·3 H2O [14] | Pc          | 8.623(2)   | 8.6310(8) | 14.896(3)  |            | 102.848(9) |            |
------------------------------------------------------------------------------------------------------------------------

Output: "Crystal"

Input:
Table 2

Bond lengths (Å) and bond angles (°) in **1**

| Bond lengths |  |  |  |
|--------------|---|---|---|
| Ag(1)–N(1)   | 2.209(6) | Ag(2)–O(1)   | 2.210(6) |
| Ag(3)–N(2)   | 2.172(9) | Ag(3)–O(2)<sup>b</sup> | 2.176(6) |
| Ag(3)⋯O(11)  | 2.58(2)  |   |   |
|              |   |   |   |
| Bond angles  |  |  |  |
| N(1)–Ag(1)–N(1)<sup>a</sup> | 176.6(3) | O(1)–Ag(2)–O(1)<sup>b</sup> | 178.3(3) |
| N(2)–Ag(3)–O(2)<sup>b</sup> | 161.2(3) | N(2)–Ag(3)⋯O(11) | 111.3(5) |

a: −*x*, *y*, 0.5−*z*.
b: 0.5−*x*, 1−*y*, *z*.

Output: "Bond & Angle"

Input:
Table 3

Characteristics of hydrogen bonds in 1a–1e

| Hydrogen bonds | 1a | 1b | 1c | 1d | 1e |
|---------------|----|----|----|----|----|
| O–H … O/O–H … O- | 1.77 | 2.60 | 166.0 | 1.88 | 2.55 |
|                 | 1.78 | 2.54 | 167.0 |      |      |
|                 | 1.79 | 2.66 | 174.0 |      |      |
|                 | 1.86 | 2.71 | 176.0 |      |      |
|                 | 1.88 | 2.73 | 166.0 |      |      |
|                 | 1.92 | 2.73 | 173.0 |      |      |
|                 | 1.93 | 2.66 | 178.0 |      |      |
|                 | 1.97 | 2.72 | 176.0 |      |      |
|                 | 2.00 | 2.74 | 170.0 |      |      |
|                 | 2.10 | 2.96 | 152.0 |      |      |
|                 | 2.19 | 2.84 | 135.0 |      |      |
|                 | 2.36 | 3.01 | 134.0 |      |      |
|                 | 2.36 | 2.96 | 141.0 |      |      |

[^a]: Symmetries: (ii) -x+2, y, -z+3/2.
[^b]: D: donor. A: acceptor.

Output: "Bond & Angle"

Input:
Table 1. Chemical analysis results for [Ln(abdc)(Habdc), nH2O]∞ with Ln=La–Eu (except Pm) and n =10.[^*]

| Ln | MW (gmol−1) | Anal. Calculated (found) | O (%) | C (%) | H (%) | N (%) |
|----|-------------|---------------------------|-------|-------|-------|-------|
| La | 678.33      | 20.5(20.5)                 | 42.5(42.4) | 28.3(28.2) | 4.6(4.8) | 4.1(4.1) |
| Ce | 679.54      | 20.6(20.7)                 | 42.4(42.5) | 28.3(28.0) | 4.6(4.7) | 4.1(4.1) |
| Pr | 680.33      | 20.7(20.4)                 | 42.3(42.2) | 28.2(28.4) | 4.6(4.7) | 4.1(4.2) |
| Nd | 683.66      | 21.1(20.8)                 | 42.1(42.3) | 28.1(28.2) | 4.6(4.7) | 4.1(4.0) |
| Sm | 689.78      | 21.8(21.8)                 | 41.7(41.6) | 27.8(28.1) | 4.5(4.3) | 4.1(4.1) |
| Eu | 691.39      | 22.0(22.2)                 | 41.6(41.5) | 27.8(27.8) | 4.5(4.5) | 4.1(4.0) |

[^*]: The reported chemical analysis is those for compounds with n =10. Other chemical analyses are not reported.

Output: "Elemental Composition"

Input:
Table 2

Atomic coordinates (×10^4) and equivalent isotropic displacement parameters (Å^2×10^3) for ZnF(TAZ)·solvents

|       | x       | y       | z       | Ueq     |
|-------|---------|---------|---------|---------|
| Zn(1) | 3749(1) | 3749(1) | 2500    | 21(1)   |
| F(1)  | 4094(1) | 3333    | 833     | 29(1)   |
| C(1)  | 3681(2) | 2121(2) | 3272(2) | 27(1)   |
| N(1)  | 3562(1) | 2740(1) | 3581(2) | 25(1)   |
| N(2)  | 3333    | 1493(1) | 4167    | 26(1)   |
| O(1)  | 5500(20)| 3480(20)| 4520(40)| 100     |
| O(2)  | 5932(9) | 3349(10)| 3716(14)| 100     |
| O(3)  | 5800(30)| 4000(40)| 960(60) | 100     |
| O(4)  | 6667    | 4900(20)| 833     | 100     |
| O(5)  | 5468(19)| 3333    | 833     | 100     |
| O(6)  | 5400(20)| 3160(30)| -40(40) | 100     |
| O(7)  | 5630(30)| 3670(50)| 620(40) | 100     |

Ueq is defined as one-third of the trace of the orthogonalized Uij tensor.

Output: "Coordinate"

Input:
Table 3

13C NMR spectral data (in ppm) of 1 ∼ 3, K4edta, K[La(edta)(H2O)3]⋅ 5H2O [24].

| Compounds | –CH2N | –NCH2CO2 | –CO2 |
| --- | --- | --- | --- |
| 1 | 57.3(3.6) | 64.4(4.3) | 183.0 (4.5) |
| 2 | 57.3(3.6) | 64.5(4.4) | 183.0 (4.5) |
| [edta]4- | 53.7 | 60.1 | 178.5 |
| K[La(edta)(H2O)3]·5H2O | 57.2(3.5) | 64.4(4.3) | 183.0(4.5) |
|  |  |  |  |
| Solid |
| 1 | 57.5, 53.6 | 62.5 | 184.9, 179.8 |
| 2 | 55.2, 53.0 | 62.5, 59.4 | 180.1, 179.4 |
| 3 | 57.4, 53.7 | 62.7, 60.9 | 182.4, 178.3 |

Output: "Property"

Input:
Table 4

Cyanosilylation of benzaldehyde in the presence of different Mg-MOF loadings.

| Entry | Cat. mol % | TMSCN | Temp.(°C) | Time (h) | Conv.% |
|-------|------------|-------|-----------|----------|--------|
| 1     | 1          | 2 eq  | r.t.      | 2        | >99    |
| 2     | 0.5        | 2 eq  | r.t.      | 2        | >99    |
| 3     | 0.1        | 2 eq  | r.t.      | 2        | >99    |

Determined by GC based on the carbonyl substrate.

Output: "Property"

Input:
{{paragraph}}

Output:"""


FT_CATEGORIZE = """Determine the category of the given markdown table from the following options: ["Crystal", "Bond & Angle", "Coordinate", "Elemental Composition", "Property"]."""


FT_HUMAN = "{paragraph}"
