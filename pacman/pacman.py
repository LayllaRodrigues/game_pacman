import pygame

Amarelo = (255, 255, 0)
Preto = ((0, 0, 0))
Velocidade = 1
Raio = 30
pygame.init() #inicializa  a biblioteca

tela = pygame.display.set_mode((640, 480), 0) #aqui passamos o tamanho, altura  e largura da tela e a qtdd de pixels
x = 10
y = 10
velo_x = Velocidade
velo_y = Velocidade


while True:
    #Calcula as regras
    x = x + velo_x
    y = y + velo_y

    if x + Raio > 640:
        velo_x = -Velocidade
    if x - Raio < 0:
        velo_x = Velocidade

    if y + Raio > 480:
        velo_y = -Velocidade
    if y - Raio < 0:
        velo_y = Velocidade

    #Pinta
    tela.fill((Preto))
    pygame.draw.circle(tela, Amarelo, (int(x), int(y)), Raio, 0)
    pygame.display.update()

    #Eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()