import time

import pygame
from settings import *
from player_control import Player
import math
from map import world_map, start1_map, FINISH_map
from drawing import *
from ray_cast import ray_casting, ray_casting1, ray_casting2
from sprites import *
from navigator import *
from datetime import datetime

pygame.display.set_icon(pygame.image.load("obama.ico"))


def load_image(name, colorkey=None):
    fullname = name
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


hearts1 = 0
start_time = 0


def start_of_game(RETRY, IS_QUIT):
    try:
        pygame.init()
        sc_start = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
        pygame.mouse.set_visible(False)
        sprites_start = Sprites_start()
        clock1 = pygame.time.Clock()
        player1 = Player(0)
        drawing1 = Drawing(sc_start)
        pygame.mixer.music.load('sounds/01_Hotel/61-_Hotel_Lobby_Music_Loop_0704.ogg')
        pygame.mixer.music.set_volume(VOLUME)
        pygame.mixer.music.play(-1)
        next_level = 1
        all_sprites1 = pygame.sprite.Group()
        sprite11 = pygame.sprite.Sprite()
        image = load_image("sprites/skulls/MonkeyPortal2.png", -1)
        sprite11.image = image
        sprite11.rect = sprite11.image.get_rect()
        all_sprites1.add(sprite11)
        sprite11.rect.x = 0
        sprite11.rect.y = 150
        count1 = 255
        surf1 = pygame.Surface((1800, 900))
        surf1.fill((0, 0, 0))
        sound2 = pygame.mixer.Sound('sounds/00_Ballroom/21-Ballroom_portal_V4.ogg')
        sound2.set_volume(VOLUME)
        sound2.play()
        while next_level:
            sc_start = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if keys[pygame.K_4]:
                    next_level = 0
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
            player1.shift = 0
            player1.movement()
            sc_start.fill('white')
            try:
                drawing1.background(player1.angle)
            except:
                pass
            walls1 = ray_casting1(player1, drawing1.texture)
            try:
                drawing1.world(walls1 + [obj.object_locate(player1) for obj in sprites_start.list_objects])
            except:
                pass
            if count1 >= 0:
                sc_start.blit(surf1, (0, 0))
                surf1.set_alpha(count1)
                count1 -= 1.5
                all_sprites1.draw(sc_start)
            pygame.display.update()
            clock1.tick(FPS)
            if player1.x // WALL_SIZE == 8 and player1.y // WALL_SIZE == 9:
                pygame.quit()
                IS_QUIT = 1
                break
            if player1.x // WALL_SIZE == 8 and player1.y // WALL_SIZE == 1:
                count = 0
                sound_of_doors = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorDoorSliding.ogg')
                sound_of_doors.set_volume(VOLUME)
                sound_of_doors.play()
                pygame.mixer.music.unload()
                sound_of_doors1 = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorMovingLoop.ogg')
                sound_of_doors1.set_volume(VOLUME)
                sound_of_doors1.play()
                while count <= 80:
                    count += 0.7
                    surf = pygame.Surface((1800, 900))
                    surf.fill((0, 0, 0))
                    surf.set_alpha(count)
                    sc_start.blit(surf, (0, 0))
                    clock1.tick(FPS)
                    pygame.display.update()
                count = 0
                while count <= 300:
                    count += 1
                    pygame.display.update()
                    clock1.tick(FPS)
                count1 = 100
                sound_of_doors2 = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorDing.ogg')
                sound_of_doors2.set_volume(VOLUME)
                sound_of_doors2.play()
                while count1 >= 0:
                    count1 -= 1
                    clock1.tick(FPS)
                    pygame.display.update()
                sound_of_doors3 = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorStopping.ogg')
                sound_of_doors3.set_volume(VOLUME)
                sound_of_doors3.play()
                count1 = 100
                while count1 >= 0:
                    count1 -= 1
                    clock1.tick(FPS)
                sound_of_doors = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorDoorSliding.ogg')
                sound_of_doors.set_volume(VOLUME)
                sound_of_doors.play()
                break
        if IS_QUIT:
            pass
        else:
            main(RETRY)
    except:
        pass


def main(RETRY):
    global hearts1
    global start_time
    start_time = datetime.now()
    try:
        def navigator_for_monkeys(monkey_poses):
            try:
                pos_player1 = (int(player.pos[0] // WALL_SIZE), int(player.pos[1] // WALL_SIZE))
                # ////////////
                # FIRST MONKEY
                # ///////////
                pos_monkey1 = monkey_poses[0]
                pos_monkey1 = (int(pos_monkey1[0] // WALL_SIZE), int(pos_monkey1[1] // WALL_SIZE))
                cur_node1 = pos_monkey1
                monkey1_next_pos = bfs(pos_player1, pos_monkey1, graph)
                monkey1_next_pos = monkey1_next_pos[cur_node1]
                pos_monkey1 = monkey_poses[0]
                if (monkey1_next_pos[0] + 0.5) * WALL_SIZE - pos_monkey1[0] > 0:
                    x1 = MONKEY_SPEED
                elif (monkey1_next_pos[0] + 0.4) * WALL_SIZE - pos_monkey1[0] < 0:
                    x1 = -MONKEY_SPEED
                else:
                    x1 = 0
                if (monkey1_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey1[1] > 0:
                    y1 = + MONKEY_SPEED
                elif (monkey1_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey1[1] < 0:
                    y1 = - MONKEY_SPEED
                else:
                    y1 = 0
                x1 = (monkey_poses[0][0] + x1) / WALL_SIZE
                y1 = (monkey_poses[0][1] + y1) / WALL_SIZE
                sprites.list_objects[-3].set_pos(x1, y1)
                # /////////////
                # SECOND MONKEY
                # /////////////
                pos_monkey2 = monkey_poses[1]
                pos_monkey2 = (int(pos_monkey2[0] // WALL_SIZE), int(pos_monkey2[1] // WALL_SIZE))
                cur_node2 = pos_monkey2
                monkey2_next_pos = bfs(pos_player1, pos_monkey2, graph)
                monkey2_next_pos = monkey2_next_pos[cur_node2]
                pos_monkey2 = monkey_poses[1]
                if (monkey2_next_pos[0] + 0.5) * WALL_SIZE - pos_monkey2[0] > 0:
                    x2 = MONKEY_SPEED + 0.5
                elif (monkey2_next_pos[0] + 0.4) * WALL_SIZE - pos_monkey2[0] < 0:
                    x2 = -MONKEY_SPEED - 0.5
                else:
                    x2 = 0
                if (monkey2_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey2[1] > 0:
                    y2 = + MONKEY_SPEED + 0.5
                elif (monkey2_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey2[1] < 0:
                    y2 = - MONKEY_SPEED - 0.5
                else:
                    y2 = 0
                x2 = (monkey_poses[1][0] + x2) / WALL_SIZE
                y2 = (monkey_poses[1][1] + y2) / WALL_SIZE
                sprites.list_objects[-2].set_pos(x2, y2)
                # ////////////
                # THIRD MONKEY
                # ////////////
                pos_monkey3 = monkey_poses[2]
                pos_monkey3 = (int(pos_monkey3[0] // WALL_SIZE), int(pos_monkey3[1] // WALL_SIZE))
                cur_node3 = pos_monkey3
                monkey3_next_pos = bfs(pos_player1, pos_monkey3, graph)
                monkey3_next_pos = monkey3_next_pos[cur_node3]
                pos_monkey3 = monkey_poses[2]
                if (monkey3_next_pos[0] + 0.5) * WALL_SIZE - pos_monkey3[0] > 0:
                    x3 = MONKEY_SPEED - 0.5
                elif (monkey3_next_pos[0] + 0.4) * WALL_SIZE - pos_monkey3[0] < 0:
                    x3 = -MONKEY_SPEED + 0.5
                else:
                    x3 = 0
                if (monkey3_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey3[1] > 0:
                    y3 = + MONKEY_SPEED - 0.5
                elif (monkey3_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey3[1] < 0:
                    y3 = - MONKEY_SPEED + 0.5
                else:
                    y3 = 0
                x3 = (monkey_poses[2][0] + x3) / WALL_SIZE
                y3 = (monkey_poses[2][1] + y3) / WALL_SIZE
                sprites.list_objects[-1].set_pos(x3, y3)
            except:
                player.death(sprites)

        pygame.init()
        sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
        pygame.mouse.set_visible(False)
        sprites = Sprites()
        clock = pygame.time.Clock()
        player = Player(1)
        drawing = Drawing(sc)
        pygame.mixer.music.load('sounds/01_Hotel/Dark_Deception_Darkness_Orch_theme_r1_071518_LOOP.ogg')
        pygame.mixer.music.set_volume(VOLUME)
        pygame.mixer.music.play(-1)
        sound1 = pygame.mixer.Sound('sounds/SharedGameplay/Soul_Shard_Pickup_v2.ogg')
        is_death = 0
        panic = 1
        loud_of_sound = 0.0001
        sprites.list_objects[-3].set_pos(1.5, 1.5)
        sprites.list_objects[-2].set_pos(4.5, 11.5)
        sprites.list_objects[-1].set_pos(23.5, 8.5)
        while True:
            hearts1 = player.hearts
            monkey_near = 0
            sound1 = pygame.mixer.Sound('sounds/SharedGameplay/Soul_Shard_Pickup_v2.ogg')
            sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                if keys[pygame.K_3]:
                    player.death(sprites)
                if keys[pygame.K_7]:
                    end_of_game()
                if keys[pygame.K_6]:
                    drawing.remaining_shards = 0
                if keys[pygame.K_ESCAPE]:
                    pygame.quit()
            player.shift = 0
            player.movement()
            sc.fill('black')
            drawing.background(player.angle)
            walls = ray_casting(player, drawing.texture)
            try:
                drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_objects])
            except:
                pass
            drawing.fps(clock)
            if MAP_ENABLE:
                drawing.draw_okantovka(player.shift, player.kart_smsh)
                pygame.draw.circle(sc, 'red',
                                   (int(player.x) // MAP_COEFF + MAPP_SDVIG_X,
                                    int(player.y) // MAP_COEFF + MAPP_SDVIG_Y + player.kart_smsh),
                                   12 - MAP_COEFF)
                for x, y in world_map:
                    pygame.draw.rect(sc, 'gray',
                                     (x // MAP_COEFF + MAPP_SDVIG_X, y // MAP_COEFF + MAPP_SDVIG_Y + player.kart_smsh,
                                      WALL_SIZE // MAP_COEFF,
                                      WALL_SIZE // MAP_COEFF), 1)
                for x1, y1 in sprites.coords_of_objects:
                    if (player.x / WALL_SIZE >= x1 - 0.2 and player.x / WALL_SIZE <= x1 + 0.2) and (
                            player.y / WALL_SIZE >= y1 - 0.2 and player.y / WALL_SIZE <= y1 + 0.2):
                        sound1.play()
                        sprites.coords_of_objects.remove((x1, y1))
                        for i in sprites.list_objects:
                            if i.x / WALL_SIZE == x1 and i.y / WALL_SIZE == y1:
                                sprites.list_objects.remove(i)
                        drawing.remaining_shards -= 1
                    pygame.draw.circle(sc, (150, 0, 255),
                                       (x1 * WALL_SIZE // MAP_COEFF + MAPP_SDVIG_X,
                                        y1 * WALL_SIZE // MAP_COEFF + MAPP_SDVIG_Y + player.kart_smsh),
                                       WALL_SIZE // MAP_COEFF // 3, 0)

            monkey_posses = []
            monkey_posses.append(sprites.list_objects[-3].pos)
            monkey_posses.append(sprites.list_objects[-2].pos)
            monkey_posses.append(sprites.list_objects[-1].pos)
            navigator_for_monkeys(monkey_posses)
            if player.x // WALL_SIZE == 8 and player.y // WALL_SIZE == 7 and drawing.remaining_shards == 0:
                count = 0
                sound_of_doors = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorDoorSliding.ogg')
                sound_of_doors.set_volume(VOLUME)
                sound_of_doors.play()
                sound_of_scream = pygame.mixer.Sound('sounds/SharedGameplay/23-Frenzy_Monkeys_Ambient_LOOP.ogg')
                sound_of_scream.set_volume(VOLUME)
                sound_of_scream.play()
                pygame.mixer.music.unload()
                sound_of_doors1 = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorMovingLoop.ogg')
                sound_of_doors1.set_volume(VOLUME)
                sound_of_doors1.play()
                while count <= 80:
                    count += 0.7
                    surf = pygame.Surface((1800, 900))
                    surf.fill((0, 0, 0))
                    surf.set_alpha(count)
                    sc.blit(surf, (0, 0))
                    clock.tick(FPS)
                    pygame.display.update()
                count = 0
                while count <= 300:
                    count += 1
                    pygame.display.update()
                    clock.tick(FPS)
                end_of_game()
            for f in monkey_posses:
                if player.x - 60 <= f[0] <= player.x + 60 and player.y - 60 <= f[1] <= player.y + 60:
                    player.death(sprites)
                    is_death = 1
            count_of_monkey = 0
            for f in monkey_posses:
                if player.x - 300 <= f[0] <= player.x + 300 and player.y - 300 <= f[1] <= player.y + 300:
                    count_of_monkey += 1
                    monkey_near = 1
            if panic and count_of_monkey == 1:
                loud_of_sound = 0.0001
                pygame.mixer.music.unload()
                pygame.mixer.music.load('sounds/01_Hotel/Dark_Deception_Darkness_theme_Panic_Mode_071518_LOOP.ogg')
                pygame.mixer.music.play(-1)
                panic = 0
            elif not monkey_near and panic == 0:
                panic = 1
                loud_of_sound = 0.0001
                pygame.mixer.music.unload()
                pygame.mixer.music.load('sounds/01_Hotel/Dark_Deception_Darkness_Orch_theme_r1_071518_LOOP.ogg')
                pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(loud_of_sound)
            if loud_of_sound <= 0.1:
                loud_of_sound += 0.001
            else:
                loud_of_sound = 0.1
            if is_death:
                time.sleep(1)
                sprites.list_objects[-3].set_pos(1.5, 1.5)
                sprites.list_objects[-2].set_pos(4.5, 11.5)
                sprites.list_objects[-1].set_pos(23.5, 8.5)
                is_death = 0
            if RETRY:
                RETRY = 0
                main()
            pygame.display.flip()
            pygame.display.flip()
            clock.tick(FPS)
    except:
        pass


def end_of_game():
    global start_time
    global hearts1

    def navigator_for_monkeys2(monkey_poses):
        try:
            pos_player1 = (int(player2.pos[0] // WALL_SIZE), int(player2.pos[1] // WALL_SIZE))
            pos_monkey1 = monkey_poses[0]
            pos_monkey1 = (int(pos_monkey1[0] // WALL_SIZE), int(pos_monkey1[1] // WALL_SIZE))
            cur_node1 = pos_monkey1
            monkey1_next_pos = bfs2(pos_player1, pos_monkey1, graph2)
            monkey1_next_pos = monkey1_next_pos[cur_node1]
            pos_monkey1 = monkey_poses[0]
            abc = 1.5
            if (monkey1_next_pos[0] + 0.5) * WALL_SIZE - pos_monkey1[0] > 0:
                x1 = MONKEY_SPEED + abc
            elif (monkey1_next_pos[0] + 0.4) * WALL_SIZE - pos_monkey1[0] < 0:
                x1 = -MONKEY_SPEED - abc
            else:
                x1 = 0
            if (monkey1_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey1[1] > 0:
                y1 = + MONKEY_SPEED + abc
            elif (monkey1_next_pos[1] + 0.5) * WALL_SIZE - pos_monkey1[1] < 0:
                y1 = - MONKEY_SPEED - abc
            else:
                y1 = 0
            x1 = (monkey_poses[0][0] + x1) / WALL_SIZE
            y1 = (monkey_poses[0][1] + y1) / WALL_SIZE
            sprites_end.list_objects[-1].set_pos(x1, y1)
        except:
            player2.death(sc_end)
            player2.x, player2.y = (750, HEIGHT + 350)
            end_of_game()

    pygame.init()
    sc_end = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
    pygame.mouse.set_visible(False)
    sprites_end = Sprites_end()
    clock2 = pygame.time.Clock()
    player2 = Player(2)
    player2.hearts = hearts1
    drawing2 = Drawing(sc_end)
    pygame.mixer.music.load('sounds/01_Hotel/Dark_Deception_Darkness_theme_Panic_Mode_071518_LOOP.ogg')
    pygame.mixer.music.set_volume(VOLUME)
    pygame.mixer.music.play(-1)
    next_level = 1
    sound2 = pygame.mixer.Sound('sounds/00_Ballroom/21-Ballroom_portal_V4.ogg')
    sound2.set_volume(VOLUME)
    sound2.play()
    is_death = 0
    sprites_end.list_objects[-1].set_pos(8.5, 8.5)
    player2.x, player2.y = (750, HEIGHT + 350)
    sound3 = pygame.mixer.Sound('sounds/Bierce_Bark_04.ogg')
    sound3.set_volume(VOLUME)
    sound3.play()
    while next_level:
        if is_death == 1:
            sprites_end.list_objects[-1].set_pos(8.5, 8.5)
            player2.x, player2.y = (750, HEIGHT + 350)
            is_death = 0
            end_of_game()
        sc_end = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
            if keys[pygame.K_4]:
                next_level = 0
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
        player2.shift = 0
        player2.movement()
        sc_end.fill('white')
        try:
            drawing2.background(player2.angle)
        except:
            pass
        walls2 = ray_casting2(player2, drawing2.texture)
        try:
            drawing2.world(walls2 + [obj.object_locate(player2) for obj in sprites_end.list_objects])
        except:
            pass
        monkey_posses = []
        monkey_posses.append(sprites_end.list_objects[-1].pos)
        navigator_for_monkeys2(monkey_posses)
        hearts1 = player2.hearts
        for f in monkey_posses:
            if player2.x - 60 <= f[0] <= player2.x + 60 and player2.y - 60 <= f[1] <= player2.y + 60:
                player2.death(sprites_end)
                player2.x, player2.y = (750, HEIGHT + 350)
                is_death = 1
        if player2.x // WALL_SIZE == 13 and player2.y // WALL_SIZE == 11:
            count = 0
            sound_of_doors = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorDoorSliding.ogg')
            sound_of_doors.set_volume(VOLUME)
            sound_of_doors.play()
            pygame.mixer.music.unload()
            sound_of_doors1 = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorMovingLoop.ogg')
            sound_of_doors1.set_volume(VOLUME)
            sound_of_doors1.play()
            while count <= 80:
                count += 0.7
                surf = pygame.Surface((1800, 900))
                surf.fill((0, 0, 0))
                surf.set_alpha(count)
                sc_end.blit(surf, (0, 0))
                clock2.tick(FPS)
                pygame.display.update()
            count = 0
            while count <= 300:
                count += 1
                pygame.display.update()
                clock2.tick(FPS)
            count1 = 100
            sound_of_doors2 = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorDing.ogg')
            sound_of_doors2.set_volume(VOLUME)
            sound_of_doors2.play()
            while count1 >= 0:
                count1 -= 1
                clock2.tick(FPS)
                pygame.display.update()
            sound_of_doors3 = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorStopping.ogg')
            sound_of_doors3.set_volume(VOLUME)
            sound_of_doors3.play()
            count1 = 100
            while count1 >= 0:
                count1 -= 1
                clock2.tick(FPS)
            sound_of_doors = pygame.mixer.Sound('sounds/01_Hotel/DD_ElevatorDoorSliding.ogg')
            sound_of_doors.set_volume(VOLUME)
            sound_of_doors.play()
            all_sprites2 = pygame.sprite.Group()
            sprite12 = pygame.sprite.Sprite()
            sprite12.image = load_image("sprites/skulls/youescaped1.png")
            sprite12.rect = sprite12.image.get_rect()
            all_sprites2.add(sprite12)
            sprite12.rect.x = 0
            sprite12.rect.y = 0
            sound_of_escape = pygame.mixer.Sound('sounds/UI/UI_YouEscaped.ogg')
            sound_of_escape.set_volume(VOLUME + 0.1)
            sound_of_escape.play()
            pygame.mixer.music.unload()
            pygame.mixer.music.load('sounds/00_Ballroom/Dark_Deception_Ballroom_Theme_Ambient_New_091718_LOOP.ogg')
            pygame.mixer.music.set_volume(VOLUME)
            pygame.mixer.music.play(-1)
            i = 255
            RETRY = 1
            end_time = datetime.now()
            while RETRY:
                if i > -1:
                    i -= 1
                all_sprites2.draw(sc_end)
                render1 = pygame.font.SysFont('darkdeceptionregular', 45, bold=True).render(str(3 - hearts1), 0,
                                                                                            'white')
                sc_end.blit(render1, (750, 420))
                render2 = pygame.font.SysFont('darkdeceptionregular', 45, bold=True).render(
                    str(end_time - start_time)[:-7], 0, 'white')
                sc_end.blit(render2, (750, 590))
                surf = pygame.Surface((1800, 900))
                surf.fill((0, 0, 0))
                surf.set_alpha(i)
                sc_end.blit(surf, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    keys = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        break
                    if keys[pygame.K_ESCAPE]:
                        pygame.quit()
                        break
                pygame.display.update()
            break
        if is_death == 1:
            sprites_end.list_objects[-1].set_pos(8.5, 8.5)
            player2.x, player2.y = (750, HEIGHT + 350)
            is_death = 0
        clock2.tick(FPS)
        pygame.display.update()


start_of_game(RETRY, IS_QUIT)

# pyinstaller --onefile --noconsole --icon=obama.ico main.py
