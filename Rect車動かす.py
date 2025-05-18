import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800,600))
img1 = pg.image.load("images/car.png")
img1 = pg.transform.scale(img1,(50,50))
myrect = pg.Rect(100,100,50,50)

while True:
    screen.fill(pg.Color("WHITE"))
    myrect.x = myrect.x + 1
    screen.blit(img1,myrect)
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
