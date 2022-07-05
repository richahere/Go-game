import random
from classBoard import *
from copy import deepcopy
from go import go
from evaluateBoard import *
class go_ai(object):
    def __init__(self,go,current_state,depth):
        self.__go=go
        self.__current_state=current_state
        self.depth=depth
        self.current_i=-1
        self.current_j=-1

    def setBoard(self,i,j,state):
        self.__go.set_board_state(i,j,state)

    def has_neighbour(self,state,i,j):
        # this will find out whther neighbour is present or not
        # in all four direction
        direction = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1),
                      (1, -1)], [(-1, -1), (1, 1)]]
        for axis in direction:
            for (x_dir, y_dir) in axis:

                if x_dir != 0 and (j + x_dir < 0 or j+ x_dir >= SIZE):
                    break
                if y_dir != 0 and (i + y_dir < 0 or i
                        + y_dir >= SIZE):
                    break
                if self.__go.getchess_map()[i + y_dir][j
                        + x_dir] != StateOfBoard.empty:
                    return True

                if x_dir != 0 and (j + x_dir * 2 < 0 or j
                        + x_dir * 2 >= SIZE):
                    break

                if y_dir != 0 and (i + y_dir * 2 < 0 or i
                        + y_dir * 2 >= SIZE):
                    break

                if self.__go.getchess_map()[i + y_dir * 2][j
                        + x_dir * 2] != StateOfBoard.empty:
                    return True
        return False
    def count_dir(self,i,j,x_dir,y_dir,state):
        count=0
        for item in range(1,5):
            if x_dir!=0 and (j+x_dir*item<0 or j+x_dir*item>=SIZE):
                    break
            if y_dir != 0 and (i + y_dir * item < 0 or i+ y_dir * item >= SIZE):
                    break
            if self.__go.getchess_map()[i+y_dir*item][j+x_dir*item]==state:
                    count+=1
            else:
                    break
            return count
    def dir_pattern(self,i,j,x_dir,y_dir,state):
        pattern_list=[]
        for item in range(-1,5):
            if x_dir!=0 and (j+x_dir*item<0 or j+x_dir*item>=SIZE):
                break
            if y_dir!=0 and (i+y_dir*item<0 or i+y_dir*item>=SIZE):
                break
            pattern_list.append(self.__go.getchess_map()[i+y_dir*item][j+x_dir*item])
        return pattern_list
    def has_five_in_row(self,state,i,j):
            directions = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1),
                      (1, -1)], [(-1, -1), (1, 1)]]
            for axis in directions:
                count_axis=1
                for(x_dir,y_dir) in axis:
                    count_axis+=(self.count_dir(i,j,x_dir,y_dir,state))
                    if count_axis>=5:
                        return True
            return False
    def check(self,state,i,j):
        # this funcation here meant to check unblocked four
        direction = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1),
                      (1, -1)], [(-1, -1), (1, 1)]]
        for item in direction:
         current_pat=[]
         for(x_dir,y_dir)in item:
            current_pat+=self.dir_pattern(i,j,x_dir,y_dir,state)
            if len(current_pat)>2:
                current_pat[1]=state
            if boardState(current_pat)==white_6_patterns[0]:
                return True
            if boardState(current_pat)==black_6_patterns[0]:
                return True
        return False
    def checkmate(self,state):
        # to check opponent's checkmate
        vec=[]
        for i in range(SIZE):
            vec.append(self.__go.getchess_map()[i][j] for i in range(SIZE))
        for j in range(SIZE):
            vec.append([self.__go.getchess_map()[i][j] for i in range(SIZE)])
        
        vec.append([self.__go.getchess_map()[x][x] for x in
                       range(SIZE)])
        for i in range(1, SIZE - 4):
            v = [self.__go.getchess_map()[x][x - i] for x in
                 range(i, SIZE)]
            vec.append(v)
            v = [self.__go.getchess_map()[y - i][y] for y in
                 range(i, SIZE)]
            vec.append(v)

        vec.append([self.__go.getchess_map()[x][SIZE - x - 1]
                       for x in range(SIZE)])
        for i in range(4, SIZE - 1):
            v = [self.__go.getchess_map()[x][i - x] for x in
                 range(i, -1, -1)]
            vec.append(v)
            v = [self.__go.getchess_map()[x][SIZE - x + SIZE - i - 2]
                 for x in range(SIZE - i - 1, SIZE)]
            vec.append(v)

        #checkmate
        for vector in vec:
            temp = boardState(vector)
            if state == StateOfBoard.BLACK:
                for pattern in white_5_patterns:
                    if small_part_big(pattern, temp):
                        return True
            if state == StateOfBoard.WHITE:
                for pattern in black_5_patterns:
                    if small_part_big(pattern, temp):
                        return True
        return False
    def generate_list(self):
        # here we are generating list of 
        # avilable points
        frontList=[]
        for i in range(SIZE):
            for j in range(SIZE):
                if self.__go.getchess_map()[i][j]!=StateOfBoard.empty:
                    continue
                if not self.has_neighbour(self.__go.getchess_map()[i][j]!=StateOfBoard.empty):
                    continue
                if self.current_state==StateOfBoard.white:
                    next_state=StateOfBoard.black
                else:
                    next_state=StateOfBoard.white
                next_play=go_ai(deepcopy(self.__go),next_state,self.depth-1)
                next_play.setBoard(i,j,self.current_state)
                frontList.append((next_play,i,j))
        frontScore=[]
        for nodes in frontList:
            frontScore.append(self.evaluatePoint(nodes[1],nodes[2]))
        frontZip=zip(frontList,frontScore)
        frontSort=sorted(frontZip,key=lambda t:t[1])
        (frontList,frontScore)=zip(*frontSort)
        return frontList
    def negate(self):
        return -self.evaluate()
    def evaluate(self):
        # here we will be returning board 
        # score for our minimax search
        vec=[]
        for i in range(SIZE):
            vec.append([self.__go.getchess_map()[i]])
        for j in range(SIZE):
            vec.append([self.__go.getchess_map()[i][j] for i in range(SIZE)])
        vec.append([self.__go.getchess_map()[x][x] for x in range(SIZE)])
        for i in range(1,SIZE-4):
            v=[self.__go.getchess_map()[x][x-i] for x in range(i,SIZE)]
            vec.append(v)
            v=[self.__go.getchess_map()[y-1][y] for y in range(i,SIZE)]
            vec.append(v)
        vec.append([self.__go.getchess_map()[x][SIZE-x-1] for x in range(SIZE)])
        for i in range(4,SIZE-1):
            v = [self.__go.getchess_map()[x][i - x] for x in
                 range(i, -1, -1)]
            vec.append(v)
            v = [self.__go.getchess_map()[x][SIZE - x + SIZE - i - 2]
                 for x in range(SIZE - i - 1, SIZE)]
            vec.append(v)
        boardscore = 0

        for v in vec:
            score = score_eval(v)
            if self.__current_state == StateOfBoard.white:
                boardscore += score['black'] - score['white']
            else:
                boardscore += score['white'] - score['black']
        return boardscore
    def evaluatePoint(self,i,j):
        vec=[]
        vec.append(self.__go.getchess_map()[i])
        vec.append([self.__go.getchess_map()[i][j] for i in range(SIZE)])
        if j>i:
            v=[self.__go.getchess_map()[x][x+j-i] for x in range(0,SIZE-j+i)]
            vec.apend(v)

        elif j==i:
            vec.append([self.__go.getchess_map()[x][x] for x in range(SIZE)])
        elif j<i:
            v=[self.__go.getchess_map()[x+i-j][x] for x in range(0,SIZE-i+j)]
            vec.append(v)

        if i+j==SIZE-1:
            v=[self.__go.getchess_map()[x][SIZE-1-x-abs(i-j)] for x in range(SIZE-abs(i-j))]
            vec.append(v)

        elif i+j<SIZE-1:
            
            v = [self.__go.getchess_map()[x][SIZE - 1 - x - abs(i
                 - j)] for x in range(SIZE - abs(i - j))]
            vec.append(v)
        elif i + j > SIZE - 1:

            vec.append([self.__go.getchess_map()[x][SIZE - 1 - x
                           + i + j - SIZE + 1] for x in range(i + j - SIZE
                           + 1, SIZE)])

        pointScore = 0
        for v in vec:
            score = score_eval(v)
            if self.__current_state == StateOfBoard.white:
                pointScore += score['white']
            else:
                pointScore += score['black']
        return pointScore
    def alpha_beta_pruning(self,ai,alpha=-10000000,beta=10000000):
        if ai.depth<=0:
            score=ai.negate()
            return score
        for(next_play,i,j) in ai.generate_list():
            temp_score=-self.alpha_beta_pruning(next_play,-beta,-alpha)
            if temp_score>beta:
                return beta
            if temp_score>alpha:
                alpha=temp_score
                (ai.__current_i,ai.__current_j)=(i,j)
        return alpha
    def firstStep(self):
        # ai will start in center
        self.__go.set_board_state(7,7,self.__current_state)
        return True
    def oneStep(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if self.__go.getchess_map()[i][j] \
                    != StateOfBoard.empty:
                    continue  # only search for available spots

                if self.has_five_in_row(self.__current_state, i, j):
                    print ('has checkmate')
                    self.__go.set_board_state(i, j,
                            self.__currentState)
                    return True

                if not self.has_neighbour(self.__go.getchess_map()[i][j],
                        i, j):
                    continue

                if self.check(self.__current_state, i, j):
                    print ('has check, checking if opponent already has one...')
                    if self.checkmate(self.__currentState) \
                        is True:
                        print ('not safe, searching other moves...')
                    elif self.checkmate(self.__current_state) \
                        is False:
                        print ('safe')
                        self.__go.set_board_state(i, j,
                                self.__current_state)
                        return True

        node = go_ai(self.__go, self.__current_state,
                        self.__depth)
        score = self.alpha_beta_prune(node)
        print (score)
        (i, j) = (node.__current_i, node.__current_j)

        if not i is None and not j is None:
            if self.__go.get_board_state(i, j) \
                != StateOfBoard.empty:
                self.oneStep()
            else:
                self.__go.set_board_state(i, j,
                        self.__current_state)
                return True
        return False




           


    







