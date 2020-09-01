import pygame

pygame.init()

window = pygame.display.set_mode([800, 580])

bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, [800, 580])

img = pygame.image.load('spaceship.png')
spaceship = img

imgX = 350
imgY = 400
speedX = 0
speedY = 0

clock = pygame.time.Clock()
while True:
  
  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        speedY = -1
      if event.key == pygame.K_DOWN:
        speedY = 1
      if event.key == pygame.K_m:
        spaceship = pygame.transform.scale(
          img, [200, 200]
        )
      if event.key == pygame.K_n:
        spaceship = pygame.transform.scale(
          img, [128, 128]
        )

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        speedY = 0
      if event.key == pygame.K_DOWN:
        speedY = 0

  window.fill((255, 255, 255))
  window.blit(bg, [0, 0])

  window.blit(spaceship, [imgX, imgY])

  imgX += speedX
  imgY += speedY

  pygame.display.update()
  clock.tick(60)