import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 600

DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Title")



def main():
    v1 = float(input("공(1)의 속력 :"))
    v2 = float(input("공(2)의 속력 :"))

    m1 = float(input("공(1)의 질량 :"))
    m2 = float(input("공(2)의 질량 :"))

    x1 = 100
    x2 = 900

    dt = 0.01
    run = True

    
    while run:
        DISPLAY.fill((255,255,255))
        pygame.draw.line(DISPLAY, (150,200,225), (0, 558), (1000, 558),60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.draw.circle(DISPLAY ,(0, 0, 255), (x1, 500), 30)
        pygame.draw.circle(DISPLAY ,(255, 0, 0), (x2, 500), 30)


        x1 = x1 + v1 * dt
        x2 = x2 - v2 * dt






        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()
    

