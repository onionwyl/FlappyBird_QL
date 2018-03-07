import random, math, json

class qlBot():
    def __init__(self):
        # Hyper parameters
        self.qlAlpha = 0.6
        self.qlGamma = 0.8
        self.qlResolution = 5
        self.qlAliveReward = 1
        self.qlDeadReward = -1000
        self.qlEpsilon = 0
        self.qlExploreJumpRate = 0.1

        # Running parameters
        self.qlRound = 0 # Count the Round of Game
        self.maxScore = 0
        self.prevPipeHeight = 0
        self.currPipeHeight = 0
        self.saveCount = 25
        self.modelName = "Q1.json"

        # Q-learning parameters
        self.A = None
        self.S = None
        self.Q = {}
        self.actions = []
        self.enableQL = True

        self.loadQ()


    def move(self, state):
        S_Next = self.getQlState(state)
        if not S_Next in self.Q:
            self.Q[S_Next] = [0, 0]
        A_Next = 0
        # ε-greedy
        if (random.random() < self.qlEpsilon):
            A_Next = 1 if random.random() < self.qlExploreJumpRate else 0
        elif S_Next in self.Q:
            A_Next = 1 if self.Q[S_Next][0] < self.Q[S_Next][1] else 0
        self.actions.append([self.S, S_Next, self.A])
        self.A = A_Next
        self.S = S_Next
        return A_Next

    def updateQL(self):
        self.qlRound  += 1
        actions = list(reversed(self.actions))
        dead = 3
        for action in actions:
            [S, S_, A] = action
            if dead != 0:
                self.updateQ(self.Q, S, S_, A, self.qlDeadReward)
                dead -=1
            else:
                self.updateQ(self.Q, S, S_, A, self.qlAliveReward)
        self.saveQ()
        self.reset()
    def updateQ(self, Q, S, S_, A, R):
        if S and S_ and A in [0, 1] and S in Q and S_ in Q:
            Q[S][A] = (1 - self.qlAlpha) * Q[S][A] + self.qlAlpha * (R + self.qlGamma * max(Q[S_]))
        return Q

    def getQlState(self, state):
        pipeList = state['pipes']
        pipeWidth = state['pipeWidth']
        playerX = state['playerX']
        playerY = state['playerY']
        index = 0
        for i in range(len(pipeList)):
            if pipeList[i]['x'] + pipeWidth >= playerX:
                index = i
                break

        if self.currPipeHeight == 0:
            self.currPipeHeight = pipeList[index]['y']
        elif self.currPipeHeight != pipeList[index]['y']:
            self.prevPipeHeight = self.currPipeHeight
            self.currPipeHeight = pipeList[index]['y']
        # dp = math.floor((self.currPipeHeight - self.prevPipeHeight) / 5)
        dx = math.floor((pipeList[index]['x'] - playerX + pipeWidth) / self.qlResolution)
        dy = math.floor((pipeList[index]['y'] - playerY) / self.qlResolution)
        yVel = state['yVel']
        S = self.mapState(dx, dy, yVel)
        return S

    def mapState(self, dx, dy, yVel):
        return str([dx, dy, yVel])

    def reset(self):
        self.A = None
        self.S = None
        self.actions = []
        self.currPipeHeight = 0
        self.prevPipeHeight = 0

    def countResult(self):
        pass

    def saveQ(self):
        if self.qlRound % self.saveCount == 0:
            f = open(self.modelName, 'w')
            json.dump(self.Q, f)
            f.close()
            # print('Q-values updated on local file.')

    def loadQ(self):
        try:
            f = open(self.modelName, 'r')
        except IOError:
            return
        self.Q = json.load(f)
        f.close()