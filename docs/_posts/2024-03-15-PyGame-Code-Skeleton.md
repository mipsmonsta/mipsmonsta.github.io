---
layout: post
title: PyGame Code Skeleton
date: 2024-03-15 18:00 +0800
categories: pygame
---

<img src="https://www.pygame.org/docs/_static/pygame_logo.png" width=300/>

## What's the minimal code for a PyGame python program?

You would need minimally the follow components for a viable PyGame code:
    
*  Module importation
*  Screen window 
*  Game loop
*  Event loop
*  Screen update

## Code

```python
import pygame

# initialize pygame
pygame.init()

# Screen surface
SCREEN_WIDTH = 600
SCRREN_HEIGHT = 400 # aspect ration of 3:2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# game loop
run = True
while run:
    screen.fill((255, 255, 255)) # white
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip() # or update() <- partial update is supported 

pygame.quit()

```