def game():
    pygame.init()
        
    window = pygame.display.set_mode((1200,700))
    Clok = pygame.time.Clock()


    image = pygame.image.load("dggame.png")
    image = pygame.transform.scale(image,(150,50))
    image2 = pygame.image.load("road.png")
    image2 = pygame.transform.scale(image2,(1200,700))


    class sprite(object):

        sprite_list = {}

        def __init__(self,speed,size,image,x,y,max_speed,hard) -> None:
            self.speed = speed
            self.size = size
            self.image = pygame.transform.scale(image,size)
            self.image_old = image
            self.x = x
            self.y = y
            self.max_speed = max_speed
            self.max_speed_old = max_speed
            self.hard = hard
            
            sprite.sprite_list[self] = [self.image,[x,y]]
        def obnow():
            for x in sprite.sprite_list:
                x.image = pygame.transform.scale(x.image_old,x.size)
                sprite.sprite_list[x] = [x.image,[x.x,x.y]]
        def exit():
            sprite.sprite_list={}



    class player(sprite):
        pass
        

        
    interesting = 50


    s = player(0,[100,100],image,100,100,300,1)
    g = sprite(1,(100,100),image,100,200,200,random.randrange(int(interesting/2),interesting)/100)
    g = sprite(1,(100,100),image,100,300,30,random.randrange(int(interesting/2),interesting)/100)
    g = sprite(1,(100,100),image,100,400,30,random.randrange(int(interesting/2),interesting)/100)

    g_r = random.randrange(200)/100


    x_a = 0


    runing = True

    race_time = (60)/2
    Fps = 60
    t = 0


    while runing:
        t += 1
        keys = pygame.key.get_pressed()

        x_a += s.speed
        if x_a >= 1200:
            x_a = 0

        for x in sprite.sprite_list:
            if x != s:
                x.x += x.speed - s.speed
                if x.speed < x.max_speed/2:
                    x.speed += x.max_speed/race_time/Fps*x.hard

            else:
                if not keys[pygame.K_d]:
                    if x.speed > 0:
                        x.speed *= 0.995
                else:
                    if s.speed < s.max_speed/2:
                        s.speed += s.max_speed/race_time/Fps


        sprite.obnow()
            




        window.blit(image2,(0-x_a,0))
        window.blit(image2,(1200-x_a,0))


        window.blits([*sprite.sprite_list.values()])



        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
                pygame.quit()
        Clok.tick(Fps)
        if t//60 >= race_time:
            p = [x[1] for x in sorted({x.x:x for x in sprite.sprite_list}.items())]
            f = p.index(s)
            runing = False
            pygame.quit()
            return f*interesting
