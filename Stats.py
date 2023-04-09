class Stats():
    """tracking statistics"""

    def __init__(self):
        """Initialising statistic"""
        self.ResetStats()


    def ResetStats(self):
        """statistics that change during the game"""
        self.GunsLeft = 0
        self.EnemyLeft = 0