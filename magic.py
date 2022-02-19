from re import X
import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player

    def heal(self,player,strength,cost,group):
        if player.energy >= cost: # and player.health < player.stats['health']:
            player.health = min(player.health + strength, player.stats['health'])
            player.energy = max(player.energy - cost, 0)
            self.animation_player.create_particles('heal',player.rect.center + pygame.math.Vector2(0,-30),group)
            self.animation_player.create_particles('aura',player.rect.center,group)
            


    def flame(self,player,cost,group):
        if player.energy >= cost:
            player.energy = max(player.energy - cost, 0)
            if player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0,-1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0,1)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1,0)
            else:
                direction = pygame.math.Vector2(1,0)

            (x,y) = player.rect.center
            for i in range(1,6):
                # x = player.rect.centerx + randint(-TILESIZE  // 3, TILESIZE // 3)
                # y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                
                # x += randint(-TILESIZE   // 9, TILESIZE // 9)
                # y += randint(-TILESIZE   // 9, TILESIZE // 9)
                if direction.x: # horizontal
                    x += direction.x * TILESIZE + randint(-TILESIZE   // 9, TILESIZE // 9)
                    y += randint(-TILESIZE   // 9, TILESIZE // 9)
                else: # vertical
                    x += randint(-TILESIZE   // 9, TILESIZE // 9)
                    y += direction.y * TILESIZE + randint(-TILESIZE   // 9, TILESIZE // 9)
                
                self.animation_player.create_particles('flame',(x,y),group)

                # self.animation_player.create_particles('flame',pos,group)


# class Magic:
