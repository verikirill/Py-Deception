import math

f = open('settings.txt', 'r', encoding='utf-8')
f1 = f.readlines()

WIDTH = 1800
HEIGHT = 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
player_pos = (HALF_WIDTH - 2 * 100 + 150, HALF_HEIGHT + 280)
player_angle = 11
player_speed = 2
PENTA_HEIGHT = 5 * HEIGHT
DOUBLE_HEIGHT = 2 * HEIGHT
FPS = float(f1[4].split('"fps/частота смены кадров": ')[1][:-1])
WALL_SIZE = 100
FPS_POS = (WIDTH - 65, 5)
MAP_ENABLE = True
MAP_COEFF = 6
MAPP_SDVIG_Y = 500
MAPP_SDVIG_X = 1300
SENSIVITY = float(f1[0].split('"sensivity/чувствительность мыши": ')[1][:-1]) / 10000
IS_QUIT = 0

quality = f1[2].split('"quality/качество графики": ')[1][:-1]
NUM_RAYS = 600
if quality == 'CALCULATOR':
    NUM_RAYS = 100
    coef_of_coef = 8
elif quality == 'LOW':
    NUM_RAYS = 300
    coef_of_coef = 4
elif quality == 'MEDIUM':
    NUM_RAYS = 600
    coef_of_coef = 2
elif quality == 'HIGH':
    NUM_RAYS = 900
    coef_of_coef = 1
elif quality == 'ULTRA':
    NUM_RAYS = 1800
    coef_of_coef = 0.5
elif quality == 'POTATO':
    NUM_RAYS = 30
    coef_of_coef = 18

VOLUME = float(f1[1].split('"volume/громкость": ')[1][:-1]) / 10
RETRY = 0
HEARTS = 3
MONKEY_SPEED = 2
FOV = math.pi / 3
HALF_FOV = FOV / 2
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
COEF = coef_of_coef * DIST * WALL_SIZE
SCALE = WIDTH // NUM_RAYS

TEXTURE_WIDTH = 1800
TEXTURE_HEIGHT = 800
TEXTURE_SCALE = TEXTURE_WIDTH // WALL_SIZE

DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 + 1
