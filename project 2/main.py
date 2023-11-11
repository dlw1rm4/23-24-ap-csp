import turtle as trtl
import random as rand
import leaderboard as lb

#-----setup-----
leaderboard_file_name = "leaderboard.txt"
master_file = "leaderboard_master.txt"
player_name = input("Player name: ")
lb_drawer = trtl.Turtle()
lb_drawer.hideturtle()

squirtle_image = "images/squirtle.gif" 
charmander_image = "images/charmander.gif"
bulbasaur_image = "images/bulbasaur.gif"
eevee_image = "images/eevee.gif"
pikachu_image = "images/pikachu.gif"
mewtwo_image = "images/mewtwo.gif"
player_image = "images/player.gif"

wn = trtl.Screen()
wn.addshape(squirtle_image) 
wn.addshape(charmander_image)
wn.addshape(bulbasaur_image)
wn.addshape(eevee_image)
wn.addshape(pikachu_image)
wn.addshape(mewtwo_image)
wn.addshape(player_image)
wn.bgpic("images/background.gif")

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.pu()
score_writer.setx(-250)
score_writer.sety(200)
score_writer.pd()
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
timer_up = False
counter_interval = 1000
counter = trtl.Turtle()
counter.hideturtle()
counter.pu()
counter.setx(175)
counter.sety(200)
counter.pd()

pokemon = trtl.Turtle()
flag = False
player_turtle = trtl.Turtle()
player_turtle.shape(player_image)
player_turtle.pu()

pokemon_char = [bulbasaur_image, charmander_image, eevee_image, squirtle_image, pikachu_image, mewtwo_image]
index = 0

#-----functions-----
def spawnPokemon():
  global pokemon
  global index
  global pokemon_char
  pokemon.penup()
  pokemon.shape(pokemon_char[index])
  wn.tracer(False)
  pokemon.setx(rand.randint(-200,200))
  pokemon.sety(rand.randint(-200,200))
  pokemon.showturtle()
  wn.tracer(True)
  wn.update()

def caught():
  global index
  global letters
  pokemon.hideturtle()
  if(index == 5):
    index = 0
  else:
    index += 1
  spawnPokemon()

def interact():
  global score
  global index
  global pokemon
  global player_turtle
  if ((player_turtle.xcor() > pokemon.xcor() - 50 and player_turtle.xcor() < pokemon.xcor() + 50) and (player_turtle.ycor() > pokemon.ycor() - 50 and player_turtle.ycor() < pokemon.ycor() + 50)):
    score += index + 1
    update_score(score)
    caught()

def typedW():
  player_turtle.setheading(90)
  player_turtle.forward(15)
  
def typedA():
  player_turtle.setheading(180)
  player_turtle.forward(20)

def typedS():
  player_turtle.setheading(270)
  player_turtle.forward(20)
  
def typedD():
  player_turtle.setheading(0)
  player_turtle.forward(20)

def update_score(score):
    score_writer.clear()
    score_writer.write("Score: " + (str) (score), font=font_setup)

def manage_leaderboard():

  global score
  global spot

  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, lb_drawer, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, lb_drawer, score)
  
  #for index in range(len(leader_names)):
    #leaderboard_file.write(leader_names[index] + "," + str(leader_scores[index]) + "\n")
  
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    player_turtle.hideturtle()
    pokemon.clear()
    pokemon.hideturtle()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

  
#-----function calls-----
spawnPokemon()
update_score(score)
wn.onkeypress(typedW, 'w')
wn.onkeypress(typedA, 'a')
wn.onkeypress(typedS, 's')
wn.onkeypress(typedD, 'd')
wn.onkeypress(interact, 'e')
wn.ontimer(countdown,counter_interval)
wn.listen()
wn.mainloop()

