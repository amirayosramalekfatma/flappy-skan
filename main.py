import pygame
import sys
import random

def draw_floor():
    screen.blit(floor,(floor_x_pos,460))
    screen.blit(floor,(floor_x_pos + 576,460))

#level 1

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos)) #midtop=midbottom pour rester en parallèle
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos - 420))
    return bottom_pipe,top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3 #rapprocher les pipes à chaque fois qu'on diminue la valeur
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

#def remove_pipes(pipes):
    #for pipe in pipes:
        #if pipe.centerx == -600:
            #pipes.remove(pipe)
    #return pipes

def check_collision(pipes):
    for pipe in pipes:
        if butterfly_rect.colliderect(pipe):
            flap_sound.play()
            return False
    if butterfly_rect.top <= -100 or butterfly_rect.bottom >= 600:
        return False

    return True

def start():
    # display = "press space bar to start"
    display = startFont.render(f"PRESS SPACE BAR TO START", True, (255, 255, 255))
    screen.blit(display, (20,200))
    pygame.display.update()

def score_display(game_state):
    if game_state == 'main game':
        score_surface = game_font.render(str(int(score)), True,(200,0,0))
        score_rect = score_surface.get_rect(center = (500,120))
        screen.blit(score_surface,score_rect)

    if game_state == 'game over':
        score_surface = game_font.render(f'Score: {int(score)}' , True,(200,0,0))
        score_rect = score_surface.get_rect(center = (150,100))
        screen.blit(score_surface,score_rect)

        high_score_surface = game_font.render(f'High_score: {int(high_score)}' , True,(200,0,0))
        high_score_rect = high_score_surface.get_rect(center = (150,70))
        screen.blit(high_score_surface,high_score_rect)

def updated_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

#level 2

def check_collision1(pipes):
    for pipe in pipes:
        if butterfly_rect.colliderect(pipe) :
            flap_sound.play()
            return False
    if butterfly_rect.top <= -100 or butterfly_rect.bottom >= 600:
        return False

    return True

def create_pipe1():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface1.get_rect(midtop = (700,random_pipe_pos)) #midtop=midbottom pour rester en parallèle
    top_pipe = pipe_surface1.get_rect(midbottom = (700,random_pipe_pos - 420))
    return bottom_pipe,top_pipe

def move_pipes1(pipes):
    for pipe in pipes:
        pipe.centerx -= 3 #rapprocher les pipes à chaque fois qu'on diminue la valeur
        pipe.centery -= 0.2

    return pipes

def draw_pipes1(pipes):
    for pipe in pipes:
        if pipe.bottom >= 800:
            screen.blit(pipe_surface1,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface1,False,True)
            screen.blit(flip_pipe,pipe)

#pygame.mixer.pre_init(frequency=110,size=16,channels=1,buffer=12)
pygame.init()
screen = pygame.display.set_mode((1024,576))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('049-19.ttf',40)

#games variables
gravity = 0.25
butterfly_movement = 0
game_active = True
score = 0
high_score = 0
x=150
y=100

#images
background = pygame.image.load("C:\\Users\\Fatma Essid\\Downloads\\noel.jpg").convert()
background = pygame.transform.scale2x(background)

floor = pygame.image.load("C:\\Users\\Fatma Essid\\OneDrive\\Bureau\\fb3.png").convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

butterfly_surface=pygame.Surface((10,10))
butterfly_surface=pygame.image.load("C:\\Users\\Fatma Essid\\Downloads\\fb2-1.png").convert_alpha()
butterfly_surface = pygame.transform.scale(butterfly_surface, (100, 100)) #dimensions de la papillon
butterfly_rect=butterfly_surface.get_rect(center=(50,30))

pipe_surface = pygame.image.load("C:\\Users\\Fatma Essid\\OneDrive\\Bureau\\fb4.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_surface1 = pygame.image.load("C:\\Users\\Fatma Essid\\OneDrive\\Bureau\\fb5.png").convert()
pipe_surface1 = pygame.transform.scale2x(pipe_surface1)
pipe_list = []
pipe_list1= []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1010)
pipe_height = [400,500,600]

#sounds
bg_music = pygame.mixer.Sound("C:\\Users\\Fatma Essid\\Downloads\\chritsmas song.mp3")
flap_sound = pygame.mixer.Sound("C:\\Users\\Fatma Essid\\Downloads\\sound_sfx_hit.wav")
score_sound = pygame.mixer.Sound("C:\\Users\\Fatma Essid\\Downloads\\sound_sfx_point.wav")
score_sound_countdown = 300

#start the game
start_surface = pygame.transform.scale2x(pygame.image.load("C:\\Users\\Fatma Essid\\Downloads\\press_to_start1.png")).convert_alpha()
start_rect = start_surface.get_rect(center = (512,230))

#game over
game_over_surface = pygame.transform.scale2x(pygame.image.load("C:\\Users\\Fatma Essid\\Downloads\\game over.png").convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (512,100))

#restart the game
restart_surface = pygame.transform.scale2x(pygame.image.load("C:\\Users\\Fatma Essid\\Downloads\\flèche.png").convert_alpha())
restart_rect = restart_surface.get_rect(center = (512,280))

while True:
    bg_music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                butterfly_movement = 0
                butterfly_movement -= 6
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                butterfly_rect.center = (50,30)
                butterfly_movement = 0
                score = 0

        if event.type == SPAWNPIPE and score<5:
            pipe_list1.clear()
            pipe_list.extend(create_pipe())
            game_active = check_collision(pipe_list)

        if event.type == SPAWNPIPE and score > 5:
            pipe_list.clear()
            pipe_list1.extend(create_pipe1())
            pipe_list1 = move_pipes1(pipe_list1)
            draw_pipes1(pipe_list1)
            game_active = check_collision1(pipe_list1)

    screen.blit(background,(0,0))

    if game_active:
        # butterfly
        butterfly_movement += gravity
        butterfly_rect.centery += butterfly_movement
        screen.blit(butterfly_surface, butterfly_rect)
        #game_active = check_collision(pipe_list)
        #game_active = check_collision1(pipe_list1)

        # pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        game_active = check_collision(pipe_list)
        pipe_list1 = move_pipes1(pipe_list1)
        draw_pipes1(pipe_list1)

        # score
        score += 0.01
        score_display('main game')
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100

    else:
        score_display('game over')
        #death_sound.play()
        screen.blit(restart_surface, restart_rect)
        screen.blit(game_over_surface, game_over_rect)
        high_score = updated_score(score, high_score)
    #if score == 5:
        # pipe_list.clear()
        #pipe_list = move_pipes1(pipe_list)
        # pipe_list = remove_pipes()
        #draw_pipes(pipe_list)
        # pipe_list.extend(create_pipe1())

    #floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -100:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(100)