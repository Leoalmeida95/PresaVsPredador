#Gabriela da Silva Almeida
#Leonardo Almeida da Silva
#Thales Fellipe Sathler Lima
import pygame, sys
from pygame.locals import *
from classes import Predador, Presa
from jogabilidade import Jogabilidade

tamanho = 10
done = False

pygame.init()
pygame.display.set_caption("TECC - Peixe vs. Tubarao")
imagem = pygame.image.load("fundo.png")
clock = pygame.time.Clock()
jogo = Jogabilidade(num_predadores=1,num_presas=5,tamanho_mapa=50,tamanho_itens=10)
pygame.mixer.music.load("theme.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while not done:
        jogo.tela.blit(imagem,(-210,-90))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        jogo.colisao()
        jogo.reproducao()
        jogo.clock()
        print(jogo.mapa)
        pygame.display.update()
        clock.tick(1)

pygame.quit()
sys.exit()