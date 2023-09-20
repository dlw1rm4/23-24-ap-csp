import turtle as trtl

drtrt = trtl.Turtle()

drtrt.penup()
drtrt.goto(-100, -100)
drtrt.pendown()
for i in range(4):
    drtrt.forward(25)
    drtrt.penup()
    drtrt.forward(25)
    drtrt.pendown()

drtrt.penup()
drtrt.goto(-100, 0)
drtrt.pendown()
drtrt.forward(200)

drtrt.penup()
drtrt.goto(0, 0)
drtrt.pendown()
drtrt.left(90)
drtrt.forward(200)
drtrt.left(90)
drtrt.forward(50)
drtrt.left(90)
drtrt.forward(50)

def head(): 
    drtrt.fillcolor('yellow')
    drtrt.begin_fill()
    drtrt.penup()
    drtrt.goto(-50, 150)
    drtrt.pendown()
    drtrt.setheading(180)
    drtrt.circle(25)
    drtrt.end_fill()
def body():
    drtrt.penup()
    drtrt.goto(-50, 100)
    drtrt.setheading(270)
    drtrt.pendown()
    drtrt.forward(50)
def leg1():
    drtrt.penup()
    drtrt.goto(-50, 50)
    drtrt.pendown()
    drtrt.setheading(315)
    drtrt.forward(30)
    drtrt.back(30)
def leg2():
    drtrt.penup()
    drtrt.goto(-50, 50)
    drtrt.pendown()
    drtrt.setheading(225)
    drtrt.forward(30)
    drtrt.back(30)
def arm1():
    drtrt.penup()
    drtrt.goto(-50, 75)
    drtrt.pendown()
    drtrt.setheading(135)
    drtrt.forward(30)
    drtrt.back(30)
def arm2():
    drtrt.penup()
    drtrt.goto(-50, 75)
    drtrt.pendown()
    drtrt.setheading(45)
    drtrt.forward(30)
    drtrt.back(30)

def letterD():
    drtrt.penup()
    drtrt.goto(-90, -100)
    drtrt.pendown()
    drtrt.setheading(90)
    drtrt.forward(20)
    drtrt.back(20)
    drtrt.setheading(0)
    drtrt.circle(10, 180, 30)
def letterU():
    drtrt.penup()
    drtrt.goto(-45, -80)
    drtrt.pendown()
    drtrt.setheading(-90)
    drtrt.forward(12)
    drtrt.circle(8, 180, 30)
    drtrt.forward(15)
def letterC():
    drtrt.penup()
    drtrt.goto(15, -98)
    drtrt.pendown()
    drtrt.setheading(25)
    drtrt.circle(10, -220, 30)
def letterK():
    drtrt.penup()
    drtrt.goto(60, -100)
    drtrt.pendown()
    drtrt.setheading(90)
    drtrt.forward(20)
    drtrt.back(10)
    drtrt.setheading(45)
    drtrt.forward(15)
    drtrt.back(15)
    drtrt.setheading(-45)
    drtrt.forward(15)
    drtrt.back(15)

wrongGuess = 0
correctGuess = 0
letters = ['d', 'D', 'u', 'U', 'c', 'C', 'k', 'K']
guessed = []

while(wrongGuess < 6 and correctGuess < 4):
    checkGuess = False
    guessedVal = False
    value = input("\nGuess a letter: ")
    for guess in letters:
        if value == guess:
            checkGuess = True
    
    for guessedLetter in guessed:
        if guessedLetter == value:
            guessedVal = True

    if guessedVal == False:
        guessed.append(value)

    if guessedVal == True:
        print("You already guessed this.")
    elif value == "":
        print("No input. Try again.")
    elif checkGuess == False:
        wrongGuess += 1
        print("Incorrect. Try again.")
        if wrongGuess == 1:
            head()
        elif wrongGuess == 2:
            body()
        elif wrongGuess == 3:
            leg1()
        elif wrongGuess == 4:
            leg2()
        elif wrongGuess == 5:
            arm1()
        else:
            arm2()
    else:
        correctGuess += 1
        if value == 'd' or value == 'D':
            letterD()
        elif value == 'u' or value == 'U':
            letterU()
        elif value == 'c' or value == 'C':
            letterC()
        elif value == 'k' or value == 'K':
            letterK()

if wrongGuess >= 6:
    print("You lost :(")
else:
    print("Congratulations! You win :)")

trtl.Screen().mainloop()
