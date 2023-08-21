PROMPT_TYPE = """Determine which type the synthesis method belongs to and print out the type of synthesis method. Each type appears as follows. You must answer only type number like "type 00".

type1 : atomic layer deposition
type2 : atomic layer etching
type3 : ball milling
type4 : blade coating
type5 : bulk metal forming
type6 : centrifugation
type7 : chemical mechanical polishing
type8 : chemical synthesis
type9 : chemical vapor deposition
type10 : directed energy deposition
type11 : drying
type12 : e-beam lithography
type13 : electrochemical deposition
type14 : electrospinning
type15 : electrical poling
type16 : casting
type17 : heat treatment
type18 : hydrothermal reaction
type19 : microwave_assisted synthesis
type20 : mixing
type21 : molecular beam epitaxy
type22 : polishing
type23 : powder bed fusion
type24 : pulsed laser deposition
type25 : rinsing
type26 : pressing
type27 : sintering
type28 : slurry casting
type29 : slot coating
type30 : solvothermal synthesis
type31 : sol-gel syntehsis
type32 : sonication
type33 : sonochemical syntehsis
type34 : spin coating
type35 : spray pyrolysis
type36 : sputter deposition
type37 : thermal evaporation
type38 : thermomechanical process
type39 : transporting
type40 : wet etching
type41 : washing
type42 : cooling

Paragraph: A mixture of tris-(4-bromophenyl)amine (2.00 g, 4.15 mmol) and CuCN (1.70 g, 18.98 mmol) was heated at reflux in 25 mL of anhydrous dimethylformamide (DMF) for 6 h under a nitrogen atmosphere at 150 °C. Upon cooling to room temperature (RT), the FeCl3/H2O/ethanol (8.00 g/10 mL/8 mL) mixture solvent was added to the reaction mixture and then heated to 125 °C. Then, dilute hydrochloric acid (100 mL, 2 M) was added into the solution. The resulting mixture was extracted with CH2Cl2 (5 × 50 mL), washed with ethylenediaminetetraacetic acid-2Na aqueous solution (5 × 100 mL), evaporated under a rotary evaporator, and dried over anhydrous MgSO4. The crude product was purified by flash chromatography on silica gel using CH2Cl2 as an eluent to afford 0.90 g (67.8%) of tris-(4-cyanophenyl)amine as a primrose yellow powder.
List: ["type8", "type41"]

Paragraph:{paragraph}
List: type number
"""