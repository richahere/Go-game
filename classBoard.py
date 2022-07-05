from enum import Enum
# now we will define size of our board
SIZE=19
# size will be 13X13
class StateOfBoard(Enum):
    # we can have 3 possible state here
    # 1.empty 2. black 3. white
    empty=0
    black=1
    white=2
