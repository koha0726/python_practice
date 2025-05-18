import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800,600))

while True:
    screen.fill(pg.Color("WHITE"))

    mdown = pg.mouse.get_pressed()
    (mx,my) = pg.mouse.get_pos()

    if mdown[0]:
        pg.draw.rect(screen,pg.Color("RED"),(mx-50,my-50,100,100)) 

    pg.display.update()
    pg.time.Clock().tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
