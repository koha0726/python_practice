import pygame as pg, sys
pg.init()
screen = pg.display.set_mode((800,600))
##紙芝居
img1 = pg.image.load("images/root1.png")
img2 = pg.image.load("images/root2.png")
img3 = pg.image.load("images/root3.png")
img4 = pg.image.load("images/root4.png")
img5 = pg.image.load("images/root5.png")
##ボタン
next_img = pg.image.load("images/nextbtn.png")
replay_img = pg.image.load("images/replaybtn.png")

pushFlag = False
##btnを押したらnewpageにジャンプする
def button_to_jump(btn, newpage):
    #global page, pushFlag
    # ユーザーからの入力を調べる
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint(mx, my) and pushFlag == False:
            page = newpage
            pushFlag = True
        else:
            pushFlag = False

def page1():
    # 画面の初期化
    screen.blit(img1, (0,0))
    btn1 = screen.blit(next_img,( 90, 220))
    btn2 = screen.blit(next_img,(590, 220))
    # 絵を描いたり、判定したりする
    button_to_jump(btn1, 2)
    button_to_jump(btn2, 3)

def page2():
    # 画面の初期化
    screen.blit(img2, (0,0))
    btn1 = screen.blit(replay_img,(600, 520))
    # 絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

def page3():
    # 画面の初期化
    screen.blit(img3, (0,0))
    btn1 = screen.blit(next_img,(190, 320))
    btn2 = screen.blit(next_img,(490, 320))
    # 絵を描いたり、判定したりする
    button_to_jump(btn1, 4)
    button_to_jump(btn2, 5)

def page4():
    # 画面の初期化
    screen.blit(img4, (0,0))
    btn1 = screen.blit(replay_img,(600, 520))
    # 絵を描いたり、判定したりする
    button_to_jump(btn1, 1)

def page5():
    # 画面の初期化
    screen.blit(img5, (0,0))
    btn1 = screen.blit(replay_img,(600, 520))
    # 絵を描いたり、判定したりする
    button_to_jump(btn1, 1)
    

page = 1
# この下をずっとループする
while True:
    if page == 1:
        page1()
    elif page == 2:
        page2()
    elif page == 3:
        page3()
    elif page == 4:
        page4()
    elif page == 5:
        page5()
    # 画面を表示する
    pg.display.update()
    pg.time.Clock().tick(60)
    # 閉じるボタンが押されたら終了する
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
