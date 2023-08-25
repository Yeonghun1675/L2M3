PROMPT_CATEGORIZE = """Determine the category of the given markdown table from the following options: ['Crystal', 'Bond & Angle', 'Coordinate', 'Property']. If the table doesn't fit any category, return an empty string "".

You must follow rules below:
- Typical 'Crystal' markdown table includes lattice parameter, spacegroup, crystal system, cell volume and etc. 'Crystal' table is mostly comprised of crystal information. In that case, return 'Crystal'.
- If the markdown table is mostly comprised of bond and angle information of specific materials, return 'Bond & Angle'.
- If the markdown table is mostly comprised of coorination information of specific materials, return 'Coordinate'.
- If the markdown table is not included in 'Crystal', 'Bond & Angle', and 'Coordinate', but contains any data that can be represented by numeric values, return 'Property'.

Begin!

Input:
Table 1

Crystallographic data for [La5Cl2(edta)3(H2O)18]nCln·8nH2O (1), [La2(NO3)2(edta)(H2O)5]n·3nH2O (2) and [La2(SO4)(edta)(H2O)3]n (3).

| Compound reference | 1 | 2 | 3 |
|--------------------|---|---|---|
| Empirical formula  | C30H88Cl3La5N6O50 | C10H28La2N4O22 | C10H18La2N2O15S |
| Formula weight     | 2133.92 | 834.18 | 716.14 |
| Crystal system     | trigonal | monoclinic | monoclinic |
| a (Å)              | 17.242(1) | 12.7623(4) | 8.1727(2) |
| b (Å)              | 17.242(1) | 8.3831(2) | 9.2832(2) |
| c (Å)              | 17.242(1) | 23.9610(7) | 24.6545(7) |
| α (°)              | 61.04 |  |  |
| β (°)              | 61.04 | 104.924(3) | 90.535(3) |
| γ (°)              | 61.04 |  |  |
| Unit cell volume (Å^3) | 3709.4(5) | 2477.1(1) | 1870.43(8) |
| T (K)              |  | 173(2) |  |
| Space group        | R-3c | P2_1/n | P2_1/c |
| No. of formula units per unit cell, Z | 2 | 4 | 4 |
| No. of reflections measured | 13,524 | 21,005 | 6417 |
| No. of independent reflections | 2303 | 5490 | 3765 |
| Rint               | 0.0674 | 0.0488 | 0.0253 |
| Final R1 values (I > 2σ(I))^a | 0.0792 | 0.0330 | 0.0303 |
| Final wR(F^2) values (I > 2σ(I)) | 0.2184 | 0.0714 | 0.1028 |
| Final R1 values (all data)^b | 0.0897 | 0.0407 | 0.0342 |
| Final wR(F^2) values (all data) | 0.2295 | 0.0747 | 0.1075 |
| Goodness-of-fit (GOF) on F^2 | 0.790 | 1.156 | 0.840 |

a R1 = Σ|Fo|-|Fc|/Σ|Fo|
b wR2 = Σ[w(Fo^2 - Fc^2)]/Σ[w(Fo^2)]^1/2

Output: 'Crystal'

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

Output: 'Crystal'

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

Output: 'Crystal'

Input:
Table 2

Selected bond lengths (Å) and angles (°) for this Zn(II) compound.

| Zn(1)-O(2) | 2.011(5) | Zn(1)-O(8)[^a^] | 2.020(6) |
|------------|----------|-----------------|----------|
| Zn(1)-O(6) | 2.046(5) | Zn(1)-N(3)[^b^] | 2.053(6) |
| Zn(1)-O(4) | 2.058(5) | Zn(2)-O(3)       | 2.022(5) |
| Zn(2)-O(5) | 2.022(6) | Zn(2)-O(7)[^a^] | 2.051(6) |
| Zn(2)-O(1) | 2.052(5) | Zn(2)-N(1)       | 2.063(7) |
| O(2)-Zn(1)-O(8)[^a^] | 86.9(2) | O(2)-Zn(1)-O(6) | 87.8(2) |
| O(8)[^a^]-Zn(1)-O(6) | 157.9(2) | O(2)-Zn(1)-N(3)[^b^] | 104.6(2) |
| O(8)[^a^]-Zn(1)-N(3)[^b^] | 102.1(3) | O(6)-Zn(1)-N(3)[^b^] | 100.0(3) |
| O(2)-Zn(1)-O(4) | 153.1(2) | O(8)[^a^]-Zn(1)-O(4) | 87.8(2) |
| O(6)-Zn(1)-O(4) | 87.3(2) | N(3)[^b^]-Zn(1)-O(4) | 102.4(2) |
| O(3)-Zn(2)-O(5) | 86.6(3) | O(3)-Zn(2)-O(7)[^a^] | 86.5(2) |
| O(5)-Zn(2)-O(7)[^a^] | 153.8(2) | O(3)-Zn(2)-O(1) | 157.9(2) |
| O(5)-Zn(2)-O(1) | 90.7(3) | O(7)[^a^]-Zn(2)-O(1) | 86.3(2) |
| O(3)-Zn(2)-N(1) | 101.4(2) | O(5)-Zn(2)-N(1) | 102.7(3) |
| O(7)[^a^]-Zn(2)-N(1) | 103.4(3) | O(1)-Zn(2)-N(1) | 100.6(3) |

[^a^]: Symmetry codes: x + 1/2, y, -z + 1/2.
[^b^]: -x + 1/2, -y + 1, z + 1/2.

Output: 'Bond & Angle'

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

Output: 'Bond & Angle'

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

Output: 'Bond & Angle'

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

Output: 'Coordinate'

Input:
Table 4

Atomic coordinates and equivalent isotropic displacement parameters (Å²) for Sr₂Zr(C₂O₄)₄·11H₂O

| Atom | Site | Occup | x    | y    | z    | Ueq    |
|------|------|-------|------|------|------|--------|
| Sr   | 16e  | 1     | 1/4  | 0.5128(1) | 1/2  | 0.023(1) |
| Zr   | 8a   | 1     | 1/2  | 3/4  | 0.08750 | 0.013(1) |
| O(1) | 32g  | 1     | 0.1846(2) | 0.5622(2) | 0.6275(1) | 0.028(1) |
| O(2) | 32g  | 1     | 0.4440(2) | 0.6954(2) | 0.9741(1) | 0.031(1) |
| O(3) | 32g  | 1     | 0.4084(2) | 0.8423(2) | 0.9066(1) | 0.030(1) |
| O(4) | 32g  | 1     | 0.3517(2) | 0.3932(2) | 0.4787(2) | 0.057(1) |
| C(1) | 32g  | 1     | 0.6346(2) | 0.8821(2) | 0.8902(2) | 0.023(1) |
| C(2) | 32g  | 1     | 0.6123(2) | 0.8592(2) | 0.9696(2) | 0.030(1) |
| O(w1A) | 32g | 0.72(1) | 0.3741(13) | 0.5936(9) | 0.5483(8) | 0.096(5) |
| O(w1B) | 32g | 0.28  | 0.4030(20) | 0.5570(40) | 0.5260(20) | 0.096(5) |
| O(w2A) | 32g | 0.41(1) | 0.2610(30) | 0.6779(7) | 0.5080(20) | 0.138(9) |
| O(w2B) | 32g | 0.09  | 0.1770(70) | 0.6450(50) | 0.4643(18) | 0.138(9) |
| O(w3)  | 8b   | 1     | 1/2  | 3/4  | 0.11250 | 0.099(5) |
| O(w4A) | 32g | 0.66(1) | 0.7718(14) | 0.7602(6) | 0.8733(6) | 0.091(4) |
| O(w4B) | 32g | 0.34  | 0.8230(30) | 0.7604(10) | 0.8777(7) | 0.091(4) |

Ueq is defined as one third of the trace of the orthogonalized Uij tensor.

Output: 'Coordinate'

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

Output: 'Property'

Input:
Table 4

Cyanosilylation of benzaldehyde in the presence of different Mg-MOF loadings.

| Entry | Cat. mol % | TMSCN | Temp.(°C) | Time (h) | Conv.% |
|-------|------------|-------|-----------|----------|--------|
| 1     | 1          | 2 eq  | r.t.      | 2        | >99    |
| 2     | 0.5        | 2 eq  | r.t.      | 2        | >99    |
| 3     | 0.1        | 2 eq  | r.t.      | 2        | >99    |

Determined by GC based on the carbonyl substrate.

Output: 'Property'

Input:
Table 1

Epoxidation of different olefin substrates catalyzed by 1 and 2.[^a]

| Substrate         | Structure | Conv. (%) | Sel.[^b] (%) | TOF[^c] (h^-1) | Conv. (%) | Sel.[^b] (%) | TOF[^c] (h^-1) |
|-------------------|-----------|-----------|--------------|----------------|-----------|--------------|----------------|
| Cyclohexene       | Figure 2  | 66.9      | 80.3         | 167            | 74.3      | 84.6         | 186            |
| Styrene           | Figure 3  | 78.3      | 60.7         | 196            | 75.2      | 48.9         | 188            |
| α-Methylstyrene   | Figure 4  | 99.9      | 37.8         | 250            | 95.1      | 30.5         | 238            |
| Ethyl cinnamate   | Figure 5  | 4.3       | 0.5          | 11             | 0.9       | 0.1          | 2              |
| Stiblene          | Figure 6  | 0.6       | NA           | NA             | 0.4       | NA           | NA             |

[^a]: Typical reaction conditions: olefin (10 mmol), TBHP (5 mL), cyclohexane (10 mL), catalyst (6 mg), reaction temperature (80 °C), reaction time (8 h). The product yields were determined by GC.
[^b]: The selectivity of epoxide.
[^c]: Moles of olefin conversion per mole of tetranuclear Cu(II) of the catalysts per hour.

Output: 'Property'

Input:
{{paragraph}}

Output:"""
