# Rhea Prahlad (rp8jd)

import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
count_tick = 0
counter = 0
character = gamebox.from_color(100, 500, "navy", 15, 40)
character.yspeed = 0
walls = [
    gamebox.from_color(150,400, "white", 200, 10),
    gamebox.from_color(400,250, "white", 200, 10),
    gamebox.from_color(650,100, "white", 200, 10),
    gamebox.from_color(650,400, "white", 200, 10),
    gamebox.from_color(150,100, "white", 200, 10)
]
coins = []
for i in range(50):
    coins.append(gamebox.from_color(random.randint(5, 795), random.randint(5, 500), "gold", 10, 10))

ground = gamebox.from_color(-100, 600, "black", 3000, 100)

def tick(keys):
    # get access to the counter
    global count_tick
    global counter
    if pygame.K_RIGHT in keys:
        character.x += 10
    if pygame.K_LEFT in keys:
        character.x -= 10
    character.yspeed += 1
    character.y = character.y + character.yspeed
    camera.clear("black")
    camera.draw(character)
    camera.draw(ground)
    if character.bottom_touches(ground):
        character.yspeed = 0
        if pygame.K_SPACE in keys:
                character.yspeed = -20
    if character.touches(ground):
        character.move_to_stop_overlapping(ground)
    camera.display()
    count_tick += 1

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -22
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)
    for coin in coins:
        if character.touches(coin):
            counter += 1
            coins.remove(coin)

        camera.draw(coin)
    camera.draw(gamebox.from_text(70,10, "Stars collected: " + str(counter),"Arial",20,"red",italic=True))
    ticks_per_second = 30
    seconds = int(count_tick / ticks_per_second)
    camera.draw(gamebox.from_text(700,10,str(seconds) + " out of 30 seconds spent","Arial",20,"red",italic=True))
    if seconds >= 30:
        gamebox.stop_loop()
        print("You found " + str(counter) + " stars.")

    camera.display()

ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)
