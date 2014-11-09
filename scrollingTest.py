import pygame

title = "Scrolling test"
fps = 60
playtime = 0

xtiles = 15
ytiles = 15

width = 400
height = 400

bigmapwidth = 1600
bigmapheight = 1600

cornerpoint=[0,0]

scrollstepx = 5
scrollstepy = 5

pygame.init()
screen=pygame.display.set_mode((width,height)) 
# note that "map" is an pygame function and can not be used as a name for a variable
bigmap = pygame.Surface((bigmapwidth, bigmapheight))
# ----------------- create bigmap -------------------
bigmap.fill((128,128,128)) # fill grey




# paint a grid of dark lines
for x in range(0,bigmapwidth,bigmapwidth/xtiles): #start, stop, step
    pygame.draw.line(bigmap, (64,64,64), (x,0), (x,bigmapheight))
for y in range(0,bigmapheight,bigmapheight/ytiles): #start, stop, step
    pygame.draw.line(bigmap, (64,64,64), (0,y), (bigmapwidth,y))
pygame.draw.rect(bigmap, (255,0,0), (0,0,bigmapwidth, bigmapheight), 25) # red bigmap edge
# paint thin red cross in the middle of the map
pygame.draw.line(bigmap, (200,0,0), (bigmapwidth /2, 0),( bigmapwidth / 2, bigmapheight),1)
pygame.draw.line(bigmap, (200,0,0), (0, bigmapheight/2),( bigmapwidth , bigmapheight/2),1)






bigmap = bigmap.convert()
# ------- background is a subsurface of bigmap ----------
background = pygame.Surface((screen.get_size()))
backgroundrect = background.get_rect()
background = bigmap.subsurface((cornerpoint[0],
                                cornerpoint[1],
                                width,
                                height)) # take snapshot of bigmap
# -----------------------------------
background = background.convert()
screen.blit(background, (0,0)) # delete all
clock = pygame.time.Clock()    # create pygame clock object


allgroup = pygame.sprite.LayeredUpdates()



mainloop = True           
while mainloop:
    milliseconds = clock.tick(fps)  # milliseconds passed since last frame
    seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
    playtime += seconds

           
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame window closed by user
            mainloop = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # exit game

    # -------- scroll the big map ----------
    scrollx = 0
    scrolly = 0
    pressedkeys = pygame.key.get_pressed()
    # --- handle Cursor keys to scroll map ----
    if pressedkeys[pygame.K_LEFT]:
         scrollx -= scrollstepx
    if pressedkeys[pygame.K_RIGHT]:
         scrollx += scrollstepx
    if pressedkeys[pygame.K_UP]:
         scrolly -= scrollstepy
    if pressedkeys[pygame.K_DOWN]:
         scrolly += scrollstepy
    # -------- scroll the visible part of the map ------
    cornerpoint[0] += scrollx
    cornerpoint[1] += scrolly
    #--------- do not scroll out of bigmap edge -----
    if cornerpoint[0] < 0:
        cornerpoint[0] = 0
        scrollx = 0
    elif cornerpoint[0] > bigmapwidth - width:
        cornerpoint[0] = bigmapwidth - width
        scrollx = 0
    if cornerpoint[1] < 0:
        cornerpoint[1] = 0
        scrolly = 0
    elif cornerpoint[1] > bigmapheight - height:
        cornerpoint[1] = bigmapheight - height
        scrolly = 0

    pygame.display.set_caption("%s FPS: %.2f playtime: %.1f " % ( title,clock.get_fps(), playtime))
    #screen.blit(background, (0,0)) # delete all
    if scrollx == 0 and scrolly == 0:    # only necessery if there was no scrolling
        allgroup.clear(screen, background) # funny effect if you outcomment this line
    else:
        background = bigmap.subsurface((cornerpoint[0],
                                        cornerpoint[1],
                                        width,
                                        height)) # take snapshot of bigmap
        screen.blit(background, (0,0))
    allgroup.update(seconds) 
    allgroup.draw(screen)
    pygame.display.flip() # flip the screen 30 times a second









    
