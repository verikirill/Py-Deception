import random
import time

import settings
from settings import *
import pygame
import math
from map import collision_walls, collision_walls1, collision_walls2
import cv2


def load_image(name, colorkey=None):
    fullname = name
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


class Player:
    def __init__(self, level):
        if level != 2:
            self.x, self.y = player_pos
        else:
            self.x, self.y = (750, HEIGHT + 350)
        self.angle = player_angle
        self.hearts = HEARTS
        self.t = 0
        self.kart_smsh = 2
        self.shift = 0
        self.dop_prov = 0
        self.sensivity = SENSIVITY
        self.side = 30
        self.rect = pygame.Rect(*player_pos, self.side, self.side)
        self.level = level
        self.e = 0

    @property
    def pos(self):
        return (self.x, self.y)

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        if self.level == 0:
            hit_indexes = next_rect.collidelistall(collision_walls1)
        elif self.level == 1:
            hit_indexes = next_rect.collidelistall(collision_walls)
        elif self.level == 2:
            hit_indexes = next_rect.collidelistall(collision_walls2)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                if self.level == 0:
                    hit_rect = collision_walls1[hit_index]
                elif self.level == 1:
                    hit_rect = collision_walls[hit_index]
                elif self.level == 2:
                    hit_rect = collision_walls2[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - next_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if abs(delta_x - delta_y) < 25:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        self.keys_control()
        self.mouse_control()
        self.rect.center = self.x, self.y
        self.angle %= DOUBLE_PI

    def keys_control(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.t = 3
            self.shift = 1
            self.dop_prov += 1
            if self.dop_prov == 8:
                self.kart_smsh = self.kart_smsh * -1
                self.dop_prov = 0
        if keys[pygame.K_w]:
            dx = player_speed * cos_a + self.t * cos_a
            dy = player_speed * sin_a + self.t * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a
            dy = -player_speed * sin_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a
            dy = -player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a
            dy = player_speed * cos_a
            self.detect_collision(dx, dy)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
        pressed = pygame.mouse.get_pressed()
        if pressed[1] != 1:
            self.e = 0
        if pressed[1] and self.e == 0:
            self.angle += 3.1
            self.e = 1
        self.t = 0

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - HALF_WIDTH
            pygame.mouse.set_pos((HALF_WIDTH, HALF_HEIGHT))
            self.angle += difference * self.sensivity

    def death(self, sprites):
        try:
            i = random.randint(1, 3)
            cap = cv2.VideoCapture(f'videos/Death{i}.mp4')
            success, img = cap.read()
            shape = img.shape[1::-1]
            wn = pygame.display.set_mode((1800, 1000), pygame.NOFRAME)
            clock = pygame.time.Clock()
            pygame.mixer.music.stop()
            sound78 = pygame.mixer.Sound(f'videos/Death{i}.mp3')
            sound78.play()
            if i == 1:
                fps = 60
            else:
                fps = 35
            try:
                while success:
                    clock.tick(fps)
                    success, img = cap.read()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            success = False
                    wn.blit(pygame.image.frombuffer(img, shape, "BGR"), (300, 150))
                    pygame.display.update()
            except:
                pass
            pygame.display.flip()
            sound1 = pygame.mixer.Sound('sounds/SharedGameplay/Soul_Shard_Pickup_v2.ogg')
            sound_of_death = pygame.mixer.Sound('sounds/UI/Life_Lost.ogg')
            self.x, self.y = player_pos
            self.angle = player_angle
            sc_of_death = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
            pygame.display.update()
            all_sprites1 = pygame.sprite.Group()
            if self.hearts >= 2:
                render1 = pygame.font.SysFont('darkdeceptionregular', 120, bold=True).render(str('LIFES REMAINING:'), 0,
                                                                                   (220, 200, 200))
                sc_of_death.blit(render1, (350, 200))
            f = random.randint(1, 5)
            bierce_say_yo_about_death = pygame.mixer.Sound(f'sounds/Gameplay/1/Bierce_Hotel_Death_0{f}.ogg')
            bierce_say_yo_about_death.set_volume(VOLUME)
            if self.hearts == 3:
                # Skull 1
                bierce_say_yo_about_death.play()
                sprite11 = pygame.sprite.Sprite()
                sprite11.image = load_image("sprites/skulls/Skull.png", -1)
                sprite11.rect = sprite11.image.get_rect()
                all_sprites1.add(sprite11)
                sprite11.rect.x = 653
                sprite11.rect.y = 450
                # Skull 2
                sprite12 = pygame.sprite.Sprite()
                sprite12.image = load_image("sprites/skulls/Skull.png", -1)
                sprite12.rect = sprite12.image.get_rect()
                all_sprites1.add(sprite12)
                sprite12.rect.x = 853
                sprite12.rect.y = 450
                # Skull 3
                sprite13 = pygame.sprite.Sprite()
                sprite13.image = load_image("sprites/skulls/Skull.png", -1)
                sprite13.rect = sprite13.image.get_rect()
                all_sprites1.add(sprite13)
                sprite13.rect.x = 1053
                sprite13.rect.y = 450
                all_sprites1.draw(sc_of_death)
                while sprite11.rect.x <= WIDTH:
                    sprite13.rect.x += 10
                    sprite12.rect.x += 10
                    sprite11.rect.x += 10
                    all_sprites1.draw(sc_of_death)
                    pygame.display.update()
                    clock.tick(60)
                sound_of_death.play()
                all_sprites1.remove(sprite11)
                sprite11.kill()
                sprite12.rect.x = -53
                sprite13.rect.x = -203
                while sprite12.rect.x <= 853:
                    sprite12.rect.x += 10
                    sprite13.rect.x += 10
                    all_sprites1.draw(sc_of_death)
                    clock.tick(60)
                    pygame.display.update()
                count = 0
                while count != 150:
                    count += 1
                    clock.tick(60)
            elif self.hearts == 2:
                bierce_say_yo_about_death.play()
                # Skull 2
                sprite12 = pygame.sprite.Sprite()
                sprite12.image = load_image("sprites/skulls/Skull.png", -1)
                sprite12.rect = sprite12.image.get_rect()
                all_sprites1.add(sprite12)
                sprite12.rect.x = 853
                sprite12.rect.y = 450
                # Skull 3
                sprite13 = pygame.sprite.Sprite()
                sprite13.image = load_image("sprites/skulls/Skull.png", -1)
                sprite13.rect = sprite13.image.get_rect()
                all_sprites1.add(sprite13)
                sprite13.rect.x = 1053
                sprite13.rect.y = 450
                all_sprites1.draw(sc_of_death)
                while sprite13.rect.x <= WIDTH + 300:
                    sprite13.rect.x += 10
                    sprite12.rect.x += 10
                    all_sprites1.draw(sc_of_death)
                    pygame.display.update()
                    clock.tick(60)
                sound_of_death.play()
                sprite13.kill()
                all_sprites1.remove(sprite13)
                pygame.display.flip()
                sprite12.rect.x = -53
                sprite13.rect.x = 30000
                while sprite12.rect.x <= 853:
                    sprite12.rect.x += 10
                    all_sprites1.draw(sc_of_death)
                    clock.tick(60)
                    pygame.display.update()
                count = 0
                while count != 150:
                    count += 1
                    clock.tick(60)
            elif self.hearts <= 1:
                sprite12 = pygame.sprite.Sprite()
                sprite12.image = load_image("sprites/skulls/dead.jpg")
                sprite12.rect = sprite12.image.get_rect()
                all_sprites1.add(sprite12)
                sprite12.rect.x = 230
                sprite12.rect.y = 100
                pygame.mixer.music.unload()
                pygame.mixer.music.load('sounds/UI/Pause_Sound_v1.ogg')
                pygame.mixer.music.set_volume(VOLUME)
                pygame.mixer.music.play(-1)
                i = 255
                RETRY = 1
                while RETRY:
                    if i > -1:
                        i -= 1
                    surf = pygame.Surface((1800, 900))
                    surf.fill((0, 0, 0))
                    surf.set_alpha(i)
                    all_sprites1.draw(sc_of_death)
                    sc_of_death.blit(surf, (0, 0))
                    pygame.display.update()
                    for event in pygame.event.get():
                        keys = pygame.key.get_pressed()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            break
                        if keys[pygame.K_ESCAPE]:
                            pygame.quit()
                            break
                        if keys[pygame.K_RETURN]:
                            RETRY = 0
                            count = 0
                            while count <= 200:
                                count += 0.7
                                surf = pygame.Surface((1800, 900))
                                surf.fill((0, 0, 0))
                                surf.set_alpha(count)
                                sc_of_death.blit(surf, (0, 0))
                                clock.tick(FPS)
                                pygame.display.update()
                            break
                    clock.tick(FPS)
            pygame.display.update()
            self.hearts -= 1
            clock.tick(FPS)
            if self.level != 2:
                sprites.list_objects[-3].set_pos(1.5, 1.5)
                sprites.list_objects[-2].set_pos(4.5, 11.5)
                sprites.list_objects[-1].set_pos(23.5, 8.5)
            else:
                sprites.list_objects[-1].set_pos(8.5, 8.5)
            pygame.mixer.music.load('sounds/01_Hotel/Dark_Deception_Darkness_Orch_theme_r1_071518_LOOP.ogg')
            pygame.mixer.music.set_volume(VOLUME)
            pygame.mixer.music.play(-1)
        except:
            pass

    def player_pos(self):
        return self.x, self.y
