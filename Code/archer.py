from search import Problem


class ArcherProblem(Problem):
    """The problem of placing N Archers on an kxk board with none attacking
    each other.  A state is represented as an N-element array, where
    a value of r in the c-th entry means there is an Archer at column c,
    row r, and a value of -1 means that the c-th column has not been
    filled in yet.  We fill in columns left to right. 
    """
    #the __init__ method always gets called  whenever a new class ArcherProblem is created
    def __init__(self, k,w,placement):  
        self.k = k  #size of the row and columns of the grids
        self.w=w #the range of each archer
       
        self.placement=placement   #this is where all the archers are going to be placed
        self.initial = tuple(placement)   # makes a tuple with all elements -1
        
        Problem.__init__(self, self.initial)

    def actions(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
      
        if state[-1] is not -1:
            return []  # All columns filled; no successors
        else:
            
             col =state.index(-1) #index shows where -1 first appears(the position)
         
             return [row for row in range(self.k)
                    if not (self.conflicted(state, row, col)and self.conflicted1(state, row, col))]  
             #return the line if there is no conflict between the row and the column

    def result(self, state, row):
        """Place the next Archer at the given row."""
        col = state.index(-1)   #we get the col index where -1 first appears
        new = list(state[:])    #: is used for slice of list(it does not affect the problem here)
        new[col] = row
      
        
        return tuple(new)
    #we have two methods used to determine if the current position that we want place an Archer on conflicts with anything placed
    #on the board already:
    #the first conflict method checks to see if there are archers on the same row column or diagonal
    #meanwhile the second conflict checks to see if the position between the archers is bigger than or equal to the range of the
    #archers
    #These two conflict methods Contribute to our two placing condtions.
    def conflicted(self, state, row, col):
        """Would placing an Archer at (row, col) conflict with anything?"""
        return  any((self.conflict(row, col, state[c], c))
                   for c in range(col))

    def conflicted1(self, state, row, col):
        """Would placing an Archer at (row, col) conflict with anything?"""
        return  any((self.conflict1(row, col, state[c], c))
                   for c in range(col))
    

    def conflict(self, row1, col1, row2, col2):
        """Would putting two Archers in (row1, col1) and (row2, col2) conflict?"""
        return ((row1 == row2 ) or  # same row
                (col1 == col2 ) or  # same column
                (row1 - col1 == row2 - col2 )   or  # same \ diagonal
                (row1 + col1 == row2 + col2))  # same / diagonal

    def conflict1(self, row1, col1, row2, col2):
        
        return (( col2-col1<=self.w) or  # range on row
                (row2-row1<=self.w) or  # range on column
                (col2-col1<=self.w and row2-row1<=self.w)   or  # range on diagonal
                ( col2-col1<=self.w and row2-row1<=self.w))  # range on diagonal

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""
        if state[-1] is -1:
            return False

        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))


