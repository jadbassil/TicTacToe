class Node:
    
    def __init__(self, XorO, level='max', successors=None, score=None, grid=[[None, None, None],[None, None, None],[None, None, None]]):
        if successors == None:
            successors = []
        self.XorO = XorO
        self.level = level
        self.successors = successors     
        self.score = score
        self.grid = grid

    def check_win(self, XorO = None):
        if XorO == None:
            XorO = self.XorO
        #check line values
        for i in range(0, 3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] == XorO:
                return True
        #check column values
        for i in range(0, 3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] == XorO:
                return True
        #check diagonales
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == XorO:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == XorO:
            return True
        return False

    def nb_none(self):
        nb = 0
        for i in self.grid:
            nb += i.count(None)
        return nb

    def none_indices(self):
        indices = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[i][j] is None:
                    indices.append((i, j))          
        return indices

    def generate_successors(self):
        successors_level = self.inverse_level()
        successors_XorO = self.inverse_XorO()
        none_indices = self.none_indices()
        for i in none_indices:
            new_grid = [x[:] for x in self.grid]
            new_grid[i[0]][i[1]] = successors_XorO
            node = Node(successors_XorO, level=successors_level, grid=new_grid)
            if node.level == 'max' and node.check_win(node.inverse_XorO()):
                node.score = 1
            elif node.level == 'max' and node.check_win():
                node.score = -1
            elif node.level == 'min' and node.check_win():
                node.score = 1
            elif node.level == 'min' and node.check_win(node.inverse_XorO()):
                node.score = -1
            elif node.nb_none() == 0:
                node.score = 0
            self.successors.append(node)
            del node
        
    def generate_tree(self):
        if self.score:
            return
        self.generate_successors()
        for succ in self.successors:
            succ.generate_tree()

    
    def inverse_level(self):
        if self.level == 'max':
            return 'min'
        elif self.level == 'min':
            return 'max'
    
    def inverse_XorO(self):
        if self.XorO == 'x':
            return 'o'
        elif self.XorO == 'o':
            return 'x'
    
    def apply(self, list_scores):
        if self.level == 'max':
            self.score = max(list_scores)
        else:
            self.score = min(list_scores)
        return self.score
    
    @classmethod
    def getNext(cls, node, score):
        for i in node.successors:
            if i.score == score:
                return i
        return None