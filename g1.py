import pygame
import random
pygame.init()

# Colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Creating game Window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Madafuckin' snakes kill them")
pygame.display.update()



# Creating a game loop
def gameloop():
        #Game Specificatoins
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 6
    snake_size = 15

    food_x = random.randint(20,screen_width)
    food_y = random.randint(20,screen_height)
    food_size = 20
    score = 0
    fps = 60

    clock = pygame.time.Clock()
    font=pygame.font.SysFont(None,48)

    def text_screen(text, color, x, y):
        screen_text = font.render(text,True,color)
        gameWindow.blit(screen_text, [x,y])

    def plot_snake(gameWindow, color, snk_list ,snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, red, [x, y, snake_size, snake_size])    

    snk_list = []    
    snk_length = 1

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen(f"Game over! Score: {score*init_velocity} Press Enter to restart", red, 150,150)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()    

        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_RIGHT:
                        snake_x = snake_x+1
                        velocity_x = init_velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_LEFT:
                        snake_x = snake_x-1
                        velocity_x = -init_velocity
                        velocity_y = 0     

                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_DOWN:
                        snake_y = snake_y+1
                        velocity_y = init_velocity
                        velocity_x = 0  

                if event.type == pygame.KEYDOWN:
                    if  event.key == pygame.K_UP:
                        snake_y = snake_y-1
                        velocity_y = -init_velocity
                        velocity_x = 0       


            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y  
            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                score = score+1        
                food_x = random.randint(20,screen_width)
                food_y = random.randint(20,screen_height)
                food_size = 20
                snk_length = snk_length+5  
                    
            gameWindow.fill(white)
            text_screen(f"Score:{score*init_velocity}", black, 5,5)
            pygame.draw.rect(gameWindow, black, [food_x, food_y, food_size, food_size])

            head = [] 
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True    

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True    
            # pygame.draw.rect(gameWindow, red, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow,red,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
gameloop()