from enum import Enum
from classBoard import *
from evaluateBoard import boardState
class go(object):
    def __init__(self):
        self.chess_map=[[StateOfBoard.empty for j in range(SIZE)]for i in range(SIZE)]
        self.current_i=-1
        self.current_j=-1
        self.current_state=StateOfBoard.empty

    def getchess_map(self):
            return self.chess_map
    def get_board_state(self,i,j):
            return self.chess_map[i][j]
    def set_board_state(self,i,j,state):
            self.chess_map[i][j]=state
            self.current_i=i
            self.current_j=j
            self.current_state=state
    def get_result(self):
            if self.connectedFive(self.current_i, self.current_j,self.current_state):
                return self.current_state
            else:
                return StateOfBoard.empty
    def count_dir(self,i,j,x_dir,y_dir,player):
            count=0
            for item in range(1,5):
                if x_dir!=0 and (j+x_dir*item<0 or j+x_dir*item>=SIZE):
                    break
                if y_dir != 0 and (i + y_dir * item < 0 or i+ y_dir * item >= SIZE):
                    break
                if self.chess_map[i+y_dir*item][j+x_dir*item]==player:
                    count+=1
                else:
                    break
            return count
    def connectedFive(self,i,j,player):
            direction = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1),
                      (1, -1)], [(-1, -1), (1, 1)]]
            for axis in direction:
                axis_count = 1
                for (x_dir, y_dir) in axis:
                    axis_count += self.count_dir(i, j, x_dir,
                            y_dir, player)
                    if axis_count >= 5:
                        return True
            return False


