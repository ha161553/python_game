# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
import time
import csv
import pandas as pd
from module_effect import *
class map():
    y = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
    x = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450]
    def map_array(self, m_c):
        lines =[]
        min_row = 0
        max_row = 15
        with open(str(m_c) + ".csv","r") as f:
            reader = csv.reader(f)
            for row in reader:
                lines.append(row)
        lines_t = []
        for row in lines:
            tt_colum = []
            for column in range(min_row, max_row):
                tt_colum.append(row[column])
            lines_t.append(tt_colum)
        return lines_t
    
    def draw_map(self, m_f, now_p, pos1, pos2, lines_t):
        bg = pygame.image.load("sky1.png").convert_alpha() # 背景画像の指定
        bg = pygame.transform.scale(bg, (1500, 1000)) # 画像を好きなサイズに調整
        map1 = pygame.image.load("wall.png").convert_alpha() # 地面の画像
        map1 = pygame.transform.scale(map1, (100, 100))
        player = pygame.image.load("man.png").convert_alpha() #playerの指定
        player = pygame.transform.scale(player, (100, 100))        
        rect_bg = bg.get_rect() # 画像のサイズ取得？？だと思われる
        rect_map1 = map1.get_rect()   
        rect_player = player.get_rect()
        screen.blit(bg, rect_bg)        
        map_array = lines_t
        x = self.x
        y = self.y
        if m_f == 1:
            rect_player = now_p
            screen.blit(player, rect_player)
        for i in range(0,10):
            for j in range(0,15):
                if int(map_array[i][j]) == 1:
                    rect_map1.center = (x[j], y[i])
                    screen.blit(map1, rect_map1)
                elif int(map_array[i][j]) == 2 and m_f == 0:
                    rect_player.center = (x[j], y[i])
                    screen.blit(player, rect_player)
                    m_f = 1
                elif int(map_array[i][j]) == 3:
                    pos1 = (x[j-1], y[i-1])
                elif int(map_array[i][j]) == 4:
                    pos2 = (x[j-1], y[i-1])       

        return rect_player, m_f, map_array, pos1, pos2
    def draw_map2(self, m_c):
        bg = pygame.image.load("pipo-battlebg001b.jpg").convert_alpha() #背景画像の指定
        bg = pygame.transform.scale(bg, (1500, 1000)) # 画像を好きなサイズに調整
        enemy = pygame.image.load("pipo-enemy"+str(m_c)+".png").convert_alpha() #敵の画像
        if m_c == -1 or m_c == 0 or m_c == 1:
            enemy = pygame.transform.scale(enemy, (240, 240))
        elif m_c == 2:
            enemy = pygame.transform.scale(enemy, (480, 480))
        rect_bg = bg.get_rect()
        rect_enemy = enemy.get_rect()
        screen.blit(bg, rect_bg)
        rect_enemy.center = (750, 600)
        screen.blit(enemy, rect_enemy)   

    def encount(self, encounter, e):
        if encounter >= 10:
            encounter = 0
            r = random.randint(1,5)
            if r == 4:
                e = 1
        return encounter, e
    
    def battle(self, e, button, a, e_h, p_h, f):
        if e == 1:
            font = pygame.font.SysFont(None, 25)
            text = font.render("Atack", True, (0,0,0))
            pygame.draw.rect(screen, (255, 0, 0), button)
            screen.blit(text, (700, 800))
            if a == 1:
                f = 1
                e_h = e_h - 10
                p_h = p_h - 10
                a = 0
        if e_h <= 0:
            font = pygame.font.SysFont(None, 100)
            text_b = font.render("Defeat", True, (255,255,255))
            screen.blit(text_b, (750, 500))
            e = 0
            f = 0
            e_h = 30
        if p_h <= 0:
            font = pygame.font.SysFont(None, 100)
            text_b = font.render("Lose", True, (255, 255, 255))
            screen.blit(text_b, (750, 500))
            e = 0
            f = 0
            e_h = 30
            p_h = 100        
        return e, e_h, a, p_h, f
    def change_map(self, v, m_c, pos1, pos2, rect_player):
        if v == 3:
            m_c = m_c - 1
            x, y = pos2
            rect_player.center = (x+100, y+100)
        elif v == 4:
            m_c = m_c + 1
            if pos1 != (2000, 2000):
                x, y  = pos1 
            elif pos1 == (2000, 2000):
                x, y = (50, 750)
            rect_player.center = (x+100, y+100)
        v = 0
        return v, m_c, rect_player


class player():

    x_p = [50, 100, 150, 200, 250, 300, 350, 400,
    450, 500, 550, 600, 650, 700, 750, 800, 850, 900,
    950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350,
    1400, 1450]     
    y_p = [50, 100, 150, 200, 250, 300, 350, 400,
    450, 500, 550, 600, 650, 700, 750, 800, 850, 900,
    950]  
    y_m = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]
    x_m = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450]    
    def move(self, m, rect_player, map_array,d_f, c, count, v, encounter):
        player = pygame.image.load("man.png").convert_alpha() #playerの指定
        player = pygame.transform.scale(player, (100, 100))                
        x_p = self.x_p
        y_p = self.y_p
        now_p = rect_player
        n_x, n_y = now_p.center


        if n_x in self.x_m and n_y in self.y_m:
            if int(map_array[self.y_m.index(n_y) + 1][self.x_m.index(n_x)]) == 1:
                d_f = 0
                if count == 1:
                    c = 1
            elif int(map_array[self.y_m.index(n_y) + 1][self.x_m.index(n_x)]) == 0:
                d_f = 1
            if int(map_array[self.y_m.index(n_y)][self.x_m.index(n_x)]) == 3 and v == 1:
                v = 3
            elif int(map_array[self.y_m.index(n_y)][self.x_m.index(n_x)]) == 4 and v == 1:
                v = 4
        elif n_x + 50 in self.x_m and n_y in self.y_m:
            if int(map_array[self.y_m.index(n_y) + 1][self.x_m.index(n_x+50)]) == 1:
                d_f = 0
                if count == 1:
                    c = 1
            elif int(map_array[self.y_m.index(n_y) + 1][self.x_m.index(n_x-50)]) == 1:
                d_f = 0
                if count == 1:
                    c = 1
            elif int(map_array[self.y_m.index(n_y) + 1][self.x_m.index(n_x+50)]) == 0 and int(map_array[self.y_m.index(n_y) + 1][self.x_m.index(n_x-50)]) == 0:
                d_f = 1
        elif n_x in self.x_m and n_y + 50 in self.y_m:
            if int(map_array[self.y_m.index(n_y+50)][self.x_m.index(n_x)]) == 0:
                d_f = 1
        elif n_x + 50 in self.x_m and n_y + 50 in self.y_m and c >= 4:
            if int(map_array[self.y_m.index(n_y+50)][self.x_m.index(n_x+50)]) == 0 and int(map_array[self.y_m.index(n_y+50)][self.x_m.index(n_x-50)]) == 0:
                d_f = 1

        if n_x in self.x_m and n_y in self.y_m and n_x + 100 in self.x_m and n_x - 100 in self.x_m:
            if int(map_array[self.y_m.index(n_y)][self.x_m.index(n_x)+1]) == 1 and m == 1:
                m = 0
            if int(map_array[self.y_m.index(n_y)][self.x_m.index(n_x)-1]) == 1 and m == -1:
                m = 0
            if int(map_array[self.y_m.index(n_y)+1][self.x_m.index(n_x)+1]) == 1 and d_f == 1 and m == 1:
                m = 0
            if int(map_array[self.y_m.index(n_y)+1][self.x_m.index(n_x)-1]) == 1 and d_f == 1 and m == -1:
                m = 0
        if n_x in self.x_m and n_y + 50 in self.y_m and n_x + 100 in self.x_m and n_x - 100 in self.x_m:
            if int(map_array[self.y_m.index(n_y+50)][self.x_m.index(n_x)+1]) == 1 and m == 1:
                m = 0
            if int(map_array[self.y_m.index(n_y+50)][self.x_m.index(n_x)-1]) == 1 and m == -1:
                m = 0
            if int(map_array[self.y_m.index(n_y-50)][self.x_m.index(n_x)+1]) == 1 and m == 1:
                m = 0
            if int(map_array[self.y_m.index(n_y-50)][self.x_m.index(n_x)-1]) == 1 and m == -1:
                m = 0
        if m == -1 and n_x != x_p[0]:
            n_x = n_x - 50 
            encounter += 1
        elif m == 1 and n_x != x_p[-1]:
            n_x = n_x + 50
            encounter += 1            
        elif m == 0:
            n_x = n_x




        


        if c == 1 and count < 4 and n_y != y_p[0]:
            n_y = n_y - 50
        elif count >= 4:
            c = 0
        if d_f == 1 and n_y < 850 and c == 0:
            n_y = n_y + 50 
        

                   
        x = n_x
        y = n_y
        now_p.center = (x, y)
        return now_p, m, d_f, c, v, encounter
    
        



        
    

if __name__ == "__main__":
    pygame.init() # 初期化
    screen = pygame.display.set_mode((1500, 1000)) # ウィンドウサイズの指定
    pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定
    m = 0
    m_c = -1
    v = 0
    m_f = 0
    d_f = 0
    now_p = (0, 0)
    count = 2
    encounter = 0
    e = 0
    a = 0
    button = pygame.Rect(700, 800, 50, 30)
    f = 0
    e_h = 30
    p_h = 100
    c = 0
    pos1 = (2000, 2000)
    pos2 = (2000, 2000)
    pos = (700, 600)
    map = map()
    player = player()
    all = pygame.sprite.RenderUpdates()
    effect.containers = all
    effect2.containers = all
    effect3.containers = all
    e_action = pygame.image.load("pipo-btleffect001.png")
    ene_action = pygame.image.load("pipo-btleffect122.png")
    e_gate = pygame.image.load("pipo-gate01b.png")
    effect.images = split_image(e_gate, 5)
    effect2.images = split_image(e_action, 5)
    effect3.images = split_image(ene_action, 5)
    effect = effect()
    effect2 = effect2()
    effect3 = effect3()
    while True:        
        lines_t = map.map_array(m_c)
        if e == 0:
            rect_player, m_f, map_array, pos1, pos2 = map.draw_map(m_f ,now_p, pos1, pos2, lines_t)
            now_p, m, d_f, c, v, encounter = player.move(m, rect_player, map_array, d_f, c, count, v, encounter)
            if effect.frame == effect.max_frame:
                effect.frame = 0
            image, effect.frame = effect.update()
            image = pygame.transform.scale(image, (160, 120))
            screen.blit(image, pos1)
            screen.blit(image, pos2)
        elif e == 1:
            map.draw_map2(m_c)
            e, e_h, a, p_h, f = map.battle(e, button, a, e_h, p_h, f)
            if f == 1:
                if effect2.frame == effect2.max_frame:
                    f = 2 
                    effect2.frame = 0
                else:  
                    image2, effect2.frame = effect2.update()
                    screen.blit(image2, pos)
            if f == 2:
                if effect3.frame == effect3.max_frame:
                    f = 0
                    effect3.frame = 0
                else:
                    image3, effect3.frame = effect3.update()
                    screen.blit(image3, pos)
        encounter, e = map.encount(encounter, e)
        v, m_c, rect_player = map.change_map(v, m_c, pos1, pos2, rect_player)

        
        pygame.time.wait(1)#更新感覚。多分ミリ秒
        pygame.display.update()#画面更新
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    a = 1
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_LEFT:
                    m = -1
                elif event.key == K_RIGHT:
                    m = 1
                elif event.key == K_UP:
                    m = 2
                if event.key == K_c and count >= 4:
                    count = 0
                if event.key == K_v:
                    v = 1
        count += 1
    
