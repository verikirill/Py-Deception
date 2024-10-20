import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // WALL_SIZE) * WALL_SIZE, (b // WALL_SIZE) * WALL_SIZE


def ray_casting(player, texture):
    try:
        walls = []
        x0, y0 = player.pos
        xm, ym = mapping(x0, y0)
        cur_angle = player.angle - HALF_FOV
        for ray in range(NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)

            if cos_a >= 0:
                x = xm + WALL_SIZE
                dx = 1
            else:
                x = xm
                dx = -1
            for i in range(0, WIDTH, WALL_SIZE):
                depth_v = (x - x0) / cos_a
                yv = y0 + depth_v * sin_a
                tile_v = mapping(x + dx, yv)
                if tile_v in world_map:
                    texture_v = world_map[tile_v]
                    break
                x += dx * WALL_SIZE
            if sin_a >= 0:
                y = ym + WALL_SIZE
                dy = 1
            else:
                y = ym
                dy = -1
            for i in range(0, WIDTH, WALL_SIZE):
                depth_h = (y - y0) / sin_a
                xh = x0 + depth_h * cos_a
                tile_h = mapping(xh, y + dy)
                if tile_h in world_map:
                    texture_h = world_map[tile_h]
                    break
                y += dy * WALL_SIZE

            depth, offset, texture1 = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
            offset = int(offset) % WALL_SIZE
            depth *= math.cos(player.angle - cur_angle)
            depth = max(depth, 0.00001)
            proj_height = min(int(COEF / depth), 2 * HEIGHT)

            wall_column = texture[texture1].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
            wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
            wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)

            walls.append((depth, wall_column, wall_pos))
            cur_angle += DELTA_ANGLE
        return walls
    except:
        pass
