# Disco_zoo_analysis

Run in terminal with all .py files in th same folder: python Disco.py

Disco Zoo is a mobile app game. A 5X5 empty game board contains animals that one must uncover within 10 moves. Each of the animals has a different pattern that is made up of 2-4 tiles. See these patterns at the following link:  http://discozoowiki.com/wiki/Patterns . 

Each game that the player undertakes has 1-3 animals to uncover in those 10 moves. In this analysis, I restrained the number of animals to uncover to 2 as 1 is too simple for calculations and 3 usually requires more than 10 moves. This program calculates the win rate for every possible 2 animal pairing. A win here is defined by completely uncovering both animals.

Results are in Probabilities_Summary.xlsx

The program runs over one habitat, change line 1 for the individual animal_dict_# you want to run over,(Farm = 1 -> Mars = 12) as well as the output.csv filename so as to not overwrite.
