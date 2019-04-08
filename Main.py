from Node import Node
from AlphaBeta import alpha_beta_rac

def main():
    choice = input('X or O: ').lower()
    while choice not in ['x', 'o']:
        choice = input('X or O: ').lower()
    root = Node(choice, grid=[[None, None, None], [None, None, None], [None, None, None]])
    while True:
        x, y = [int(x) for x in input('enter position(x y): ').split()]
        while not x in range(0, 3) and not y in range(0, 3):
            try:
                x, y = [int(x) for x in input('enter position(x y): ').split()]
            except ValueError:
                continue
        
        if root.grid[x][y]:
            print('position already taken. Choose another one.')
            continue
        
        root.grid[x][y] = choice
        root.generate_tree()
        succ = alpha_beta_rac(root, 'max')
        print()
        for i in succ.grid:
            print(i)
        root = succ
        root.level = root.inverse_level()
        root.XorO = root.inverse_XorO()
        if root.check_win():
            print('you won')
            return
        elif root.check_win(root.inverse_XorO()):
            print('you lost')
            return
        elif root.nb_none() == 0:
            print("it's a tie")
            return
        input('\npress enter to continue: \n')
    
main()