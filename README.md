
# Maximal_repeats 

This program is a solution to Rosalind's problem about maximal repeats. From a fasta file, it's return the 
maximal repetitions present in a sequence.

## Description

This script take as principal argument a fasta file and search for all the maximal repeats in the sequence.
It also take 1 or 2 optional arguments setting the length limits of the repetitions to be searched. If there is
only one argument, then the search will be limited to repetitions of at least the length spent as an argument.
If there are two arguments then the search will be limited to repetitions between the two lengths. Without these
two arguments, it is repetitions larger than 20 that are sought.


## Extensions

In order to find the maximum repetitions in the sequence, several intermediate functions were used:

- *readfasta* : takes a fasta file and k the length of the pattern  as arguments and returns the sequence contained in the file
- *occurences* : takes a fasta file as arguments  returns a dictionnary with all the words and the number of their occurences
- *sort* : takes a fasta file and k the length of the pattern as arguments and returns a sorted list of our dictionnary
- *get_positions_word* : takes a fasta file and a pattern as arguments and returns a list of the positions of the word
- *get_nt_bef* : takes a fasta file and a pattern as arguments and returns a list of all the nucleotides before the pattern
- *get_nt_after* : takes a fasta file and a pattern as arguments and returns a list of all the nucleotides after the pattern
- *full_position* : takes a fasta file and a pattern as argument and returns a list of the positions of the words, the nucleotide before and the nucleotide after 
- *all_words* : takes a fasta file and the length of the pattern k and returns a list (full_position) of each element of my sorted list (sort)
- *maximal_repeats* : takes a fasta file and the length of the pattern and returns a list of the maximal repeats in the file 

## How to launch the program

In your terminal , execute these command line for seeing the different cases

```
python3 maximal_repeats sequencetest.txt
```
```
python3 maximal_repeats sequencetest.txt 30
```
```
python3 maximal_repeats sequencetest.txt 20 30
```

## Excepted results

Let's take the exemple of the sequence of 18S rRNA of Saccharomyces cerevisiae. The software REPuter ,
who can show all the maximal repeats in a sequence , show the following results:


9  479 F     9 1514  0 3.21e+00 

9  649 F     9 1435  0 3.21e+00

9  759 F     9  897  0 3.21e+00

9  886 F     9 1302  0 3.21e+00

8   26 F     8 1466  0 1.28e+01

8   31 F     8  878  0 1.28e+01

8   36 F     8 1603  0 1.28e+01

8   98 F     8  521  0 1.28e+01

8  214 F     8 1218  0 1.28e+01

8  291 F     8 1339  0 1.28e+01

8  305 F     8 1141  0 1.28e+01

8  334 F     8 1114  0 1.28e+01

8  370 F     8  716  0 1.28e+01

8  446 F     8 1496  0 1.28e+01

8  474 F     8 1276  0 1.28e+01

8  724 F     8 1503  0 1.28e+01

8  991 F     8 1208  0 1.28e+01

8 1047 F     8 1393  0 1.28e+01

8 1124 F     8 1253  0 1.28e+01

8 1250 F     8 1627  0 1.28e+01



After launching this command line :

```
python3 maximal_repeats sacc.fasta 8
```
the results are :

GTGAAACT 8

26 ('A', 'G') 1466 ('T', 'C') 31 ('A', 'T') 878 ('T', 'A') 36 ('C', 'C') 1603 ('T', 'T')

98 ('T', 'T') 521 ('C', 'C') 214 ('C', 'T') 1218 ('T', 'G') 291 ('T', 'C') 1339 ('C', 'G') 

305 ('A', 'T') 1141 ('C', 'A') 334 ('G', 'A') 1114 ('T', 'C') 370 ('C', 'C') 716 ('A', 'T') 

446 ('C', 'G') 1496 ('A', 'A') 474 ('T', 'G') 1276 ('G', 'C') 724 ('G', 'G') 1503 ('T', 'T') 

991 ('C', 'T') 1208 ('T', 'G') 1047 ('G', 'G') 1393 ('C', 'C') 1124 ('G', 'T') 1253 ('T', 'G')

1250 ('G', 'A') 1627 ('A', 'G') AACGAGGAA 9 479 ('T', 'C') 1514 ('C', 'T') 649 ('G', 'A') 1435 

('T', 'G') 759 ('T', 'G') 897 ('A', 'T') 886 ('A', 'C') 1302 ('T', 'T')

Indeed, we notice that all the different occurences are shown, but not in a order way.


For the sequence initially giving as test (sequencetest.txt) , the results are pretty much conform with 
the results excepted. The results excepted are :

$ python3 maximal_repeats.py test.fasta 20 30
ATGGGTCCAGAGTTTTGTAATTT 23 10 (A,C) 35 (C,A) 74 (A,C) 99 (C,A)


```
python3 maximal_repeats sequencetest.txt 20 30
```
This command  should give us the word with a length between 20 and 30:

ATGGGTCCAGAGTTTTGTAATTT 23
10 ('A', 'C')
35 ('C', 'A')
74 ('A', 'C')
99 ('C', 'A')


Let's take another exemple. We're doing the test with a random sequence of DNA contained in the random.txt

```
python3 maximal_repeats random.txt 
```
The program will only take the words with a length superior to 20 
The results from REPuter with a minimal length of 20 gives us :

22  24 F 22  99  0 3.50e-10

Our command line will give us the results :
TAGACATAGCGATCATCAGACA 22 
24 ('C', 'T')
99 ('T', 'C')

These three comparaisons show us that the program works effectively. Only the output format will differ from 
the two programs


## Program Weakness

Due to a lack of optimization of the program(in this case the number of loops used in the different functions)
 this program is only able to take small sequences. Indeed, it will search for all words ranging from the number
 entered (to 20 by default) to the length of the sequence filled in. So the time he'll take to resolve a sequence
 of 100pb sequence will be shorter than the time taken for a 35000pb sequence. 

## Contact

If you found an issue or would like to submit an improvment to this project , you can contact me via [LinkedIn](https://www.linkedin.com/in/ndeye-khoudia-thiam/) or by email (khoudiathiampro@gmail.com)
