# Problem:

# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:

# banana.png

# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# Constraints



# Sample Input

# BANANA
# Sample Output

# Stuart 12
# Note :
# Vowels are only defined as . In this problem,  is not considered a vowel.
# Solution: The total number of substrings from the given position including itself is the length of the substring from the given position
# so you just need to check whether the given position is starting with vowel or not and add it to the respective person
inputtext =  "BANANA"
vowels =['A','E','I','O','U']
stuart_score=0
kevin_score=0
for index,i in enumerate(inputtext):
    if i in vowels:
        kevin_score=kevin_score+(len(inputtext)-(index-0))
    else:
        stuart_score=stuart_score+(len(inputtext)-(index-0))
if kevin_score>stuart_score:
    print(f"Kevin {kevin_score}")
elif stuart_score>kevin_score:
    print(f"Stuart {stuart_score}")
