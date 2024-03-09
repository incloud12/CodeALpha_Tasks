import pygame
import math
import random

# Setting Display
pygame.init()
WIDTH, HEIGHT = 900, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game :)") 


# fonts
Letter_font = pygame.font.SysFont('Oswald', 40)
Word_Font = pygame.font.SysFont('Oswald', 60)
Title_Font = pygame.font.SysFont('MOswald', 50)
Hint_Font= pygame.font.SysFont('Oswald',30)


# Creating buttons
Radius = 25
Space = 15
letters = []
startx = round((WIDTH - (Radius * 2 + Space) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + Space * 2 + ((Radius * 2 + Space) * (i % 13))
    y = starty + ((i // 13) * (Space + Radius * 2))
    letters.append([x, y, chr(A + i), True])
    

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["SCIENCE","PYTHON","PROGRAMMING","ALGORITHMS","MATHS","ROBOTICS",]
word = random.choice(words)
guessed = []

# color
GREEN = (128,225,155)
BLACK = (0,0,0)
YELLOW=(249,255,128)
PASTEL_BLUE = (202,228,241)

def draw():
    win.fill(PASTEL_BLUE)

    # draw title
    text = Title_Font.render("SAVE THE HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = Word_Font.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win,BLACK, (x, y), Radius, 3)
            
            text = Letter_font.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(PASTEL_BLUE)
    text = Word_Font.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < Radius:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You WON!")
            break

        if hangman_status == 6:
            display_message("You LOST!")
            break
    
while True:
    
    main()
    
pygame.quit()
