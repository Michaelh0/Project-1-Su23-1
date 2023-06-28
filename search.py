# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    #print("Start:", problem.getStartState())
   # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
   # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
   
    prevLocation = set()
    prevLocation.add(problem.getStartState())

    trackingpops = []

    direct = []

    direction = 0

    stack = util.Stack()
    for i in problem.getSuccessors(problem.getStartState()):
        stack.push((problem.getStartState(),i))

    popped = stack.pop()
    while not problem.isGoalState(popped[1][0]):
        if not (popped[1][0] in prevLocation):
            #print (popped)
            for i in problem.getSuccessors(popped[1][0]):
                stack.push((popped[1][0],i))
            prevLocation.add((popped[1][0]))
            trackingpops = trackingpops + [popped]
        popped = stack.pop()
        
    trackingpops = trackingpops + [popped]
    #print(popped)
    next_direction = 0
    direction = trackingpops.pop()
    while len(trackingpops) != 0:
        next_direction = trackingpops.pop()
        #print(direction[0], next_direction[1][0])
        if direction[0] == next_direction[1][0]:
            direct = direct + [direction[1][1]] #[compass]
            direction = next_direction
            
    direct = direct + [direction[1][1]]#[compass]
    direct.reverse()
    #print(direct)
    return direct
    #util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    prevLocation = set()
    prevLocation.add(problem.getStartState())

    trackingpops = []

    direct = []

    direction = 0

    queue = util.Queue()
    for i in problem.getSuccessors(problem.getStartState()):
        queue.push((problem.getStartState(),i))

    popped = queue.pop()
    while not problem.isGoalState(popped[1][0]):
        if not (popped[1][0] in prevLocation):
            #print (popped)
            for i in problem.getSuccessors(popped[1][0]):
                queue.push((popped[1][0],i))
            prevLocation.add((popped[1][0]))
            trackingpops = trackingpops + [popped]
        popped = queue.pop()
        
    trackingpops = trackingpops + [popped]
    #print(popped)
    next_direction = 0
    direction = trackingpops.pop()
    while len(trackingpops) != 0:
        next_direction = trackingpops.pop()
        #print(direction[0], next_direction[1][0])
        if direction[0] == next_direction[1][0]:
            direct = direct + [direction[1][1]] #[compass]
            direction = next_direction
            
    direct = direct + [direction[1][1]]#[compass]
    direct.reverse()
    #print(direct)
    return direct

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    prevLocation = set()
    prevLocation.add(problem.getStartState())

    trackingpops = []

    direct = []
    costtracker = {}
    direction = 0
    newcost = 0
    stack = util.PriorityQueue()
    costtracker[problem.getStartState()] = 0
    for i in problem.getSuccessors(problem.getStartState()):
        stack.push((problem.getStartState(),i),i[2])
        costtracker[i[0]] = i[2]
    popped = stack.pop()
    while not problem.isGoalState(popped[1][0]):
        if not (popped[1][0] in prevLocation):
            for i in problem.getSuccessors(popped[1][0]):
                newcost = i[2] + costtracker[popped[1][0]]
                stack.push((popped[1][0],i), newcost)
                costtracker[i[0]] = newcost
            prevLocation.add((popped[1][0]))
            trackingpops = trackingpops + [popped]
        popped = stack.pop()
    trackingpops = trackingpops + [popped]
    #print(popped)
    next_direction = 0
    direction = trackingpops.pop()
    while len(trackingpops) != 0:
        next_direction = trackingpops.pop()
        #print(direction[0], next_direction[1][0])
        if direction[0] == next_direction[1][0]:
            direct = direct + [direction[1][1]] #[compass]
            direction = next_direction
            
    direct = direct + [direction[1][1]]#[compass]
    direct.reverse()
    #print(direct)
    return direct

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
