import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800,600))
img1 = pg.image.load("images/car.png")
img1 = pg.transform.scale(img1,(50,50))

while True:
    screen.fill(pg.Color("WHITE"))
    screen.blit(img1,(100,100))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
