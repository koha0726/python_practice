import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800,600))
imageR = pg.image.load("images/playerR.png")
imageL = pg.transform.flip(imageR,True,False)
myrect = pg.Rect(300,200,80,100)
rightFlag = True

while True:
    screen.fill(pg.Color("WHITE"))
    vx = 0
    
    key = pg.key.get_pressed()
    
    if(key[pg.K_RIGHT]):
        vx = 5
        rightFlag = True
    
    if(key[pg.K_LEFT]):
        vx = -5
        rightFlag = False
    
    myrect.x = myrect.x + vx
    if rightFlag:
        screen.blit(imageR,myrect)
    else:
        screen.blit(imageL,myrect)
    
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
