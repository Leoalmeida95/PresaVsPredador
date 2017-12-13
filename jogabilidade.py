#Gabriela da Silva Almeida
#Leonardo Almeida da Silva
#Thales Fellipe Sathler Lima
import numpy as np
from classes import Predador,Presa
import pygame

class Jogabilidade():
    
    def __init__(self,num_predadores=1,num_presas=1,tamanho_mapa=12,tamanho_itens=10):
        self.tamanho_tela = tamanho_mapa*tamanho_itens
        self.tela = pygame.display.set_mode((self.tamanho_tela, self.tamanho_tela))
        self.mapa = np.zeros((tamanho_mapa,tamanho_mapa))
        self.tamanho_itens = tamanho_itens
        self.predadores = [Predador(self) for i in range(num_predadores)] 
        self.presas = [Presa(self) for i in range(num_presas)]

    def __str__(self):
        text = ""
        for idx,predador in enumerate(self.predadores):
            text += 'Predador '+str(idx)+' na posicao: x=' +str(predador.sprite.x)+' y='+str(predador.sprite.y)
        return text

    def distancia(self, p, q):
        return (abs(p[0] - q[0]) + abs(p[1] - q[1]))/10

    def percepcao(self,Ator):
        dictonary = {}
        visaoYmin = Ator.rect.y - (self.tamanho_itens*Ator.visao)
        visaoYmax = Ator.rect.y + (self.tamanho_itens*Ator.visao)
        visaoXmin = Ator.rect.x - (self.tamanho_itens*Ator.visao)
        visaoXmax = Ator.rect.x + (self.tamanho_itens*Ator.visao)

        if Ator.codigo == 1:
            for presa in self.presas:
                if ((visaoYmin < presa.rect.y < visaoYmax) and 
                    (visaoXmin < presa.rect.x < visaoXmax)):
                    dictonary[self.distancia((Ator.rect.x,Ator.rect.y),(presa.rect.x,presa.rect.y))] = (presa.rect.x,presa.rect.y)  
            return dictonary
            

    def clock(self):
        for predador in self.predadores:
            dictPredador = self.percepcao(predador)
            for presa in self.presas:
                presa.move()
            predador.move(dictPredador)


    def colisao(self):
        for predador in self.predadores:
            for presa in self.presas:
                if (not(predador.rect.x > presa.rect.right)) and (not(predador.rect.x < presa.rect.left)) and (not(predador.rect.y > presa.rect.bottom)) and (not(predador.rect.y < presa.rect.top)):
                    som = pygame.mixer.Sound("gameOver.wav")
                    som.set_volume(0.9)
                    som.play(1);
                    self.presas.remove(presa)
                    break

    def reproducao(self):
        for presa in self.presas:
            for p in self.presas:
                if not(presa == p):
                    if (not(presa.rect.x > p.rect.right)) and (not(presa.rect.x < p.rect.left)) and (not(presa.rect.y > p.rect.bottom)) and (not(presa.rect.y < p.rect.top)):
                        som = pygame.mixer.Sound("win.wav")
                        som.set_volume(0.9)
                        som.play(1);
                        presax = Presa(self)
                        #presax.cor = (0,0,255)
                        self.presas.append(presax)
                        break
