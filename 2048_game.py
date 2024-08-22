import pygame
import random
import math

pygame.init()

FPS=60
width, height= 800,800
Rows=4
Cols=4

Rect_height= height//Rows
Rect_width=width//Cols

outline_color=(255,0,0)
otline_thinkness=10
background_color=(205,192,180)
font_color=(119,110,101)

font=pygame.font.SysFont("comicsans",60,bold=True)
move_vel=20

window=pygame.display.set_mode((width,height))
pygame.display.set_caption("2048")

class Tile:
    colors=[
       (237,229,218),
       (238,225,201),
       (243,178,122),
       (246,150,101),
       (247,124,95),
       (247,95,59),
       (237,208,115),
       (237,204,99),
       (236,202,80),
   ] 

    def __init__(self, value,row,col):
       self.value=value
       self.row=row
       self.col=col
       self.x=col*Rect_width
       self.y=row*Rect_height

    def get_color(self):
       color_index=int(math.log2(self.value))-1
       color= self.colors[color_index]
       return color
   
    def draw(self,Window):
       color=self.get_color()
       pygame.draw.rect(Window,color,(self.x, self.y, Rect_width, Rect_height))
   
    def set_pos(self):
       pass
    
    def move(self,delta):
        pass
    
       
def draw_grid(Window):
    for row in range(1,Rows):
        y= row*Rect_height
        pygame.draw.line(Window, outline_color,(0,y),(width,y),otline_thinkness)

    for col in range(1,Cols):
        x= col*Rect_height
        pygame.draw.line(Window, outline_color,(x,0),(x,height),otline_thinkness)

    pygame.draw.rect(Window, outline_color,(0,0,width,height),otline_thinkness)

def draw(Window):
    Window.fill(background_color)
    
    draw_grid(Window)
    pygame.display.update()


def main(Window):
    clock=pygame.time.Clock()
    run=True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
                break

        draw(Window)

    pygame.quit()            

if __name__=="__main__":
    main(window)