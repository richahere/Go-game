from cgitb import enable
from operator import truediv
import pygame
from pygame.locals import *
from sys import exit
from classBoard import *
from go import go
from go_ai import *
from display import display
if __name__=='__main__':
    go_i=go()
    display_screen=display(go_i)
    ai1=go_ai(go_i,StateOfBoard.black,2)
    # 2 is depth here
    ai2=go_ai(go_i,StateOfBoard.white,1)
    res=StateOfBoard.empty
    enable_ai1=True
    enable_ai2=False
    ai1.firstStep()
    res=go_i.get_result()
    display_screen.change_state()
    while True:
        if enable_ai2:
            ai2.oneStep()
            res=go_i.get_result()
            if res!= StateOfBoard.empty:
                print(res,"WINS")
                break
            if enable_ai1:
                ai1.oneStep()
                res=go_i.get_result()
                if res!=StateOfBoard.empty:
                    print(res,"WINS")
                    break
            else:
                display_screen.change_state()
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            elif event.type==MOUSEBUTTONDOWN:
                if display_screen.step():
                    res=go_i.get_result()
                else:
                    continue
                if res !=StateOfBoard.empty:
                    break
                if enable_ai1:
                    ai1.oneStep()
                    res=go_i.get_result()
                else:
                    display_screen.change_state()
        display_screen.draw_board()
        display_screen.mouse()
        if res!=StateOfBoard.empty:
            display_screen.result(res)
        pygame.display.update()

