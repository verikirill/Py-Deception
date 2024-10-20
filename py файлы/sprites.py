import math

import pygame
from settings import *
from collections import deque


class Sprites:
    def __init__(self):
        self.sprite_parametrs = {
            'sprite_Crystal': {
                'sprite': pygame.image.load('sprites/crystal/Crystal1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 1.5,
                'scale': 0.2,
                'animation': deque(
                    [pygame.image.load(f'sprites/crystal/Crystal{i}.png').convert_alpha() for i in range(1, 9)]),
                'animation_dist': 300,
                'animation_speed': 5,
            },
            'sprite_Monkey': {
                'sprite': pygame.image.load('sprites/monkeys/monkey1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/monkeys/monkey{i}.png').convert_alpha() for i in range(1, 5)]),
                'animation_dist': 10000,
                'animation_speed': 10,
            },
        }

        self.crystal_size = 0.2
        self.crystal_height = 1.8
        self.list_objects = [
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (1.5, 1.5)),
            # 1
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (3.5, 1.5)),
            # 2
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (5.5, 1.5)),
            # 3
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (7.5, 1.5)),
            # 4
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (9.5, 1.5)),
            # 5
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (11.5, 1.5)),
            # 6
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (13.5, 1.5)),
            # 7
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (15.5, 1.5)),
            # 8
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (17.5, 1.5)),
            # 9
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (19.5, 1.5)),
            # 10
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (21.5, 1.5)),
            # 11
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (23.5, 1.5)),
            # 12
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (1.5, 3.5)),
            # 13
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (3.5, 3.5)),
            # 14
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (8.5, 3.5)),
            # 15
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (10.5, 3.5)),
            # 16
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (12.5, 3.5)),
            # 17
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (15.5, 3.5)),
            # 18
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (17.5, 3.5)),
            # 19
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (19.5, 3.5)),
            # 20
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (23.5, 3.5)),
            # 21
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (7.5, 4.5)),
            # 22
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (11.5, 4.5)),
            # 23
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (13.5, 4.5)),
            # 24
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (18.5, 4.5)),
            # 25
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (20.5, 4.5)),
            # 26
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (23.5, 5.5)),
            # 27
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (21.5, 5.5)),
            # 28
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (17.5, 5.5)),
            # 29
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (15.5, 5.5)),
            # 30
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (8.5, 5.5)),
            # 31
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (6.5, 5.5)),
            # 32
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (4.5, 5.5)),
            # 33
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (1.5, 5.5)),
            # 34
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (1.5, 7.5)),
            # 35
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (4.5, 7.5)),
            # 36
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (11.5, 7.5)),
            # 37
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (13.5, 7.5)),
            # 38
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (15.5, 7.5)),
            # 39
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (17.5, 7.5)),
            # 40
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (19.5, 7.5)),
            # 41
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (21.5, 7.5)),
            # 42
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (23.5, 7.5)),
            # 43
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (2.5, 8.5)),
            # 44
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (12.5, 8.5)),
            # 45
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (10.5, 8.5)),
            # 46
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (3.5, 9.5)),
            # 47
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (6.5, 9.5)),
            # 48
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (9.5, 9.5)),
            # 49
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (13.5, 9.5)),
            # 50
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (15.5, 9.5)),
            # 51
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (19.5, 9.5)),
            # 52
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (21.5, 9.5)),
            # 53
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (23.5, 9.5)),
            # 54
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (2.5, 10.5)),
            # 55
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (16.5, 10.5)),
            # 56
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (18.5, 10.5)),
            # 57
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (3.5, 11.5)),
            # 58
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (5.5, 11.5), ),
            # 59
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (9.5, 11.5)),
            # 60
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (11.5, 11.5)),
            # 61
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (13.5, 11.5)),
            # 62
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (15.5, 11.5)),
            # 63
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (19.5, 11.5)),
            # 64
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (21.5, 11.5)),
            # 65
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (23.5, 11.5)),
            # 66
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (16.5, 12.5)),
            # 67
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (2.5, 12.5)),
            # 68
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (1.5, 13.5)),
            # 69
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (4.5, 13.5)),
            # 70
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (6.5, 13.5)),
            # 71
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (8.5, 13.5)),
            # 72
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (12.5, 13.5)),
            # 73
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (14.5, 13.5)),
            # 74
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (17.5, 13.5), ),
            # 75
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (19.5, 13.5), ),
            # 76
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (21.5, 13.5), ),
            # 77
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (3.5, 14.5)),
            # 78
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (10.5, 14.5)),
            # 79
            SpriteObject(self.sprite_parametrs['sprite_Crystal'], (18.5, 14.5)),
            # 80
        ]
        self.list_objects.append(SpriteObject(self.sprite_parametrs['sprite_Monkey'], (1.5, 1.5)), )
        self.list_objects.append(SpriteObject(self.sprite_parametrs['sprite_Monkey'], (4.5, 14.5)), )
        self.list_objects.append(SpriteObject(self.sprite_parametrs['sprite_Monkey'], (23.5, 8.5)), )
        self.coords_of_objects = [
            (1.5, 1.5), (3.5, 1.5), (5.5, 1.5), (7.5, 1.5), (9.5, 1.5), (11.5, 1.5), (13.5, 1.5), (15.5, 1.5),
            (17.5, 1.5), (19.5, 1.5), (21.5, 1.5), (23.5, 1.5), (1.5, 3.5), (3.5, 3.5), (8.5, 3.5), (10.5, 3.5),
            (12.5, 3.5), (15.5, 3.5), (17.5, 3.5), (19.5, 3.5), (23.5, 3.5), (7.5, 4.5), (11.5, 4.5), (13.5, 4.5),
            (18.5, 4.5), (20.5, 4.5), (23.5, 5.5), (21.5, 5.5), (17.5, 5.5), (15.5, 5.5), (8.5, 5.5),
            (6.5, 5.5), (4.5, 5.5), (1.5, 5.5), (1.5, 7.5), (4.5, 7.5), (11.5, 7.5), (13.5, 7.5), (15.5, 7.5),
            (17.5, 7.5), (19.5, 7.5), (21.5, 7.5), (23.5, 7.5), (2.5, 8.5), (12.5, 8.5), (10.5, 8.5), (3.5, 9.5),
            (6.5, 9.5), (9.5, 9.5), (13.5, 9.5), (15.5, 9.5), (19.5, 9.5), (21.5, 9.5), (23.5, 9.5), (2.5, 10.5),
            (16.5, 10.5), (18.5, 10.5), (3.5, 11.5), (5.5, 11.5), (9.5, 11.5), (11.5, 11.5), (13.5, 11.5), (15.5, 11.5),
            (19.5, 11.5), (21.5, 11.5), (23.5, 11.5), (16.5, 12.5), (2.5, 12.5), (1.5, 13.5), (4.5, 13.5), (6.5, 13.5),
            (8.5, 13.5), (12.5, 13.5), (14.5, 13.5), (17.5, 13.5), (19.5, 13.5), (21.5, 13.5), (3.5, 14.5),
            (10.5, 14.5), (18.5, 14.5),
        ]


class Sprites_start:
    def __init__(self):
        self.sprite_parametrs = {
            'sprite_Tutorial1': {
                'sprite': pygame.image.load(f'textures/ControlTutorialTexture.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'textures/ControlTutorialTexture.png').convert_alpha() for i in range(1, 1)]),
                'animation_dist': 10000,
                'animation_speed': 10,
            },
            'sprite_Tutorial2': {
                'sprite': pygame.image.load(f'textures/ControlTutorialTexture1.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'textures/ControlTutorialTexture1.png').convert_alpha() for i in range(1, 1)]),
                'animation_dist': 10000,
                'animation_speed': 10,
            },
            'sprite_Tutorial3': {
                'sprite': pygame.image.load(f'textures/ControlTutorialTexture2.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'textures/ControlTutorialTexture2.png').convert_alpha() for i in range(1, 1)]),
                'animation_dist': 10000,
                'animation_speed': 10,
            },
            'sprite_Tutorial4': {
                'sprite': pygame.image.load(f'textures/ControlTutorialTexture3.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'textures/ControlTutorialTexture3.png').convert_alpha() for i in range(1, 1)]),
                'animation_dist': 10000,
                'animation_speed': 10,
            },
            'sprite_Tutorial5': {
                'sprite': pygame.image.load(f'textures/ControlTutorialTexture4.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'textures/ControlTutorialTexture4.png').convert_alpha() for i in range(1, 1)]),
                'animation_dist': 10000,
                'animation_speed': 10,
            },
            'sprite_Tutorial6': {
                'sprite': pygame.image.load(f'textures/ControlTutorialTexture5.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'textures/ControlTutorialTexture5.png').convert_alpha() for i in range(1, 1)]),
                'animation_dist': 10000,
                'animation_speed': 10,
            },
        }

        self.crystal_size = 0.2
        self.crystal_height = 1.8
        self.list_objects = [
            SpriteObject(self.sprite_parametrs['sprite_Tutorial1'], (7.5, 5.5)),
            SpriteObject(self.sprite_parametrs['sprite_Tutorial2'], (7.5, 4.5)),
            SpriteObject(self.sprite_parametrs['sprite_Tutorial3'], (7.5, 3.5)),
            SpriteObject(self.sprite_parametrs['sprite_Tutorial4'], (9.5, 5.5)),
            SpriteObject(self.sprite_parametrs['sprite_Tutorial5'], (9.5, 4.5)),
            SpriteObject(self.sprite_parametrs['sprite_Tutorial6'], (9.5, 3.5)),
        ]


class Sprites_end:
    def __init__(self):
        self.sprite_parametrs = {
            'sprite_Monkeyevil': {
                'sprite': pygame.image.load('sprites/monkeys/monkey21.png').convert_alpha(),
                'viewing_angles': None,
                'shift': 0.1,
                'scale': 1,
                'animation': deque(
                    [pygame.image.load(f'sprites/monkeys/monkey{i}.png').convert_alpha() for i in range(21, 25)]),
                'animation_dist': 1500,
                'animation_speed': 10,
            },
        }

        self.crystal_size = 0.2
        self.crystal_height = 1.8
        self.list_objects = [
            SpriteObject(self.sprite_parametrs['sprite_Monkeyevil'], (8.5, 8.5)),
        ]


class SpriteObject:
    def __init__(self, parametrs, pos):
        self.object = parametrs['sprite']
        self.viewing_angles = parametrs['viewing_angles']
        self.shift = parametrs['shift']
        self.scale = parametrs['scale']
        self.animation = parametrs['animation']
        self.animation_dist = parametrs['animation_dist']
        self.animation_speed = parametrs['animation_speed']
        self.animation_count = 0
        self.pos = self.x, self.y = pos[0] * WALL_SIZE, pos[1] * WALL_SIZE

        if self.viewing_angles:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_position = {angle: pos for angle, pos in zip(self.sprite_angles, self.object)}

    def object_locate(self, player):
        try:
            dx, dy = self.x - player.x, self.y - player.y
            distance_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

            theta = math.atan2(dy, dx)
            gamma = theta - player.angle
            if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
                gamma += DOUBLE_PI

            delta_rays = int(gamma / DELTA_ANGLE)
            current_ray = CENTER_RAY + delta_rays
            distance_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)
            fake_ray = current_ray + FAKE_RAYS
            if 0 <= fake_ray <= FAKE_RAYS_RANGE and distance_to_sprite > 30:
                proj_height = min(int(COEF / distance_to_sprite * self.scale), DOUBLE_HEIGHT)
                half_proj_height = proj_height // 2
                shift = half_proj_height * self.shift

                if self.viewing_angles:
                    if theta < 0:
                        theta += DOUBLE_PI
                    theta = 360 - int(math.degrees(theta))

                    for angles in self.sprite_angles:
                        if theta in angles:
                            self.object = self.sprite_position[angles]
                            break

                sprite_object = self.object
                if self.animation and distance_to_sprite < self.animation_dist:
                    sprite_object = self.animation[0]
                    if self.animation_count < self.animation_speed:
                        self.animation_count += 1
                    else:
                        self.animation.rotate()
                        self.animation_count = 0

                sprite_pos = (current_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
                sprite = pygame.transform.scale(sprite_object, (proj_height, proj_height))
                return (distance_to_sprite, sprite, sprite_pos)
            else:
                return (False,)
        except:
            pass

    def set_pos(self, x, y):
        self.x = x * WALL_SIZE
        self.y = y * WALL_SIZE
        self.pos = self.x, self.y
