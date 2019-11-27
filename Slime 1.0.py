# ------------------------------------------- #

# Working on:

# Slime Engine is working!

# ------------------------------------------- #


import pygame

pygame.init()

run = True

screenWidth = 1200
screenHeight = 660

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Slime")

x = 0.3 * screenWidth
y = 225
gameX = 0.3 * screenWidth
speed = 5
height = 18
hbSize = 40

jumping = False
fallAccel = 1
jumpCount = 0
fallCount = 0

canBreak = False
collide = False
frame = 0
levelWidth = 1600
dirLeft = True
spriteNum = 0

cubeHitbox = pygame.Rect(x, y, hbSize, hbSize)
cubeXbox = pygame.Rect(x, y, 40, 39)


devFont = pygame.font.SysFont("Arial", 20)
sprites = [pygame.image.load("C:\Desktop\Slime\jumpcubeLeft.gif"), pygame.image.load("C:\Desktop\Slime\jumpcubeRight.gif")]
platImg = [pygame.image.load("C:\Desktop\Slime\platformInvisible.gif"), pygame.image.load("C:\Desktop\Slime\platformLargeH.gif"),
           pygame.image.load("C:\Desktop\Slime\platformMLargeH.gif"), pygame.image.load("C:\Desktop\Slime\platformMSmallH.gif"),
           pygame.image.load("C:\Desktop\Slime\platformSmallH.gif"), pygame.image.load("C:\Desktop\Slime\platformLargeV.gif"),
           pygame.image.load("C:\Desktop\Slime\platformMLargeV.gif"), pygame.image.load("C:\Desktop\Slime\platformMSmallV.gif"),
           pygame.image.load("C:\Desktop\Slime\platformSmallV.gif")]
platforms = []


class plat:
    def __init__(self, pType, px, py):
        platforms.append(self)
        if pType == "ground":
            self.x = px + 0.3 * screenWidth
        else:
            self.x = px + 0.3 * screenWidth
        self.y = py
        self.type = pType
        if self.type == "lH":
            self.type = 1
            self.width = 120
            self.height = 10
        elif self.type == "mlH":
            self.type = 2
            self.width = 80
            self.height = 10
        elif self.type == "msH":
            self.type = 3
            self.width = 40
            self.height = 10
        elif self.type == "sH":
            self.type = 4
            self.width = 20
            self.height = 10
        elif self.type == "lV":
            self.type = 5
            self.width = 10
            self.height = 120
        elif self.type == "mlV":
            self.type = 6
            self.width = 10
            self.height = 80
        elif self.type == "msV":
            self.type = 7
            self.width = 10
            self.height = 40
        elif self.type == "sV":
            self.type = 8
            self.width = 10
            self.height = 20
        elif self.type == "barH":
            self.type = 0
            self.width = screenWidth
            self.height = 10
        elif self.type == "barV":
            self.type = 0
            self.width = 10
            self.height = screenHeight
        elif self.type == "ground":
            self.type = 0
            self.width = levelWidth
            self.height = 10
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)


def cubeUpdate():
    global cubeHitbox, cubeXbox
    cubeHitbox = pygame.Rect(x, y, hbSize, hbSize)
    cubeXbox = pygame.Rect(x, y, 40, 39)


cubeUpdate()


def devKit():
    devCX = devFont.render("X Collision False", False, (0, 0, 0))
    devCY = devFont.render("Y Collision False", False, (0, 0, 0))
    devGX = devFont.render("GameX: %s" % gameX, False, (0, 0, 0))
    devY = devFont.render("Y: %s" % y, False, (0, 0, 0,))
    devX = devFont.render("X: %s" % x, False, (0, 0, 0,))
    devAccel = devFont.render("FallAccel: %s" % fallAccel, False, (0, 0, 0))
    devFrame = devFont.render("Frame %s" % frame, False, (0, 0, 0))
    for platform in platforms:
        if cubeXbox.colliderect(platform.hitbox):
            devCX = devFont.render("X Collision True", False, (0, 0, 0))
        if cubeHitbox.colliderect(platform.hitbox):
            devCY = devFont.render("Y Collision True", False, (0, 0, 0))
    screen.blit(devX, (20, 20))
    screen.blit(devY, (20, 45))
    screen.blit(devCX, (20, 70))
    screen.blit(devCY, (20, 95))
    screen.blit(devGX, (20, 120))
    screen.blit(devAccel, (20, 145))
    screen.blit(devFrame, (20, 170))
    # pygame.draw.rect(screen, (255, 0, 0), [x, y, hbSize, hbSize], 1)
    pygame.draw.rect(screen, (0, 255, 0), [x, y, hbSize, 39], 1)


# Objects
cubeUpdate()
ground = plat("ground", 0, screenHeight)
wallLeft = plat("barV", -10, 0)
wallRight = plat("barV", levelWidth, 0)

# Platforms
plat1 = plat("lH", 260, 480)
plat2 = plat("msH", 170, 450)
plat3 = plat("lH", 350, 365)
plat4 = plat("mlH", 210, 325)
plat5 = plat("mlH", 250, 195)
plat6 = plat("mlH", 350, 560)
plat7 = plat("mlV", 470, 285)
plat8 = plat("msV", 470, 155)

plat9 = plat("lH", 660, 380)
plat10 = plat("msH", 570, 350)
plat11 = plat("lH", 750, 265)
plat12 = plat("mlH", 610, 225)
plat13 = plat("mlH", 650, 95)
plat14 = plat("mlH", 750, 460)
plat15 = plat("mlV", 870, 185)
plat16 = plat("msV", 870, 55)

plat17 = plat("lH", 1060, 580)
plat18 = plat("msH", 970, 550)
plat19 = plat("lH", 1150, 465)
plat20 = plat("mlH", 1010, 425)
plat21 = plat("mlH", 1050, 295)
plat22 = plat("mlH", 1150, 660)
plat23 = plat("mlV", 1270, 385)
plat24 = plat("msV", 1270, 255)

# Slime
screen.fill((255, 255, 255))
screen.blit(sprites[spriteNum], (x, y))
devKit()

# Drawing Platforms
for platform in platforms:
    screen.blit(platImg[platform.type], (platform.x - gameX, platform.y))
for platform in platforms:
    platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)

pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Jump
    if jumping:
        # Short Jump
        if not keys[pygame.K_w]:
            height = 18
            jumping = False
        elif height > 0:
            jumpCount = round((height ** 2) / 16)
            height -= 1
            # Head collision
            for jump in range(0, jumpCount):
                y -= 1
                cubeUpdate()
                # Ejecting Out of Platform
                for platform in platforms:
                    if cubeHitbox.colliderect(platform.hitbox):
                        while cubeHitbox.colliderect(platform.hitbox):
                            y += 1
                            cubeUpdate()
                        jumping = False
                        height = 18
                        canBreak = True
                        break
                if canBreak:
                    # Lock
                    for platform in platforms:
                        if y + hbSize == platform.y:
                            y += 1
                            cubeUpdate()
                            break
                    canBreak = False
                    break
        else:
            jumping = False
            height = 18

    # Keybinds
    elif keys[pygame.K_w]:
        # Jump Trigger
        for platform in platforms:
            if cubeHitbox.colliderect(platform.hitbox):
                y -= 1
                jumping = True
                fallAccel = 1
                cubeUpdate()
                for platform2 in platforms:
                    if cubeHitbox.colliderect(platform2.hitbox):
                        y += 1
                        cubeUpdate()
                        jumping = False
                        fallAccel = 3
                        break
                break

    if keys[pygame.K_a] and x > 0:
        dirLeft = True
        # X- collision
        for move in range(0, speed):
            gameX -= 1
            for platform in platforms:
                platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)
            # X- Scroll Lock
            if gameX < 0.3 * screenWidth:
                gameX += 1
                for platform in platforms:
                    platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)
                x -= 1
                cubeUpdate()
            # X+ Scroll Unlock
            if x > 0.3 * screenWidth:
                gameX += 1
                for platform in platforms:
                    platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)
                x -= 1
                cubeUpdate()
            # Ejection
            for platform in platforms:
                if cubeXbox.colliderect(platform.hitbox):
                    while cubeXbox.colliderect(platform.hitbox):
                        if x < 0.3 * screenWidth:
                            x += 1
                            cubeUpdate()
                        else:
                            gameX += 1
                            for platform2 in platforms:
                                platform2.hitbox = pygame.Rect(platform2.x - gameX, platform2.y, platform2.width, platform2.height)
                    canBreak = True
                    break
            if canBreak:
                canBreak = False
                break

    if keys[pygame.K_d] and x < screenWidth - 40:
        dirLeft = False
        # X+ collision
        for move in range(0, speed):
            gameX += 1
            for platform in platforms:
                platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)
            # X+ Scroll Lock
            if gameX > levelWidth - 0.7 * screenWidth:
                gameX -= 1
                for platform in platforms:
                    platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)
                x += 1
                cubeUpdate()
            # X- Scroll Unlock
            if x < 0.3 * screenWidth:
                gameX -= 1
                for platform in platforms:
                    platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)
                x += 1
                cubeUpdate()
            # Ejection
            for platform in platforms:
                if cubeXbox.colliderect(platform.hitbox):
                    while cubeXbox.colliderect(platform.hitbox):
                        if x > levelWidth - 0.7 * screenWidth:
                            x -= 1
                            cubeUpdate()
                        else:
                            gameX -= 1
                            for platform2 in platforms:
                                platform2.hitbox = pygame.Rect(platform2.x - gameX, platform2.y, platform2.width, platform2.height)
                    canBreak = True
                    break
            if canBreak:
                canBreak = False
                break

    # Slime Direction
    if dirLeft:
        spriteNum = 0
    else:
        spriteNum = 1

    # Grav Collision
    for platform in platforms:
        if cubeHitbox.colliderect(platform.hitbox):
            collide = True
            # Ejection
            while cubeHitbox.colliderect(platform.hitbox):
                y -= 1
                cubeUpdate()
            # Lock
            if y + hbSize == platform.y:
                y += 1
                cubeUpdate()
                fallAccel = 3
            break
    # Gravity
    if not collide and not jumping:
        fallCount = round((fallAccel ** 2) / 4)
        for fall in range(0, fallCount):
            y += 1
            cubeUpdate()
            # Collision
            for platform in platforms:
                if cubeHitbox.colliderect(platform.hitbox):
                    fallAccel = 2.8
                    canBreak = True
                    break
            if canBreak:
                canBreak = False
                break
        fallAccel += 0.2

    # Animation
    screen.fill((255, 255, 255))
    screen.blit(sprites[spriteNum], (x, y))

    # Hitboxes
    cubeUpdate()

    devKit()

    # Platforms Updates
    for platform in platforms:
        screen.blit(platImg[platform.type], (platform.x - gameX, platform.y))
    for platform in platforms:
        platform.hitbox = pygame.Rect(platform.x - gameX, platform.y, platform.width, platform.height)
    pygame.display.update()
    frame += 1
    collide = False

    pygame.time.delay(16)

pygame.quit()
