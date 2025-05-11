# CSCI-3412-HW-6

## Question 1
###
Output:  
```
Node(A) with Weight:0 is added to the 'Visited' ['A']  
Relaxed: vertex[B]: OLD:Infinity, NEW:4, Paths:{'B': 'A'}  
Relaxed: vertex[C]: OLD:Infinity, NEW:2, Paths:{'B': 'A', 'C': 'A'}  
Node(C) with Weight:2 is added to the 'Visited' ['A', 'C']  
Relaxed: vertex[D]: OLD:Infinity, NEW:6, Paths:{'B': 'A', 'C': 'A', 'D': 'C'}  
Relaxed: vertex[E]: OLD:Infinity, NEW:7, Paths:{'B': 'A', 'C': 'A', 'D': 'C', 'E': 'C'}  
Relaxed: vertex[B]: OLD:4, NEW:3, Paths:{'B': 'C', 'C': 'A', 'D': 'C', 'E': 'C'}  
Node(B) with Weight:3 is added to the 'Visited' ['A', 'B', 'C']  
No edge relaxation is needed for node, C  
Relaxed: vertex[D]: OLD:6, NEW:5, Paths:{'B': 'C', 'C': 'A', 'D': 'B', 'E': 'C'}  
Relaxed: vertex[E]: OLD:7, NEW:6, Paths:{'B': 'C', 'C': 'A', 'D': 'B', 'E': 'B'}  
Node(D) with Weight:5 is added to the 'Visited' ['A', 'B', 'C', 'D']  
No outgoing edge from the node, D  
Node(E) with Weight:6 is added to the 'Visited' ['A', 'B', 'C', 'D', 'E']  
No edge relaxation is needed for node, D  
{'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}, {'B': 'C', 'C': 'A', 'D': 'B', 'E': 'B'}  
```
  
## Question 2
###  
Output:  
```
Dijkstra's

Output:  
Distance from Denver to 'Denver': 0 with path: (Denver)  
Distance from Denver to 'Dallas': 1064 with path: (Denver to Dallas)  
Distance from Denver to 'LA': 1335 with path: (Denver to LA)  
Distance from Denver to 'Memphis': 1411 with path: (Denver to Memphis)  
Distance from Denver to 'Houston': 1426 with path: (Denver to Dallas to Houston)  
Distance from Denver to 'Chicago': 1474 with path: (Denver to Chicago)  
Distance from Denver to 'SF': 1894 with path: (Denver to LA to SF)  
Distance from Denver to 'Atlanta': 2221 with path: (Denver to Dallas to Atlanta)  
Distance from Denver to 'Washington': 2395 with path: (Denver to Washington)  
Distance from Denver to 'Phoenix': 2486 with path: (Denver to Dallas to Phoenix)  
Distance from Denver to 'Philadelphia': 2594 with path: (Denver to Washington to Philadelphia)  
Distance from Denver to 'NY': 2619 with path: (Denver to Chicago to NY)  
Distance from Denver to 'Boston': 2839 with path: (Denver to Boston)  
Distance from Denver to 'Seattle': 2879 with path: (Denver to LA to Seattle)  
Distance from Denver to 'Miami': 3194 with path: (Denver to Dallas to Atlanta to Miami)  
  

Prim's

Denver is selected. Distance: 0  
Dallas is selected. Distance: 1064  
Houston is selected. Distance: 362  
Memphis is selected. Distance: 675  
Atlanta is selected. Distance: 1157  
Miami is selected. Distance: 973  
LA is selected. Distance: 1335  
SF is selected. Distance: 559  
Seattle is selected. Distance: 1092  
Philadelphia is selected. Distance: 1413  
Washington is selected. Distance: 199  
Phoenix is selected. Distance: 1422  
Chicago is selected. Distance: 1474  
NY is selected. Distance: 1145  
Boston is selected. Distance: 306  

                Edge                            Weight 

         Dallas         Atlanta ................1157  
   Philadelphia      Washington .................199  
        Atlanta           Miami .................973  
        Memphis    Philadelphia ................1413  
             SF         Seattle ................1092  
         Dallas         Phoenix ................1422  
         Denver          Denver ...................0  
         Dallas         Houston .................362  
             NY          Boston .................306  
         Denver          Dallas ................1064  
         Dallas         Memphis .................675  
             LA              SF .................559  
         Denver              LA ................1335  
        Chicago              NY ................1145  
         Denver         Chicago ................1474  

Total MST:       13176  
```

## Question 3
###
Output:  
```
Enter a file to zip: 
King.txt
character       Weight        Huffman Code
' '               1623                 111
e                  885                 010
t                  656                1011
o                  604                1010
i                  542                1000
a                  539                0111
n                  450                0011
s                  419                0001
r                  413                0000
h                  385               11011
l                  328               11000
d                  254               01101
f                  220               00101
m                  181              110101
c                  176              110100
u                  175              110011
g                  167              100111
w                  146              100101
y                  124              011001
b                  110              011000
p                   93             1100101
v                   81             1100100
.                   75             1001100
,                   71             1001001
'\n'                58             0010011
k                   51             0010010
N                   24            00100010
I                   23            00100000
j                   20           100110110
A                   18           100110100
W                   18           100110101
T                   14           100100000
L                   12           001000011
"                   12          1001101111
G                    9          1001000111
!                    8          1001000010
'                    8          1001000011
S                    8          1001000110
M                    7          0010001110
C                    6          0010000100
q                    6          0010001100
z                    6          0010001101
x                    5         10011011101
B                    4         10010001001
F                    4         10010001010
O                    4         10011011100
P                    3         00100001010
Y                    3         00100001011
-                    2        001000111101
:                    2        001000111110
;                    2        001000111111
€                    1        001000111100
?                    1       1001000100000
D                    1       1001000100001
E                    1       1001000100010
H                    1       1001000100011
J                    1       1001000101100
R                    1       1001000101101
â                    1       1001000101110
”                    1       1001000101111

King.txt zipped to huffman.zip

Expected cost of Huffman code: 39683
Expected cost of ASCII code: 72504
Huffman efficiency improvement over ASCII code: 83%
Expected cost of optimal FCL code: 54378
Huffman efficiency improvement over FCL: 37%
The size of King.txt: 9063
The size of huffman.zip: 4961
The size of huffman.unzipped.txt: 9121  //There are 58 newline characters which accounts for this discrepancy
```