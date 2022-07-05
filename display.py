import pygame
from pygame.locals import *
from evaluateBoard import *
from go import go
path='images/'
width=520
height=520
margin=22
grid=(width-2*margin)/(SIZE-1)
piece=32
class display(object):
    def __init__(self,go):
        self.__go=go
        self.__currentstate=StateOfBoard.black
        pygame.init()
        self.__screen=pygame.display.set_mode((width,height),0,32)
        pygame.display.set_caption('GO GAME')
        self.__images_board=pygame.image.load(path+'board.jpg').convert()
        self.__images_black=pygame.image.load(path+'black.png').convert_alpha()
        self.__images_white=pygame.image.load(path+'white.png').convert_alpha()
    def transform_map_to_pixel(self,i,j):
        return(margin+j*grid-piece/2,margin+i*grid-piece/2)

    def transform_pixel_to_map(self,x,y):
        (i,j)=(int(round((y-margin+piece/2)/grid)),int(round((x-margin+piece/2)/grid)))
        if i<0 or i>=SIZE or j<0 or j>=SIZE:
            return (None,None) 
        else:
            return(i,j)
    def draw_board(self):
          self.__screen.blit(self.__images_board,(0,0))
          for i in range(0,SIZE):
            for j in range(0,SIZE):
                (x,y)=self.transform_map_to_pixel(i,j)
                state=self.__go.get_board_state(i,j)
                if state==StateOfBoard.black:
                    self.__screen.blit(self.__images_black,(x,y))
                elif state==StateOfBoard.white:
                    self.__screen.blit(self.__images_white,(x,y))
                else:
                    pass
    def mouse(self):
        (x,y)=pygame.mouse.get_pos()
        if self.__currentstate==StateOfBoard.black:
            self.__screen.blit(self.__images_black,(x-piece/2,y-piece/2))
        else:
            self.__screen.blit(self.__images_white,(x-piece/2,y-piece/2))
    def result(self,result):
        font=pygame.font.SysFont('Arial',55)
        res='**********GAME OVER'
        if result==StateOfBoard.black:
            res=res+'! BLACK WINS*********'
        elif result==StateOfBoard.white:
            res=res+'! WHITE WINS*********'
        else:
            res=res+'! DRAW*********'
        word=font.render(res,True,(0,0,255))
        self.__screen.blit(word,(width/2-200, height/2-50))
    def step(self):
        (i,j)=(None,None)
        mouse=pygame.mouse.get_pressed()
        if mouse[0]:
            (x,y)=pygame.mouse.get_pos()
            (i,j)=self.transform_pixel_to_map(x,y)
        if not i is None and not j is None:
            if self.__go.get_board_state(i, j)!= StateOfBoard.empty:
                return False
            else:
                self.__go.set_board_state(i, j,self.__currentstate)
                return True
        return False

    def change_state(self):
        if self.__currentstate == StateOfBoard.black:
            self.__currentstate = StateOfBoard.white
        else:
            self.__currentstate = StateOfBoard.black