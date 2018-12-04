import pygame
import os

class Player(object):
       
    def __init__(self, name, display_name, x, y, width, height, player_number):
        self.name = name
        self.name = display_name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.isJump = False
        self.jumpCount = 10
        self.walkCount = 0
        self.right = False
        self.left = False
        self.player_number = player_number

        def _getSprites():
            right_1 = pygame.image.load(os.path.join('art', self.name, 'right_1.png')) 
            right_2 = pygame.image.load(os.path.join('art', self.name, 'right_2.png'))
            left_1 = pygame.transform.flip(right_1, True, False)
            left_2 = pygame.transform.flip(right_2, True, False)       
            jump_right = pygame.image.load(os.path.join('art', self.name, 'jump_right.png'))
            jump_left = pygame.transform.flip(jump_right, True, False)
            stand = pygame.image.load(os.path.join('art', self.name, 'stand.png'))
            
            sprites = {
                "right" : [right_1, right_2],
                "left": [left_1, left_2],
                "jump_left": jump_left,
                "jump_right": jump_right,
                "stand" : stand,
            }
            return sprites
        
        self.sprites = _getSprites()
        self.current_sprite = None
    
    def move(self, keys, game_surface):
        keyDict = {
            1: {
                "up" : pygame.K_UP,
                "down" : pygame.K_DOWN,
                "left" : pygame.K_LEFT,
                "right" : pygame.K_RIGHT,
            },
            2: {
                "up" : pygame.K_w,
                "down" : pygame.K_s,
                "left" : pygame.K_a,
                "right" : pygame.K_d,
            }
        }

        if keys[keyDict[self.player_number]["left"]] and self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
        elif keys[keyDict[self.player_number]["right"]] and self.x < game_surface.get_width() - self.width - self.vel:
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
            self.walkCount = 0

        if not(self.isJump):
            if keys[keyDict[self.player_number]["up"]]:
                self.isJump = True
                self.right = False
                self.left = False
                self.walkCount = 0
        else:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
    
    def draw(self, game_surface):
        ## Draw the character
        if self.walkCount >= 2:
            self.walkCount = 0

        if self.current_sprite == None:
            self.current_sprite = self.sprites["stand"]

        # display lumping jumping if character is in mid jump
        if self.isJump:
            if self.right:
                self.current_sprite = self.sprites["jump_right"]
            elif self.left:
                 self.current_sprite = self.sprites["jump_left"]
            else:
                 self.current_sprite = self.current_sprite
                 
        # otherwise display the left, right or stand sprite
        else:   
            if self.left:
                self.current_sprite = self.sprites["left"][self.walkCount % 2]
                self.walkCount += 1
            elif self.right:
                self.current_sprite = self.sprites["right"][self.walkCount % 2]
                self.walkCount += 1
            else:
                self. current_sprite = self.current_sprite
                
        
        game_surface.blit(self.current_sprite, (self.x, self.y))