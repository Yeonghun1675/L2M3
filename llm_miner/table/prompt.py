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
