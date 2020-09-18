class Player ():
    def __init__(self):
        self.total_hit = 0
        self.total_try = 0 #put 0 after debugging

    def get_score(self):
        try:
            return (int(100*self.total_hit/self.total_try))
        except:
            print("ERROR SCORE INVALID")
            return None
    
    def set_score(self, total_hit, total_try):
        self.total_hit += total_hit
        self.total_try += total_try