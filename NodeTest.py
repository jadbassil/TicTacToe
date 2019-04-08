from Node import Node
import unittest

class NodeTest(unittest.TestCase):

    def setUp(self):
        self.t = Node('x', grid=[['x', None, None], [None, None, None], [None, None, None]])
        self.t1 = Node('x', grid=[['x','x','x'], [None, 'o', 'o'], [None, None, 'o']])
        self.t2 = Node('x', grid=[['x','o','x'], ['x', 'o', None], ['x', 'o', 'o']])
        self.t3 = Node('x', grid=[['x','o','x'], ['o', 'x', None], ['x', 'o', 'x']])
        self.t4 = Node('x', grid=[['x','o','x'], ['o', 'x', None], ['x', 'o', 'o']])

    def test_check_win(self):
        r1 = self.t1.check_win()
        r2 = self.t2.check_win()
        r3 = self.t3.check_win()
        r4 = self.t4.check_win()
        self.assertEqual(r1, True)
        self.assertEqual(r2, True)
        self.assertEqual(r3, True)
        self.assertEqual(r4, True)

    def test_nb_none(self):
        r1 = self.t1.nb_none()
        r3 = self.t3.nb_none()
        self.assertEqual(r1, 3)
        self.assertEqual(r3, 1)

    def test_none_indices(self):
        r1 = self.t1.none_indices()
        self.assertEqual(r1, [(1,0), (2,0), (2,1)])

    def test_generate_successors(self):
        self.t2.generate_successors()
        self.assertEqual(self.t2.successors[0].grid, [['x','o','x'], ['x', 'o', 'o'], ['x', 'o', 'o']])
        self.t1.generate_successors()
        self.assertEqual(self.t1.successors[0].grid, [['x','x','x'], ['o', 'o', 'o'], [None, None, 'o']])
        self.assertEqual(self.t1.successors[1].grid, [['x','x','x'], [None, 'o', 'o'], ['o', None, 'o']])

    def test_generate_tree(self):
        t = Node('x', grid=[['x', None, None], [None, None, None], [None, None, None]])
        t.generate_tree()
        self.assertEqual(t.successors[0].grid, [['x', 'o', None], [None, None, None], [None, None, None]])
        self.assertEqual(t.successors[0].successors[0].grid, [['x', 'o', 'x'], [None, None, None], [None, None, None]])
        self.assertEqual(t.successors[0].successors[6].grid, [['x', 'o', None], [None, None, None], [None, None, 'x']])
        self.assertEqual(t.successors[7].grid, [['x', None, None], [None, None, None], [None, None, 'o']])

unittest.main()
