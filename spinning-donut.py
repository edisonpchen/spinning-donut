import pygame
import math

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

WIDTH = 1366
HEIGHT = 768

x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0  # rotation animation

theta_spacing = 10
phi_spacing = 1

chars = ".,-~:;=!*#$@"  # luminance indexing

screen = pygame.display.set_mode((WIDTH, HEIGHT))

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPINNING DONUT")
font = pygame.font.SysFont('Arial', 18, bold=True)


def text_display(letter, x_starting, y_starting):
    text = font.render(str(letter), True, white)
    display_surface.blit(text, (x_starting, y_starting))


run = True

while run:
    screen.fill(black)

    # rotation logic
    z = [0] * screen_size  # Fills Donut Space
    b = [' '] * screen_size  # Fills Emtpy Space

    for j in range(0, 628, theta_spacing):
        for i in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            L = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (L * h * m - t * n))  # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (L * h * n + t * m))  # 3D y coordinate after rotation
            o = int(x + columns * y)  # 3D z coordinate after rotation
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - L * d * n))  # luminance index
            if rows > y > 0 and 0 < x < columns and D > z[o]:
                z[o] = int(D)
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        A += 0.00003
        B += 0.000015
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator

    pygame.display.update()

    # end the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
