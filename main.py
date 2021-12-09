import turtle as t
from diem import Score
from ball import Ball
from paddle import Paddle



start_position = [(-370, 0), (360, 0)]

screen = t.Screen()
screen.title("pong the game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

game_on = True

paddle_player = Paddle(start_position[0])
AI_paddle_player = Paddle(start_position[1])

ball = Ball()

screen.listen()
screen.onkeypress(paddle_player.up, "Up")
screen.onkeypress(paddle_player.down, "Down")
screen.onkeypress(AI_paddle_player.up, "w")
screen.onkeypress(AI_paddle_player.down, "s")

score=Score()
score.update_score()
# main game_loop
while game_on:
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceborder()
    if (
            ball.xcor() < -360 and ball.ycor() > -362 and ball.ycor() < paddle_player.ycor() + 50 and ball.ycor() > paddle_player.ycor() - 50) or (
            ball.xcor() > 348 and ball.xcor() < 351 and ball.ycor() < AI_paddle_player.ycor() + 50 and ball.ycor() > AI_paddle_player.ycor() - 50):
        ball.bounce_paddle()

    # score and reset position
    if ball.xcor()<-370:
        ball.reset_position()
        score.r_score+=1
        score.update_score()

    if ball.xcor()>365:
        ball.reset_position()
        score.l_score+=1
        score.update_score()

