# Scrabble Project
This project was inspired by my friend's homework assignment from UC Berkeley MIDS program. 
I thought it would be fun to implement it since I never played Scrabble before.

## ☁️ About The Project
For those of you not familiar with the game (like me), I wrote down some basic rules that are implemented in this project. 
You can search for Scrabble rules if you are more interested in the official rule.

* You can use two to seven letters (upper or lower case) to create valid words in English dictionary
* You will not be restrict with the number of same tiles (i.e., you can input ZZZZZQQ)
* You are allowed to use one of each wildcards, namely "*" and "?"
* Your score will be computed based on the word that you created (wildcards are scored as 0 points) 


## 📝 Overview
*scrabble.py* contains the main function that takes a Scrabble rack (the letters) as a function argument
and prints a list of valid Scrabble english words that can be constructed from the rack, along with their Scrabble scores,
and total number of valid words as an integer. The list is sorted by scores and then by the word alphabetically.\
\
*wordscore.py* simply calculates the score of the word that is constructed by the rack. It contains a score table as a reference.\
\
*sowpods.txt* has all valid Scrabble English words in the official list, one word per line.
You can use http://courses.cms.caltech.edu/cs11/material/advjava/lab1/sowpods.zip if you want to download it yourself.\
\
Because the assignment disallowed error handling or raising an exception, input errors were handled crudely.
I might update the error handle or implement additional rules in the future.
