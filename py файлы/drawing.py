import math

import pygame
from settings import *
from ray_cast import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.sdvig_teksta = - 10
        self.texture = {'1': pygame.image.load('textures/Wall1Texture.png').convert(),
                        '2': pygame.image.load('textures/Wall2.jpg').convert(),
                        '3': pygame.image.load('textures/Wall3.jpg').convert(),
                        '4': pygame.image.load('textures/Wall4.jpg').convert(),
                        '5': pygame.image.load('textures/Wall5.jpg').convert(),
                        '6': pygame.image.load('textures/Wall6.jpg').convert(),
                        '7': pygame.image.load('textures/WallOfLiftTexture.png').convert(),
                        '8': pygame.image.load('textures/WallOfHotelTexture.png').convert(),
                        '9': pygame.image.load('textures/Wall2OfHotelTexture.png').convert(),
                        '*': pygame.image.load('textures/ExitTexture.png').convert(),
                        '%': pygame.image.load('textures/ControlTutorialTexture.png').convert(),
                        'sky': pygame.image.load('textures/potolok.png').convert(), }
        self.remaining_shards = 80

    def background(self, angle):
        try:
            sky_offset = -5 * math.degrees(angle) % WIDTH
            self.sc.blit(self.texture['sky'], (sky_offset, 0))
            self.sc.blit(self.texture['sky'], (sky_offset - WIDTH, 0))
            self.sc.blit(self.texture['sky'], (sky_offset + WIDTH, 0))
            pygame.draw.rect(self.sc, (40, 40, 40), (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        except:
            pass

    def world(self, world_objects):
        try:
            for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
                if obj[0]:
                    _, object, object_pos = obj
                    self.sc.blit(object, object_pos)
        except:
            pass

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = pygame.font.SysFont('Arial', 36, bold=True).render(display_fps, 0, 'red')
        self.sc.blit(render, FPS_POS)

    def draw_okantovka(self, shift, smesh):
        pygame.draw.rect(self.sc, 'black',
                         (MAPP_SDVIG_X - 35, MAPP_SDVIG_Y - 90 + smesh, 2400 // MAP_COEFF + 80, 2400 // MAP_COEFF + 50),
                         0)
        pygame.draw.rect(self.sc, (30, 30, 30),
                         (MAPP_SDVIG_X - 15, MAPP_SDVIG_Y - 20 + smesh, 2400 // MAP_COEFF + 45, 2400 // MAP_COEFF - 50),
                         0)
        pygame.draw.rect(self.sc, 'black',
                         (MAPP_SDVIG_X - 5, MAPP_SDVIG_Y - 10 + smesh, 2400 // MAP_COEFF + 27, 2400 // MAP_COEFF - 115),
                         0)
        render1 = pygame.font.SysFont('darkdeceptionregular', 40, bold=True).render(str(self.remaining_shards), 0, 'white')
        self.sc.blit(render1, ((MAPP_SDVIG_X + 190 + self.sdvig_teksta), (MAPP_SDVIG_Y - 70 + smesh)))
        if self.remaining_shards < 10:
            self.sdvig_teksta = 0
        render2 = pygame.font.SysFont('YandexSans', 40, bold=True).render(f'Собери все осколки', 0, 'white')
        self.sc.blit(render2, ((MAPP_SDVIG_X + 45), (MAPP_SDVIG_Y + 290 + smesh)))
