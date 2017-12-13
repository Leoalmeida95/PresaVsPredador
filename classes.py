#Gabriela da Silva Almeida
#Leonardo Almeida da Silva
#Thales Fellipe Sathler Lima
import pygame, sys
from pygame.locals import *
from random import randint, choice

class Ator(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        #self.image = pygame.image.load(path)
        self.rect = pygame.Rect(0,0, self.game.tamanho_itens,self.game.tamanho_itens)
        #self.rect = self.image.get_rect()
    
    def move(self,dictonary={}):
        self.game.mapa[self.rect.x/self.game.tamanho_itens,self.rect.y/self.game.tamanho_itens] = 0
        self.move_aleatorio(dictonary)
        self.game.mapa[self.rect.x/self.game.tamanho_itens,self.rect.y/self.game.tamanho_itens] = self.codigo
        pygame.draw.rect(self.game.tela,self.cor,self.rect)

    def move_aleatorio(self,dictonary={}):
        posicao = 1
        x = 0
        y = 0
        transloc = self.game.tamanho_itens
        direcao = randint(1, 4)

        if self.codigo == 1 and len(dictonary) > 0:
            #print len(dictonary)#printa quantos tem na visao
            listManhayam = dictonary.keys()
            listManhayam.sort()
            menor_Manhatam = listManhayam[0]#pega o mais perto
            presaX,presaY = dictonary[menor_Manhatam]
            if self.rect.x < presaX:
                posicao = 1
            elif self.rect.x > presaX:
                posicao = 2
            elif self.rect.y < presaY:
                posicao = 3
            elif self.rect.y > presaY:
                posicao = 4
            aleat = randint(1, 2)
            posicoes = [posicao,posicao,aleat]
            direcao = choice(posicoes)

        if direcao == 1:
            x = transloc
        elif direcao == 2:
            x = -transloc
        elif direcao == 3:
            y = transloc
        else:
            y = -transloc


        if (self.rect.x + x < 0 or self.rect.x + x >= self.game.tamanho_tela) or (self.rect.y + y < 0 or self.rect.y + y >= self.game.tamanho_tela):
            return
        else:
            self.rect.move_ip(x,y)


class Predador(Ator):
    def __init__(self,game):
        super(Predador,self).__init__(game)
        self.rect.x = randint(0, ((self.game.tamanho_tela-10)/self.game.tamanho_itens))*self.game.tamanho_itens
        self.rect.y = randint(0, ((self.game.tamanho_tela-10)/self.game.tamanho_itens))*self.game.tamanho_itens
        self.codigo = 1
        self.visao = 10
        self.cor = (255,0,0)

class Presa(Ator):
    id = 0
    def __init__(self,game):
        super(Presa,self).__init__(game)
        self.rect.x = randint(0, ((self.game.tamanho_tela-10)/self.game.tamanho_itens))*self.game.tamanho_itens
        self.rect.y = randint(0, ((self.game.tamanho_tela-10)/self.game.tamanho_itens))*self.game.tamanho_itens
        self.codigo = 2
        self.visao = 5
        self.cor = (100,100,100)
        Presa.id += 1
        self.id = Presa.id