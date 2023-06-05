import pygame
from helper import load_image
from Button import Button

class SpaceGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.x_button = Button("close_button.png", self.screen)

        self.x_button.resize(25,25)
        self.x_button.set_coords(self.screen.get_width() - self.x_button.width, 0)
    
    def welcome_loop(self):
        while True:
            pass

    
    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_logic()
            self._draw()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the close button is clicked
                if self.x_button.rect.collidepoint(event.pos):
                    self.running = False

    def _process_logic(self):
        pass

    def _draw(self):
        self.screen.fill("black")
        self.screen.blit(self.x_button.image, (self.x_button.x, self.x_button.y))
        pygame.display.flip()

# # pygame setup
# def run():
#     pygame.init()
#     screen = pygame.display.set_mode((1280, 720))
#     clock = pygame.time.Clock()
#     running = True
#     dt = 0

#     #code for welcome screen


#     player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#     new_image = load_image("close_button.png")
#     close_button_image = pygame.transform.scale(new_image, (25, 25))

#     close_button_x = screen.get_width()  - close_button_image.get_width() 
#     close_button_y = 0
#     close_button_width = close_button_image.get_width()
#     close_button_height = close_button_image.get_height()
#     close_button_rect = pygame.Rect(close_button_x, close_button_y, close_button_width, close_button_height)

#     while running:
#         # poll for events
#         # pygame.QUIT event means the user clicked X to close your window
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 # Check if the close button is clicked
#                 if close_button_rect.collidepoint(event.pos):
#                     running = False

#         # fill the screen with a color to wipe away anything from last frame
#         screen.fill("black")

#         pygame.draw.circle(screen, "red", player_pos, 40)

#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_w]:
#             player_pos.y -= 300 * dt
#         if keys[pygame.K_s]:
#             player_pos.y += 300 * dt
#         if keys[pygame.K_a]:
#             player_pos.x -= 300 * dt
#         if keys[pygame.K_d]:
#             player_pos.x += 300 * dt

#         screen.blit(close_button_image, (close_button_x, close_button_y))

#         # flip() the display to put your work on screen
#         pygame.display.flip()

#         # limits FPS to 60
#         # dt is delta time in seconds since last frame, used for framerate-
#         # independent physics.
#         dt = clock.tick(60) / 1000

#     pygame.quit()

if __name__ == '__main__':
    game = SpaceGame()
    game.main_loop()