import pygame

pygame.init()

size = (500, 500)
screen = pygame.display.set_mode(size)

vertices = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), 
            (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), 
         (2, 3), (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]

position = [250, 250, 0]
rotation = [0, 0, 0]

speed = 1


done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotation[1] += speed
            elif event.key == pygame.K_RIGHT:
                rotation[1] -= speed
            elif event.key == pygame.K_UP:
                rotation[0] += speed
            elif event.key == pygame.K_DOWN:
                rotation[0] -= speed
            elif event.key == pygame.K_q:
                rotation[2] += speed
            elif event.key == pygame.K_e:
                rotation[2] -= speed
    

    screen.fill((255, 255, 255))
    
    transformed_vertices = []
    for vertex in vertices:

        x = vertex[0] * cos(rotation[1]) + vertex[2] * sin(rotation[1])
        z = -vertex[0] * sin(rotation[1]) + vertex[2] * cos(rotation[1])
        y = vertex[1] * cos(rotation[0]) - z * sin(rotation[0])
        z = z * cos(rotation[0]) + vertex[1] * sin(rotation[0])
        x = x * cos(rotation[2]) - y * sin(rotation[2])
        y = y * cos(rotation[2]) + x * sin(rotation[2])
     
        x += position[0]
        y += position[1]
        z += position[2]

        transformed_vertices.append((int(x), int(y), int(z)))
    

    for edge in edges:
        start = transformed_vertices[edge[0]]
        end = transformed_vertices[edge[1]]
        pygame.draw.line(screen, (0, 0, 0), start, end, 2)
    

    pygame.display.flip()
    me
    clock.tick(60)

pygame.quit()
