class Problem(object):
    """The abstract class for a formal problem."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal."""
        self.initial = initial
        self.goal = goal
        
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value."""
        raise NotImplementedError


# ______________________________________________________________________________


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    
   

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Returns the child of the current node."""
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next_node))




# Uninformed Search algorithm



def depth_first_tree_search(problem,archerNumber,restrict):
    """Search the deepest nodes in the search tree first.
        Search through the successors of a problem to find a goal.
        The argument frontier should be an empty queue.
        Repeats infinitely in case of loops."""
    
    frontier = [Node(problem.initial)]  #This is the  Stack which holds our solutions
    solutions=0  #This is used to count the total number of solutions found
    while frontier:
        node = frontier.pop()
        
        if problem.goal_test(node.state):#if we reached a solution then we are going to start printing our output data
            
            solutions=solutions+1
            m=list(node.state)  #m gets the current state of the node which holds one of the correct solutions of the algorithm
            archer_number_possible=0  #this will help us determine how many archers the algorithms was able to place on the grid
            #The printing process has 4 steps:
            #1.printing the pattern of the archers in a list
            #2.printing the positions where walls are placed by using the "restrict" list which holds the position of each wall
            #3.printing the board so we can easily visualise the solution where we have the following purpose for each element placed:
             #a.element "A" means there is an archer on that position
             #b.element "W" means that there is a wall placed on that position
             #c.element "." means that the position on the grid is empty
            #4.
            print("Placement pattern", end =" ")
            print(m)
            print("Positions where walls are placed", end =" ")
            print(restrict)
            for row in range(len(m)):
                line = ""
                for column in range(len(m)):
                    
                    if m[row] == column and column<=archerNumber and not find_walls(restrict,m[row]): #this condition is used to see if the position of the archers
                                                                                                      #interferes with that of a wall
                        line += "A "
                        archer_number_possible=archer_number_possible+1
                    elif  find_walls(restrict,m[row]) and column==row:
                        line +="W "
                    else:
                        line += ". "
                print(line)
            print("The number of Archers placed:")
            print(archer_number_possible)
            print("\n")
        
        frontier.extend(node.expand(problem)) #we select for expansion the last element that was added to the frontier.

    print("The number of solutions found is",end=" ")
    print(solutions)
    return None

#this function is used to find if any of the walls listed in the "restrict" list interfere with our board
def find_walls(restrict,archer):
    for i in range(len(restrict)):
        if(archer==restrict[i]):
            return True
    return False