# Music Personality Quiz
# Author: Adrion Mercer
# A quiz/questionnaire program built for CS 104 Project 1

# Variables to keep track of music genre scores
hip_hop = 0
rnb = 0
pop = 0

print("====================================")
print("       MUSIC FAN PERSONALITY QUIZ")
print("====================================")
print("Answer the questions to find out what type of music fan you are!")
print()

# Question 1
print("Question 1: What type of music do you listen to the most?")
print("1. Hip-Hop/Rap")
print("2. R&B")
print("3. Pop")
print("4. A little bit of everything")

answer1 = input("Enter 1, 2, 3, or 4: ")

if answer1 == "1":
    hip_hop += 1
elif answer1 == "2":
    rnb += 1
elif answer1 == "3":
    pop += 1
else:
    hip_hop += 1
    rnb += 1
    pop += 1
