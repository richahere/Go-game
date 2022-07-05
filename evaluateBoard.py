from classBoard import *
white_6_patterns = [['empty', 'white', 'white', 'white', 'white','empty'],
                   ['empty', 'white', 'white', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'white', 'white','empty'],
                   ['empty', 'white', 'white', 'empty', 'white','empty'],
                   ['empty', 'white', 'empty', 'white', 'white','empty'],
                   ['empty', 'empty', 'white', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'empty', 'white','empty'],
                   ['empty', 'white', 'empty', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'empty', 'empty','empty'],
                   ['empty', 'empty', 'empty', 'white', 'empty','empty']]
white_6_scores = [50000,5000,5000,500,500,100,100,100,10,10]
white_5_patterns = [['white', 'white', 'white', 'white', 'white'],
                   ['white', 'white', 'white', 'white', 'empty'],
                   ['empty', 'white', 'white', 'white', 'white'],
                   ['white', 'white', 'empty', 'white', 'white'],
                   ['white', 'empty', 'white', 'white', 'white'],
                   ['white', 'white', 'white', 'empty', 'white']]
white_5_scores = [1000000,5000,5000,5000,5000,5000]
black_6_patterns = [['empty', 'black', 'black', 'black', 'black','empty'],
                   ['empty', 'black', 'black', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'black', 'black','empty'],
                   ['empty', 'black', 'black', 'empty', 'black','empty'],
                   ['empty', 'black', 'empty', 'black', 'black','empty'],
                   ['empty', 'empty', 'black', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'empty', 'black','empty'],
                   ['empty', 'black', 'empty', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'empty', 'empty','empty'],
                   ['empty', 'empty', 'empty', 'black', 'empty','empty']]
black_6_scores = [50000,5000,5000,500,500,100,100,100,10,10]
black_5_patterns = [['black', 'black', 'black', 'black', 'black'],
                   ['black', 'black', 'black', 'black', 'empty'],
                   ['empty', 'black', 'black', 'black', 'black'],
                   ['black', 'black', 'empty', 'black', 'black'],
                   ['black', 'empty', 'black', 'black', 'black'],
                   ['black', 'black', 'black', 'empty', 'black']]
black_5_scores = [1000000,5000,5000,5000,5000,5000]
# now we will be defining funcation which will return true if smaller
# part is subset of bigger part.
def small_part_big(small,big):
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if(big[i+j]!=small[j]):
                break
        else:
            return True
    return False
# now funcation to change board state
def boardState(vec):
    list=[]
    for items in vec:
        if items==StateOfBoard.black:
            list.append('black')
        elif items==StateOfBoard.white:
            list.append('white')
        else:
            list.append('empty')
    return list
# now here funcation which will return score
def score_eval(vec):
    list=boardState(vec)
    score={'white':0, 'black':0}
    length=len(list)
    if length==5:
        for i in range(len(white_5_patterns)):
            if white_5_patterns[i]==list:
                score['white']+=white_5_scores[i]
            if black_5_patterns[i]==list:
                score['black']+=black_5_scores[i]
        return score       
    for i in range(length-5):
        temp=[list[i],list[i+1],list[i+2],list[i+3],list[i+4]]
        for i in range(len(white_5_patterns)):
            if white_5_patterns[i]==temp:
                score['white']+=white_5_scores[i]
            if black_5_patterns[i]==temp:
                score['black']+=black_5_scores[i]
    for i in range(length - 6):
        temp = [list[i],list[i + 1],list[i + 2],list[i + 3], list[i + 5],]
        for i in range(len(white_6_patterns)):
            if white_6_patterns[i] == temp:
                score['white'] += white_6_scores[i]
            if black_6_patterns[i] == temp:
                score['black'] += black_6_scores[i]
    return score

