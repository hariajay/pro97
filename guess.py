number = int(7)
chance = int(5)
print('Guess a number between 1 and 20')
guess = int(input('Enter your guess:'))
clue = ["It is ID number of world's 2nd best football player",
        "It is neutral PH number",
        "It is number of colors in visible spectrum",
        "It is number of dwarfs in snow white movie"] 
g = -1
type = int(0)

while (guess != number) & (chance > 1):
   if g < 5:
    g = g + 1
   print(clue[g])
   guess = int(input('Enter your guess: '))
   chance = chance - 1 

if guess == number:
   print('Congratulations, You Won!!')
if chance == 1:
   print('Game over. The number is '+ str(number))