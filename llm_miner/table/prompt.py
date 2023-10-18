# XML table이 너무 길어서 여기서는 예제 안넣음.
CONVERT2MD = """Your goal is to convert the provided XML/HTML table into a clear and concise Markdown format, ensuring that essential information, such as title label, captions and footnotes, is not omitted. Do not add any additional explanatory details. If there is no content except for the Footnote, return 'Empty Content'. You must conclude with '<END>'.

Begin!

Input:
<table-wrap id="tbl1" orientation="portrait" position="float">
<label>1</label>
<caption>
<title>Knoevenagel Condensation Reaction of Butyl Cyanoacetate with Substrates Catalyzed by PCNs-100 and -101</title>
</caption>
<oasis:table colsep="0" rowsep="0">
<oasis:tgroup cols="1">
<oasis:colspec colname="col1"></oasis:colspec>
<oasis:tbody>
<oasis:row>
<oasis:entry>
<graphic id="fx1" orientation="portrait" position="anchor" xlink:href="ic-2010-01935f_0011.tif"></graphic>
</oasis:entry>
</oasis:row>
</oasis:tbody>
</oasis:tgroup>
</oasis:table>
</table-wrap>
MD table:
Empty Content
<END>

Input:
<table-wrap position="float">
<label>1</label>
<caption>
<title>Photovoltaic Parameters Obtained from J–V Curves of the Solid-State TiO<sub>2</sub>-Based
Solar Cells Sensitized with Co-DAPV at Various LbL Cycles, Showing
Highest Power Conversion Efficiency at 15 LbL Cycles of Sensitization</title>
</caption>
<oasis:table colsep="0" rowsep="0">
<oasis:tgroup cols="5">
<oasis:colspec align="char" char="." colname="col1"></oasis:colspec>
<oasis:colspec align="char" char="." colname="col2"></oasis:colspec>
<oasis:colspec align="char" char="." colname="col3"></oasis:colspec>
<oasis:colspec align="char" char="." colname="col4"></oasis:colspec>
<oasis:colspec align="char" char="." colname="col5"></oasis:colspec>
<oasis:thead>
<oasis:row>
<oasis:entry align="center">no. of LbL cycles</oasis:entry>
<oasis:entry align="center">
V
<sub>oc</sub> (V)</oasis:entry>
<oasis:entry align="center">
J
<sub>sc</sub> (mA cm<sup>–2</sup>)</oasis:entry>
<oasis:entry align="center">FF</oasis:entry>
<oasis:entry align="center">eff (%)</oasis:entry>
</oasis:row>
</oasis:thead>
<oasis:tbody>
<oasis:row>
<oasis:entry>5</oasis:entry>
<oasis:entry>0.58</oasis:entry>
<oasis:entry>0.98</oasis:entry>
<oasis:entry>0.57</oasis:entry>
<oasis:entry>0.42</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>10</oasis:entry>
<oasis:entry>0.61</oasis:entry>
<oasis:entry>4.07</oasis:entry>
<oasis:entry>0.50</oasis:entry>
<oasis:entry>1.55</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>15</oasis:entry>
<oasis:entry>0.67</oasis:entry>
<oasis:entry>4.92</oasis:entry>
<oasis:entry>0.57</oasis:entry>
<oasis:entry>2.10</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>20</oasis:entry>
<oasis:entry>0.67</oasis:entry>
<oasis:entry>3.20</oasis:entry>
<oasis:entry>0.51</oasis:entry>
<oasis:entry>1.12</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>30</oasis:entry>
<oasis:entry>0.66</oasis:entry>
<oasis:entry>3.24</oasis:entry>
<oasis:entry>0.52</oasis:entry>
<oasis:entry>1.14</oasis:entry>
</oasis:row>
</oasis:tbody>
</oasis:tgroup>
</oasis:table>
</table-wrap>
MD table:
Table 1. Photovoltaic Parameters Obtained from J–V Curves of the Solid-State TiO<sub>2</sub>-Based Solar Cells Sensitized with Co-DAPV at Various LbL Cycles, Showing Highest Power Conversion Efficiency at 15 LbL Cycles of Sensitization

| no. of LbL cycles | V<sub>oc</sub> (V) | J<sub>sc</sub> (mA cm<sup>–2</sup>) | FF  | eff (%) |
|-------------------|-------------------|-----------------------------------|-----|---------|
| 5                 | 0.58              | 0.98                              | 0.57| 0.42    |
| 10                | 0.61              | 4.07                              | 0.50| 1.55    |
| 15                | 0.67              | 4.92                              | 0.57| 2.10    |
| 20                | 0.67              | 3.20                              | 0.51| 1.12    |
| 30                | 0.66              | 3.24                              | 0.52| 1.14    |
<END>

Input:
<table-wrap orientation="portrait" position="float">
<label>1</label>
<caption>
<title>Comparison of Separation Performance
for Substituted Benzenes between Ala-ZIF-8@Capillary and Cys-ZIF-8@Capillary</title>
</caption>
<oasis:table colsep="0" rowsep="0">
<oasis:tgroup cols="5">
<oasis:colspec align="left" colname="col1"></oasis:colspec>
<oasis:colspec align="left" colname="col2"></oasis:colspec>
<oasis:colspec align="left" colname="col3"></oasis:colspec>
<oasis:colspec align="left" colname="col4"></oasis:colspec>
<oasis:colspec align="left" colname="col5"></oasis:colspec>
<oasis:thead>
<oasis:row>
<oasis:entry align="center" rowsep="1">columns</oasis:entry>
<oasis:entry align="center" rowsep="1">Ala-ZIF-8@capillary</oasis:entry>
<oasis:entry align="center" rowsep="1">Cys-ZIF-8@capillary</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry align="center">analytes</oasis:entry>
<oasis:entry align="center">Rs</oasis:entry>
<oasis:entry align="center">
<italic toggle="yes">N</italic> (plates/m)</oasis:entry>
<oasis:entry align="center">Rs</oasis:entry>
<oasis:entry align="center">
<italic toggle="yes">N</italic> (plates/m)</oasis:entry>
</oasis:row>
</oasis:thead>
<oasis:tbody>
<oasis:row>
<oasis:entry>benzene</oasis:entry>
<oasis:entry></oasis:entry>
<oasis:entry>43,203</oasis:entry>
<oasis:entry></oasis:entry>
<oasis:entry>75,016</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>methylbenzene</oasis:entry>
<oasis:entry>1.42</oasis:entry>
<oasis:entry>40,934</oasis:entry>
<oasis:entry>1.77</oasis:entry>
<oasis:entry>74,406</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>styrene</oasis:entry>
<oasis:entry>1.31</oasis:entry>
<oasis:entry>29,978</oasis:entry>
<oasis:entry>1.83</oasis:entry>
<oasis:entry>59,664</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>ethylbenzene</oasis:entry>
<oasis:entry>1.58</oasis:entry>
<oasis:entry>26,912</oasis:entry>
<oasis:entry>2.23</oasis:entry>
<oasis:entry>42,641</oasis:entry>
</oasis:row>
<oasis:row>
<oasis:entry>allylbenzene</oasis:entry>
<oasis:entry>1.31</oasis:entry>
<oasis:entry>20,793</oasis:entry>
<oasis:entry>1.86</oasis:entry>
<oasis:entry>29,671</oasis:entry>
</oasis:row>
</oasis:tbody>
</oasis:tgroup>
</oasis:table>
</table-wrap>
MD table:
Table 1. Comparison of Separation Performance for Substituted Benzenes between Ala-ZIF-8@Capillary and Cys-ZIF-8@Capillary

| columns analytes | Ala-ZIF-8@capillary Rs | Ala-ZIF-8@capillary N (plates/m) | Cys-ZIF-8@capillary Rs | Cys-ZIF-8@capillary N (plates/m) |
|------------------|------------------------|----------------------------------|------------------------|----------------------------------|
| benzene          |                        | 43,203                           |                        | 75,016                           |
| methylbenzene    | 1.42                   | 40,934                           | 1.77                   | 74,406                           |
| styrene          | 1.31                   | 29,978                           | 1.83                   | 59,664                           |
| ethylbenzene     | 1.58                   | 26,912                           | 2.23                   | 42,641                           |
| allylbenzene     | 1.31                   | 20,793                           | 1.86                   | 29,671                           |
<END>

Input:
{paragraph}
MD table:"""


FT_CONVERT = """Your goal is to convert the provided XML/HTML table into a clear and concise Markdown format, ensuring that essential information, such as title label, captions and footnotes, is not omitted. If there is no content except for the Footnote, return 'Empty Content'. You must conclude with '<END>'."""


FT_HUMAN = "{paragraph}"
