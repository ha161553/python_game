# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import random
import time



class effect(pygame.sprite.Sprite):
    #爆発エフェクト
    animcycle = 2  # アニメーション速度
    frame = 0
    def __init__(self):
        # imagesとcontainersはmain()でセット
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        #self.rect.center = pos
        self.max_frame = len(self.images) * self.animcycle   # 消滅するフレーム
    def update(self):
        # キャラクターアニメーション
        self.image = self.images[int(self.frame/self.animcycle)]
        self.frame += 1
        if self.frame == self.max_frame:
            self.kill()  # 消滅
        return self.image, self.frame

class effect2(pygame.sprite.Sprite):
    #爆発エフェクト
    animcycle = 1  # アニメーション速度
    frame = 0
    def __init__(self):
        # imagesとcontainersはmain()でセット
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        #self.rect.center = pos
        self.max_frame = len(self.images) * self.animcycle   # 消滅するフレーム
    def update(self):
        # キャラクターアニメーション
        self.image = self.images[int(self.frame/self.animcycle)]
        self.frame += 1
        if self.frame == self.max_frame:
            self.kill()  # 消滅
        return self.image, self.frame

class effect3(pygame.sprite.Sprite):
    #爆発エフェクト
    animcycle = 1  # アニメーション速度
    frame = 0
    def __init__(self):
        # imagesとcontainersはmain()でセット
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        #self.rect.center = pos
        self.max_frame = len(self.images) * self.animcycle   # 消滅するフレーム
    def update(self):
        # キャラクターアニメーション
        self.image = self.images[int(self.frame/self.animcycle)]
        self.frame += 1
        if self.frame == self.max_frame:
            self.kill()  # 消滅
        return self.image, self.frame

def split_image(image, n):
    #横に長いイメージを同じ大きさのn枚のイメージに分割
    #分割したイメージを格納したリストを返す
    image_list = []
    w = int(image.get_width())
    h = int(image.get_height())
    w1 = int(w / n)
    for i in range(1, w, w1):
        surface = pygame.Surface((w1,h))
        surface.blit(image, (0,0), (i,0,w1,h))
        surface.set_colorkey(surface.get_at((0,0)), RLEACCEL)
        surface.convert()
        image_list.append(surface)
    return image_list