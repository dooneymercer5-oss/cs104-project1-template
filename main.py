# [Music Personality Quiz]
# Author: [Adrion Mercer]
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

# Question 2
print()
print("Question 2: What do you care about most in a song?")
print("1. A good beat")
print("2. The emotions and vocals")
print("3. A catchy chorus")
print("4. All of these")

answer2 = input("Enter 1, 2, 3, or 4: ")

if answer2 == "1":
    hip_hop += 1
elif answer2 == "2":
    rnb += 1
elif answer2 == "3":
    pop += 1
else:
    hip_hop += 1
    rnb += 1
    pop += 1

# Question 3
print()
print("Question 3: Where would you rather hear your favorite music?")
print("1. At a party")
print("2. In the car")
print("3. At a concert")
print("4. Anywhere")

answer3 = input("Enter 1, 2, 3, or 4: ")

if answer3 == "1":
    hip_hop += 1
elif answer3 == "2":
    rnb += 1
elif answer3 == "3":
    pop += 1
else:
    hip_hop += 1
    rnb += 1
    pop += 1

    # Question 4
print()
print("Question 4: What makes an artist stand out to you?")
print("1. Their lyrics")
print("2. Their voice")
print("3. Their popularity")
print("4. Their overall style")

answer4 = input("Enter 1, 2, 3, or 4: ")

if answer4 == "1":
    hip_hop += 1
elif answer4 == "2":
    rnb += 1
elif answer4 == "3":
    pop += 1
else:
    hip_hop += 1
    rnb += 1
    pop += 1

    # Question 5
print()
print("Question 5: How often do you listen to music?")
print("1. All day")
print("2. A few hours a day")
print("3. Sometimes")
print("4. Whenever I feel like it")

answer5 = input("Enter 1, 2, 3, or 4: ")

if answer5 == "1":
    hip_hop += 1
elif answer5 == "2":
    rnb += 1
elif answer5 == "3":
    pop += 1
else:
    hip_hop += 1
    rnb += 1
    pop += 1

    # Display final results
print()
print("====================================")
print("             YOUR RESULT")
print("====================================")

if hip_hop > rnb and hip_hop > pop:
    print("You are a HIP-HOP FAN!")
    print("You enjoy strong beats, lyrics, and high-energy music.")

elif rnb > hip_hop and rnb > pop:
    print("You are an R&B FAN!")
    print("You enjoy smooth vocals, emotions, and meaningful songs.")

elif pop > hip_hop and pop > rnb:
    print("You are a POP FAN!")
    print("You enjoy catchy songs, big artists, and memorable hooks.")

else:
    print("You are a MIXED MUSIC FAN!")
    print("You enjoy different types of music and different genres.")

print()
print("Thanks for taking the Music Fan Personality Quiz!")


# Display final results
print()
print("====================================")
print("             YOUR RESULT")
print("====================================")

if hip_hop > rnb and hip_hop > pop:
    print("You are a HIP-HOP FAN!")
    print("You enjoy strong beats, lyrics, and high-energy music.")

elif rnb > hip_hop and rnb > pop:
    print("You are an R&B FAN!")
    print("You enjoy smooth vocals, emotions, and meaningful songs.")

elif pop > hip_hop and pop > rnb:
    print("You are a POP FAN!")
    print("You enjoy catchy songs, big artists, and memorable hooks.")

else:
    print("You are a MIXED MUSIC FAN!")
    print("You enjoy different types of music and different genres.")

print()
print("Thanks for taking the Music Fan Personality Quiz!")
