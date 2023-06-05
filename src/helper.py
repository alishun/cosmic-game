import os
import pygame

def load_image (image):
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    sibling_dir = os.path.join(parent_dir, 'assets')
    file_path = os.path.join(sibling_dir, image)
    return pygame.image.load(file_path)