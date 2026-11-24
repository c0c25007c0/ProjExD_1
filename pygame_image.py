import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) #2
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #1
    kk_img = pg.image.load("fig/3.png") #3
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_img2 = pg.transform.flip(bg_img, True, False)#8
    kk_rct = kk_img.get_rect()
    kk_rct.center= 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if event.type == pg.QUIT:return
        kk_rct.move_ip((-1, 0))
        if key_lst[pg.K_UP]:
            kk_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:  # 下矢印キーが押されたら
            kk_rct.move_ip((0, +1))  # 縦に+1動かす
        if key_lst[pg.K_LEFT]:  # 左矢印キーが押されたら
            kk_rct.move_ip((-1, 0))  # 横に-1動かす            
        if key_lst[pg.K_RIGHT]:  # 右矢印キーが押されたら
            kk_rct.move_ip((+2, 0))  # 横に+1動かす

        

        x =tmr%3200 #5.9
        screen.blit(bg_img, [-x, 0]) #2.5
        screen.blit(bg_img2, [-x+1610, 0]) #7
        screen.blit(bg_img, [-x+3200, 0]) #2.5
        screen.blit(kk_img, kk_rct) #4
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)#6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()