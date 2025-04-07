'''
Consider cities and states in the US. Each state is given a two letter abbreviation.
You are tasked to read n cities and states from the user and determine the number 
of special pairs.

Here is an example of a special pair: 
SCRANTON PA and PARKER SC
This is a special pair wince the first two characters of each city gies the 
abbreviation for the other cit's state. That is SC PA and PA SC.

A pair of cities is special if they meet this property and they are not in
the same state. Your task is to determine the number of special pairs of 
cities in the provided input. Make sure your code is efficient.

INPUT SPECIFICATION:
--> First line contains the integer n (n can be as large as 200000), 
number of cities and states.
--> the next n lines are the n cities with the corresponding state. 
Each line gives the name of the city, a space, state's 2 letter abbreviation. 
Note that the same city name can exist in multiple states, but will not appear 
more than once in the same state.

SAMPLE INPUT:
12
SCRANTON PA
MANISTEE MI
NASHUA NH
PARKER SC
LAFAYETTE CO
WASHOUGAL WA
MIDDLEBOROUGH MA
MADISON MI
MILFORD MA
MIDDELTON MA
COVINGTON LA
LAKEWOOD CO

SAMPLE OUTPUT:
9

Read 5 sample inputs from the user and write it to a file such that 
there is an empty line between any 2 sample inputs. Then from this file, 
read each sample input and determine the number of special pair of cities.
'''
