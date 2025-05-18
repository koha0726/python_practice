import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800,600))

while True:
    screen.fill(pg.Color("WHITE"))
    pg.draw.rect(screen,pg.Color("RED"),(100,100,100,150))
    pg.draw.line(screen,pg.Color("BLUE"),(250,100),(350,250),5)
    pg.draw.ellipse(screen,pg.Color("GREEN"),(400,100,150,150),5)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
