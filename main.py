import pygame


pygame.init()
SCREEN_WIDTH = 795
SCREEN_HEIGHT = 410
WHITE = (0, 0, 0)
Start_Screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('STRANDED')

# Images

background = pygame.image.load('Assets/Images/Background_Image.jpg')
background = pygame.transform.scale(background, (800, 409))

Start_Button_Image = pygame.image.load('Assets/Images/Start_Game_Button.png').convert_alpha()
Start_Button_Image = pygame.transform.scale(Start_Button_Image, (300, 300))

# Music

Start_Music = pygame.mixer.music.load('Assets/Sound/Start_Screen_Music.mp3')
pygame.mixer.music.play(-1)





#Button
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False



    def draw(self):
        action = False
        # draw button on screen
        Start_Screen.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()

        def game_loop(self):
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] != 1 or self.clicked != False:
                    pass
                else:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            return action


start_button = Button (250, 60, Start_Button_Image)

# Game Events

GamePlaying = True
while GamePlaying:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            GamePlaying = False


    Start_Screen.blit(background, (0, 0))

    if start_button.draw():
        print('START')

    pygame.display.update()

pygame.quit()
