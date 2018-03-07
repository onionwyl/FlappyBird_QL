class qlBot():
    def __init__(self):
        # Hyper parameters
        self.qlAlpha = 0.7
        self.qlGamma = 0.8
        self.qlResolution = 8
        self.qlAliveReward = 1
        self.qlDeadReward = -1000
        self.qlEpsilon = 0
        self.qlExploreJumpRate = 0.1

        # Running parameters
        self.qlRound = 0 # Count the Round of Game
        self.maxScore = 0

        # Q-learning parameters
        self.A = None
        self.S = None
        self.Q = {}
        self.actions = []
        self.enableQL = True

        self.loadQ()


    def move(self):
        pass

    def updateQL(self):
        pass

    def updateQ(self, Q, S, S_, A, R):
        pass

    def getQlState(self):
        pass

    def mapState(self):
        pass

    def reset(self):
        pass

    def countResult(self):
        pass

    def saveQ(self):
        pass

    def loadQ(self):
        pass