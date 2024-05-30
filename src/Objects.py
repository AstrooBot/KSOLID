import pygame
class objects:
    def __init__(self, screen, board, image):
        self.surface = screen
        self.board = board
        self.image = pygame.image.load(str('../images/' + image))
        self.rect = self.image.get_rect()
    
    def set_object(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def detect_collissions(self, object):

        if self.rect.x == self.object.rect.x:
            return True
        else:
            return False