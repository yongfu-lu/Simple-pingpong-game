import pygame
from pygame.locals import *
from Paddle import *
from Ball import *

pygame.init()

#window set up
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Ping Pong")

fps = 60
clock = pygame.time.Clock()

#colors
bg_color = (234, 218, 184)
paddle_col = (142, 135, 123)
paddle_outline = (100, 100, 100)
ball_color = (255, 165, 0)


#font
font_color = (78, 81, 139)
font = pygame.font.SysFont("Constantia", 30)

#draw text
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


#player paddles
player1 = Paddle(1, screen_width, screen_height)
player2 = Paddle(2, screen_width, screen_height)

#Pingpong Ball
ball = Ball(player1)

#functions
def draw_player(player):
    pygame.draw.rect(screen, paddle_col, player.rect)
    pygame.draw.rect(screen, paddle_outline, player.rect, 3)


def draw_ball(ball):
    pygame.draw.circle(screen, ball_color, (ball.rect.x + ball.rad, ball.rect.y + ball.rad), ball.rad)

def playerControl():
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player2.rect.top > 0:
        player2.move(0)

    if key[pygame.K_DOWN] and player2.rect.bottom < screen_height:
        player2.move(1)

    if key[pygame.K_w] and player1.rect.top > 0:
        player1.move(0)

    if key[pygame.K_s] and player1.rect.bottom < screen_height:
        player1.move(1)


def ball_move(ball):
    #player 2 wins
    if ball.rect.left < 0:
        return 2
    #player1 wins
    if ball.rect.right > screen_width:
        return 1

    if ball.rect.top < 0 or ball.rect.bottom > screen_height:
        ball.speed_y *= -1

    ball.move()


def check_collision(ball, player):
    if ball.rect.colliderect(player):
        # check if collision was from above:
        if abs(ball.rect.bottom - player.rect.top) < collision_thresh and ball.speed_y > 0:
            ball.speed_y *= -1
        # check if collision was from below:
        if abs(ball.rect.top - player.rect.bottom) < collision_thresh and ball.speed_y < 0:
            ball.speed_y *= -1
        # check if collision was from left:
        if abs(ball.rect.right - player.rect.left) < collision_thresh and ball.speed_x > 0:
            ball.speed_x *= -1
        # check if collision was from right:
        if abs(ball.rect.left - player.rect.right) < collision_thresh and ball.speed_x < 0:
            ball.speed_x *= -1

#game variables
collision_thresh = 5
run = True
game_on = -1
winner = 0
first_player_turn = True
player1_score = 0
player2_score = 0

#running game
while run:
    clock.tick(fps)
    screen.fill(bg_color)

    draw_player(player1)
    draw_player(player2)
    draw_ball(ball)
    draw_text(f"{player1_score} : {player2_score} ", font, font_color, 270, 30)

    if game_on == -1:
        draw_text("Click Any Where To Start", font, font_color, 150, screen_height // 2 + 100)

    elif game_on == 1:
        playerControl()
        result = ball_move(ball)
        check_collision(ball, player1)
        check_collision(ball, player2)

        if result == 1 or result == 2:
            game_on = 0
            first_player_turn = not first_player_turn
            winner = result
            if result == 1:
                player1_score += 1
            else:
                player2_score += 1

    elif game_on == 0:
        draw_text(f"Player {winner} Won!", font, font_color, 200, screen_height // 2 + 100)
        draw_text("Click For Next Round", font, font_color, 130, screen_height // 2 + 150)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and game_on != 1:
            game_on = True
            player1.reset(1,screen_width,screen_height)
            player2.reset(2,screen_width,screen_height)
            if first_player_turn:
                ball.reset(player1)
            else:
                ball.reset(player2)

    pygame.display.update()


pygame.quit()