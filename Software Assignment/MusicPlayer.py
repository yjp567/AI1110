import numpy as np
import pygame
import os

# Set up pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((350, 200))
pygame.display.set_caption("Music Player")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the songs
songs = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3", "6.mp3", "7.mp3", "8.mp3", "9.mp3", "10.mp3", "11.mp3", "12.mp3", "13.mp3", "14.mp3", "15.mp3", "16.mp3", "17.mp3", "18.mp3", "19.mp3", "20.mp3"]
np.random.shuffle(songs)
# Set up the current song and the player
current_song = 0
player = pygame.mixer.music

# Play the first song
player.load(os.path.join("songs", songs[current_song]))
player.play()

# Set up the buttons
pause_button = pygame.Rect(50, 100, 90, 50)
next_button = pygame.Rect(200, 100, 70, 50)

# Run the game loop
running = True
while running:
     	
    # Check for events
    for event in pygame.event.get():

        # Quit if the window is closed
        if event.type == pygame.QUIT:
            running = False

        # Check for mouse button clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Check if the pause button was clicked
            if pause_button.collidepoint(event.pos):
                if player.get_busy():
                    player.pause()
                else:
                    player.unpause()

            # Check if the next button was clicked
            elif next_button.collidepoint(event.pos):
                current_song = (current_song + 1) % len(songs)
                player.load(os.path.join("songs", songs[current_song]))
                player.play()

    # Update the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), pause_button)
    pygame.draw.rect(screen, (0, 0, 255), next_button)
    screen.blit(font.render("Pause", True, (255, 255, 255)), (pause_button.x + 10, pause_button.y + 10))
    screen.blit(font.render("Next", True, (255, 255, 255)), (next_button.x + 10, next_button.y + 10))
    current_song_name = songs[current_song]
    screen.blit(font.render(current_song_name, True, (0, 0, 0)), (130, 50))
    pygame.display.flip()

# Quit pygame
pygame.quit()
