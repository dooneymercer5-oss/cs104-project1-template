# [Music Fan Personality Quiz]
> Discover what your music taste says bout you!!

## Overview
This program is a Music Personality Quiz that asks the user five questions about their music preferences. Each answer gives points to a specific music genre: Hip-Hop, R&B, or Pop. At the end of the quiz, the program compares the genre scores and gives the user a music personality result.

The possible results are:
Hip-Hop Fan
R&B Fan
Pop Fan
Mixed Music Fan

## Sample Questions and Responses
Question 1
What type of music do you listen to the most?
A.Hip-Hop/Rap
B.R&B
C.Pop
D.A little bit of everything

Question 2
What do you care about most in a song?
A.A good beat
B.The emotions and vocals
C.A catchy chorus
D.All of these

Question 3
Where would you rather hear your favorite music?
A.At a party
B.In the car
C.At a concert
D.Anywhere

Question 4
What makes an artist stand out to you?
A.Their lyrics
B.Their voice
C.Their popularity
D.Their overall style

Question 5
How often do you listen to music?
A.All day
B.A few hours a day
C.Sometimes
D.Whenever I feel like it

## Variables
hip_hop (int): keeps track of the number of Hip-Hop points the user earns. A separate variable is needed because the program compares Hip-Hop's score with the other genres at the end.

rnb (int): keeps track of the number of R&B points the user earns. It is separate so the program can compare the R&B score with the other genre scores.

pop (int): keeps track of the number of Pop points the user earns. It is separate so the program can compare the Pop score with Hip-Hop and R&B.

answer1 (str): stores the user's response to Question 1 so the program can determine which genre should receive points.

answer2 (str): stores the user's response to Question 2.

answer3 (str): stores the user's response to Question 3.

answer4 (str): stores the user's response to Question 4.

answer5 (str): stores the user's response to Question 5.

Separate variables are used for the three genre scores because the program needs to compare them individually. A single score would not show which genre the user's answers matched.

## Conditional Logic Outline
Conditional statement 1 — Question 1
If the user chooses 1, which represents Hip-Hop/Rap, add 1 point to hip_hop.
Else if the user chooses 2, which represents R&B, add 1 point to rnb.
Else if the user chooses 3, which represents Pop, add 1 point to pop.
Else, add 1 point to all three genres because the user chose a response representing a variety of music.

Conditional statement 2 — Question 2
If the user chooses 1, which represents caring about a good beat, add 1 point to hip_hop.
Else if the user chooses 2, which represents emotions and vocals, add 1 point to rnb.
Else if the user chooses 3, which represents a catchy chorus, add 1 point to pop.
Else, add 1 point to all three genres.

Conditional statement 3 — Question 3
If the user chooses 1, which represents listening at a party, add 1 point to hip_hop.
Else if the user chooses 2, which represents listening in the car, add 1 point to rnb.
Else if the user chooses 3, which represents listening at a concert, add 1 point to pop.
Else, add 1 point to all three genres.

Conditional statement 4 — Question 4
If the user chooses 1, which represents an artist's lyrics, add 1 point to hip_hop.
Else if the user chooses 2, which represents an artist's voice, add 1 point to rnb.
Else if the user chooses 3, which represents an artist's popularity, add 1 point to pop.
Else, add 1 point to all three genres.

Conditional statement 5 — Question 5
If the user chooses 1, which represents listening to music all day, add 1 point to hip_hop.
Else if the user chooses 2, which represents listening for a few hours a day, add 1 point to rnb.
Else if the user chooses 3, which represents listening sometimes, add 1 point to pop.
Else, add 1 point to all three genres.

Conditional statement 6 — Final Results
If the Hip-Hop score is greater than both the R&B and Pop scores, display "Hip-Hop Fan."
Else if the R&B score is greater than both the Hip-Hop and Pop scores, display "R&B Fan."
Else if the Pop score is greater than both the Hip-Hop and R&B scores, display "Pop Fan."
Else, display "Mixed Music Fan."
This final conditional is not nested because it runs after all five questions have been answered and uses the three accumulated genre scores to determine the final result.

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
