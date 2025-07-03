**Voting System Analysis Data Summary Document**

DATA ATTRIBUTION:
https://www.idea.int/data-tools/data/electoral-system-design-database - voting system dataset, with voting turnouts, voting systems and national legislature size
https://www.gapminder.org/data/ - GapMinder Systema Globalis dataset, including social metrics

# DATA FROM VOTING SYSTEM ANALYSIS

## DESCRIPTIVE STATISTICS

### VOTING SYSTEMS
Voting systems used in Presidential elections (by type):
Not applicable    104    
TRS                87    
FPTP               22    
Other               1    
STV                 1    
In transition       1    
SV                  1    
Name: count, dtype: int64

------------------------------------------------------------

Voting systems used in Parliamentary elections (by type):
List PR                  76
FPTP                     47
Parallel                 25
TRS                      17
BV                       10
MMP                       7
No direct elections       7
SNTV                      5
#FPTP\n#BV                3
STV                       3
#BV\n#FPTP                3
#FPTP\n#PBV               2
#FPTP\n#List PR           2
AV                        2
#FPTP\n#PBV\n#List PR     1
#TRS\n#PBV\n#List PR      1
#TRS\n#PBV                1
LV                        1
Modified BC               1
Name: count, dtype: int64

------------------------------------------------------------

### Compulsion of voting
Is voting for President compulsory? (by answer):
No     99
Yes    17

Is voting for the Parliament compulsory (by answer, where applicable):
No     25
Yes     4

Average turnouts for presidential elections for countries in which presidential voting is compulsory
  PresComp  Presidential Avg Turnout %
0       No                    0.638358
1      Yes                    0.698612

Average turnouts for parliamentary elections for countries in which parliamentary voting is compulsory
  ParlComp  Parliamentary Avg Turnout %
0       No                     0.679482
1      Yes                     0.717663

------------------------------------------------------------
### Turnout data
Overall description of turnout data:
       PresVotTurn  ParlVotTurn
count  1260.000000  2384.000000
mean     65.353643    71.169417
std      15.225068    16.256280
min      18.110000     2.730000
25%      55.020000    60.345000
50%      65.260000    73.120000
75%      76.680000    83.722500
max      98.410000   102.620000

Overall description of average turnout data:
       PresVotTurn  Presidential Avg Turnout %  ParlVotTurn  Parliamentary Avg Turnout %
count   113.000000                  113.000000   199.000000                   199.000000
mean     64.742301                    0.647423    69.148936                     0.691489
std      16.814379                    0.168144    13.229125                     0.132291
min      18.110000                    0.181100    29.156667                     0.291567
25%      54.090000                    0.540900    61.832222                     0.618322
50%      64.810000                    0.648100    69.251667                     0.692517
75%      77.490000                    0.774900    77.220833                     0.772208
max      98.410000                    0.984100    99.860000                     0.998600

Lowest average presidential turnout: Haiti (18.11%)
Country                            Haiti
PresVotTurn                        18.11
Presidential Avg Turnout %        0.1811
ParlVotTurn                    35.023333
Parliamentary Avg Turnout %     0.350233

Lowest average parliamentary turnout: Mali (29.16%)
Country                             Mali
PresVotTurn                        34.42
Presidential Avg Turnout %        0.3442
ParlVotTurn                    29.156667
Parliamentary Avg Turnout %     0.291567

Highest average presidential turnout: Equatorial Guinea (91.8%)
Country                        Equatorial Guinea
PresVotTurn                                98.41
Presidential Avg Turnout %                0.9841
ParlVotTurn                                 91.8
Parliamentary Avg Turnout %                0.918

Highest average parliamentary turnout: Somalia (99.86%)
Country                        Somalia
PresVotTurn                        NaN
Presidential Avg Turnout %         NaN
ParlVotTurn                      99.86
Parliamentary Avg Turnout %     0.9986

Minimal recorded presidential turnout: Haiti 2016 (17.82%):
Country             Haiti
ISO2                 HT
ISO3                HTI
Year           2016-11-20
PresVotTurn         18.11

Minimal recorded parliamentary turnout: Jamaica 1983 (2.73%):
Country           Jamaica
ISO2                 JM
ISO3                JAM
year           1983-01-01
ParlVotTurn          2.73

Maximal recorded presidential turnout: Equatorial Guinea 2022 (98.41%):
Country        Equatorial Guinea
ISO2                        GQ
ISO3                       GNQ
Year                  2022-01-01
PresVotTurn                98.41

Maximal recorded parliamentary turnout: Bolivia 1978 (102.62%):*
Country           Bolivia
ISO2                 BO
ISO3                BOL
year           1978-01-01
ParlVotTurn        102.62


------------------------------------------------------------
### Voting system data
Count of types of votes used in parliamentary elections

List PR                  76
FPTP                     47
Parallel                 25
TRS                      17
BV                       10
MMP                       7
No direct elections       7
SNTV                      5
#FPTP\n#BV                3
STV                       3
#BV\n#FPTP                3
#FPTP\n#PBV               2
#FPTP\n#List PR           2
AV                        2
#FPTP\n#PBV\n#List PR     1
#TRS\n#PBV\n#List PR      1
#TRS\n#PBV                1
LV                        1
Modified BC               1

Count of types of votes used in presidential elections
Not applicable    104
TRS                87
FPTP               22
Other               1
STV                 1
In transition       1
SV                  1


Average turnouts for presidential election per election system
       PresSystem  Presidential Avg Turnout %
0            FPTP                    0.703427
1   In transition                         NaN
2  Not applicable                    0.596450
3           Other                    0.903700
4             STV                    0.438700
5              SV                    0.794600
6             TRS                    0.632864

Average turnouts for parliamentary elections per election system
               ParlSystem  Parliamentary Avg Turnout %
0              #BV\n#FPTP                     0.607260
1              #FPTP\n#BV                     0.703652
2         #FPTP\n#List PR                     0.606506
3             #FPTP\n#PBV                     0.651535
4   #FPTP\n#PBV\n#List PR                     0.680400
5              #TRS\n#PBV                     0.400630
6    #TRS\n#PBV\n#List PR                     0.530467
7                      AV                     0.810531
8                      BV                     0.783967
9                    FPTP                     0.683911
10                     LV                     0.751325
11                List PR                     0.702444
12                    MMP                     0.723615
13            Modified BC                     0.921927
14    No direct elections                     0.998600
15               Parallel                     0.658565
16                   SNTV                     0.581679
17                    STV                     0.822492
18                    TRS                     0.671378












* From [Wikipedia](https://en.wikipedia.org/wiki/1978_Bolivian_general_election):
"The official results were inconsistent; the reported total number of votes cast was 1,971,968, around 50,000 more than the number of registered voters (1,921,556), giving a turnout of 102.6%. However, the total of votes cast for each party and invalid votes was 1,990,671, nearly 20,000 higher than the reported total and representing a turnout of 103.6%"