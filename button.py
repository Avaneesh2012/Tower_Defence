import pygame as pg

class Button():
  def __init__(self, x, y, image, single_click):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False
    self.single_click = single_click

