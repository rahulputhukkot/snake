import random
import pygame

pygame.init()

dis_width = 600
dis_height = 400

yellow = (255, 255, 102) # score
black = (0, 0, 0) # background
red = (213, 50, 80) # message
green = (0, 255, 0) # food
blue = (50, 153, 213) # snake


#snake size
snake_block = 10
snake_speed=15

display = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake game")
 
clock = pygame.time.Clock()

font = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("cambria", 35)

def snake(snake_block, snake_list):
    for loc in snake_list:
        pygame.draw.rect(display, blue, [loc[0], loc[1], snake_block, snake_block])

def display_score(score):
    value = font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])
           
def message(msg,color):
    mesg = font.render(msg, True, color)
    display.blit(mesg, [0, dis_height/4])

def gameloop():
    #postion the snake at the center       
    x = dis_width/2 
    y = dis_height /2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    game_over = False
    game_close = False

    # position of food 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        while game_close == True:
            display.fill(black)
            message("You Lost! press Q to quit or P to play again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close=False
                        game_over=True
                    elif event.key == pygame.K_p:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >=dis_width or x < 0 or y >= dis_height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(black)
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block]) # food
        
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]   
        
        for i in snake_list[:-1]:
            if i == snake_Head:
                game_close = True 

        snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()
        
        print("X:",x, "y:", y, "foodx", foodx, "foody", foody)
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            print("Tasty!!")
            length_of_snake +=1
            global snake_speed
            snake_speed +=2

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameloop()