# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 480
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha') #trocamos o titulo

# ----- Inicia assets
METEOR_WIDTH = 50 #largura meteoro
METEOR_HEIGHT = 38 #altura meteoro
SHIP_WIDTH = 50 #largura da nave
SHIP_HEIGHT = 38 #altura da nave
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('assets/img/starfield.png').convert() #imagem da tela que em breve será substituida
meteor_img = pygame.image.load('assets/img/meteorBrown_med1.png').convert_alpha() #transparencia na imagem de meteoro
meteor_img_small = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT)) #diminuindo o tamanho do meteoro
ship_img = pygame.image.load ('assets/img/playerShip1_orange.png').convert_alpha() #imagem da nave
ship_img = pygame.transform.scale(ship_img, (SHIP_WIDTH, SHIP_HEIGHT))
# ----- Inicia estruturas de dados

meteor_x = random.randint(0, WIDTH-METEOR_WIDTH) #posição em x
# y negativo significa que está acima do topo da janela. O meteoro começa fora da janela
meteor_y = random.randint(-100, -METEOR_HEIGHT ) #começar a cima da tela / posiçaõ em y
meteor_speedx = random.randint(-3,3) #velocidade x
meteor_speedy = random.randint(2,9) #velocidade y


# ----- Inicia estruturas de dados
class Ship (pygame.sprite.Sprite):
    def __init__(self, img):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = -5 #velocidade x

    def update(self): #update vai garantir a movimentação da nave
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Definindo os novos tipos
class Meteor(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
        self.rect.y = random.randint(-100, -METEOR_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self): #update vai garantir a movimentação dos meteoros
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)



game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30 #velocidade do jogo 

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
# Criando o jogador
player = Ship(ship_img)
all_sprites.add(player)
# Criando os meteoros
for i in range(8):
    meteor = Meteor(meteor_img)
    all_sprites.add(meteor)

# ===== Loop principal =====
while game:
    clock.tick(FPS)


    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


  
   # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background, (0, 0))
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

