import copy

class MapPool:
    def __init__(self, position):
        self.size = 20
        self.pool = None

    def create(self, position):
        self.pool = {'free': [], 'busy': []}
        for i in range(self.size):
            self.pool['free'].append(copy.deepcopy(position))

    def borrow(self, data):
        if not self.pool:
            self.create(data)
        if not self.pool['free']:
            return None
        else:
            pool_object = self.pool['free'].pop()
            self.pool['busy'].append(pool_object)
            for i in range(len(data)):
                for j in range(len(data)):
                    pool_object[i][j] = []
                    for item in data[i][j]:
                        pool_object[i][j].append(item)
            return pool_object

    def give_back(self, pool_object):
        self.pool['busy'].remove(pool_object)
        self.pool['free'].append(pool_object)
